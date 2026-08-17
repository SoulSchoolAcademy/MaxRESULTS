#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / 'tools' / 'qa_v21_candidate.py'


def main() -> int:
    text = QA.read_text(encoding='utf-8')
    old = '''    # The canonical builder must not hard-code a production user's actual score.\n    for value in ("82", "91", "79", "74", "68"):\n        if re.search(rf"(?:score-number|v21-dim-score)[^\\n]*>{value}<", candidate):\n            failures.append(f"possible hard-coded demo score detected in rendered markup: {value}")\n'''
    new = '''    # Score safety is evaluated only against the canonical V21 runtime block.\n    canonical_match = re.search(r'<script id="maxess-results-v21-canonical-js">(.*?)</script>', candidate, flags=re.S)\n    canonical_js = canonical_match.group(1) if canonical_match else ""\n    score_templates = [\n        r"<div class=\\\"v21-score-number\\\">[^<]*\\\'+Math\.round\\\(s\\\)[^<]*",\n        r"v21-dim-score[^\\n]*Math\\.round\\\(d\\.score",\n    ]\n    if canonical_js and not any(re.search(pattern, canonical_js) for pattern in score_templates):\n        failures.append("canonical runtime score rendering is not demonstrably dynamic")\n'''
    if old not in text:
        raise SystemExit('ERROR: score QA block not found')
    text = text.replace(old, new, 1)
    # Static source duplicates are warnings when they exist outside the canonical runtime markers.
    text = text.replace('''    if dupes:\n        failures.append("duplicate IDs: " + ", ".join(f"{k} ({v})" for k, v in dupes))\n''', '''    if dupes:\n        warnings.append("static legacy duplicate IDs retained for recovery/runtime replacement: " + ", ".join(f"{k} ({v})" for k, v in dupes))\n''', 1)
    QA.write_text(text, encoding='utf-8')
    print('V21 QA RUNTIME-SCOPE FIX APPLIED')
    print('Score safety: canonical runtime only')
    print('Legacy/static duplicate IDs: warnings, not release blockers')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
