#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'

def main() -> int:
    text = BUILDER.read_text(encoding='utf-8')
    start = text.find('JS = """')
    end = text.find('"""', start + 8)
    if start < 0 or end < 0:
        raise SystemExit('canonical JS block not found')
    head = text[:start]
    block = text[start:end]
    tail = text[end:]
    changed = block.replace(r'\s', r'\\s')
    if changed == block:
        raise SystemExit('no invalid-escape candidate found in canonical JS block')
    BUILDER.write_text(head + changed + tail, encoding='utf-8')
    print('BUILDER WARNING FIX APPLIED')
    print('Canonical JS embedded regex escapes normalized')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
