#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"


def check_js(js_text: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
        fh.write(js_text)
        path = fh.name
    try:
        proc = subprocess.run(["node", "--check", path], capture_output=True, text=True)
        if proc.returncode:
            raise RuntimeError(proc.stderr.strip())
    finally:
        Path(path).unlink(missing_ok=True)


def main() -> int:
    if not BUILDER.exists():
        print("ERROR: canonical builder missing")
        return 2
    text = BUILDER.read_text(encoding="utf-8")
    original = text

    # Remove the /100 suffix from the canonical report score presentation.
    text, n_score = re.subn(
        r"(<div class=\\\"v21-cell\\\"><span>OVERALL RESULT</span><b>\"\+Math\.round\(s\)\+\") / 100(</b><small>)",
        r"\1\2",
        text,
        count=1,
    )
    if n_score == 0 and "/ 100</b>" in text:
        text = text.replace(" / 100</b>", "</b>", 1)
        n_score = 1

    # Eliminate the Python invalid-escape warning in the embedded JS regex.
    # Convert a single backslash before s into a doubled backslash in the
    # Python triple-quoted builder source.
    text, n_escape = re.subn(r"(?<!\\)\\s\+", r"\\\\s+", text)

    if text == original:
        print("ERROR: no warning-producing patterns were changed")
        return 3

    # Confirm the embedded canonical JS still parses.
    m = re.search(r'<script id="maxess-results-v21-canonical-js">(.*?)</script>', text, flags=re.S)
    if not m:
        print("ERROR: canonical JS block not found")
        return 4
    check_js(m.group(1))

    BUILDER.write_text(text, encoding="utf-8")
    print("V21 REMAINING WARNINGS FIXED")
    print(f"/100 score presentation replacements: {n_score}")
    print(f"Python escape normalizations: {n_escape}")
    print("Canonical JS syntax: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
