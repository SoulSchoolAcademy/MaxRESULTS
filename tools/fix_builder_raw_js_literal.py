#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'

text = BUILDER.read_text(encoding='utf-8')
needle = 'JS = """'
replacement = 'JS = r"""'
count = text.count(needle)
if count != 1:
    raise SystemExit(f'ERROR: expected exactly one JS triple-quoted literal, found {count}')

BUILDER.write_text(text.replace(needle, replacement, 1), encoding='utf-8')
print('BUILDER JS PAYLOAD MARKED RAW')
print('Python invalid-escape source warning should be eliminated')
