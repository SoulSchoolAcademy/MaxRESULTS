#!/usr/bin/env python3
"""Prove five real MAXESS micro-edits without touching the working tree.

The harness copies the authoritative builder to a temporary file, applies five
real targeted edits using the same functions as fast_edit_maxess.py, validates
Python/JS syntax after each edit, and emits before/after hashes plus diff size.
"""
from __future__ import annotations

import difflib
import importlib.util
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"
TOOL = ROOT / "tools" / "fast_edit_maxess.py"


spec = importlib.util.spec_from_file_location("fast_edit", TOOL)
if not spec or not spec.loader:
    raise SystemExit("Cannot load fast_edit_maxess.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


TESTS = [
    ("orb-size", -15),
    ("naya-up", 6),
    ("primary-button-electric", None),
    ("score-size", 10),
    ("naya-headline-spacing", 16),
]


def main() -> int:
    original = BUILDER.read_text(encoding="utf-8")
    current = original
    print("MAXESS FAST EDIT SYSTEM PROOF")
    print("WORKING TREE: UNTOUCHED")
    print(f"BASE BUILDER SHA: {module.sha256(original)}")

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as f:
        temp_path = Path(f.name)
        f.write(original)

    try:
        for index, (edit, value) in enumerate(TESTS, 1):
            before = current
            before_sha = module.sha256(before)
            after = module.EDITORS[edit](before, value if value is not None else 0)
            after_sha = module.sha256(after)
            if before_sha == after_sha:
                raise SystemExit(f"EDIT {index} FAILED: no source delta for {edit}")
            module.validate_node(after)
            diff_lines = list(difflib.unified_diff(before.splitlines(), after.splitlines(), lineterm=""))
            changed = len(diff_lines)
            current = after
            print(f"EDIT {index}: PASS | {edit} | hash {before_sha[:12]} -> {after_sha[:12]} | diff-lines {changed}")
        print("FIVE MICRO-EDITS: PASS")
        print(f"FINAL TEMP BUILDER SHA: {module.sha256(current)}")
        print("TARGETED SYNTAX: PASS")
        print("REAL SOURCE DELTA: VERIFIED")
        return 0
    finally:
        temp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
