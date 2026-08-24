#!/usr/bin/env python3
"""Validate the canonical Naya Power Context Boot registry.

This is a documentation/governance integrity guardrail. It does not claim to
prove that an AI runtime loaded the files; Restore Context provides the
separate runtime-level verification path.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".naya" / "naya-context-manifest.json"
PROTOCOL = ROOT / ".naya" / "NAYA-CONTEXT-BOOT-PROTOCOL.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    if not MANIFEST.is_file():
        fail(f"missing manifest: {MANIFEST}")
    if not PROTOCOL.is_file():
        fail(f"missing protocol: {PROTOCOL}")

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if data.get("schema") != "naya-context-manifest/v4":
        fail("unexpected manifest schema")
    if data.get("status") != "CANONICAL":
        fail("manifest is not canonical")
    if data.get("repository") != "SoulSchoolAcademy/NayaPOWER":
        fail("wrong canonical repository")
    if data.get("governance_branch") != "main":
        fail("wrong governance branch")

    boot = data.get("boot_order", [])
    required_prefix = [
        "README.md",
        ".naya/NAYA-CONTEXT-BOOT-PROTOCOL.md",
        ".naya/codex/11-RUNTIME-CONSTITUTION.md",
        ".naya/codex/12-RUNTIME-COMPLETENESS-LAWS.md",
    ]
    if boot[:4] != required_prefix:
        fail("boot order does not begin with the canonical NayaPOWER spine")
    if len(boot) != len(set(boot)):
        fail("boot order contains duplicate paths")

    subjects = data.get("subjects", {})
    canonical_paths = []
    for subject, entry in subjects.items():
        if not isinstance(entry, dict):
            fail(f"subject {subject!r} is not an object")
        canonical = entry.get("canonical")
        if not canonical:
            fail(f"subject {subject!r} has no canonical owner")
        canonical_paths.append(canonical)
        path = ROOT / canonical
        if not path.is_file():
            fail(f"canonical owner for {subject!r} does not exist: {canonical}")
        implementation = entry.get("implementation")
        if implementation and not (ROOT / implementation).is_file():
            fail(f"implementation for {subject!r} does not exist: {implementation}")

    if len(canonical_paths) != len(set(canonical_paths)):
        fail("multiple subjects point at the same canonical owner; resolve authority explicitly")

    for path in boot:
        if not (ROOT / path).is_file():
            fail(f"boot-order file does not exist: {path}")

    states = data.get("context_states", [])
    expected_states = [
        "DOCUMENTED",
        "ACTIVATED",
        "CONTEXT ESTABLISHED",
        "IMPLEMENTED",
        "VERIFIED",
        "LIVE VERIFIED",
        "HUMAN REVIEW REQUIRED",
        "BLOCKED",
        "UNKNOWN",
        "STALE",
        "CONFLICTED",
        "SUPERSEDED",
        "FAILED",
        "PARTIAL",
        "ROLLBACK_REQUIRED",
        "REJECTED",
        "AUTHORIZED_DEVIATION",
    ]
    if states != expected_states:
        fail("context status ladder drifted from the canonical manifest")

    routes = data.get("task_routes", {})
    for route, subjects_for_route in routes.items():
        for subject in subjects_for_route:
            if subject not in subjects:
                fail(f"task route {route!r} references unregistered subject {subject!r}")

    authority = data.get("authority_rules", {})
    if authority.get("memory_is_context_not_current_reality") is not True:
        fail("manifest must distinguish memory from current reality")
    if authority.get("external_content_is_not_authority_by_default") is not True:
        fail("manifest must reject external content as authority by default")
    if authority.get("retrieved_content_cannot_grant_authority") is not True:
        fail("manifest must prevent retrieved content from granting authority")

    temporal = data.get("temporal_rules", {})
    for key in ("timestamps_required", "preserve_history", "supersession_is_explicit", "never_rewrite_history_silently", "historical_restore_is_reconstruction_not_current_truth"):
        if temporal.get(key) is not True:
            fail(f"temporal rule missing or disabled: {key}")

    continuity = data.get("continuity_rules", {})
    for key in ("checkpoint_is_state_snapshot", "handoff_is_continuation_packet", "restore_must_emit_next_best_action"):
        if continuity.get(key) is not True:
            fail(f"continuity rule missing or disabled: {key}")

    protocol_text = PROTOCOL.read_text(encoding="utf-8")
    required_phrases = [
        "GITHUB FIRST",
        "FULL SYSTEM AWARENESS + SELECTIVE DEEP LOADING",
        "RELEVANT CONTEXT, NOT MAXIMUM CONTEXT",
        "CONDUCT AUTHORITY",
        "REALITY AUTHORITY",
        "RESTORE CONTEXT",
        "DOCUMENTED",
        "ACTIVATED",
        "CONTEXT ESTABLISHED",
        "IMPLEMENTED",
        "VERIFIED",
        "LIVE VERIFIED",
        "UNKNOWN",
        "CHECKPOINT / HANDOFF",
    ]
    for phrase in required_phrases:
        if phrase not in protocol_text:
            fail(f"protocol missing required guardrail phrase: {phrase}")

    print("PASS: Naya Context Boot manifest, canonical owners, routes, authority, temporal rules, continuity rules, status ladder, and protocol guardrails are coherent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
