#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '20260817 912am RESULTS PAGE CODE'
REPORT = ROOT / 'V21-INTERACTION-RELEASE-QA-V2.md'

text = SOURCE.read_text(encoding='utf-8') if SOURCE.exists() else ''
fail: list[str] = []
warn: list[str] = []
canon = re.search(r'<script id="maxess-results-v21-canonical-js">(.*?)</script>', text, re.S)
js = canon.group(1) if canon else ''
if not canon:
    fail.append('canonical V21 JS layer not found')
css_match = re.search(r'<style id="maxess-results-v21-canonical-css">(.*?)</style>', text, re.S)
css = css_match.group(1) if css_match else ''
for token, label in [
    ('window.MAXESS_RESULT', 'MAXESS_RESULT source of truth'),
    ('Array.isArray(r.dimensions)', 'dimension array normalization'),
    ('list.slice(0,5)', 'five-dimension constraint'),
    ("data-results-state','awaiting'", 'missing-result safe state'),
    ("data-results-state','ready'", 'ready-result state'),
]:
    if token not in js: fail.append(f'missing runtime contract behavior: {label}')
for token, label in [
    ("addEventListener('click',listen)", 'Listen click handler'),
    ("root.querySelectorAll('.v21-dim')", 'dimension selection wiring'),
    ('scrollIntoView({behavior:', 'dimension explanation focus'),
    ("CustomEvent('maxess:naya-listen'", 'Naya listen fallback event'),
]:
    if token not in js: fail.append(f'missing interaction behavior: {label}')
for token, label in [
    ('aria-label="Listen to Naya interpret your MAXESS results"', 'Listen accessible name'),
    ('role="list"', 'dimension list semantics'),
    ('role="listitem"', 'dimension item semantics'),
    ('.v21-listen:focus-visible', 'Listen visible keyboard focus'),
]:
    if token not in text and token not in css: fail.append(f'missing accessibility behavior: {label}')
for token, label in [
    ('prefers-reduced-motion:reduce', 'reduced motion'),
    ('@media(max-width:980px)', 'tablet breakpoint'),
    ('@media(max-width:760px)', 'mobile breakpoint'),
    ('@media(max-width:480px)', 'narrow mobile breakpoint'),
    ('@media print', 'print stylesheet'),
]:
    if token not in css: fail.append(f'missing responsive/output behavior: {label}')
for token, label in [
    ('break-inside:avoid', 'print card/page-break control'),
    ('.v21-report-grid', 'report print grouping'),
    ('.v21-three', 'next-move print grouping'),
]:
    if token not in css: warn.append(f'print/PDF intent not strongly expressed: {label}')
listen_count = len(re.findall(r'class="v21-listen"', js))
if listen_count != 1: fail.append(f'canonical Listen CTA count = {listen_count}, expected 1')
# Do not treat legitimate mastery thresholds such as 91 as user scores.
# Inspect only static numeric literals embedded in rendered UI strings, excluding stage logic.
stage_function = re.search(r'function stage\(s\)\{.*?\n  \}', js, re.S)
js_ui = js if not stage_function else js.replace(stage_function.group(0), '')
render_literals = re.findall(r"(?<![A-Za-z0-9_])(?:82|91|79|74|68)(?![A-Za-z0-9_])", js_ui)
for score in sorted(set(render_literals)):
    fail.append(f'possible hard-coded score literal survives canonical rendered UI: {score}')
if "detail.innerHTML=" not in js: fail.append('dimension interaction does not render explanation content')
if 'cards.length>=18' not in js: fail.append('18 Naya Masters source extraction is not constrained to 18')
if 'naya-playground' not in js: fail.append('Playground preservation hook is missing')
report = ['# MAXESS V21 — INTERACTION / RELEASE QA V2','',f'- Source lines: `{len(text.splitlines())}`',f'- Failures: `{len(fail)}`',f'- Warnings: `{len(warn)}`','', '## Failures']
report += [f'- {x}' for x in fail] if fail else ['- NONE']
report += ['', '## Warnings'] + ([f'- {x}' for x in warn] if warn else ['- NONE']) + ['', '## Gate', 'PASS' if not fail else 'FAIL', '']
REPORT.write_text('\n'.join(report), encoding='utf-8')
for x in fail: print('FAIL:', x)
for x in warn: print('WARN:', x)
print(f'SOURCE LINES: {len(text.splitlines())}')
print(f'FAILURES: {len(fail)}')
print(f'WARNINGS: {len(warn)}')
print('V21 INTERACTION / RELEASE QA V2 PASS' if not fail else 'V21 INTERACTION / RELEASE QA V2 FAIL')
raise SystemExit(0 if not fail else 5)
