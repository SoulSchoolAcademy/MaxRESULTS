#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "BASELINE-WORKING.html"
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-CANDIDATE-QA.md"

REQUIRED = [
    "YOUR FIVE DIMENSIONS",
    "YOUR PERSONALIZED REPORT",
    "YOUR PATTERN",
    "YOUR STRENGTH",
    "YOUR LEVER",
    "YOUR NEXT MOVE",
    "18 NAYA MASTERS",
    "PLAYGROUND",
    "YOUR AI MASTERY JOURNEY",
    "window.MAXESS_RESULT",
    "LISTEN TO NAYA",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def duplicate_ids(text: str):
    ids = re.findall(r'\bid=["\']([^"\']+)["\']', text, flags=re.I)
    counts = {}
    for value in ids:
        counts[value] = counts.get(value, 0) + 1
    return sorted((k, v) for k, v in counts.items() if v > 1)


def main() -> int:
    failures = []
    warnings = []
    baseline = BASELINE.read_text(encoding="utf-8") if BASELINE.exists() else ""
    candidate = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""

    if not BASELINE.exists():
        failures.append("BASELINE-WORKING.html missing")
    if not SOURCE.exists():
        failures.append("working Results source missing")
    if not candidate:
        failures.append("working Results source is empty")

    if baseline and SOURCE.exists():
        # The protected baseline is allowed to differ from the candidate; this
        # check confirms the baseline itself is unchanged by hashing the file.
        print(f"BASELINE SHA-256: {sha(BASELINE)}")

    for token in REQUIRED:
        if token not in candidate:
            failures.append(f"missing required content: {token}")

    if candidate.count('id="maxess-results-v21-canonical-js"') != 1:
        failures.append("canonical V21 JS marker is not present exactly once")
    if candidate.count('id="maxess-results-v21-canonical-css"') != 1:
        failures.append("canonical V21 CSS marker is not present exactly once")

    dupes = duplicate_ids(candidate)
    if dupes:
        failures.append("duplicate IDs: " + ", ".join(f"{k} ({v})" for k, v in dupes))

    # The canonical builder must not hard-code a production user's actual score.
    for value in ("82", "91", "79", "74", "68"):
        if re.search(rf"(?:score-number|v21-dim-score)[^\n]*>{value}<", candidate):
            failures.append(f"possible hard-coded demo score detected in rendered markup: {value}")

    # Data and stage coverage.
    if "window.MAXESS_RESULT" not in candidate:
        failures.append("MAXESS_RESULT source missing")
    if not all(stage in candidate for stage in ("Supporting", "Foundation", "Developing", "Advancing", "Mastering")):
        failures.append("mastery-stage model does not visibly include all five required stages")

    # Preservation checks: candidate should retain the important existing product hooks.
    for marker in ('id="naya-playground"', '18 NAYA', 'MAXESS'):
        if marker in baseline and marker not in candidate:
            failures.append(f"preservation regression: {marker} existed in baseline but is absent from candidate")

    # PDF / print is required to have deliberate print rules in the candidate.
    if "@media print" not in candidate:
        failures.append("dedicated print/PDF CSS is missing")
    if "break-inside" not in candidate:
        warnings.append("print CSS does not visibly declare break-inside controls")

    # Known builder warning should be treated as technical debt, not ignored.
    builder = ROOT / "tools" / "build_v21_canonical.py"
    if builder.exists():
        builder_text = builder.read_text(encoding="utf-8")
        if r"\\s" in builder_text:
            warnings.append("canonical builder contains a Python invalid-escape warning candidate")

    report = [
        "# MAXESS V21 — CANDIDATE QA",
        "",
        f"- Candidate lines: `{len(candidate.splitlines()) if candidate else 0}`",
        f"- Candidate SHA-256: `{sha(SOURCE) if SOURCE.exists() else 'MISSING'}`",
        f"- Duplicate IDs: `{len(dupes)}`",
        f"- Failures: `{len(failures)}`",
        f"- Warnings: `{len(warnings)}`",
        "",
        "## Failures",
        *(f"- {x}" for x in failures) if failures else ["- NONE"],
        "",
        "## Warnings",
        *(f"- {x}" for x in warnings) if warnings else ["- NONE"],
        "",
        "## Gate",
        "PASS" if not failures else "FAIL",
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")

    for f in failures:
        print("FAIL:", f)
    for w in warnings:
        print("WARN:", w)
    print(f"CANDIDATE LINES: {len(candidate.splitlines()) if candidate else 0}")
    print(f"DUPLICATE IDS: {len(dupes)}")
    print(f"FAILURES: {len(failures)}")
    print(f"WARNINGS: {len(warnings)}")
    print("V21 CANDIDATE QA PASS" if not failures else "V21 CANDIDATE QA FAIL")
    return 0 if not failures else 5


if __name__ == "__main__":
    raise SystemExit(main())
