#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-EXPERIENCE-QA.md"


def count(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, flags=re.I | re.S))


def main() -> int:
    text = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""
    failures: list[str] = []
    warnings: list[str] = []

    if not text:
        failures.append("working Results source missing or empty")
        return 5

    required_order = [
        "NAYA · YOUR AI GUIDE",
        "YOUR RESULT",
        "YOUR FIVE DIMENSIONS",
        "YOUR PERSONALIZED REPORT",
        "YOUR PATTERN",
        "YOUR STRENGTH",
        "YOUR LEVER",
        "YOUR NEXT MOVE",
        "18 NAYA MASTERS",
        "PLAYGROUND",
        "YOUR AI MASTERY JOURNEY",
    ]
    positions = []
    for token in required_order:
        pos = text.find(token)
        if pos < 0:
            failures.append(f"missing canonical section: {token}")
            continue
        positions.append((pos, token))
    if positions and [t for _, t in sorted(positions)] != required_order:
        failures.append("canonical section order is not the intended narrative order")

    if count(text, r"class=\"v21-listen\"") != 1:
        failures.append("canonical Listen CTA is not exactly one")
    if count(text, r"class=\"v21-dim\"") < 1:
        failures.append("canonical dimension controls are missing")
    if "slice(0,5)" not in text:
        failures.append("canonical runtime does not explicitly constrain dimensions to five")
    if "window.MAXESS_RESULT" not in text:
        failures.append("MAXESS_RESULT source-of-truth is missing")
    if "data-results-data-source=\"window.MAXESS_RESULT\"" not in text:
        warnings.append("runtime data-source marker is missing")

    # Five-stage model and meaningful stage thresholds.
    for stage in ("Supporting", "Foundation", "Developing", "Advancing", "Mastering"):
        if stage not in text:
            failures.append(f"mastery stage missing: {stage}")

    # Print/PDF and accessibility.
    if "@media print" not in text:
        failures.append("print/PDF rules missing")
    if "prefers-reduced-motion:reduce" not in text:
        failures.append("reduced-motion handling missing")
    if "focus-visible" not in text:
        failures.append("focus-visible handling missing")
    if 'aria-label="Listen to Naya' not in text:
        failures.append("Listen CTA accessibility label missing")

    # Anti-regression checks for forbidden static presentation.
    if re.search(r"Math\.round\(s\)\s*/\s*100", text):
        failures.append("canonical source still contains a score / 100 presentation")

    # The dormant baseline may contain historical implementation, but the canonical layer
    # must be the single active renderer marker.
    if count(text, r'id=\"maxess-results-v21-canonical-js\"') != 1:
        failures.append("canonical JS marker is not exactly once")
    if count(text, r'id=\"maxess-results-v21-canonical-css\"') != 1:
        failures.append("canonical CSS marker is not exactly once")

    report = [
        "# MAXESS V21 — EXPERIENCE QA",
        "",
        f"- Source lines: `{len(text.splitlines())}`",
        f"- Failures: `{len(failures)}`",
        f"- Warnings: `{len(warnings)}`",
        "",
        "## Failures",
    ]
    report.extend(f"- {x}" for x in failures) if failures else report.append("- NONE")
    report.append("")
    report.append("## Warnings")
    report.extend(f"- {x}" for x in warnings) if warnings else report.append("- NONE")
    report += ["", "## Gate", "PASS" if not failures else "FAIL", ""]
    REPORT.write_text("\n".join(report), encoding="utf-8")

    for failure in failures:
        print("FAIL:", failure)
    for warning in warnings:
        print("WARN:", warning)
    print(f"SOURCE LINES: {len(text.splitlines())}")
    print(f"FAILURES: {len(failures)}")
    print(f"WARNINGS: {len(warnings)}")
    print("V21 EXPERIENCE QA PASS" if not failures else "V21 EXPERIENCE QA FAIL")
    return 0 if not failures else 5


if __name__ == "__main__":
    raise SystemExit(main())
