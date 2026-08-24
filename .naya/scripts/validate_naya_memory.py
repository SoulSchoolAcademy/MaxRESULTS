#!/usr/bin/env python3
"""Deterministic validator for the Naya Power Memory Runtime.

This validator checks structure and consistency, not semantic truth.
Truth remains an evidence/authority question governed by Naya Power protocols.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print(f"ERROR: PyYAML is required: {exc}")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / ".naya" / "memory"
NOTES = MEMORY / "notes"
SCHEMA = MEMORY / "note-schema.yaml"
TAXONOMY = MEMORY / "taxonomy.yaml"
INDEX = MEMORY / "memory-index.yaml"
BOOTSTRAP = MEMORY / "restore-context.json"

ID_RE = re.compile(r"^SN-\d{8}-\d{3,}$")
ISO_TZ_RE = re.compile(r"(Z|[+-]\d{2}:\d{2})$")


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_data(path: Path):
    if path.suffix.lower() == ".json":
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    return load_yaml(path)


def err(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_timestamp(value, field: str, errors: list[str], path: Path) -> None:
    if not isinstance(value, str) or not ISO_TZ_RE.search(value):
        err(errors, f"{path}: {field} must be an ISO timestamp with timezone")
        return
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        err(errors, f"{path}: {field} is not a valid ISO timestamp")


def validate_note(path: Path, note: dict, taxonomy: dict, seen_ids: dict[str, Path], errors: list[str]) -> None:
    required = [
        "id", "title", "created_at", "category", "status", "scope", "keywords",
        "aliases", "summary", "source", "knowledge_state", "what_happened",
        "what_we_learned", "why_it_matters", "required_behavior", "evidence",
    ]
    for field in required:
        if field not in note or note[field] in (None, "", []):
            err(errors, f"{path}: missing required field '{field}'")

    note_id = note.get("id")
    if note_id:
        if not isinstance(note_id, str) or not ID_RE.match(note_id):
            err(errors, f"{path}: invalid id '{note_id}' (expected SN-YYYYMMDD-NNN)")
        elif note_id in seen_ids:
            err(errors, f"{path}: duplicate note id '{note_id}' also used by {seen_ids[note_id]}")
        else:
            seen_ids[note_id] = path

    title = note.get("title")
    if isinstance(title, str) and not 8 <= len(title) <= 140:
        err(errors, f"{path}: title length must be 8–140 characters")

    categories = set(taxonomy.get("categories", []))
    statuses = set(taxonomy.get("statuses", []))
    scopes = set(taxonomy.get("scopes", []))
    states = set(taxonomy.get("knowledge_states", []))
    relations = set(taxonomy.get("relation_types", []))

    for field, allowed in (("category", categories), ("status", statuses), ("scope", scopes), ("knowledge_state", states)):
        if note.get(field) not in allowed:
            err(errors, f"{path}: {field} '{note.get(field)}' is outside canonical taxonomy")

    validate_timestamp(note.get("created_at"), "created_at", errors, path)
    if note.get("updated_at"):
        validate_timestamp(note.get("updated_at"), "updated_at", errors, path)

    keywords = note.get("keywords")
    if not isinstance(keywords, list) or not 5 <= len(keywords) <= 15 or len(set(keywords)) != len(keywords):
        err(errors, f"{path}: keywords must contain 5–15 unique plain-language terms")

    aliases = note.get("aliases")
    if not isinstance(aliases, list) or not aliases or len(set(aliases)) != len(aliases):
        err(errors, f"{path}: aliases must be a non-empty unique list")

    for field in ("summary", "what_happened", "what_we_learned", "why_it_matters", "required_behavior", "source"):
        value = note.get(field)
        if not isinstance(value, str) or len(value.strip()) < 10:
            err(errors, f"{path}: {field} is too short to preserve durable meaning")

    evidence = note.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        err(errors, f"{path}: evidence must contain at least one record")

    if note.get("status") == "SUPERSEDED" and "superseded_by" not in note:
        err(errors, f"{path}: SUPERSEDED note must declare superseded_by, even when the replacement is unknown")

    note_relations = note.get("relations", []) or []
    for relation in note_relations:
        if isinstance(relation, dict) and relation.get("type") not in relations:
            err(errors, f"{path}: unknown relation type '{relation.get('type')}'")

    if note.get("knowledge_state") == "VERIFIED" and not evidence:
        err(errors, f"{path}: VERIFIED knowledge requires evidence")


def validate_runtime(errors: list[str]) -> dict:
    for path in (SCHEMA, TAXONOMY, INDEX, BOOTSTRAP):
        if not path.exists():
            err(errors, f"missing runtime contract: {path.relative_to(ROOT)}")

    if errors:
        return {}

    schema = load_yaml(SCHEMA)
    taxonomy = load_yaml(TAXONOMY)
    index = load_yaml(INDEX)
    bootstrap = load_data(BOOTSTRAP)

    if schema.get("schema") != "naya-smart-note/v1":
        err(errors, "note schema has unexpected schema identifier")
    if taxonomy.get("schema") != "naya-memory-taxonomy/v1":
        err(errors, "taxonomy has unexpected schema identifier")
    if index.get("schema") != "naya-memory-index/v1":
        err(errors, "memory index has unexpected schema identifier")
    if bootstrap.get("schema") != "naya-restore-context/v1":
        err(errors, "restore manifest has unexpected schema identifier")

    for key in ("retrieval_pipeline", "query_expansion", "ranking", "authority_order", "minimum_sufficient_context"):
        if not index.get(key):
            err(errors, f"memory index missing required runtime section '{key}'")

    if not isinstance(bootstrap.get("boot_sequence"), list) or len(bootstrap["boot_sequence"]) < 8:
        err(errors, "restore manifest boot_sequence is incomplete")
    if not bootstrap.get("restored_state_contract", {}).get("required"):
        err(errors, "restore manifest lacks restored-state output contract")

    return taxonomy


def main() -> int:
    global ROOT, MEMORY, NOTES, SCHEMA, TAXONOMY, INDEX, BOOTSTRAP
    parser = argparse.ArgumentParser(description="Validate Naya Power Memory Runtime")
    parser.add_argument("--root", default=str(ROOT), help="repository root")
    args = parser.parse_args()

    ROOT = Path(args.root).resolve()
    MEMORY = ROOT / ".naya" / "memory"
    NOTES = MEMORY / "notes"
    SCHEMA = MEMORY / "note-schema.yaml"
    TAXONOMY = MEMORY / "taxonomy.yaml"
    INDEX = MEMORY / "memory-index.yaml"
    BOOTSTRAP = MEMORY / "restore-context.json"

    errors: list[str] = []
    taxonomy = validate_runtime(errors)

    note_files = []
    if NOTES.exists():
        note_files = sorted([p for p in NOTES.rglob("*") if p.suffix.lower() in {".yaml", ".yml", ".json"}])

    seen_ids: dict[str, Path] = {}
    for path in note_files:
        try:
            note = load_data(path)
            if not isinstance(note, dict):
                err(errors, f"{path}: note must decode to an object")
                continue
            if taxonomy:
                validate_note(path, note, taxonomy, seen_ids, errors)
        except Exception as exc:  # noqa: BLE001
            err(errors, f"{path}: cannot parse note: {exc}")

    print("NAYA POWER MEMORY RUNTIME VALIDATION")
    print(f"Repository: {ROOT}")
    print(f"Runtime notes discovered: {len(note_files)}")
    if errors:
        print(f"STATUS: FAIL ({len(errors)} issue(s))")
        for item in errors:
            print(f"- {item}")
        return 1

    print("STATUS: PASS")
    print("Contracts: schema + taxonomy + index + restore manifest")
    print("Notes: deterministic structural validation passed")
    print("Important: PASS means structurally valid, not automatically true or production-safe")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
