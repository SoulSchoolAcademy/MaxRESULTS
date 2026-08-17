#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '20260817 912am RESULTS PAGE CODE'
REPORT = ROOT / 'V21-RUNTIME-AUTHORITY-QA.md'

text = SOURCE.read_text(encoding='utf-8') if SOURCE.exists() else ''
fail: list[str] = []
warn: list[str] = []

canon = re.search(r'<script id="maxess-results-v21-canonical-js">(.*?)</script>', text, re.S)
js = canon.group(1) if canon else ''

if not canon:
    fail.append('canonical V21 JS layer not found')

checks = [
    ("window.MAXESS_RESULT", 'authoritative result source'),
    ("root.classList.add('v21-canonical')", 'V21 canonical shell ownership'),
    ("root.setAttribute('data-results-version','v21-canonical')", 'V21 version marker'),
    ("root.setAttribute('data-results-state','ready')", 'V21 ready marker'),
    ("setTimeout", 'late runtime reassertion capability'),
    ("MutationObserver", 'runtime authority observer'),
    ("v21-canonical", 'canonical runtime marker'),
]
for token, label in checks:
    if token not in js:
        fail.append(f'missing runtime authority behavior: {label}')

# There should be a single V21 Listen CTA in the canonical builder.
if len(re.findall(r'class="v21-listen"', js)) != 1:
    fail.append('canonical V21 Listen CTA count is not exactly 1')

# The canonical runtime should be the final renderer, not a CSS-only overlay.
if 'root.innerHTML=' not in js:
    fail.append('V21 runtime does not own root rendering')

# Detect the known competing runtime class in the source. Presence is acceptable only
# if the V21 authority guard is also present.
if 'v18-preservation' in text and 'MutationObserver' not in js:
    fail.append('known V18 preservation runtime remains without V21 authority protection')

if 'maxess-results-v18-preservation-js' in text:
    warn.append('legacy V18 preservation runtime text remains in source; runtime authority must supersede it')

report = [
    '# MAXESS V21 — RUNTIME AUTHORITY QA',
    '',
    f'- Source lines: `{len(text.splitlines())}`',
    f'- Failures: `{len(fail)}`',
    f'- Warnings: `{len(warn)}`',
    '',
    '## Failures',
]
report += [f'- {x}' for x in fail] if fail else ['- NONE']
report += ['', '## Warnings']
report += [f'- {x}' for x in warn] if warn else ['- NONE']
report += ['', '## Gate', 'PASS' if not fail else 'FAIL', '']
REPORT.write_text('\n'.join(report), encoding='utf-8')

for x in fail:
    print('FAIL:', x)
for x in warn:
    print('WARN:', x)
print(f'SOURCE LINES: {len(text.splitlines())}')
print(f'FAILURES: {len(fail)}')
print(f'WARNINGS: {len(warn)}')
print('V21 RUNTIME AUTHORITY QA PASS' if not fail else 'V21 RUNTIME AUTHORITY QA FAIL')
raise SystemExit(0 if not fail else 5)
