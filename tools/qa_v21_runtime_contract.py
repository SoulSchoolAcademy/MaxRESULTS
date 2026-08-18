#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-RUNTIME-CONTRACT-QA.md"


def canonical_sections(js: str) -> list[str]:
    """Extract actual emitted <section> chunks from the root.innerHTML renderer.

    Do not infer order from helper-function strings. The owner of narrative order
    is the actual canonical root renderer payload.
    """
    m = re.search(
        r"root\.innerHTML='?<div class=\\?\"v21-shell\\?\">.*?",
        js,
        re.I | re.S,
    )
    # The V21 renderer in the current source uses root.innerHTML assembled from
    # string concatenation. Find the assignment, then capture through the final
    # root.appendChild(experience) / root.classList.add boundary.
    if not m:
        start = js.find("root.innerHTML=")
        if start < 0:
            return []
    else:
        start = m.start()

    tail = js[start:]
    end_candidates = [
        tail.find("root.appendChild(experience)"),
        tail.find("root.classList.add('v21-release')"),
    ]
    ends = [e for e in end_candidates if e >= 0]
    if not ends:
        return []
    payload = tail[: min(ends)]

    # Support escaped and literal markup inside JS strings/templates.
    payload = payload.replace('\\\"', '\"').replace("\\'", "'")
    return re.findall(r"<section\\?s+[^>]*>(?:.|\\n)*?</section>", payload, re.I)


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
    if 'aria-label="Listen to Naya interpret your MAXESS results"' not in js:
        failures.append("Listen accessibility label missing")

    sections = canonical_sections(js)
    if not sections:
        failures.append("canonical renderer sections could not be parsed from the actual root renderer")
    else:
        texts = [section_text(s) for s in sections]
        # Runtime contract owns the actual renderer sequence. This is deliberately
        # limited to sections the renderer emits; broader runtime-injected content
        # is governed by the Master Contract and other QA gates.
        order = [
            "NAYA · YOUR AI GUIDE",
            "YOUR MAXESS SCORE",
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
        for marker in order:
            found = next((i for i, t in enumerate(texts) if marker in t), None)
            if found is None:
                failures.append(f"canonical renderer section marker missing: {marker}")
            else:
                positions.append(found)
        if len(positions) == len(order) and positions != sorted(positions):
            failures.append("canonical runtime section order is incorrect")

        # Playground preservation is structural: a preserved section may be found
        # by content/selector and moved into the V21 experience. Do not require one
        # obsolete DOM lookup token when the renderer preserves it through a more
        # robust structural path.
        playground_present = any("PLAYGROUND" in t for t in texts) or "findSection(/playground/)" in js
        if not playground_present:
            failures.append("runtime requirement missing: Playground preservation")

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
