#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-RUNTIME-CONTRACT-QA.md"


def canonical_render(js: str) -> str:
    """Extract the real V21 root.innerHTML renderer assembly source."""
    markers = [
        "root.innerHTML='<div class=\"v21-shell\">'+",
        "root.innerHTML='<div class=\\\"v21-shell\\\">'+",
    ]
    start = next((js.find(m) for m in markers if js.find(m) >= 0), -1)
    if start < 0:
        return ""
    end = js.find("var btn=root.querySelector('.v21-listen')", start)
    if end < 0:
        return ""
    return js[start:end]


def main() -> int:
    text = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""
    failures: list[str] = []
    warnings: list[str] = []

    m = re.search(r'<script id="maxess-results-v21-canonical-js">(.*?)</script>', text, re.I | re.S)
    js = m.group(1) if m else ""
    if not js:
        failures.append("canonical V21 runtime JS block missing")

    required_js = {
        "source-of-truth": "window.MAXESS_RESULT",
        "dynamic overall score": "function score(r)",
        "five dimensions": "slice(0,5)",
        "five-stage model": "Supporting",
        "safe fallback": "Your result is not loaded yet.",
        "single Listen control": 'class=\\"v21-listen\\"',
        "dimension interaction": ".addEventListener('click'",
        "ready state": "data-results-state','ready",
    }
    for label, token in required_js.items():
        if token not in js:
            failures.append(f"runtime requirement missing: {label}")

    for stage in ("Supporting", "Foundation", "Developing", "Advancing", "Mastering"):
        if stage not in js:
            failures.append(f"runtime mastery stage missing: {stage}")

    if re.search(r"v21-score-number[^\n]*>\s*(82|91|79|74|68)\s*<", js):
        failures.append("canonical runtime contains hard-coded demo score")

    if "@media print" not in text:
        failures.append("print CSS missing")
    if "prefers-reduced-motion:reduce" not in text:
        failures.append("reduced-motion CSS missing")
    if 'aria-label=\\"Listen to Naya interpret your MAXESS results\\"' not in js:
        failures.append("Listen accessibility label missing")

    render = canonical_render(js)
    if not render:
        failures.append("canonical renderer root.innerHTML assembly could not be isolated")
    else:
        # Approved current narrative. Do not reintroduce obsolete sections merely
        # because older runtime validators expected them.
        order = [
            "NAYA · YOUR AI GUIDE",
            "YOUR RESULT",
            "YOUR FIVE DIMENSIONS",
            "YOUR PERSONALIZED REPORT",
            "YOUR AI FINGERPRINT",
            "YOUR STRENGTH",
            "18 NAYA MASTERS",
            "NAYA · IN PRACTICE",
            "YOUR AI MASTERY JOURNEY",
        ]
        positions = [render.find(marker) for marker in order]
        if any(p < 0 for p in positions):
            missing = [marker for marker, pos in zip(order, positions) if pos < 0]
            failures.append("approved renderer section marker missing: " + ", ".join(missing))
        elif positions != sorted(positions):
            failures.append("canonical renderer section order is incorrect")

        obsolete = ["PLAYGROUND", "YOUR LEVER", "YOUR NEXT MOVE"]
        present = [marker for marker in obsolete if marker in render]
        if present:
            failures.append("obsolete renderer sections still present: " + ", ".join(present))

    report = [
        "# MAXESS V21 — RUNTIME CONTRACT QA", "",
        f"- Runtime JS lines: `{len(js.splitlines()) if js else 0}`",
        f"- Failures: `{len(failures)}`",
        f"- Warnings: `{len(warnings)}`", "", "## Failures",
    ]
    report.extend(f"- {x}" for x in failures) if failures else report.append("- NONE")
    report += ["", "## Warnings"]
    report.extend(f"- {x}" for x in warnings) if warnings else report.append("- NONE")
    report += ["", "## Gate", "PASS" if not failures else "FAIL", ""]
    REPORT.write_text("\n".join(report), encoding="utf-8")

    for x in failures:
        print("FAIL:", x)
    for x in warnings:
        print("WARN:", x)
    print(f"RUNTIME JS LINES: {len(js.splitlines()) if js else 0}")
    print(f"FAILURES: {len(failures)}")
    print(f"WARNINGS: {len(warnings)}")
    print("V21 RUNTIME CONTRACT QA PASS" if not failures else "V21 RUNTIME CONTRACT QA FAIL")
    return 0 if not failures else 5


if __name__ == '__main__':
    raise SystemExit(main())
