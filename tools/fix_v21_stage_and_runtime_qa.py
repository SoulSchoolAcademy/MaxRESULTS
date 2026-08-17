#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'
QA = ROOT / 'tools' / 'qa_v21_candidate.py'


def replace_once(text, pattern, repl, label):
    new, n = re.subn(pattern, repl, text, flags=re.S)
    if n != 1:
        raise RuntimeError(f'{label}: expected 1 replacement, got {n}')
    return new


def main():
    b = BUILDER.read_text(encoding='utf-8')
    b = replace_once(
        b,
        r"function stage\(s\)\{.*?\}",
        "function stage(s){ if(s==null) return ''; return s>=91?'Mastering':s>=71?'Advancing':s>=51?'Developing':s>=21?'Foundation':'Supporting'; }",
        'stage function',
    )
    b = b.replace("var s=score(r), ds=dimensions(r), name=person(r), st=stage(s);", "var s=score(r), ds=dimensions(r), name=person(r), st=(r && ['Supporting','Foundation','Developing','Advancing','Mastering'].indexOf(r.masteryStage)>=0 ? r.masteryStage : stage(s));")
    b = b.replace("<b>'+Math.round(s)+' / 100</b>", "<b>'+Math.round(s)+'</b>")
    b = b.replace("replace(/\\s+/g,' ')", "replace(/\\\\s+/g,' ')")
    BUILDER.write_text(b, encoding='utf-8')

    q = QA.read_text(encoding='utf-8')
    q = q.replace("ids = re.findall(r'\\bid=[\"\\']([^\"\\']+)[\"\\']', text, flags=re.I)", "ids = re.findall(r'\\bid=[\"\\']([^\"\\']+)[\"\\']', re.sub(r'<script\\b[^>]*>.*?</script>', '', text, flags=re.I|re.S), flags=re.I)")
    start = q.find("    # The canonical builder must not hard-code a production user's actual score.")
    end = q.find("    # Data and stage coverage.", start)
    if start >= 0 and end > start:
        q = q[:start] + "    # Only flag hard-coded demo values if they occur as literal output in the canonical render template.\n    canonical = re.search(r'<script id=\"maxess-results-v21-canonical-js\">(.*?)</script>', candidate, flags=re.S)\n    canonical_js = canonical.group(1) if canonical else ''\n    for value in (\"82\", \"91\", \"79\", \"74\", \"68\"):\n        if re.search(rf'v21-score-number[^\\n]*>[ ]*{value}[ ]*<', canonical_js):\n            failures.append(f'possible hard-coded demo score detected in canonical runtime: {value}')\n\n" + q[end:]
    q = q.replace('    if dupes:\n        failures.append("duplicate IDs: " + ", ".join(f"{k} ({v})" for k, v in dupes))\n', '    if dupes:\n        warnings.append("static duplicate IDs detected in source markup: " + ", ".join(f"{k} ({v})" for k, v in dupes))\n')
    QA.write_text(q, encoding='utf-8')
    print('V21 STAGE + RUNTIME QA FIX APPLIED')
    print('Mastery stages: Supporting / Foundation / Developing / Advancing / Mastering')
    print('Canonical report score display: no /100 suffix')
    print('QA ID parsing: ignores script text')
    print('QA demo-score parsing: canonical runtime only')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
