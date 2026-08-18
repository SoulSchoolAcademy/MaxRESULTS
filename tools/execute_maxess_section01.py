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
GROOVE_EMBED = ROOT / "docs" / "SECTION-01-ORB-GROOVE-EMBED.html"
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
    if not GROOVE_EMBED.exists():
        raise SystemExit("NITRO LAW FAIL: Section 01 Groove delivery artifact is missing")

    master = MASTER_CONTRACT.read_text(encoding="utf-8")
    task = TASK_CONTRACT.read_text(encoding="utf-8")
    embed = GROOVE_EMBED.read_text(encoding="utf-8")

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

    required_embed = (
        "MAXESS NITRO — SECTION 01 / ORB + SCORE REVEAL",
        "window.MAXESS_RESULT",
        "overallScore",
        "mx-nitro-orbit",
        "6s ease-in-out infinite",
        "10s linear infinite",
        "prefers-reduced-motion:reduce",
        "width:100vw",
        "calc(50% - 50vw)",
    )
    missing_embed = [x for x in required_embed if x not in embed]
    if missing_embed:
        raise SystemExit("NITRO LAW FAIL: Groove embed integrity missing: " + ", ".join(missing_embed))


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
    token = re.compile(r"'(?:\\.|[^'\\])*" + re.escape(label) + r"(?:\\.|[^'\\])*'\s*\+", re.S)
    matches = list(token.finditer(js))
    if len(matches) > 1:
        raise SystemExit(f"SECTION 01: multiple active {label} chunks found ({len(matches)})")
    if not matches:
        return js, 0
    return js[:matches[0].start()] + replacement + "\n" + js[matches[0].end():], 1


def refine_top_presentation(js: str) -> tuple[str, int]:
    """Add one idempotent post-render refinement to the V21 Section 01 owner.

    This deliberately preserves the existing V21 section order, score source,
    Orb construction, and listen control. It only improves the visible top
    presentation and guarantees the contract-required Orbital Bead exists.
    """
    marker = "  function build(r){"
    if marker not in js:
        raise SystemExit("SECTION 01: V21 build function anchor missing")

    if "function refineSection01Top()" in js:
        return js, 0

    helper = r'''  function refineSection01Top(){
    var shell=root.querySelector('.v21-shell');
    if(!shell) throw new Error('SECTION 01: V21 shell missing after render');
    var sections=shell.querySelectorAll(':scope > .v21-section');
    if(sections.length<2) throw new Error('SECTION 01: expected Naya + score sections');

    var nayaSection=sections[0];
    var scoreSection=sections[1];
    var naya=nayaSection.querySelector('.v21-naya');
    var scoreWrap=scoreSection.querySelector('.v21-score-wrap');
    var orb=scoreSection.querySelector('.v21-score-orb');
    if(!naya || !scoreWrap || !orb) throw new Error('SECTION 01: protected top components missing');

    var nayaTitle=naya.querySelector('.b1s1-title,.v21-naya-title');
    if(nayaTitle) nayaTitle.textContent="Hi, I'm Naya.";

    var nayaSub=naya.querySelector('.b1s1-sub,.v21-naya-sub');
    if(nayaSub){
      nayaSub.textContent="I've got your results. Take a look through your report, and when you're ready, listen to me walk you through what it means.";
    }

    var scoreKicker=scoreWrap.querySelector('.v21-kicker');
    if(scoreKicker) scoreKicker.textContent='YOUR AI SCORE';

    var scoreLabel=orb.querySelector('.v21-score-label');
    if(scoreLabel) scoreLabel.setAttribute('hidden','');

    var scoreNumber=orb.querySelector('.v21-score-number');
    var rawScore=scoreNumber ? scoreNumber.textContent.trim() : '';
    var numericScore=Number(rawScore);
    if(!Number.isFinite(numericScore)) throw new Error('SECTION 01: score presentation value is invalid');
    orb.setAttribute('role','img');
    orb.setAttribute('aria-label','Your AI score is '+Math.round(numericScore)+' out of 100');

    var context=scoreWrap.querySelector('.v21-final-note');
    if(context){
      context.textContent="Your score isn't a judgment. It's a signal — a snapshot of your current AI capability and a clue to where your next breakthrough could create the most leverage.";
    }

    scoreWrap.querySelectorAll('.v21-stage,.v21-stage-five').forEach(function(el){ el.setAttribute('hidden',''); });

    var bead=orb.querySelector('.b1s1-orbital-bead');
    if(!bead){
      bead=document.createElement('span');
      bead.className='b1s1-orbital-bead';
      bead.setAttribute('aria-hidden','true');
      orb.appendChild(bead);
    }else{
      bead.setAttribute('aria-hidden','true');
    }

    naya.setAttribute('data-section01-role','naya-welcome');
    scoreSection.setAttribute('data-section01-role','score-reveal');
    orb.setAttribute('data-section01-role','signature-orb');
    bead.setAttribute('data-section01-role','orbital-bead');
  }

'''
    js = js.replace(marker, helper + marker, 1)

    call_marker = "    var btn=root.querySelector('.v21-listen');if(btn)btn.addEventListener('click',listen);"
    if call_marker not in js:
        raise SystemExit("SECTION 01: V21 post-render binding anchor missing")
    js = js.replace(call_marker, "    refineSection01Top();\n" + call_marker, 1)

    final_sync = r'''
  function reinforceSection01Top(){
    var tries=0;
    (function tick(){
      if(root.querySelector('.v21-shell')){
        try{ refineSection01Top(); }catch(e){ root.setAttribute('data-section01-top-error',String(e && e.message || e)); }
      }
      if(++tries<20) setTimeout(tick,150);
    })();
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',reinforceSection01Top,{once:true}); else reinforceSection01Top();
'''
    end_marker = "\n})();"
    end_index = js.rfind(end_marker)
    if end_index < 0:
        raise SystemExit("SECTION 01: canonical V21 script closing anchor missing")
    js = js[:end_index] + final_sync + js[end_index:]
    return js, 1


def align(js: str) -> tuple[str, dict[str, int]]:
    changes: dict[str, int] = {}

    js, n = replace_section_chunk(js, "YOUR LEVER", "")
    changes["YOUR LEVER"] = n

    js, n = replace_section_chunk(js, "YOUR NEXT MOVE", "")
    changes["YOUR NEXT MOVE"] = n

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

    old_ids = "var ids=['#mx-naya-listen','#v11-naya-listen','#v13-listen','.mx-naya-listen','.v18-listen'];"
    new_ids = "var ids=['.v21-listen.b1s1-listen','.v21-listen'];"
    if old_ids in js:
        js = js.replace(old_ids, new_ids)
        changes["LISTEN OWNER"] = 1
    else:
        changes["LISTEN OWNER"] = 0

    js, n = refine_top_presentation(js)
    changes["TOP PRESENTATION"] = n

    bad_patterns = (
        "root.innerHTML='<div class=\"root.innerHTML=",
        "root.innerHTML=\"<div class=\"root.innerHTML=",
    )
    if any(p in js for p in bad_patterns):
        raise SystemExit("SECTION 01: renderer self-corruption guard triggered")

    return js, changes


def validate_section01_builder(text: str) -> None:
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
        'function refineSection01Top()',
        "YOUR AI SCORE",
        "I'm Naya.",
        "I've got your results.",
        "Your score isn't a judgment.",
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
        print("TOP PRESENTATION: ALREADY REFINED")
        print("LISTEN OWNER: V21 HERO CONTROL")
        print("NITRO MASTER CONTRACT: READ + VERIFIED")
        print("SECTION 01 CONTRACT: READ + VERIFIED")
        print("GROOVE EMBED: PRESENT + VERIFIED")
        print("STATIC SECTION 01 EVIDENCE: PASS")
        return 0

    BUILDER.write_text(updated, encoding="utf-8")

    print("MAXESS SECTION 01 PRODUCT ALIGNMENT: PASS")
    print("GOLDEN MASTER: PRESERVED")
    print(f"YOUR LEVER: {'REMOVED' if changes['YOUR LEVER'] else 'ALREADY ABSENT'}")
    print(f"YOUR NEXT MOVE: {'REMOVED' if changes['YOUR NEXT MOVE'] else 'ALREADY ABSENT'}")
    print(f"PLAYGROUND: {'REPLACED -> NAYA · IN PRACTICE' if changes['PLAYGROUND'] else 'ALREADY ABSENT/ALIGNED'}")
    print(f"TOP PRESENTATION: {'REFINED' if changes['TOP PRESENTATION'] else 'ALREADY REFINED'}")
    print(f"LISTEN OWNER: {'V21 HERO CONTROL' if changes['LISTEN OWNER'] or '.v21-listen.b1s1-listen' in aligned_js else 'UNCHANGED'}")
    print("NODE CHECK: PASS")
    print("PYTHON CHECK: PASS")
    print("STATIC SECTION 01 EVIDENCE: PASS")
    print("NITRO MASTER CONTRACT: READ + VERIFIED")
    print("SECTION 01 CONTRACT: READ + VERIFIED")
    print("GROOVE EMBED: PRESENT + VERIFIED")
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