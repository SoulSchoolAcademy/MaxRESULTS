#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'

b = BUILDER.read_text(encoding='utf-8')
changes = 0

replacements = [
    ("JS = \"\"\"", "JS = r\"\"\"", "make embedded JS raw"),
    ("<b>'+Math.round(s)+' / 100</b>", "<b>'+Math.round(s)+'</b>", "remove report /100 suffix"),
    ("<b>'+escapeHtml(d.name)+' · '+Math.round(d.score||0)+' / 100</b>", "<b>'+escapeHtml(d.name)+' · '+Math.round(d.score||0)+'</b>", "remove dimension /100 suffix"),
]

for old, new, label in replacements:
    if old not in b:
        raise SystemExit(f'ERROR: missing expected builder literal: {label}')
    b = b.replace(old, new, 1)
    changes += 1

BUILDER.write_text(b, encoding='utf-8')
print('BUILDER DIRECT FIX COMPLETE')
print(f'Changes: {changes}')
print('Embedded JS: raw Python string')
print('Canonical score: no /100 suffix')
