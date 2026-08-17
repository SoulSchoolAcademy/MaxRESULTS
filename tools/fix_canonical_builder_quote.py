#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "tools" / "build_v21_canonical.py"

def main() -> int:
    if not TARGET.exists():
        print("ERROR: canonical builder missing")
        return 2
    text = TARGET.read_text(encoding="utf-8")
    patterns = [
        (r"Hi\. I've looked at your results\.", "Hi. I have looked at your results."),
        (r"This isn't your judgment\. <strong>It's your map\.</strong>", "This is not your judgment. <strong>It is your map.</strong>"),
    ]
    changed = 0
    for pattern, replacement in patterns:
        text2, n = re.subn(pattern, replacement, text)
        text = text2
        changed += n
    if changed == 0:
        # Also normalize any quote-sensitive literal strings inside the generated JS
        # without depending on the exact Python source serialization.
        if "I\u2019ve looked at your results." in text:
            text = text.replace("I\u2019ve looked at your results.", "I have looked at your results.")
            changed += 1
        if "I’ve looked at your results." in text:
            text = text.replace("I’ve looked at your results.", "I have looked at your results.")
            changed += 1
    if changed == 0:
        print("ERROR: no quote-sensitive canonical copy found")
        return 3
    TARGET.write_text(text, encoding="utf-8")
    print("CANONICAL BUILDER QUOTE FIX APPLIED")
    print(f"Quote-sensitive replacements: {changed}")
    print("Canonical builder will run its JavaScript syntax gate before writing the candidate.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
