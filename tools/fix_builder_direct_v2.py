#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"


def main():
    text = BUILDER.read_text(encoding="utf-8")
    original = text
    changes = []

    # Make the embedded JavaScript payload raw so Python does not interpret JS regex escapes.
    text, n = re.subn(r'(?m)^JS = """$', 'JS = r"""', text, count=1)
    if n:
        changes.append("embedded JS converted to raw Python string")

    # Remove the visible /100 suffix from the canonical report score.
    text, n = re.subn(
        r"Math\.round\(s\)\+?'\s*/\s*100'",
        "Math.round(s)+' '",
        text,
        count=1,
    )
    if n:
        changes.append("removed report /100 suffix")

    # Remove the visible /100 suffix from dimension detail.
    text, n = re.subn(
        r"Math\.round\(d\.score\|\|0\)\+'\s*/\s*100'",
        "Math.round(d.score||0)+' '",
        text,
        count=1,
    )
    if n:
        changes.append("removed dimension-detail /100 suffix")

    if text == original:
        raise SystemExit("ERROR: no direct builder changes matched")

    BUILDER.write_text(text, encoding="utf-8")
    print("BUILDER DIRECT V2 APPLIED")
    for change in changes:
        print("-", change)


if __name__ == "__main__":
    main()
