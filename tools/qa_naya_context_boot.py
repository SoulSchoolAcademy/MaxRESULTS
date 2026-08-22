#!/usr/bin/env python3
"""Validate the canonical Naya Context Boot registry.

This is a documentation/governance integrity guardrail. It does not claim to
prove that an AI runtime actually loaded the files; runtime activation remains
an environment-level verification state.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

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
    if data.get("schema") != "naya-context-manifest/v1":
        fail("unexpected manifest schema")
    if data.get("status") != "CANONICAL":
        fail("manifest is not canonical")
    if data.get("repository") != "SoulSchoolAcademy/MaxRESULTS":
        fail("wrong canonical repository")

    boot = data.get("boot_order", [])
    required_prefix = [
        "START-HERE.md",
        ".naya/NAYA-LAW-SYSTEM-PROTOCOL.md",
        "docs/REPOSITORY-MAP.md",
        "NAYA-OS.md",
    ]
    if boot[:4] != required_prefix:
        fail("boot order does not begin with the mandatory repository-first spine")
    if len(boot) != len(set(boot)):
        fail("boot order contains duplicate paths")

    subjects = data.get("subjects", {})
    canonical_paths = []
    for subject, entry in subjects.items():
        canonical = entry.get("canonical")
        if not canonical:
            fail(f"subject {subject!r} has no canonical owner")
        canonical_paths.append(canonical)
        path = ROOT / canonical
        if not path.is_file():
            fail(f"canonical owner for {subject!r} does not exist: {canonical}")

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
    ]
    if states != expected_states:
        fail("context status ladder drifted from the canonical protocol")

    routes = data.get("task_routes", {})
    for route, subjects_for_route in routes.items():
        for subject in subjects_for_route:
            if subject not in subjects:
                fail(f"task route {route!r} references unregistered subject {subject!r}")

    protocol_text = PROTOCOL.read_text(encoding="utf-8")
    required_phrases = [
        "GITHUB FIRST",
        "FULL SYSTEM AWARENESS + SELECTIVE DEEP LOADING",
        "RELEVANT CONTEXT, NOT MAXIMUM CONTEXT",
        "DOCUMENTED",
        "ACTIVATED",
        "CONTEXT ESTABLISHED",
        "IMPLEMENTED",
        "VERIFIED",
        "LIVE VERIFIED",
        "UNKNOWN",
        "WHY IS THIS NOT A 10?",
    ]
    for phrase in required_phrases:
        if phrase not in protocol_text:
            fail(f"protocol missing required guardrail phrase: {phrase}")

    print("PASS: Naya Context Boot manifest, canonical owners, task routes, status ladder, and protocol guardrails are coherent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
