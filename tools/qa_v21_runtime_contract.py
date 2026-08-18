#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-RUNTIME-CONTRACT-QA.md"


def canonical_sections(js: str) -> list[str]:
    """Extract real <section> chunks from the canonical V21 root renderer."""
    start = js.find("root.innerHTML='<div class=\"v21-shell\">")
    if start < 0:
        start = js.find("root.innerHTML='<div class=\\\"v21-shell\\\">")
    if start < 0:
        return []

    tail = js[start:]
    end_candidates = [
        tail.find("root.appendChild(experience)"),
        tail.find("root.classList.add('v21-release')"),
        tail.find("root.appendChild(host)"),
    ]
    ends = [e for e in end_candidates if e >= 0]
    payload = tail[: min(ends)] if ends else tail
    payload = payload.replace('\\\"', '\"').replace("\\'", "'")

    # IMPORTANT: section tags are literal HTML emitted inside JavaScript strings.
    # The previous validator used a malformed pattern that searched for the
    # character 's' after <section instead of HTML whitespace.
    return re.findall(r"<section\s+[^>]*>(?:.|\n)*?</section>", payload, re.I)


def section_text(section: str) -> str:
    return re.sub(r"<[^>]+>", " ", section).replace("&amp;", "&").strip().upper()


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
        "single Listen control": 'class=\"v21-listen\"',
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

    if "root.querySelectorAll('.v21-dim').forEach" not in js:
        failures.append("dimension controls do not have a delegated per-dimension interaction loop")

    if "@media print" not in text:
        failures.append("print CSS missing")
    if "prefers-reduced-motion:reduce" not in text:
        failures.append("reduced-motion CSS missing")
    if 'aria-label=\"Listen to Naya interpret your MAXESS results\"' not in js:
        failures.append("Listen accessibility label missing")

    sections = canonical_sections(js)
    if not sections:
        failures.append("canonical renderer sections could not be parsed from the actual root renderer")
    else:
        texts = [section_text(s) for s in sections]
        # Current approved runtime narrative. Playground, lever and next-move are
        # intentionally excluded from the V21 Results story contract.
        order = [
            "NAYA · YOUR AI GUIDE",
            "YOUR RESULT",
            "YOUR FIVE DIMENSIONS",
            "WHAT YOUR SCORES MEAN",
            "YOUR PERSONALIZED REPORT",
            "YOUR AI FINGERPRINT",
            "YOUR PATTERN",
            "YOUR STRENGTH",
            "18 NAYA MASTERS",
            "NAYA · IN PRACTICE",
            "YOUR AI MASTERY JOURNEY",
        ]
        positions: list[int] = []
        for marker in order:
            found = next((i for i, t in enumerate(texts) if marker in t), None)
            if found is None:
                failures.append(f"canonical renderer section marker missing: {marker}")
            else:
                positions.append(found)
        if len(positions) == len(order) and positions != sorted(positions):
            failures.append("canonical runtime section order is incorrect")

    report = [
        "# MAXESS V21 — RUNTIME CONTRACT QA", "",
        f"- Runtime JS lines: `{len(js.splitlines()) if js else 0}`",
        f"- Parsed canonical sections: `{len(canonical_sections(js))}`",
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
    print(f"PARSED CANONICAL SECTIONS: {len(canonical_sections(js))}")
    print(f"FAILURES: {len(failures)}")
    print(f"WARNINGS: {len(warnings)}")
    print("V21 RUNTIME CONTRACT QA PASS" if not failures else "V21 RUNTIME CONTRACT QA FAIL")
    return 0 if not failures else 5


if __name__ == '__main__':
    raise SystemExit(main())
