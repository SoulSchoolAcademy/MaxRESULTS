#!/usr/bin/env python3
"""Deterministically repair V21 canonical builder integrity and narrative order."""
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
    parts.append(m.group("ours"))
    last = m.end()
parts.append(s[last:])
patched = "".join(parts)

if any(re.search(r"(?m)^(<<<<<<<|=======|>>>>>>>)", ln) for ln in patched.splitlines()):
    raise SystemExit("CANONICAL MERGE REPAIR: conflict markers remain after repair")


def normalize_narrative(text: str) -> tuple[str, bool]:
    root_start = text.find("root.innerHTML=")
    if root_start < 0:
        raise SystemExit("CANONICAL MERGE REPAIR: root.innerHTML assembly not found")
    root_end = text.find("\n    var btn=root.querySelector", root_start)
    if root_end < 0:
        raise SystemExit("CANONICAL MERGE REPAIR: root.innerHTML assembly end not found")

    prefix = text[:root_start]
    assembly = text[root_start:root_end]
    suffix = text[root_end:]

    section_re = re.compile(
        r"(?ms)(?P<lead>^[ \t]*)'(?P<body><section class=\\\"v21-section.*?</section>)'\\+\s*\\n"
    )
    matches2 = list(section_re.finditer(assembly))
    if not matches2:
        raise SystemExit("CANONICAL MERGE REPAIR: no canonical sections found")

    dim_idx = [i for i, m in enumerate(matches2) if "YOUR FIVE DIMENSIONS" in m.group("body")]
    pattern_idx = [i for i, m in enumerate(matches2) if "YOUR PATTERN" in m.group("body")]
    if len(dim_idx) != 1 or len(pattern_idx) != 1:
        raise SystemExit(
            f"CANONICAL MERGE REPAIR: expected one Five Dimensions and one Pattern section; found dims={len(dim_idx)} pattern={len(pattern_idx)}"
        )

    d, p = dim_idx[0], pattern_idx[0]
    if d < p:
        return text, False

    section_chunks = [m.group(0) for m in matches2]
    dimensions_chunk = section_chunks.pop(d)
    if d < p:
        p -= 1
    section_chunks.insert(p, dimensions_chunk)

    out = []
    cursor = 0
    for m, chunk in zip(matches2, section_chunks):
        out.append(assembly[cursor:m.start()])
        out.append(chunk)
        cursor = m.end()
    out.append(assembly[cursor:])

    return prefix + "".join(out) + suffix, True

patched, changed = normalize_narrative(patched)
BUILDER.write_text(patched, encoding="utf-8")
print(f"CANONICAL MERGE REPAIR: PASS ({len(matches)} conflict block{'s' if len(matches) != 1 else ''} repaired)")
print("Kept Updated upstream implementation for every detected conflict block.")
print("CANONICAL NARRATIVE ORDER:", "NORMALIZED" if changed else "ALREADY CORRECT")
