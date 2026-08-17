#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"


def main() -> int:
    text = BUILDER.read_text(encoding="utf-8")

    replacements = {
        "'<b>'+Math.round(s)+' / 100</b>'": "'<b>'+Math.round(s)+'</b>'",
        "replace(/\\s+/g,' ')": "replace(/\\\\s+/g,' ')",
    }

    changed = 0
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new)
            changed += 1

    if changed != len(replacements):
        missing = [old for old in replacements if old not in BUILDER.read_text(encoding="utf-8")]
        raise SystemExit(f"ERROR: expected {len(replacements)} hygiene literals; missing {len(missing)}")

    BUILDER.write_text(text, encoding="utf-8")
    print("BUILDER HYGIENE FINALIZED")
    print(f"Replacements: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
