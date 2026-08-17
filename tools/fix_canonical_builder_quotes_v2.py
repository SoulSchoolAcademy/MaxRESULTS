#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "tools" / "build_v21_canonical.py"

REPLACEMENTS = [
    ("I\\\\'ve looked at your results.", "I have looked at your results."),
    ("This isn\\\\'t your judgment. <strong>It\\\\'s your map.</strong>", "This is not your judgment. <strong>It is your map.</strong>"),
    ("MAXESS is designed for people who want exceptional results from AI—not “good enough.”", "MAXESS is designed for people who want exceptional results from AI—not ‘good enough.’"),
]

def main() -> int:
    text = TARGET.read_text(encoding="utf-8")
    changed = 0
    for old, new in REPLACEMENTS:
        if old in text:
            text = text.replace(old, new)
            changed += 1
    if changed == 0:
        print("ERROR: no matching canonical quote literals found")
        return 3
    TARGET.write_text(text, encoding="utf-8")
    print(f"CANONICAL BUILDER QUOTES FIXED: {changed}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
