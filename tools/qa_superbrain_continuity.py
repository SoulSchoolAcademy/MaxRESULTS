#!/usr/bin/env python3
"""Machine acceptance for the NayaPOWER Superbrain continuity contract.

This guardrail verifies that canonical orientation surfaces exist, agree with
observed git HEAD, and declare the machine-testable continuity lifecycle. It is
not proof that an external AI literally followed the boot sequence.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / ".naya/SUPERBRAIN-COLD-START-AND-CONTINUITY-CONTRACT.md"
BRIEFING = ROOT / ".naya/memory/NAYAPOWER-RUNTIME-BRIEFING.md"
FEED = ROOT / ".naya/SUPERBRAIN-COLLECTIVE-RUNNING-FEED.md"
PROJECT = ROOT / ".naya/projects/CURRENT-PROJECT.md"
START = ROOT / "START-HERE.md"


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def extract_head(value: str) -> str | None:
    patterns = (
        r"Current live HEAD.*?([0-9a-f]{40})",
        r"Current `main` verified immediately before this feed update.*?([0-9a-f]{40})",
        r"LIVE `main` at start of this update.*?([0-9a-f]{40})",
        r'current_main"\s*:\s*\{\s*"commit"\s*:\s*"([0-9a-f]{40})"',
    )
    for pattern in patterns:
        match = re.search(pattern, value, flags=re.S)
        if match:
            return match.group(1)
    return None


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def main() -> int:
    for path in (CONTRACT, BRIEFING, FEED, PROJECT, START):
        if not path.is_file():
            return fail(f"missing required artifact: {path.relative_to(ROOT)}")

    contract = text(CONTRACT)
    required_contract = (
        "IDENTIFY → RESTORE → UPDATE → INHERIT → PRIORITIZE → EXECUTE → VERIFY → LEARN → CAPTURE → PROPAGATE → CHECKPOINT → HAND OFF → REPEAT",
        "Acceptance is behavioral, not merely textual.",
        "exactly one preferred executable next action",
        "NOTE EVENT → PIS / PRIMARY INTELLIGENCE → RUNNING FEED / STATE PROJECTION → FUTURE NAYA RETRIEVAL",
    )
    for phrase in required_contract:
        if phrase not in contract:
            return fail(f"canonical continuity contract missing: {phrase}")

    actual = git("rev-parse", "HEAD")
    briefing = text(BRIEFING)
    feed = text(FEED)
    project = text(PROJECT)

    briefing_head = extract_head(briefing)
    feed_head = extract_head(feed)
    if briefing_head is None:
        return fail("could not extract a current HEAD from Runtime Briefing")
    if feed_head is None:
        return fail("could not extract a current HEAD from Running Feed")
    if briefing_head != actual:
        return fail(f"Runtime Briefing HEAD {briefing_head} != observed HEAD {actual}")
    if feed_head != actual:
        return fail(f"Running Feed HEAD {feed_head} != observed HEAD {actual}")

    if "## NEXT ACTION" not in briefing:
        return fail("Runtime Briefing has no NEXT ACTION field")
    if "# CURRENT EXECUTION QUEUE" not in feed:
        return fail("Running Feed has no CURRENT EXECUTION QUEUE")
    if "## NEXT EXECUTION" not in project:
        return fail("CURRENT-PROJECT has no NEXT EXECUTION")

    # Deliberate negative: the known legacy identity contradiction must remain
    # visible until START-HERE is repaired; this prevents a false green claim.
    if "CANONICAL NAYA NITRO / MAXESS RESULTS REPOSITORY:" in text(START) and "`SoulSchoolAcademy/MaxRESULTS`" in text(START):
        return fail("START-HERE still declares MaxRESULTS as the canonical Naya repository; identity reconciliation is required")

    print("PASS — Superbrain orientation surfaces agree with observed HEAD and the canonical continuity lifecycle is structurally present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
