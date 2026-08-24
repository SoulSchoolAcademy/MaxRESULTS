#!/usr/bin/env python3
"""Deterministic Naya Power Restore Context runtime.

This is the first complete continuity slice: bootstrap the canonical runtime,
reconstruct repository reality, apply temporal filtering, retrieve relevant
Smart Notes, detect stale/superseded/conflicted memory, and emit a compact
machine-readable handoff/checkpoint without pretending that memory is truth.

Standard-library only. No network access is required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
NAYA = ROOT / ".naya"
MEMORY = NAYA / "memory"
STATE_PATH = MEMORY / "STATE.json"
MANIFEST_PATH = NAYA / "naya-context-manifest.json"
BOOTSTRAP_PATH = MEMORY / "BOOTSTRAP.md"
NOTE_DIR = MEMORY / "notes"
CHECKPOINT_DIR = NAYA / "checkpoints"
HANDOFF_DIR = NAYA / "handoffs"

sys.path.insert(0, str(MEMORY))
from memory_runtime import load_json, notes, retrieve, validate  # noqa: E402

ISO_Z_RE = re.compile(r"Z$")


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    value = ISO_Z_RE.sub("+00:00", value)
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        raise ValueError("timestamp must include timezone")
    return dt.astimezone(timezone.utc)


def now() -> datetime:
    return datetime.now(timezone.utc)


def run_git(*args: str) -> str | None:
    try:
        p = subprocess.run(
            ["git", *args], cwd=ROOT, text=True, capture_output=True, check=True
        )
        return p.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def repository_reality(at: datetime | None = None) -> dict[str, Any]:
    if at is None:
        head = run_git("rev-parse", "HEAD")
        branch = run_git("branch", "--show-current")
        status = run_git("status", "--porcelain")
        commit = run_git("show", "-s", "--format=%H|%cI|%s", "HEAD")
    else:
        stamp = at.isoformat()
        head = run_git("log", "-1", "--format=%H", f"--before={stamp}")
        branch = run_git("branch", "--show-current")
        status = None
        commit = run_git("show", "-s", "--format=%H|%cI|%s", head) if head else None
    commit_parts = commit.split("|", 2) if commit else []
    return {
        "available": head is not None,
        "root": str(ROOT),
        "branch": branch,
        "head_sha": head,
        "clean": status == "",
        "working_tree_status": status,
        "commit": {
            "sha": commit_parts[0] if len(commit_parts) > 0 else None,
            "timestamp": commit_parts[1] if len(commit_parts) > 1 else None,
            "subject": commit_parts[2] if len(commit_parts) > 2 else None,
        },
        "historical": at is not None,
        "requested_at": at.isoformat() if at else None,
    }


def load_state() -> dict[str, Any]:
    return load_json(STATE_PATH)


def load_manifest() -> dict[str, Any]:
    return load_json(MANIFEST_PATH)


def note_is_visible(note: dict[str, Any], at: datetime | None) -> bool:
    status = note.get("status")
    if status == "SUPERSEDED" and note.get("superseded_at"):
        return False if at is None else parse_time(note["superseded_at"]) <= at
    if status == "STALE" and at is None:
        return False
    if at is None:
        return status not in {"SUPERSEDED", "STALE"}
    effective = parse_time(note.get("effective_at"))
    if effective and effective > at:
        return False
    if note.get("superseded_at") and parse_time(note["superseded_at"]) <= at:
        return False
    return True


def memory_snapshot(query: str, at: datetime | None, limit: int) -> dict[str, Any]:
    all_notes = []
    for _, note in notes():
        if "__parse_error__" in note or not note_is_visible(note, at):
            continue
        all_notes.append(note)
    if query:
        ranked = [(score, note) for score, note in retrieve(query, max(limit * 3, 10)) if note in all_notes]
        ranked.sort(key=lambda item: (-item[0], item[1].get("effective_at", ""), item[1].get("id", "")))
        selected = [n for _, n in ranked[:limit]]
    else:
        selected = sorted(all_notes, key=lambda n: (n.get("effective_at", ""), n.get("id", "")), reverse=True)[:limit]
    counts: dict[str, int] = {}
    for note in all_notes:
        counts[note.get("status", "UNKNOWN")] = counts.get(note.get("status", "UNKNOWN"), 0) + 1
    conflicts = [n for n in all_notes if n.get("status") == "CONFLICTED"]
    return {
        "count_visible": len(all_notes),
        "counts_by_status": counts,
        "conflicts": [n.get("id") for n in conflicts],
        "selected": selected,
    }


def stale_memory() -> list[dict[str, Any]]:
    out = []
    for path, note in notes():
        if "__parse_error__" in note:
            out.append({"path": str(path), "reason": "parse_error"})
        elif note.get("status") in {"STALE", "CONFLICTED", "SUPERSEDED"}:
            out.append({
                "id": note.get("id"),
                "title": note.get("title"),
                "status": note.get("status"),
                "path": str(path),
            })
    return out


def build_restore(query: str = "", at: str | None = None, limit: int = 10) -> dict[str, Any]:
    target = parse_time(at)
    state = load_state()
    manifest = load_manifest()
    structural_errors = validate()
    repo = repository_reality(target)
    memory = memory_snapshot(query, target, limit)
    return {
        "schema": "naya-power-restore-context/v1",
        "status": "VERIFIED" if not structural_errors and repo["available"] else "UNKNOWN",
        "generated_at": now().isoformat(),
        "mode": "RESTORE-TIME" if target else "RESTORE-STANDARD",
        "requested_at": target.isoformat() if target else None,
        "authority": manifest.get("authority_rules", {}),
        "current_state": state,
        "repository_reality": repo,
        "memory": memory,
        "stale_or_superseded": stale_memory(),
        "validation": {"passed": not structural_errors, "errors": structural_errors},
        "mission": state.get("current_mission"),
        "protected": state.get("protected", []),
        "known": ["Canonical repository is SoulSchoolAcademy/NayaPOWER", "Runtime state and Smart Notes are stored under .naya/memory"],
        "unknown": state.get("unknown", []),
        "what_changed": state.get("recent_changes", []),
        "what_is_unfinished": state.get("unknown", []),
        "next_best_action": state.get("next_best_action"),
    }


def canonical_json(data: Any) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def write_artifact(directory: Path, prefix: str, payload: dict[str, Any]) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    stamp = now().strftime("%Y%m%dT%H%M%SZ")
    path = directory / f"{prefix}-{stamp}.json"
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def checkpoint(restore: dict[str, Any]) -> dict[str, Any]:
    payload = {
        "schema": "naya-power-checkpoint/v1",
        "created_at": now().isoformat(),
        "restore_status": restore["status"],
        "repository_reality": restore["repository_reality"],
        "mission": restore["mission"],
        "current_state": restore["current_state"],
        "memory_summary": {
            "count_visible": restore["memory"]["count_visible"],
            "counts_by_status": restore["memory"]["counts_by_status"],
            "conflicts": restore["memory"]["conflicts"],
        },
        "protected": restore["protected"],
        "unknown": restore["unknown"],
        "next_best_action": restore["next_best_action"],
        "integrity_sha256": hashlib.sha256(canonical_json(restore).encode("utf-8")).hexdigest(),
    }
    path = write_artifact(CHECKPOINT_DIR, "checkpoint", payload)
    return {"path": str(path.relative_to(ROOT)), "checkpoint": payload}


def handoff(restore: dict[str, Any]) -> dict[str, Any]:
    payload = {
        "schema": "naya-power-handoff/v1",
        "created_at": now().isoformat(),
        "mission": restore["mission"],
        "current_state": restore["current_state"],
        "what_changed": restore["what_changed"],
        "verified": restore["status"] == "VERIFIED",
        "unknown": restore["unknown"],
        "protected_elements": restore["protected"],
        "repository": restore["repository_reality"],
        "memory_conflicts": restore["memory"]["conflicts"],
        "next_best_action": restore["next_best_action"],
    }
    path = write_artifact(HANDOFF_DIR, "handoff", payload)
    return {"path": str(path.relative_to(ROOT)), "handoff": payload}


def main() -> int:
    ap = argparse.ArgumentParser(description="Naya Power deterministic Restore Context runtime")
    sub = ap.add_subparsers(dest="command", required=True)
    r = sub.add_parser("restore")
    r.add_argument("query", nargs="?", default="")
    r.add_argument("--at", help="ISO-8601 timestamp with timezone")
    r.add_argument("--limit", type=int, default=10)
    r.add_argument("--pretty", action="store_true")
    c = sub.add_parser("checkpoint")
    c.add_argument("query", nargs="?", default="")
    c.add_argument("--at")
    h = sub.add_parser("handoff")
    h.add_argument("query", nargs="?", default="")
    h.add_argument("--at")
    args = ap.parse_args()

    if args.command == "restore":
        result = build_restore(args.query, args.at, args.limit)
        print(json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False))
        return 0 if result["status"] == "VERIFIED" else 2
    result = build_restore(args.query, args.at)
    artifact = checkpoint(result) if args.command == "checkpoint" else handoff(result)
    print(json.dumps(artifact, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "VERIFIED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
