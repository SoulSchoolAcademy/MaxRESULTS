#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-EXPERIENCE-QA-V2.md"
SCRIPT_TAG = '<script id="maxess-results-v21-canonical-js">'

RENDERER_ORDER = [
    "NAYA · YOUR AI GUIDE",
    "YOUR RESULT",
    "WHAT YOUR SCORES MEAN",
    "YOUR PERSONALIZED REPORT",
    "YOUR FIVE DIMENSIONS",
    "YOUR PATTERN",
    "YOUR STRENGTH",
    "YOUR LEVER",
    "YOUR NEXT MOVE",
    "18 NAYA MASTERS",
    "PLAYGROUND",
    "YOUR AI MASTERY JOURNEY",
]


def extract_canonical(text: str) -> str:
    start = text.find(SCRIPT_TAG)
    if start < 0:
        return ""
    end = text.find("</script>", start)
    if end < 0:
        return ""
    return text[start:end + len("</script>")]


def extract_render_payload(canonical: str) -> str:
    # The production renderer uses a root.innerHTML assignment assembled from
    # string fragments. Capture that assignment through its terminating
    # render-enforcement statement rather than relying on arbitrary title text.
    start = canonical.find("root.innerHTML")
    if start < 0:
        return ""
    end_candidates = [
        canonical.find("\n    var btn=", start),
        canonical.find("\n  var btn=", start),
        canonical.find("\nfunction enforce", start),
    ]
    end_candidates = [x for x in end_candidates if x >= 0]
    end = min(end_candidates) if end_candidates else len(canonical)
    return canonical[start:end]


def parse_section_chunks(render_payload: str) -> list[str]:
    # Parse emitted section boundaries structurally. Accept quoted/escaped
    # representations because the renderer lives inside a JavaScript string.
    starts = [m.start() for m in re.finditer(r"<section\s+class=\\?[\"']v21-section\\?[\"']", render_payload)]
    if not starts:
        return []
    return [render_payload[s:(starts[i + 1] if i + 1 < len(starts) else len(render_payload))] for i, s in enumerate(starts)]


def section_name(chunk: str) -> str:
    for token in RENDERER_ORDER:
        if token in chunk:
            return token
    return ""


def main() -> int:
    text = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""
    failures: list[str] = []
    warnings: list[str] = []

    if not text:
        failures.append("working Results source missing or empty")
    canonical = extract_canonical(text) if text else ""
    if not canonical:
        failures.append("canonical V21 JS layer could not be isolated")

    marker_count = text.count(SCRIPT_TAG) if text else 0
    if marker_count != 1:
        failures.append(f"canonical JS script tag is not exactly once: {marker_count}")

    render_payload = extract_render_payload(canonical)
    if not render_payload:
        failures.append("canonical root.innerHTML renderer could not be isolated")

    chunks = parse_section_chunks(render_payload)
    if not chunks:
        failures.append("canonical renderer sections could not be parsed from root.innerHTML")

    names = [section_name(chunk) for chunk in chunks]
    actual_names = [name for name in names if name]

    for token in RENDERER_ORDER:
        if token not in actual_names:
            failures.append(f"missing canonical renderer section: {token}")

    filtered_expected = [token for token in RENDERER_ORDER if token in actual_names]
    if actual_names != filtered_expected:
        failures.append("canonical section order is not the renderer narrative order")

    listen_count = len(re.findall(r'class=[\"\']v21-listen[\"\']', render_payload, flags=re.I))
    if listen_count != 1:
        failures.append(f"canonical Listen CTA is not exactly one: {listen_count}")

    if len(re.findall(r'class=[\"\']v21-dim[\"\']', render_payload, flags=re.I)) < 1:
        failures.append("canonical dimension controls are missing")

    if "slice(0,5)" not in canonical:
        failures.append("canonical runtime does not explicitly constrain dimensions to five")

    if "window.MAXESS_RESULT" not in canonical:
        failures.append("MAXESS_RESULT source-of-truth is missing from canonical runtime")

    if (
        'data-results-data-source=\\"window.MAXESS_RESULT\\"' not in canonical
        and "data-results-data-source='window.MAXESS_RESULT'" not in canonical
        and "setAttribute('data-results-data-source','window.MAXESS_RESULT')" not in canonical
        and 'setAttribute("data-results-data-source","window.MAXESS_RESULT")' not in canonical
    ):
        warnings.append("runtime data-source marker is missing from canonical text")

    for stage in ("Supporting", "Foundation", "Developing", "Advancing", "Mastering"):
        if stage not in canonical:
            failures.append(f"mastery stage missing: {stage}")

    if "@media print" not in text:
        failures.append("print/PDF rules missing")
    if "prefers-reduced-motion:reduce" not in text:
        failures.append("reduced-motion handling missing")
    if "focus-visible" not in text:
        failures.append("focus-visible handling missing")
    if not re.search(r'aria-label=\\?[\"\']Listen to Naya', canonical, flags=re.I):
        failures.append("Listen CTA accessibility label missing")

    if re.search(r"Math\.round\(s\)\s*/\s*100", canonical):
        warnings.append("canonical source contains a /100-style score presentation")

    if text.count('id="maxess-results-v21-canonical-css"') != 1:
        failures.append("canonical CSS marker is not exactly once")

    report = [
        "# MAXESS V21 — EXPERIENCE QA V2",
        "",
        f"- Source lines: `{len(text.splitlines())}`",
        f"- Canonical lines: `{len(canonical.splitlines()) if canonical else 0}`",
        f"- Failures: `{len(failures)}`",
        f"- Warnings: `{len(warnings)}`",
        "",
        "## Failures",
    ]
    report.extend(f"- {x}" for x in failures) if failures else report.append("- NONE")
    report += ["", "## Warnings"]
    report.extend(f"- {x}" for x in warnings) if warnings else report.append("- NONE")
    report += ["", "## Gate", "PASS" if not failures else "FAIL", ""]
    REPORT.write_text("\n".join(report), encoding="utf-8")

    for failure in failures:
        print("FAIL:", failure)
    for warning in warnings:
        print("WARN:", warning)
    print(f"SOURCE LINES: {len(text.splitlines())}")
    print(f"CANONICAL LINES: {len(canonical.splitlines()) if canonical else 0}")
    print(f"FAILURES: {len(failures)}")
    print(f"WARNINGS: {len(warnings)}")
    print("V21 EXPERIENCE QA V2 PASS" if not failures else "V21 EXPERIENCE QA V2 FAIL")
    return 0 if not failures else 5


if __name__ == "__main__":
    raise SystemExit(main())
