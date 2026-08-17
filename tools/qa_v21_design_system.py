#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '20260817 912am RESULTS PAGE CODE'
REPORT = ROOT / 'V21-DESIGN-SYSTEM-QA.md'

text = SOURCE.read_text(encoding='utf-8') if SOURCE.exists() else ''
canon = re.search(r'<style id="maxess-results-v21-canonical-css">(.*?)</style>.*?<script id="maxess-results-v21-canonical-js">(.*?)</script>', text, re.S)
fail=[]; warn=[]
if not canon:
    fail.append('canonical CSS/JS layer not found')
else:
    css, js = canon.group(1), canon.group(2)
    checks = {
        'dark section treatment': '.v21-dark' in css,
        'light section treatment': '.v21-light' in css,
        'purple section treatment': '.v21-purple' in css,
        'primary score orb': '.v21-score-orb' in css,
        'five dimension orb treatment': '.v21-dim' in css and 'border-radius:50%' in css,
        'premium Listen styling': '.v21-listen' in css and 'box-shadow' in css,
        'Listen hover': '.v21-listen:hover' in css,
        'Listen focus': '.v21-listen:focus-visible' in css,
        'responsive 980': '@media(max-width:980px)' in css,
        'responsive 760': '@media(max-width:760px)' in css,
        'responsive 480': '@media(max-width:480px)' in css,
        'reduced motion': 'prefers-reduced-motion:reduce' in css,
        'print foundation': '@media print' in css,
        'large hero score': 'font-size:clamp(94px,13vw,170px)' in css,
        'strong section headline': '.v21-section-title' in css,
        'report surface': '.v21-report' in css,
        'deep card surfaces': '.v21-card' in css,
    }
for label, ok in checks.items():
    if not ok: fail.append(f'missing design-system requirement: {label}')

# Visual rhythm in canonical JS output order.
if canon:
    required = ['v21-dark','v21-dark','v21-light','v21-light','v21-dark','v21-light','v21-purple','v21-dark','v21-dark','v21-light','v21-purple']
    actual = re.findall(r'<section class="v21-section\s+(v21-(?:dark|light|purple))', js)
    if actual[:len(required)] != required:
        warn.append(f'canonical section color rhythm differs from preferred pattern: {actual}')

# Interaction expectations.
for token, label in [
    ('addEventListener(\'click\',listen)', 'Naya Listen interaction'),
    ('.v21-dim', 'dimension interactions'),
    ('scrollIntoView', 'dimension detail focus behavior'),
    ("root.setAttribute('data-results-state','ready')", 'ready-state marker'),
]:
    if token not in js: fail.append(f'missing interaction requirement: {label}')

report = ['# MAXESS V21 — DESIGN SYSTEM QA','',f'- Failures: `{len(fail)}`',f'- Warnings: `{len(warn)}`','', '## Failures']
report += [f'- {x}' for x in fail] if fail else ['- NONE']
report += ['', '## Warnings']
report += [f'- {x}' for x in warn] if warn else ['- NONE']
report += ['', '## Gate', 'PASS' if not fail else 'FAIL', '']
REPORT.write_text('\n'.join(report), encoding='utf-8')
for x in fail: print('FAIL:', x)
for x in warn: print('WARN:', x)
print(f'FAILURES: {len(fail)}')
print(f'WARNINGS: {len(warn)}')
print('V21 DESIGN SYSTEM QA PASS' if not fail else 'V21 DESIGN SYSTEM QA FAIL')
raise SystemExit(0 if not fail else 5)
