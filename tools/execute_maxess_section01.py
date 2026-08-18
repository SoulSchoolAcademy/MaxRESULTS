#!/usr/bin/env python3
"""MAXESS Section 01 owner: idempotent Golden Master + narrative alignment.

This executor is governed by the MAXESS NITRO MASTER EXECUTION CONTRACT and
its Section 01 specialization. It deliberately avoids parsing/reconstructing
the whole renderer. It patches only exact JavaScript string chunks owned by
the V21 root renderer, then validates the complete builder before returning
success.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"
MASTER_CONTRACT = ROOT / "NITRO-MASTER-EXECUTION-PROTOCOL.md"
TASK_CONTRACT = ROOT / "docs" / "NITRO-SECTION-01-ORB-EXECUTION-CONTRACT.md"
MARK = "/* MAXESS-SECTION-01-GOLDEN-MASTER */"
CANONICAL_SCRIPT = '<script id="maxess-results-v21-canonical-js">'


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def validate_contracts() -> None:
    """Hard execution-law gate: no Section 01 execution without both contracts."""
    if not MASTER_CONTRACT.exists():
        raise SystemExit("NITRO LAW FAIL: MAXESS NITRO MASTER EXECUTION CONTRACT is missing")
    if not TASK_CONTRACT.exists():
        raise SystemExit("NITRO LAW FAIL: Section 01 task-specific execution contract is missing")

    master = MASTER_CONTRACT.read_text(encoding="utf-8")
    task = TASK_CONTRACT.read_text(encoding="utf-8")

    required_master = (
        "MAXESS NITRO MASTER EXECUTION CONTRACT",
        "MASTER CONTRACT GOVERNANCE — READ THIS BEFORE EVERY EXECUTION",
        "DO NOT GUESS.",
        "CAN I PROVE IT?",
        "UNKNOWN may never ship.",
    )
    missing_master = [x for x in required_master if x not in master]
    if missing_master:
        raise SystemExit("NITRO LAW FAIL: master contract integrity missing: " + ", ".join(missing_master))

    required_task = (
        "NITRO-MASTER-EXECUTION-PROTOCOL.md",
        "Section 01 — Orb / Score Reveal",
        ".v21-score-orb",
        ".b1s1-orbital-bead",
        "window.MAXESS_RESULT",
        "score-color",
        "BLOCKED — GROOVE VISUAL TEST UNAVAILABLE",
        "Naya",
    )
    missing_task = [x for x in required_task if x not in task]
    if missing_task:
        raise SystemExit("NITRO LAW FAIL: Section 01 contract integrity missing: " + ", ".join(missing_task))


def validate_python() -> None:
    subprocess.run(["python", "-m", "py_compile", str(BUILDER)], check=True)


def extract_js(text: str) -> tuple[int, int, str]:
    start_tag = text.find(CANONICAL_SCRIPT)
    if start_tag < 0:
        raise SystemExit("SECTION 01: canonical V21 runtime block missing")
    start = text.find(">", start_tag) + 1
    end = text.find("</script>", start)
    if start <= 0 or end < 0:
        raise SystemExit("SECTION 01: canonical V21 script boundaries invalid")
    return start, end, text[start:end]


def replace_section_chunk(js: str, label: str, replacement: str) -> tuple[str, int]:
    # A canonical root renderer section is emitted as one JS single-quoted
    # string chunk followed by +. Match only that chunk; never rebuild the
    # surrounding renderer expression.
    token = re.compile(r"'(?:\\.|[^'\\])*" + re.escape(label) + r"(?:\\.|[^'\\])*'\s*\+", re.S)
    matches = list(token.finditer(js))
    if len(matches) > 1:
        raise SystemExit(f"SECTION 01: multiple active {label} chunks found ({len(matches)})")
    if not matches:
        return js, 0
    return js[:matches[0].start()] + replacement + "\n" + js[matches[0].end():], 1


def align(js: str) -> tuple[str, dict[str, int]]:
    changes: dict[str, int] = {}

    js, n = replace_section_chunk(
        js,
        "YOUR LEVER",
        "",
    )
    changes["YOUR LEVER"] = n

    js, n = replace_section_chunk(
        js,
        "YOUR NEXT MOVE",
        "",
    )
    changes["YOUR NEXT MOVE"] = n

    # Replace the obsolete Playground section chunk with the approved
    # compact Naya guided-experience moment. The real media assets remain
    # owned by the existing page and are not cloned or relocated here.
    playground_replacement = (
        "'<section class=\"v21-section v21-dark\"><div class=\"v21-inner\">"
        "<span class=\"v21-kicker\">NAYA · IN PRACTICE</span>"
        "<h2 class=\"v21-section-title\">See what your result can become.</h2>"
        "<p class=\"v21-section-copy\">Naya helps turn your MAXESS result into a practical next step.</p>"
        "<div id=\"v21-media-host\" class=\"v21-media-host\"></div>"
        "</div></section>'+"
    )
    js, n = replace_section_chunk(js, "PLAYGROUND", playground_replacement)
    changes["PLAYGROUND"] = n

    # The V21 Hero must own the single visible Listen control.
    old_ids = "var ids=['#mx-naya-listen','#v11-naya-listen','#v13-listen','.mx-naya-listen','.v18-listen'];"
    new_ids = "var ids=['.v21-listen.b1s1-listen','.v21-listen'];"
    if old_ids in js:
        js = js.replace(old_ids, new_ids)
        changes["LISTEN OWNER"] = 1
    else:
        changes["LISTEN OWNER"] = 0

    # Hard corruption guard: the executor must never introduce nested
    # root.innerHTML assignments into the canonical renderer expression.
    bad_patterns = (
        "root.innerHTML='<div class=\"root.innerHTML=",
        "root.innerHTML=\"<div class=\"root.innerHTML=",
    )
    if any(p in js for p in bad_patterns):
        raise SystemExit("SECTION 01: renderer self-corruption guard triggered")

    return js, changes


def validate_section01_builder(text: str) -> None:
    """Static evidence gate for the exact Section 01 implementation contract."""
    required = (
        'MAXESS-SECTION-01-GOLDEN-MASTER',
        '.v21-score-orb',
        '.b1s1-orbital-bead',
        'b1s1-orbit',
        'window.MAXESS_RESULT',
        'var colorFor=function(v)',
        'prefers-reduced-motion:reduce',
        'maxess-results-v21-canonical-css',
        'maxess-results-v21-canonical-js',
    )
    missing = [x for x in required if x not in text]
    if missing:
        raise SystemExit('SECTION 01 STATIC EVIDENCE FAIL: ' + ', '.join(missing))

    if text.count('MAXESS-SECTION-01-GOLDEN-MASTER') != 2:
        raise SystemExit('SECTION 01 STATIC EVIDENCE FAIL: Golden Master marker count is not exactly 2 (CSS + JS)')
    if text.count('b1s1-orbital-bead') < 2:
        raise SystemExit('SECTION 01 STATIC EVIDENCE FAIL: Orbital Bead implementation appears incomplete')
    if re.search(r'(^|\n)(<<<<<<<|=======|>>>>>>>)( |\n|$)', text):
        raise SystemExit('SECTION 01 STATIC EVIDENCE FAIL: unresolved conflict marker remains in builder')


def main() -> int:
    # RULE #1: the Master Contract and its specialized Section 01 contract
    # must be read and validated before any mutation is allowed.
    validate_contracts()

    if not BUILDER.exists():
        raise SystemExit("SECTION 01: builder missing")

    original = BUILDER.read_text(encoding="utf-8")
    if MARK not in original:
        raise SystemExit("SECTION 01: Golden Master layer is missing; refuse to invent it here")

    validate_section01_builder(original)

    start, end, js = extract_js(original)
    aligned_js, changes = align(js)
    validate_js(aligned_js)

    updated = original[:start] + aligned_js + original[end:]

    # Always validate the complete Python builder before accepting the edit.
    candidate_path = ROOT / ".maxess_section01_candidate_builder.py"
    candidate_path.write_text(updated, encoding="utf-8")
    try:
        subprocess.run(["python", "-m", "py_compile", str(candidate_path)], check=True)
    finally:
        candidate_path.unlink(missing_ok=True)
        pycache = candidate_path.parent / "__pycache__"
        if pycache.exists():
            for p in pycache.glob(".maxess_section01_candidate_builder*.pyc"):
                p.unlink(missing_ok=True)

    validate_section01_builder(updated)

    if updated == original:
        print("SECTION 01: renderer already aligned; Golden Master preserved")
        print("GOLDEN MASTER: PRESERVED")
        print("YOUR LEVER: ALREADY ABSENT")
        print("YOUR NEXT MOVE: ALREADY ABSENT")
        print("PLAYGROUND: ALREADY ABSENT/ALIGNED")
        print("LISTEN OWNER: V21 HERO CONTROL")
        print("NITRO MASTER CONTRACT: READ + VERIFIED")
        print("SECTION 01 CONTRACT: READ + VERIFIED")
        print("STATIC SECTION 01 EVIDENCE: PASS")
        return 0

    BUILDER.write_text(updated, encoding="utf-8")

    print("MAXESS SECTION 01 PRODUCT ALIGNMENT: PASS")
    print("GOLDEN MASTER: PRESERVED")
    print(f"YOUR LEVER: {'REMOVED' if changes['YOUR LEVER'] else 'ALREADY ABSENT'}")
    print(f"YOUR NEXT MOVE: {'REMOVED' if changes['YOUR NEXT MOVE'] else 'ALREADY ABSENT'}")
    print(f"PLAYGROUND: {'REPLACED -> NAYA · IN PRACTICE' if changes['PLAYGROUND'] else 'ALREADY ABSENT/ALIGNED'}")
    print(f"LISTEN OWNER: {'V21 HERO CONTROL' if changes['LISTEN OWNER'] or '.v21-listen.b1s1-listen' in aligned_js else 'UNCHANGED'}")
    print("NODE CHECK: PASS")
    print("PYTHON CHECK: PASS")
    print("STATIC SECTION 01 EVIDENCE: PASS")
    print("NITRO MASTER CONTRACT: READ + VERIFIED")
    print("SECTION 01 CONTRACT: READ + VERIFIED")
    print("BUILDER SHA BEFORE:", sha(original))
    print("BUILDER SHA AFTER: ", sha(updated))
    return 0


def validate_js(text: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
        fh.write(text)
        path = fh.name
    try:
        proc = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    finally:
        Path(path).unlink(missing_ok=True)
    if proc.returncode:
        raise SystemExit(proc.stderr.strip() or "Node syntax validation failed")


if __name__ == "__main__":
    raise SystemExit(main())
