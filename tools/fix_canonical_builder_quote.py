#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "tools" / "build_v21_canonical.py"
OLD = "I've looked at your results."
NEW = "I have looked at your results."

def main() -> int:
    if not TARGET.exists():
        print("ERROR: canonical builder missing")
        return 2
    text = TARGET.read_text(encoding="utf-8")
    if OLD not in text:
        print("ERROR: expected quote collision text not found")
        return 3
    text = text.replace(OLD, NEW)
    TARGET.write_text(text, encoding="utf-8")
    print("CANONICAL BUILDER QUOTE FIX APPLIED")
    print(f"Replaced: {OLD!r}")
    print(f"With: {NEW!r}")
    print("The builder will re-run its JavaScript syntax gate before writing the candidate.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
