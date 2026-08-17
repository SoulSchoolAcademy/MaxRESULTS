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
REPORT = ROOT / "V21-PACKET2-VALIDATION.md"
MARKER = 'id="maxess-results-v21-authority-js"'


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def extract_scripts(text: str):
    return re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", text, re.I | re.S)


def main() -> int:
    if not SOURCE.exists() or not BASELINE.exists():
        print("ERROR: source or baseline missing")
        return 2
    text = SOURCE.read_text(encoding="utf-8")
    baseline_sha = sha(BASELINE)
    source_sha = sha(SOURCE)
    checks: list[str] = []
    failures: list[str] = []

    count = text.count(MARKER)
    (checks if count == 1 else failures).append(f"V21 authority marker count = {count}")

    scripts = extract_scripts(text)
    checks.append(f"inline script blocks = {len(scripts)}")

    js_ok = True
    for idx, script in enumerate(scripts, 1):
        if not script.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
            fh.write(script)
            tmp = fh.name
        proc = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        Path(tmp).unlink(missing_ok=True)
        if proc.returncode != 0:
            js_ok = False
            failures.append(f"script {idx} syntax failure: {proc.stderr.strip()}")
    if js_ok:
        checks.append("all non-empty inline JavaScript blocks pass node --check")

    required = [
        "Hi. I’ve looked at your results.",
        "This isn’t your judgment. It’s your map.",
        "LISTEN TO NAYA",
        "MAXESS SCORE",
        "SELECT A DIMENSION",
        "YOUR PERSONALIZED REPORT",
        "window.MAXESS_RESULT",
    ]
    for token in required:
        (checks if token in text else failures).append(f"required token present: {token!r}")

    if text.count("v21-dim-orb") < 1:
        failures.append("V21 dimension orb implementation not found")
    if text.count("v21-report") < 1:
        failures.append("V21 report implementation not found")

    out = [
        "# MAXESS V21 — PACKET 2 VALIDATION",
        "",
        f"Source SHA-256: `{source_sha}`",
        f"Baseline SHA-256: `{baseline_sha}`",
        f"Source lines: `{len(text.splitlines())}`",
        "",
        "## Checks",
        *[f"- PASS: {x}" for x in checks],
        "",
        "## Failures",
        *([f"- FAIL: {x}" for x in failures] or ["- NONE"]),
        "",
        "## Gate",
        "PASS" if not failures else "FAIL",
    ]
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(REPORT.name)
    print(f"Source SHA-256: {source_sha}")
    print(f"Baseline SHA-256: {baseline_sha}")
    print(f"Inline scripts: {len(scripts)}")
    if failures:
        print("PACKET 2 VALIDATION FAILED")
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PACKET 2 VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
