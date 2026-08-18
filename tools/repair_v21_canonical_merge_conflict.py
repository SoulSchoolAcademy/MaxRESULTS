#!/usr/bin/env python3
"""Idempotently repair V21 canonical builder integrity and narrative order."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"

s = BUILDER.read_text(encoding="utf-8")

marker_re = re.compile(
    r"(?ms)^(?P<start><{7}[^\n]*)\n"
    r"(?P<ours>.*?)"
    r"^={7}\n"
    r"(?P<theirs>.*?)"
    r"^(?P<end>>{7}[^\n]*)$"
)

matches = list(marker_re.finditer(s))

if matches:
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
else:
    patched = s


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

    # Canonical HTML lives inside JavaScript string literals, so the class quote may
    # be escaped as class=\"...\". Accept either escaped or literal quote syntax.
    section_start_re = re.compile(r"<section\s+class=\\?[\"']v21-section")
    starts = [m.start() for m in section_start_re.finditer(assembly)]
    if not starts:
        raise SystemExit("CANONICAL MERGE REPAIR: no canonical sections found")

    chunks = [
        assembly[start:(starts[i + 1] if i + 1 < len(starts) else len(assembly))]
        for i, start in enumerate(starts)
    ]

    tokens = (
        "NAYA · YOUR AI GUIDE",
        "YOUR RESULT",
        "WHAT YOUR SCORES MEAN",
        "YOUR PERSONALIZED REPORT",
        "YOUR AI FINGERPRINT",
        "YOUR FIVE DIMENSIONS",
        "YOUR PATTERN",
        "YOUR STRENGTH",
        "YOUR LEVER",
        "YOUR NEXT MOVE",
        "18 NAYA MASTERS",
        "PLAYGROUND",
        "NAYA · IN PRACTICE",
        "YOUR AI MASTERY JOURNEY",
    )

    def section_name(chunk: str) -> str:
        for token in tokens:
            if token in chunk:
                return token
        return ""

    names = [section_name(c) for c in chunks]
    if names.count("YOUR FIVE DIMENSIONS") != 1 or names.count("YOUR PATTERN") != 1:
        raise SystemExit(
            "CANONICAL MERGE REPAIR: expected one Five Dimensions and one Pattern section; "
            f"found dims={names.count('YOUR FIVE DIMENSIONS')} pattern={names.count('YOUR PATTERN')}"
        )

    d = names.index("YOUR FIVE DIMENSIONS")
    p = names.index("YOUR PATTERN")
    if d < p:
        return text, False

    moved = chunks.pop(d)
    p = names.index("YOUR PATTERN")
    chunks.insert(p, moved)
    return prefix + "".join(chunks) + suffix, True


patched, changed = normalize_narrative(patched)
BUILDER.write_text(patched, encoding="utf-8")

if matches:
    print(f"CANONICAL MERGE REPAIR: PASS ({len(matches)} conflict block{'s' if len(matches) != 1 else ''} repaired)")
else:
    print("CANONICAL MERGE REPAIR: PASS (no conflict blocks present; idempotent no-op)")
print("Kept Updated upstream implementation for every detected conflict block.")
print("CANONICAL NARRATIVE ORDER:", "NORMALIZED" if changed else "ALREADY CORRECT")
