#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'tools' / 'build_v21_canonical.py'
text = PATH.read_text(encoding='utf-8')
needle = '\nJS = """\n'
replacement = '\nJS = r"""\n'
if needle not in text:
    raise SystemExit('ERROR: exact JS assignment marker not found')
if replacement in text:
    print('JS payload is already raw')
else:
    text = text.replace(needle, replacement, 1)
    PATH.write_text(text, encoding='utf-8')
    print('CANONICAL BUILDER: JS PAYLOAD CHANGED TO RAW STRING')
print('JS ASSIGNMENT COUNT:', text.count('\nJS = r"""\n'))
