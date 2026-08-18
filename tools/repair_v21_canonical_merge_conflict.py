#!/usr/bin/env python3
"""Deterministically remove an unresolved merge-conflict block from the V21 canonical builder.

Safety model:
- exactly one conflict block must exist;
- keep the Updated upstream side;
- preserve all text outside the conflict unchanged;
- fail loudly if the structure is not exactly what we expect.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"

s = BUILDER.read_text(encoding="utf-8")
start = s.find("<<<<<<< Updated upstream")
mid = s.find("\n=======\n", start)
end = s.find("\n>>>>>>> Stashed changes", mid)

if start < 0 or mid < 0 or end < 0:
    raise SystemExit("CANONICAL MERGE REPAIR: expected conflict markers not found")

if s.find("<<<<<<<", start + 1) >= 0:
    raise SystemExit("CANONICAL MERGE REPAIR: multiple conflict blocks detected")

ours = s[start:mid]
# The marker line itself is not source content; retain everything after the marker.
kept = ours.split("<<<<<<< Updated upstream\n", 1)[1]
kept = kept.lstrip("\n")

patched = s[:start] + kept + s[end + len("\n>>>>>>> Stashed changes"):]

if any(marker in patched for marker in ("<<<<<<<", "=======", ">>>>>>>")):
    raise SystemExit("CANONICAL MERGE REPAIR: conflict markers remain after repair")

BUILDER.write_text(patched, encoding="utf-8")
print("CANONICAL MERGE REPAIR: PASS")
print("Kept Updated upstream implementation; removed unresolved Stashed changes block.")
