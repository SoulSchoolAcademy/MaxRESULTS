#!/usr/bin/env python3
"""Deterministically remove unresolved merge-conflict blocks from the V21 canonical builder.

Safety model:
- detect only real git conflict-marker lines at the start of a line;
- require balanced <<<<<<< / ======= / >>>>>>> triplets;
- keep the Updated upstream side of each conflict;
- preserve all text outside conflicts unchanged;
- fail loudly on malformed/nested/unbalanced conflicts.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"

s = BUILDER.read_text(encoding="utf-8")

marker_re = re.compile(
    r"(?ms)^(?P<start><<<<<<[^\n]*)\n"
    r"(?P<ours>.*?)"
    r"^=======\n"
    r"(?P<theirs>.*?)"
    r"^(?P<end>>>>>>[^\n]*)$"
)

matches = list(marker_re.finditer(s))
if not matches:
    raise SystemExit("CANONICAL MERGE REPAIR: no real conflict blocks found")

# Reject anything that looks like an unmatched conflict marker line.
line_markers = [ln for ln in s.splitlines() if re.match(r"^(<<<<<<<|=======|>>>>>>>)", ln)]
covered = set()
for m in matches:
    covered.update(s[m.start():m.end()].splitlines())
for ln in line_markers:
    if ln not in covered:
        raise SystemExit("CANONICAL MERGE REPAIR: unmatched conflict marker detected")

parts = []
last = 0
for m in matches:
    parts.append(s[last:m.start()])
    ours = m.group("ours")
    parts.append(ours)
    last = m.end()
parts.append(s[last:])
patched = "".join(parts)

if any(re.search(r"(?m)^(<<<<<<<|=======|>>>>>>>)", ln) for ln in patched.splitlines()):
    raise SystemExit("CANONICAL MERGE REPAIR: conflict markers remain after repair")

BUILDER.write_text(patched, encoding="utf-8")
print(f"CANONICAL MERGE REPAIR: PASS ({len(matches)} conflict block{'s' if len(matches) != 1 else ''} repaired)")
print("Kept Updated upstream implementation for every detected conflict block.")
