#!/usr/bin/env python3
"""Execute MAXESS Batch 1 against the real canonical builder.

Batch 1 owns the first three experience chapters:
1. Naya Arrival / Orientation
2. MAXESS Score / Orb
3. What Your Score Means

This tool is intentionally a PRODUCT MUTATION tool. It refuses to succeed when
none of the three product sections materially change.
"""

from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"
LEDGER = ROOT / "docs" / "MAXESS-CHANGE-LEDGER.md"
NOTES = ROOT / "docs" / "MAXESS-SMART-NOTES.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    new, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 match, found {count}")
    return new


def main() -> int:
    if not BUILDER.exists():
        raise SystemExit("MAXESS Batch 1: canonical builder missing")

    before = sha(BUILDER)
    s = BUILDER.read_text(encoding="utf-8")

    # Naya Arrival: make the opening a clear personal conversation, not merely a header.
    s = replace_once(
        s,
        r"<div class=\\\"v21-naya\\\"><img class=\\\"v21-avatar\\\".*?</div>\\\\n?\\s*</div></section>\\\\n",
        '''<div class=\\\"v21-naya\\\"><div class=\\\"v21-naya-presence\\\"><span class=\\\"v21-kicker\\\">NAYA · YOUR AI GUIDE</span><div class=\\\"v21-naya-orbit\\\"><img class=\\\"v21-avatar\\\" src=\\\"https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg\\\" alt=\\\"Naya, your AI guide\\\"><span class=\\\"v21-naya-spark\\\" aria-hidden=\\\"true\\\"></span></div></div><div><h1 class=\\\"v21-naya-title\\\">'+(name?reportName:'Hi. I have looked at your results.')+'</h1><p class=\\\"v21-naya-sub\\\">This is not your judgment. <strong>It is your map.</strong></p><p class=\\\"v21-naya-whisper\\\">I am going to help you see what is already working, what matters most, and what to do next.</p></div><button class=\\\"v21-listen v21-btn-primary\\\" type=\\\"button\\\" aria-label=\\\"Listen to Naya interpret your MAXESS results\\\">LISTEN TO NAYA <span aria-hidden=\\\"true\\\">▶</span></button></div></div></section>\\n''',
        "SECTION 01 NAYA",
    )

    # Score / Orb: make the score reveal more signature and informative.
    s = replace_once(
        s,
        r"<section class=\\\"v21-section v21-dark\\\"><div class=\\\"v21-inner v21-score-wrap\\\">.*?</section>\\\\n",
        '''<section class=\\\"v21-section v21-dark v21-score-hero\\\"><div class=\\\"v21-inner v21-score-wrap\\\"><span class=\\\"v21-kicker\\\">YOUR MAXESS SCORE</span><div class=\\\"v21-score-intro\\\">One number. A much bigger picture.</div><div class=\\\"v21-score-orb v21-orb-signature\\\" aria-label=\\\"Your MAXESS score is '+Math.round(s)+' out of 100\\\"><span class=\\\"v21-orb-ring v21-orb-ring-a\\\" aria-hidden=\\\"true\\\"></span><span class=\\\"v21-orb-ring v21-orb-ring-b\\\" aria-hidden=\\\"true\\\"></span><span class=\\\"v21-orb-glow\\\" aria-hidden=\\\"true\\\"></span><div><div class=\\\"v21-score-number\\\">'+Math.round(s)+'</div><div class=\\\"v21-score-label\\\">MAXESS SCORE</div></div></div><span class=\\\"v21-stage\\\">'+st+'</span><div class=\\\"v21-stage-five\\\">'+stageHTML+'</div><p class=\\\"v21-final-note\\\">Your score is a starting point—not a verdict. The next section turns the number into something you can understand and use.</p></div></section>\\n''',
        "SECTION 02 SCORE ORB",
    )

    # Score meaning: turn the overall score into an explicit interpretation chapter.
    s = replace_once(
        s,
        r"<section class=\\\"v21-section v21-light\\\"><div class=\\\"v21-inner\\\"><span class=\\\"v21-kicker\\\" style=\\\"color:#7445ad\\\">WHAT YOUR SCORES MEAN</span>.*?</section>\\\\n",
        '''<section class=\\\"v21-section v21-light v21-score-meaning\\\"><div class=\\\"v21-inner\\\"><span class=\\\"v21-kicker\\\" style=\\\"color:#7445ad\\\">WHAT YOUR SCORE MEANS</span><h2 class=\\\"v21-section-title\\\">The number is useful. <em>The meaning is the value.</em></h2><div class=\\\"v21-meaning-lead\\\"><div class=\\\"v21-meaning-score\\\"><strong>'+Math.round(s)+'</strong><span>'+st+'</span></div><div><h3>What this score says</h3><p>It describes your current AI capability across five connected dimensions. It shows where you have momentum and where focused improvement can create more leverage.</p><h3>What it does not say</h3><p>It is not a judgment of your intelligence, creativity, or potential. It is a starting position you can improve.</p></div></div><div class=\\\"v21-create-score-improve\\\"><span>YOUR WORKING LOOP</span><b>CREATE</b><i>→</i><b>SCORE</b><i>→</i><b>IMPROVE</b><p>Use the result as feedback. Make something real, judge the quality, improve the weak point, and repeat.</p></div><div class=\\\"v21-naya-note\\\"><img src=\\\"https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg\\\" alt=\\\"Naya, your AI guide\\\"><div><b>Naya · your guide</b><strong>Here is how I would use your result.</strong><p>Don't chase a higher number just to chase a higher number. Use your strongest capability, build your clearest leverage point, and make the improvement visible.</p></div></div></div></section>\\n''',
        "SECTION 03 SCORE MEANING",
    )

    # New visual language for Batch 1. Insert before canonical CSS closing tag.
    batch_css = r'''
#maxess-results-10.v21-canonical .v21-naya{grid-template-columns:auto 1fr auto;position:relative;overflow:hidden;background:radial-gradient(circle at 0% 0%,rgba(155,99,255,.24),transparent 40%),linear-gradient(135deg,#09060f,#12091e 58%,#08050d);border-color:rgba(202,168,255,.24)}
#maxess-results-10.v21-canonical .v21-naya-presence{display:grid;justify-items:center;gap:8px}
#maxess-results-10.v21-canonical .v21-naya-orbit{position:relative;width:92px;height:92px;display:grid;place-items:center}
#maxess-results-10.v21-canonical .v21-naya-orbit::before{content:"";position:absolute;inset:3px;border-radius:50%;border:1px solid rgba(202,168,255,.34);box-shadow:0 0 32px rgba(155,99,255,.22)}
#maxess-results-10.v21-canonical .v21-avatar{width:72px;height:72px;position:relative;z-index:2}
#maxess-results-10.v21-canonical .v21-naya-spark{position:absolute;right:3px;top:9px;width:11px;height:11px;border-radius:50%;background:#d8baff;box-shadow:0 0 18px #b990ff;z-index:3}
#maxess-results-10.v21-canonical .v21-naya-whisper{margin:10px 0 0;color:rgba(255,255,255,.58);font-size:14px;max-width:720px}
#maxess-results-10.v21-canonical .v21-btn-primary{background:linear-gradient(135deg,#b990ff,#7445ad);border-color:#d8c0ff;box-shadow:inset 0 1px rgba(255,255,255,.28),0 14px 32px rgba(80,34,145,.34)}
#maxess-results-10.v21-canonical .v21-score-hero{padding-top:clamp(70px,9vw,124px);padding-bottom:clamp(70px,9vw,124px)}
#maxess-results-10.v21-canonical .v21-score-intro{margin:10px auto 18px;color:rgba(255,255,255,.62);font-size:clamp(15px,2vw,19px)}
#maxess-results-10.v21-canonical .v21-orb-signature{overflow:visible;border-color:rgba(202,168,255,.28);background:radial-gradient(circle at 34% 22%,rgba(255,255,255,.30),transparent 9%),radial-gradient(circle at 50% 50%,rgba(155,99,255,.26),transparent 48%),radial-gradient(circle at 55% 65%,rgba(68,217,206,.10),transparent 62%),#08060c;box-shadow:inset 0 0 110px rgba(155,99,255,.24),0 46px 120px rgba(0,0,0,.62),0 0 120px rgba(155,99,255,.20)}
#maxess-results-10.v21-canonical .v21-orb-ring{position:absolute;inset:-18px;border-radius:50%;border:1px solid rgba(202,168,255,.10);pointer-events:none}
#maxess-results-10.v21-canonical .v21-orb-ring-b{inset:-38px;border-color:rgba(155,99,255,.08);transform:rotate(12deg) scaleX(.96)}
#maxess-results-10.v21-canonical .v21-orb-glow{position:absolute;inset:-4px;border-radius:50%;background:radial-gradient(circle,rgba(184,144,255,.20),transparent 62%);filter:blur(12px);pointer-events:none}
#maxess-results-10.v21-canonical .v21-score-meaning .v21-section-title em{font-style:normal;color:#7445ad}
#maxess-results-10.v21-canonical .v21-meaning-lead{display:grid;grid-template-columns:180px 1fr;gap:30px;align-items:center;margin-top:30px;padding:28px;border-radius:30px;background:linear-gradient(135deg,#fff,#f4eefb);border:1px solid rgba(40,22,60,.10);box-shadow:0 28px 70px rgba(40,20,70,.10)}
#maxess-results-10.v21-canonical .v21-meaning-score{width:150px;aspect-ratio:1;border-radius:50%;display:grid;place-items:center;align-content:center;text-align:center;background:radial-gradient(circle at 34% 22%,rgba(255,255,255,.95),transparent 13%),radial-gradient(circle,#b990ff22,transparent 58%),#fff;border:1px solid #d9c3ef;box-shadow:inset 0 0 42px #b990ff22,0 20px 45px rgba(45,20,75,.12)}
#maxess-results-10.v21-canonical .v21-meaning-score strong{font-size:62px;line-height:.8;letter-spacing:-.08em;color:#17131d}
#maxess-results-10.v21-canonical .v21-meaning-score span{margin-top:10px;font-size:9px;letter-spacing:.15em;text-transform:uppercase;font-weight:950;color:#7445ad}
#maxess-results-10.v21-canonical .v21-meaning-lead h3{margin:0 0 6px;font-size:18px}
#maxess-results-10.v21-canonical .v21-meaning-lead p{margin:0 0 18px;color:#5d5764;max-width:760px}
#maxess-results-10.v21-canonical .v21-create-score-improve{margin-top:18px;padding:24px 26px;border-radius:28px;background:#0a070f;color:#fff;border:1px solid rgba(202,168,255,.18);display:flex;align-items:center;gap:12px;flex-wrap:wrap;box-shadow:0 24px 60px rgba(0,0,0,.20)}
#maxess-results-10.v21-canonical .v21-create-score-improve span{width:100%;font-size:9px;letter-spacing:.16em;color:#caa8ff;font-weight:950}
#maxess-results-10.v21-canonical .v21-create-score-improve b{font-size:15px}
#maxess-results-10.v21-canonical .v21-create-score-improve i{font-style:normal;color:#b990ff}
#maxess-results-10.v21-canonical .v21-create-score-improve p{width:100%;margin:2px 0 0;color:rgba(255,255,255,.66);font-size:14px}
@media(max-width:760px){#maxess-results-10.v21-canonical .v21-naya{grid-template-columns:1fr;text-align:center}.v21-naya-presence{justify-items:center}.v21-listen{grid-column:auto}.#maxess-results-10.v21-canonical .v21-meaning-lead{grid-template-columns:1fr;text-align:center}.#maxess-results-10.v21-canonical .v21-meaning-score{margin:auto}}
'''
    s = replace_once(s, r"\n</style>", "\n" + batch_css + "</style>", "BATCH1 CSS")

    after = sha(BUILDER) if False else None
    if s == BUILDER.read_text(encoding="utf-8"):
        raise SystemExit("MAXESS BATCH 1: NO PRODUCT SOURCE CHANGE")

    BUILDER.write_text(s, encoding="utf-8")
    after = sha(BUILDER)

    # Durable evidence: append a compact record, without changing status until QA proves it.
    if LEDGER.exists():
        ledger = LEDGER.read_text(encoding="utf-8")
        entry = (
            "\n## 2026-08-17 — Batch 1 product mutation executed\n\n"
            f"Builder SHA before: `{before}`\n"
            f"Builder SHA after: `{after}`\n\n"
            "Sections targeted: Naya Arrival, Score/Orb, What Your Score Means.\n"
            "Status remains IN PROGRESS until rebuild + QA + visual evidence confirms completion.\n"
        )
        LEDGER.write_text(ledger + entry, encoding="utf-8")

    if NOTES.exists():
        notes = NOTES.read_text(encoding="utf-8")
        notes += (
            "\n## 2026-08-17 — Batch 1 execution\n\n"
            "Product execution is now section-driven rather than marker-driven. The batch executor refuses a no-op and requires a real builder/source delta before reporting success.\n"
        )
        NOTES.write_text(notes, encoding="utf-8")

    print("MAXESS BATCH 1 PRODUCT MUTATION: SOURCE CHANGED")
    print(f"Builder SHA before: {before}")
    print(f"Builder SHA after:  {after}")
    print("Sections mutated: 01 Naya Arrival / 02 Score Orb / 03 Score Meaning")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
