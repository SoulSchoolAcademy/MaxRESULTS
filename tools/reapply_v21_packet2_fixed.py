#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
BASELINE = ROOT / "BASELINE-WORKING.html"
REPORT = ROOT / "V21-PACKET2-FIXED-RESULT.md"
MARKER = 'id="maxess-results-v21-authority-js"'


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def normalize_fragment(fragment: str) -> str:
    # The original generator stored literal backslash-n sequences in raw Python strings.
    # Convert only those newline escapes; leave JavaScript escaping intact.
    return fragment.replace('\\n', '\n')


def extract_scripts(text: str):
    return re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", text, re.I | re.S)


def check_js(text: str) -> tuple[bool, list[str]]:
    failures = []
    for idx, script in enumerate(extract_scripts(text), 1):
        if not script.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
            fh.write(script)
            path = fh.name
        proc = subprocess.run(["node", "--check", path], capture_output=True, text=True)
        Path(path).unlink(missing_ok=True)
        if proc.returncode != 0:
            failures.append(f"script {idx}: {proc.stderr.strip()}")
    return not failures, failures


def main() -> int:
    if not SOURCE.exists() or not BASELINE.exists():
        print("ERROR: source or baseline missing")
        return 2

    # Import the existing design fragments, then normalize their serialization safely.
    import importlib.util
    spec = importlib.util.spec_from_file_location("packet2", ROOT / "tools" / "apply_v21_packet2.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    css = normalize_fragment(mod.V21_CSS)
    js = normalize_fragment(mod.V21_JS)
    insertion = css + "\n" + js

    baseline_text = BASELINE.read_text(encoding="utf-8")
    if baseline_text.count('</body>') > 0:
        candidate = baseline_text.replace('</body>', insertion + '\n</body>', 1)
    else:
        candidate = baseline_text + '\n' + insertion + '\n'

    if candidate.count(MARKER) != 1:
        print(f"ERROR: V21 marker count would be {candidate.count(MARKER)}, expected 1")
        return 3

    ok, failures = check_js(candidate)
    if not ok:
        print("ERROR: candidate failed JavaScript syntax gate")
        for f in failures:
            print(f"FAIL: {f}")
        return 4

    SOURCE.write_text(candidate, encoding="utf-8")
    source_sha = sha(SOURCE)
    baseline_sha = sha(BASELINE)
    REPORT.write_text(
        "# MAXESS V21 — FIXED PACKET 2\n\n"
        f"- Baseline SHA-256: `{baseline_sha}`\n"
        f"- New source SHA-256: `{source_sha}`\n"
        f"- Source lines: `{len(candidate.splitlines())}`\n"
        "- V21 marker count: `1`\n"
        "- JavaScript syntax gate: `PASS`\n"
        "\nThe candidate was rebuilt from the frozen baseline and passed syntax validation before write.\n",
        encoding="utf-8",
    )
    print("V21 FIXED PACKET 2 APPLIED")
    print(f"Baseline SHA-256: {baseline_sha}")
    print(f"New SHA-256: {source_sha}")
    print(f"Lines: {len(candidate.splitlines())}")
    print("JS SYNTAX GATE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
