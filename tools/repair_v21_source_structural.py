#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / 'tools' / 'build_v21_canonical.py'
s = P.read_text(encoding='utf-8')

# Replace stage() by locating its boundaries structurally.
start = s.find('function stage(s)')
end = s.find('function dimCopy', start)
if start < 0 or end < 0:
    raise SystemExit(f'STAGE BOUNDARY NOT FOUND: start={start} end={end}')
new_stage = '''function stage(s){
    if(s==null) return '';
    return s>=91?'Mastering':
           s>=76?'Advancing':
           s>=51?'Developing':
           s>=21?'Foundation':
           'Supporting';
  }
  '''
s = s[:start] + new_stage + s[end:]

# Restrict changes to the JS payload only.
js_start = s.find('JS = """')
js_end = s.find('"""', js_start + 8)
if js_start < 0 or js_end < 0:
    raise SystemExit(f'JS PAYLOAD BOUNDARY NOT FOUND: start={js_start} end={js_end}')
js = s[js_start:js_end]

# Remove score-denominator UI labels while preserving calculations.
js2 = js.replace("+' / 100</b>", "+'</b>")
if js2 == js:
    raise SystemExit('No /100 display literal found in canonical JS payload')
s = s[:js_start] + js2 + s[js_end:]

# Make provenance explicit in the canonical markup before rendering.
marker = '<div class="v21-shell">'
if 'data-results-data-source="window.MAXESS_RESULT"' not in js2:
    replacement = '<div class="v21-shell" data-results-data-source="window.MAXESS_RESULT">'
    if marker not in s:
        raise SystemExit('Canonical shell marker not found')
    s = s.replace(marker, replacement, 1)

P.write_text(s, encoding='utf-8')
print('V21 STRUCTURAL SOURCE REPAIR COMPLETE')
print('Mastery: Supporting → Foundation → Developing → Advancing → Mastering')
print('Canonical /100 UI labels removed')
print('Result Contract provenance embedded in canonical shell')
