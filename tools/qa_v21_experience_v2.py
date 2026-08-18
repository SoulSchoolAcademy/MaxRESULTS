#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-EXPERIENCE-QA-V2.md"
SCRIPT_TAG = '<script id="maxess-results-v21-canonical-js">'

# The product contract defines the complete 15-part narrative, but the
# canonical root renderer does not own every chapter. Runtime-owned chapters
# such as Score Meaning and Five Dimensions are assembled elsewhere.
ROOT_RENDERER_ORDER = [
    "NAYA · YOUR AI GUIDE",
    "YOUR RESULT",
    "YOUR PERSONALIZED REPORT",
    "YOUR AI FINGERPRINT",
    "YOUR STRENGTH",
    "YOUR LEVER",
    "YOUR PATTERN",
    "YOUR NEXT MOVE",
    "18 NAYA MASTERS",
    "YOUR AI MASTERY JOURNEY",
]

RUNTIME_REQUIRED = [
    "WHAT YOUR SCORE MEANS",
    "YOUR FIVE DIMENSIONS",
]


def main() -> int:
    text = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""
    failures: list[str] = []
    warnings: list[str] = []

    if not text:
        failures.append("working Results source missing or empty")

    marker_count = text.count(SCRIPT_TAG) if text else 0
    if marker_count != 1:
        failures.append(f"canonical JS script tag is not exactly once: {marker_count}")

    canonical = ""
    if marker_count == 1:
        start = text.find(SCRIPT_TAG)
        end = text.find("</script>", start)
        if end >= 0:
            canonical = text[start:end + len("</script>")]
        else:
            failures.append("canonical V21 JS closing script tag missing")

    if not canonical:
        failures.append("canonical V21 JS layer could not be isolated")

    # Anchor to the actual V21 shell renderer. Legacy code contains several
    # other root.innerHTML assignments and must not participate in this gate.
    anchor_re = re.compile(
        r"root\.innerHTML\s*=\s*['\"]<div class=\\?[\"']v21-shell\\?[\"']>"
    )
    anchor = anchor_re.search(canonical)
    render_payload = ""
    if not anchor:
        failures.append("canonical V21 root renderer anchor could not be isolated")
    else:
        render_payload = canonical[anchor.start():]
        for terminator in ("\n    var btn=", "\n  var btn=", "\nfunction enforce", "\n  function enforce"):
            pos = render_payload.find(terminator)
            if pos >= 0:
                render_payload = render_payload[:pos]
                break

    if not render_payload:
        failures.append("canonical root.innerHTML renderer payload is empty")
    else:
        section_starts = [
            m.start()
            for m in re.finditer(
                r"<section\s+class=\\?[\"']v21-section(?:\s|\\?[\"'])",
                render_payload,
            )
        ]
        if not section_starts:
            failures.append("canonical renderer sections could not be parsed from root.innerHTML")
            chunks: list[str] = []
        else:
            chunks = [
                render_payload[s:(section_starts[i + 1] if i + 1 < len(section_starts) else len(render_payload))]
                for i, s in enumerate(section_starts)
            ]

        def section_name(chunk: str) -> str:
            for token in ROOT_RENDERER_ORDER:
                if token in chunk:
                    return token
            return ""

        names = [section_name(chunk) for chunk in chunks]
        actual_names = [name for name in names if name]

        for token in ROOT_RENDERER_ORDER:
            if token not in actual_names:
                failures.append(f"missing canonical root-renderer section: {token}")

        filtered_expected = [token for token in ROOT_RENDERER_ORDER if token in actual_names]
        if actual_names != filtered_expected:
            failures.append("canonical root renderer section order is not the renderer narrative order")

        listen_count = len(re.findall(r'class=[\"\']v21-listen[\"\']', render_payload, flags=re.I))
        if listen_count != 1:
            failures.append(f"canonical Listen CTA is not exactly one: {listen_count}")

        if len(re.findall(r'class=[\"\']v21-dim[\"\']', render_payload, flags=re.I)) < 1:
            failures.append("canonical dimension controls are missing from root renderer")

    # Runtime-owned chapters must exist in the canonical runtime layer, even
    # when they are not emitted by the root.innerHTML renderer itself.
    for token in RUNTIME_REQUIRED:
        if token not in canonical:
            failures.append(f"missing runtime-owned canonical section: {token}")

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
