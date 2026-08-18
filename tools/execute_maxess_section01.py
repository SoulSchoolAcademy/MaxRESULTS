#!/usr/bin/env python3
"""Governed MAXESS Section 01 refinement owner.

Patches only the canonical V21 runtime owner. The generated Results artifact is
rebuilt by the repository workflow; this file never becomes a second renderer.
"""
from __future__ import annotations
from pathlib import Path
import hashlib
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"
MASTER = ROOT / "NITRO-MASTER-EXECUTION-PROTOCOL.md"
TASK = ROOT / "docs" / "NITRO-SECTION-01-ORB-EXECUTION-CONTRACT.md"
EMBED = ROOT / "docs" / "SECTION-01-ORB-GROOVE-EMBED.html"
CANONICAL = '<script id="maxess-results-v21-canonical-js">'
MARK = '/* MAXESS-SECTION-01-GOLDEN-MASTER */'

def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def require_contracts() -> None:
    for p, label in ((MASTER, "master contract"), (TASK, "Section 01 contract"), (EMBED, "Groove embed")):
        if not p.exists(): raise SystemExit(f"NITRO LAW FAIL: {label} missing: {p}")
    master = MASTER.read_text(encoding="utf-8")
    task = TASK.read_text(encoding="utf-8")
    embed = EMBED.read_text(encoding="utf-8")
    for token in ("MAXESS NITRO MASTER EXECUTION CONTRACT", "DO NOT GUESS.", "CAN I PROVE IT?"):
        if token not in master: raise SystemExit(f"NITRO LAW FAIL: master token missing: {token}")
    for token in ("Section 01 — Orb / Score Reveal", ".v21-score-orb", ".b1s1-orbital-bead", "window.MAXESS_RESULT", "Naya"):
        if token not in task: raise SystemExit(f"NITRO LAW FAIL: Section 01 token missing: {token}")
    for token in ("MAXESS NITRO — SECTION 01 / ORB + SCORE REVEAL", "window.MAXESS_RESULT", "overallScore", "mx-nitro-orbit", "prefers-reduced-motion:reduce"):
        if token not in embed: raise SystemExit(f"NITRO LAW FAIL: Groove token missing: {token}")

def extract_js(source: str) -> tuple[int, int, str]:
    tag = source.find(CANONICAL)
    if tag < 0: raise SystemExit("SECTION 01 FAIL: canonical V21 script missing")
    start = source.find(">", tag) + 1
    end = source.find("</script>", start)
    if start <= 0 or end < 0: raise SystemExit("SECTION 01 FAIL: canonical V21 script boundaries invalid")
    return start, end, source[start:end]

def validate_js(js: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(js); path = Path(f.name)
    try: result = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)
    finally: path.unlink(missing_ok=True)
    if result.returncode: raise SystemExit(result.stderr.strip() or "SECTION 01 FAIL: Node syntax check failed")

def validate_builder(text: str) -> None:
    required = (MARK, ".v21-score-orb", ".b1s1-orbital-bead", "b1s1-orbit", "window.MAXESS_RESULT", "var colorFor=function(v)", "prefers-reduced-motion:reduce", "maxess-results-v21-canonical-css", "maxess-results-v21-canonical-js", "YOUR AI SCORE", "I'm Naya.", "I've got your results.", "Your score isn't a judgment.")
    missing = [x for x in required if x not in text]
    if missing: raise SystemExit("SECTION 01 STATIC EVIDENCE FAIL: " + ", ".join(missing))
    if text.count(MARK) != 2: raise SystemExit("SECTION 01 STATIC EVIDENCE FAIL: Golden Master marker count != 2")
    if text.count("b1s1-orbital-bead") < 2: raise SystemExit("SECTION 01 STATIC EVIDENCE FAIL: Orbital Bead evidence incomplete")
    if re.search(r"(^|\n)(<<<<<<<|=======|>>>>>>>)( |\n|$)", text): raise SystemExit("SECTION 01 STATIC EVIDENCE FAIL: conflict marker remains")

def patch_runtime(js: str) -> tuple[str, bool]:
    marker = "function refineSection01HeroV2()"
    if marker in js: return js, False
    insert_at = js.find("  function reinforceSection01Top()")
    if insert_at < 0: insert_at = js.rfind("\n})();")
    if insert_at < 0: raise SystemExit("SECTION 01 FAIL: canonical runtime insertion anchor missing")
    helper = r'''  function refineSection01HeroV2(){
    var root=document.getElementById('maxess-results-10');
    if(!root || !root.classList.contains('v21-canonical')) return false;
    var shell=root.querySelector('.v21-shell');
    if(!shell) return false;
    var sections=shell.querySelectorAll(':scope > .v21-section');
    if(sections.length<2) return false;
    var naya=sections[0].querySelector('.v21-naya');
    var scoreSection=sections[1];
    var scoreWrap=scoreSection.querySelector('.v21-score-wrap');
    var orb=scoreSection.querySelector('.v21-score-orb');
    if(!naya || !scoreWrap || !orb) return false;
    var styleId='maxess-section01-naya-hero-v2';
    if(!document.getElementById(styleId)){
      var style=document.createElement('style'); style.id=styleId;
      style.textContent=`
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"]{position:relative;isolation:isolate;overflow:hidden;grid-template-columns:128px minmax(0,1fr) auto;gap:26px;max-width:1160px;min-height:198px;padding:30px 32px;border:1px solid rgba(214,180,255,.34);border-radius:34px;background:radial-gradient(circle at 8% 50%,rgba(164,91,255,.20),transparent 30%),radial-gradient(circle at 82% 15%,rgba(255,255,255,.08),transparent 25%),radial-gradient(circle at 94% 90%,rgba(82,126,255,.11),transparent 28%),linear-gradient(135deg,#08050d 0%,#170b29 48%,#08050e 100%);box-shadow:0 34px 110px rgba(0,0,0,.52),inset 0 1px rgba(255,255,255,.17),inset 0 -1px rgba(0,0,0,.45)}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"]::before{content:"";position:absolute;left:-90px;top:-120px;width:340px;height:340px;border-radius:50%;background:radial-gradient(circle,rgba(196,133,255,.24),transparent 68%);filter:blur(10px);z-index:-1;pointer-events:none}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"]::after{content:"";position:absolute;right:8%;bottom:0;width:280px;height:2px;background:linear-gradient(90deg,transparent,rgba(205,163,255,.80),transparent);opacity:.72;z-index:0;pointer-events:none}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .b1s1-avatar{position:relative;z-index:2;width:128px;height:128px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.90);box-shadow:0 0 0 9px rgba(155,99,255,.13),0 0 42px rgba(155,99,255,.22),0 22px 48px rgba(0,0,0,.48)}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .b1s1-title{position:relative;z-index:2;margin-top:7px;max-width:780px;font-size:clamp(34px,4vw,54px);line-height:.96;font-weight:950;letter-spacing:-.065em;color:#fff}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .b1s1-sub{position:relative;z-index:2;max-width:760px;margin:12px 0 0;color:rgba(255,255,255,.78);font-size:16px;line-height:1.55}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .b1s1-kicker{position:relative;z-index:2;color:#d6b9ff;font-size:10px;font-weight:950;letter-spacing:.22em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .v21-listen.b1s1-listen{position:relative;z-index:2;align-self:center;min-width:186px;min-height:58px;padding:0 24px;border-radius:18px;border:1px solid rgba(218,187,255,.72);background:linear-gradient(180deg,#19101f,#09070c);color:#fff;font-size:12px;font-weight:950;letter-spacing:.08em;box-shadow:inset 0 1px rgba(255,255,255,.13),0 16px 34px rgba(0,0,0,.40),0 0 24px rgba(155,99,255,.12)}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .v21-listen.b1s1-listen:hover{transform:translateY(-2px);border-color:#d9bbff;box-shadow:inset 0 1px rgba(255,255,255,.18),0 20px 42px rgba(0,0,0,.48),0 0 30px rgba(155,99,255,.18)}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .v21-listen.b1s1-listen:focus-visible{outline:2px solid #fff;outline-offset:5px}
@media(max-width:820px){#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"]{grid-template-columns:108px minmax(0,1fr);min-height:176px;padding:26px;gap:22px}#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .b1s1-avatar{width:108px;height:108px}#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .v21-listen.b1s1-listen{grid-column:1/-1;width:100%}}
@media(max-width:520px){#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"]{grid-template-columns:1fr;text-align:center;min-height:0;padding:26px 20px;gap:14px}#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .b1s1-avatar{width:104px;height:104px;margin:0 auto}#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .b1s1-sub{margin-left:auto;margin-right:auto;max-width:420px}#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .v21-listen.b1s1-listen{margin-top:4px;min-width:0}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v21-canonical .v21-naya.b1s1-naya[data-section01-role="naya-welcome"] .v21-listen.b1s1-listen{transition:none;transform:none}}
`;
      document.head.appendChild(style);
    }
    var title=naya.querySelector('.v21-naya-title,.b1s1-title');
    if(title) title.textContent="Hi, I'm Naya.";
    var sub=naya.querySelector('.v21-naya-sub,.b1s1-sub');
    if(sub) sub.textContent="I've got your results. Take a look through your report, and when you're ready, listen to me walk you through what it means.";
    var kicker=naya.querySelector('.v21-kicker,.b1s1-kicker');
    if(kicker) kicker.textContent='NAYA · YOUR GUIDE';
    var listen=naya.querySelector('.v21-listen');
    if(listen){listen.classList.add('b1s1-listen');listen.innerHTML='<span aria-hidden="true">▶</span><span> LISTEN TO NAYA</span>';listen.setAttribute('aria-label','Listen to Naya interpret your MAXESS results');listen.type='button'}
    var scoreKicker=scoreWrap.querySelector('.v21-kicker');
    if(scoreKicker) scoreKicker.textContent='YOUR AI SCORE';
    scoreWrap.setAttribute('data-section01-role','score-reveal');
    var label=orb.querySelector('.v21-score-label');
    if(label) label.setAttribute('hidden','');
    var number=orb.querySelector('.v21-score-number');
    var score=number?Number(number.textContent.trim()):NaN;
    if(!Number.isFinite(score)) return false;
    orb.setAttribute('role','img');orb.setAttribute('aria-label','Your AI score is '+Math.round(score)+' out of 100');
    var note=scoreWrap.querySelector('.v21-final-note');
    if(note) note.textContent="Your score isn't a judgment. It's a signal — a snapshot of your current AI capability and a clue to where your next breakthrough could create the most leverage.";
    naya.setAttribute('data-section01-role','naya-welcome');naya.setAttribute('aria-label','Naya welcome');
    var bead=orb.querySelector('.b1s1-orbital-bead');
    if(bead) bead.setAttribute('aria-hidden','true');
    return true;
  }

'''
    js = js[:insert_at] + helper + js[insert_at:]
    tail = "  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',function(){refineSection01HeroV2();},{once:true}); else refineSection01HeroV2();\n"
    end = js.rfind("\n})();")
    if end < 0: raise SystemExit("SECTION 01 FAIL: canonical closing anchor missing")
    js = js[:end] + tail + js[end:]
    return js, True

def main() -> int:
    require_contracts()
    if not BUILDER.exists(): raise SystemExit("SECTION 01 FAIL: canonical builder missing")
    original = BUILDER.read_text(encoding="utf-8")
    if MARK not in original: raise SystemExit("SECTION 01 FAIL: Golden Master layer missing; refusing to invent authority")
    validate_builder(original)
    start, end, js = extract_js(original)
    patched_js, changed = patch_runtime(js)
    validate_js(patched_js)
    updated = original[:start] + patched_js + original[end:]
    validate_builder(updated)
    if updated == original:
        print("SECTION 01: already aligned"); print("GOLDEN MASTER: PRESERVED"); print("NAYA HERO V2: ALREADY PRESENT"); print("STATIC SECTION 01 EVIDENCE: PASS"); return 0
    candidate = ROOT / ".section01_candidate.py"
    candidate.write_text(updated, encoding="utf-8")
    try: subprocess.run(["python", "-m", "py_compile", str(candidate)], check=True)
    finally: candidate.unlink(missing_ok=True)
    BUILDER.write_text(updated, encoding="utf-8")
    print("MAXESS SECTION 01 NITRO REFINEMENT: PASS")
    print("GOLDEN MASTER: PRESERVED"); print("NAYA HERO V2: REFINED"); print("SCORE SYSTEM: PRESERVED"); print("ORB: PRESERVED"); print("ORBITAL BEAD: PRESERVED"); print("LISTEN CONTROL: PRESERVED"); print("STATIC SECTION 01 EVIDENCE: PASS")
    print("BUILDER SHA BEFORE:", sha(original)); print("BUILDER SHA AFTER: ", sha(updated))
    return 0

if __name__ == "__main__": raise SystemExit(main())