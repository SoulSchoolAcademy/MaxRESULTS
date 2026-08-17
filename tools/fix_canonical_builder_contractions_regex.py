#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'tools' / 'build_v21_canonical.py'

REPLACEMENTS = [
    (re.compile(r"I[\u0027\u2019]ve looked at your results\."), 'I have looked at your results.'),
    (re.compile(r"isn[\u0027\u2019]t your judgment\. " ), 'is not your judgment. '),
    (re.compile(r"[Ii]t[\u0027\u2019]s your map\."), 'It is your map.'),
]


def main() -> int:
    if not TARGET.exists():
        print('ERROR: canonical builder missing')
        return 2
    text = TARGET.read_text(encoding='utf-8')
    original = text
    total = 0
    for pattern, replacement in REPLACEMENTS:
        text, count = pattern.subn(replacement, text)
        total += count
    if total == 0:
        print('ERROR: no contraction patterns found')
        # Print a targeted diagnostic so the next run is deterministic.
        for needle in ('looked at your results', 'your judgment', 'your map'):
            pos = text.find(needle)
            print(f'{needle}: ' + ('FOUND' if pos >= 0 else 'NOT FOUND'))
        return 3
    TARGET.write_text(text, encoding='utf-8')
    print('CANONICAL BUILDER CONTRACTIONS FIXED')
    print(f'Replacements: {total}')
    print(f'Changed: {text != original}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
