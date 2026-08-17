#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'

def main() -> int:
    text = BUILDER.read_text(encoding='utf-8')
    target = 'JS = """'
    if text.count(target) != 1:
        raise SystemExit(f'ERROR: expected exactly one JS assignment literal, found {text.count(target)}')
    text = text.replace(target, 'JS = r"""', 1)
    BUILDER.write_text(text, encoding='utf-8')
    print('BUILDER JS PAYLOAD CONVERTED TO RAW STRING')
    print('Changed: JS = """ -> JS = r"""')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
