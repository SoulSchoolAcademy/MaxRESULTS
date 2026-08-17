#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "tools" / "build_v21_canonical.py"

# The builder source stores JavaScript apostrophes as escaped literals inside the
# Python triple-quoted JS template. Replace those exact serialized forms with
# typographic apostrophes so the emitted JS remains quote-safe without changing
# the intended human wording.
REPLACEMENTS = {
    r"I\\'ve": "I’ve",
    r"isn\\'t": "isn’t",
    r"It\\'s": "It’s",
}

def main() -> int:
    if not TARGET.exists():
        print("ERROR: canonical builder missing")
        return 2
    text = TARGET.read_text(encoding="utf-8")
    found = []
    for old, new in REPLACEMENTS.items():
        if old in text:
            text = text.replace(old, new)
            found.append(old)
    if not found:
        # Fall back to a context-safe rewrite of the exact affected sentence.
        pattern = re.compile(r"Hi\. I.?ve looked at your results\.|This isn.?t your judgment\.\s*<strong>It.?s your map\.</strong>")
        text, n = pattern.subn(lambda m: m.group(0).replace("'", "’"), text)
        if n == 0:
            print("ERROR: no canonical contraction literals found")
            return 3
    TARGET.write_text(text, encoding="utf-8")
    print("CANONICAL BUILDER ESCAPED-QUOTE FIX APPLIED")
    print(f"Replacements: {len(found)}")
    print("Emitted V21 JS will use quote-safe typographic apostrophes.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
