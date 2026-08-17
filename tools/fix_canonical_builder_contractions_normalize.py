#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "tools" / "build_v21_canonical.py"

# Normalize every form that can appear inside the generated JS source string.
# Handles straight apostrophes, escaped apostrophes, and curly apostrophes.
REPLACEMENTS = [
    (re.compile(r"I(?:\\)?['’]ve", re.I), "I have"),
    (re.compile(r"(?:isn)(?:\\)?['’]t", re.I), "is not"),
    (re.compile(r"(?:it|It)(?:\\)?['’]s"), "It is"),
]


def syntax_check(text: str) -> None:
    # Extract canonical JS from the Python triple-quoted JS fragment and check it.
    m = re.search(r'<script id="maxess-results-v21-canonical-js">(.*?)</script>', text, re.S)
    if not m:
        raise RuntimeError("canonical JS fragment not found")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
        fh.write(m.group(1))
        path = fh.name
    proc = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    Path(path).unlink(missing_ok=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip())


def main() -> int:
    if not TARGET.exists():
        print("ERROR: canonical builder missing")
        return 2

    text = TARGET.read_text(encoding="utf-8")
    original = text
    changed = 0
    for pattern, replacement in REPLACEMENTS:
        text, n = pattern.subn(replacement, text)
        changed += n

    if changed == 0:
        print("ERROR: no contraction variants found in canonical builder")
        for needle in ["I've", "I\\'ve", "isn't", "isn\\'t", "It's", "It\\'s"]:
            print(f"{needle}: {'FOUND' if needle in original else 'not found'}")
        return 3

    # Prove the canonical JS is valid BEFORE committing the builder mutation to disk.
    syntax_check(text)

    TARGET.write_text(text, encoding="utf-8")
    print("CANONICAL BUILDER CONTRACTIONS NORMALIZED")
    print(f"Replacements: {changed}")
    print("Canonical JS syntax: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
