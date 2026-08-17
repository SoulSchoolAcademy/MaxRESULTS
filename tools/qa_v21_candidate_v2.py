#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "BASELINE-WORKING.html"
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-CANDIDATE-QA-V2.md"

REQUIRED = [
    "YOUR FIVE DIMENSIONS", "YOUR PERSONALIZED REPORT", "YOUR PATTERN",
    "YOUR STRENGTH", "YOUR LEVER", "YOUR NEXT MOVE", "18 NAYA MASTERS",
    "PLAYGROUND", "YOUR AI MASTERY JOURNEY", "window.MAXESS_RESULT",
    "LISTEN TO NAYA"
]

class MarkupParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids: dict[str,int] = {}
        self.in_script = False
        self.in_style = False
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ("script", "style"):
            if tag.lower() == "script": self.in_script = True
            if tag.lower() == "style": self.in_style = True
            return
        for k,v in attrs:
            if k.lower() == "id" and v:
                self.ids[v] = self.ids.get(v,0) + 1
    def handle_endtag(self, tag):
        if tag.lower() == "script": self.in_script = False
        if tag.lower() == "style": self.in_style = False

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def canonical_js(text: str) -> str:
    start = text.find('<script id="maxess-results-v21-canonical-js">')
    if start < 0: return ''
    start = text.find('>', start) + 1
    end = text.find('</script>', start)
    return text[start:end] if end >= 0 else ''

def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    if not BASELINE.exists(): failures.append('BASELINE-WORKING.html missing')
    if not SOURCE.exists(): failures.append('working Results source missing')
    if failures:
        print(*[f'FAIL: {x}' for x in failures], sep='\n'); return 5

    candidate = SOURCE.read_text(encoding='utf-8')
    baseline = BASELINE.read_text(encoding='utf-8')
    parser = MarkupParser(); parser.feed(candidate)
    dupes = sorted((k,v) for k,v in parser.ids.items() if v > 1)

    for token in REQUIRED:
        if token not in candidate: failures.append(f'missing required content: {token}')
    if candidate.count('id="maxess-results-v21-canonical-js"') != 1: failures.append('canonical V21 JS marker count != 1')
    if candidate.count('id="maxess-results-v21-canonical-css"') != 1: failures.append('canonical V21 CSS marker count != 1')

    # Duplicate IDs are checked only in actual HTML markup, not strings inside JS/CSS.
    if dupes:
        failures.append('active/static duplicate IDs: ' + ', '.join(f'{k} ({v})' for k,v in dupes))

    js = canonical_js(candidate)
    if not js: failures.append('canonical V21 JS body missing')
    else:
        if "Math.round(s)" not in js: failures.append('canonical score is not dynamically derived from result score')
        if "ds.map" not in js: failures.append('canonical dimensions are not dynamically rendered')
        if "window.MAXESS_RESULT" not in js: failures.append('canonical JS does not read window.MAXESS_RESULT')
        if "Supporting" not in js or "Foundation" not in js or "Developing" not in js or "Advancing" not in js or "Mastering" not in js:
            failures.append('canonical mastery-stage model does not contain all five stages')
        for demo in ('82','91','79','74','68'):
            # Flag only literal rendered score markup, not comparison thresholds or prose.
            if re.search(rf'v21-score-number[^>]*>\s*{re.escape(demo)}\s*<', js):
                failures.append(f'hard-coded demo score in canonical rendered markup: {demo}')
        if '/ 100' in js or 'out of 100' in js.lower():
            warnings.append('canonical layer contains a /100-style score presentation')

    if 'window.MAXESS_RESULT' not in candidate: failures.append('MAXESS_RESULT source missing')
    if '@media print' not in candidate: failures.append('dedicated print/PDF CSS missing')
    if 'break-inside' not in candidate: warnings.append('print CSS lacks visible break-inside controls')
    for marker in ('id="naya-playground"','18 NAYA','MAXESS'):
        if marker in baseline and marker not in candidate: failures.append(f'preservation regression: {marker}')

    builder = ROOT / 'tools' / 'build_v21_canonical.py'
    if builder.exists() and r'\s' in builder.read_text(encoding='utf-8'):
        warnings.append('canonical builder contains a Python invalid-escape warning candidate')

    report = [
        '# MAXESS V21 — CANDIDATE QA V2','',
        f'- Candidate lines: `{len(candidate.splitlines())}`',
        f'- Candidate SHA-256: `{sha(SOURCE)}`',
        f'- Markup duplicate IDs: `{len(dupes)}`',
        f'- Failures: `{len(failures)}`',
        f'- Warnings: `{len(warnings)}`','',
        '## Failures'
    ] + ([f'- {x}' for x in failures] or ['- NONE']) + ['','## Warnings'] + ([f'- {x}' for x in warnings] or ['- NONE']) + ['','## Gate', 'PASS' if not failures else 'FAIL','']
    REPORT.write_text('\n'.join(report), encoding='utf-8')
    print(f'BASELINE SHA-256: {sha(BASELINE)}')
    for x in failures: print('FAIL:',x)
    for x in warnings: print('WARN:',x)
    print(f'CANDIDATE LINES: {len(candidate.splitlines())}')
    print(f'MARKUP DUPLICATE IDS: {len(dupes)}')
    print(f'FAILURES: {len(failures)}')
    print(f'WARNINGS: {len(warnings)}')
    print('V21 CANDIDATE QA V2 PASS' if not failures else 'V21 CANDIDATE QA V2 FAIL')
    return 0 if not failures else 5

if __name__ == '__main__': raise SystemExit(main())
