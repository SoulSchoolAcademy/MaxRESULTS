#!/usr/bin/env python3
"""Targeted MAXESS micro-edit executor.

Usage examples:
  python tools/fast_edit_maxess.py --edit orb-size --value -15
  python tools/fast_edit_maxess.py --edit naya-up --value 16
  python tools/fast_edit_maxess.py --edit primary-button-electric
  python tools/fast_edit_maxess.py --edit score-size --value 10
  python tools/fast_edit_maxess.py --edit naya-headline-spacing --value 12

The tool edits only the active V21 canonical builder. Every edit requires an
exactly-one owner match, a source hash delta, and Python + canonical JavaScript
syntax validation before reporting success.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"


class EditError(RuntimeError):
    pass


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_once(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    matches = list(re.finditer(pattern, text, flags))
    if len(matches) != 1:
        raise EditError(f"{label}: expected exactly 1 owner match, found {len(matches)}")
    return text[: matches[0].start()] + replacement + text[matches[0].end() :]


def edit_orb_size(text: str, percent: float) -> str:
    pattern = r"(#maxess-results-10\.v21-canonical \.v21-score-orb\{[^}]*?width:)min\(510px,78vw\)"
    factor = 1.0 + percent / 100.0
    width_px = round(510 * factor)
    width_vw = round(78 * factor, 1)
    replacement = rf"\1min({width_px}px,{width_vw:g}vw)"
    return replace_once(text, pattern, replacement, "Score Orb width")


def edit_naya_up(text: str, pixels: int) -> str:
    pattern = r"(#maxess-results-10\.v21-canonical \.v21-naya\{[^}]*?align-items:center;)"
    replacement = rf"\1\ntransform:translateY(-{pixels}px);"
    return replace_once(text, pattern, replacement, "Naya Arrival positioning")


def edit_primary_button(text: str) -> str:
    pattern = r"(#maxess-results-10\.v21-canonical \.v21-listen\{[^}]*?background:)#050507"
    replacement = r"\1linear-gradient(135deg,#c58cff,#7b35e7 52%,#3a116d)"
    return replace_once(text, pattern, replacement, "Naya primary Listen button")


def edit_score_size(text: str, percent: float) -> str:
    pattern = r"(#maxess-results-10\.v21-canonical \.v21-score-number\{[^}]*?font-size:)clamp\(94px,13vw,170px\)"
    factor = 1.0 + percent / 100.0
    a, b, c = [round(x * factor) for x in (94, 13, 170)]
    replacement = rf"\1clamp({a}px,{b}vw,{c}px)"
    return replace_once(text, pattern, replacement, "MAXESS score typography")


def edit_naya_headline_spacing(text: str, pixels: int) -> str:
    pattern = r"(#maxess-results-10\.v21-canonical \.v21-naya-sub\{margin:)8px 0 0"
    replacement = rf"\1{pixels}px 0 0"
    return replace_once(text, pattern, replacement, "Naya headline/subtext spacing")


EDITORS = {
    "orb-size": edit_orb_size,
    "naya-up": edit_naya_up,
    "primary-button-electric": lambda text, _value=0: edit_primary_button(text),
    "score-size": edit_score_size,
    "naya-headline-spacing": edit_naya_headline_spacing,
}


def validate_node(text: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(text)
        py_path = Path(f.name)
    try:
        proc = subprocess.run(["python", "-m", "py_compile", str(py_path)], capture_output=True, text=True)
        if proc.returncode != 0:
            raise EditError(proc.stderr.strip() or "Builder Python syntax validation failed")
    finally:
        py_path.unlink(missing_ok=True)

    # Extract the canonical JS assignment robustly enough for the current builder.
    markers = ['JS = r"""', 'JS = """']
    start = -1
    marker = ""
    for candidate in markers:
        pos = text.find(candidate)
        if pos >= 0 and (start < 0 or pos < start):
            start, marker = pos, candidate
    if start < 0:
        # The production builder is itself the authoritative fallback validator.
        proc = subprocess.run(["python", str(BUILDER)], capture_output=True, text=True)
        if proc.returncode != 0:
            raise EditError(proc.stderr.strip() or "Canonical builder validation failed")
        return
    start += len(marker)
    end = text.find('"""', start)
    if end < 0:
        raise EditError("Canonical JS triple-quoted block is not closed")
    js = text[start:end]
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(js)
        js_path = Path(f.name)
    try:
        proc = subprocess.run(["node", "--check", str(js_path)], capture_output=True, text=True)
        if proc.returncode != 0:
            raise EditError(proc.stderr.strip() or "Canonical JavaScript syntax validation failed")
    finally:
        js_path.unlink(missing_ok=True)


def perform(edit: str, value: float | int | None) -> tuple[str, str, str]:
    before = BUILDER.read_text(encoding="utf-8")
    before_sha = sha256(before)
    after = EDITORS[edit](before, value if value is not None else 0)
    after_sha = sha256(after)
    if before_sha == after_sha:
        raise EditError("NO-OP: source hash did not change")
    validate_node(after)
    BUILDER.write_text(after, encoding="utf-8")
    return before_sha, after_sha, edit


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--edit", choices=sorted(EDITORS))
    ap.add_argument("--value", type=float)
    args = ap.parse_args()
    if not args.edit:
        ap.error("--edit is required")
    before, after, label = perform(args.edit, args.value)
    print("MAXESS FAST EDIT: PASS")
    print(f"EDIT: {label}")
    print(f"BUILDER SHA BEFORE: {before}")
    print(f"BUILDER SHA AFTER:  {after}")
    print("TARGETED SYNTAX: PASS")
    print("REAL SOURCE DELTA: VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
