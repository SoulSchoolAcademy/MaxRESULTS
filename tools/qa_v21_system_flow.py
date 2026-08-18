#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / '20260817 912am RESULTS PAGE CODE'
REPORT = ROOT / 'V21-SYSTEM-FLOW-QA.md'
fail = []
warn = []

rt = RESULTS.read_text(encoding='utf-8') if RESULTS.exists() else ''
if not RESULTS.exists():
    fail.append('Results working artifact not found')

required_contract = [
    ('window.MAXESS_RESULT', 'authoritative runtime result source'),
    ('function result()', 'result resolver'),
    ('Array.isArray(r.dimensions)', 'dimension normalization'),
    ('list.slice(0,5)', 'five-dimension constraint'),
    ("data-results-state','awaiting'", 'safe missing-data state'),
    ("data-results-state','ready'", 'ready state'),
]
for token, label in required_contract:
    if token not in rt:
        fail.append('missing Results contract behavior: ' + label)

required_experience = [
    ('YOUR RESULT', 'result section'),
    ('YOUR FIVE DIMENSIONS', 'dimensions section'),
    ('YOUR PERSONALIZED REPORT', 'report section'),
    ('YOUR STRENGTH', 'strength section'),
    ('18 NAYA MASTERS', 'Masters section'),
    ('LISTEN TO NAYA', 'Naya CTA'),
]
for token, label in required_experience:
    if token not in rt:
        fail.append('missing Results experience element: ' + label)

# Current V21 narrative may use the governed replacement for the older
# Playground / Lever / Next Move sections. These are warnings, not hard
# failures, so the validator cannot force obsolete UI back into production.
if 'NAYA · IN PRACTICE' not in rt:
    warn.append('current V21 narrative marker NAYA · IN PRACTICE not found')

if 'dimensions' not in rt:
    fail.append('Results lacks dimensions contract field')

if not any(x in rt for x in ('overallScore', 'masterScore', 'score', 'overall')):
    fail.append('Results lacks accepted overall score field')

if 'This page does not invent a score when real result data is unavailable.' not in rt:
    fail.append('Results lacks no-fabrication safety message')

# Never fetch or depend on the legacy SoulSchoolAcademy/maxess repository.
# Results-side system-flow QA must be deterministic and repository-local.
if 'SoulSchoolAcademy/maxess' in rt or 'raw.githubusercontent.com/SoulSchoolAcademy/maxess' in rt:
    fail.append('working Results artifact contains an unauthorized legacy repository dependency')

report = [
    '# MAXESS V21 — SYSTEM FLOW QA',
    '',
    '- Journey: `MAXESS Assessment → Result Contract → window.MAXESS_RESULT → Results`',
    '- Results source: `20260817 912am RESULTS PAGE CODE`',
    f'- Results source lines: `{len(rt.splitlines())}`',
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
print(f'Results source lines: {len(rt.splitlines())}')
print(f'FAILURES: {len(fail)}')
print(f'WARNINGS: {len(warn)}')
print('V21 SYSTEM FLOW QA PASS' if not fail else 'V21 SYSTEM FLOW QA FAIL')
raise SystemExit(0 if not fail else 5)
