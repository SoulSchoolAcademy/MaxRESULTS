#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"


CSS_APPEND = r'''
/* MAXESS-AAA-FINAL-PRODUCT-CSS */
#maxess-results-10.v21-canonical .v21-fingerprint-panel{display:grid;grid-template-columns:minmax(280px,.9fr) minmax(0,1.1fr);gap:28px;align-items:center;margin-top:30px;padding:28px;border-radius:36px;background:linear-gradient(145deg,#faf9fd,#f1eafa);border:1px solid rgba(90,52,130,.12);box-shadow:0 28px 80px rgba(30,15,50,.12)}
#maxess-results-10.v21-canonical .v21-fingerprint-visual{position:relative;aspect-ratio:1;display:grid;place-items:center}
#maxess-results-10.v21-canonical .v21-fingerprint-visual svg{width:100%;height:100%;overflow:visible}
#maxess-results-10.v21-canonical .v21-fingerprint-core{position:absolute;inset:0;display:grid;place-items:center;text-align:center;pointer-events:none}
#maxess-results-10.v21-canonical .v21-fingerprint-core b{display:block;font-size:clamp(56px,8vw,94px);line-height:.8;letter-spacing:-.08em;color:#17131d}
#maxess-results-10.v21-canonical .v21-fingerprint-core span{display:block;margin-top:10px;font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase;color:#7445ad}
#maxess-results-10.v21-canonical .v21-meaning-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:24px}
#maxess-results-10.v21-canonical .v21-meaning-item{padding:20px;border-radius:22px;background:#fff;border:1px solid rgba(30,20,40,.10);box-shadow:0 18px 45px rgba(30,15,50,.08)}
#maxess-results-10.v21-canonical .v21-meaning-item b{display:block;font-size:12px;letter-spacing:.08em}
#maxess-results-10.v21-canonical .v21-meaning-item p{margin:8px 0 0;color:#5d5764;font-size:14px}
#maxess-results-10.v21-canonical .v21-naya-note{display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:start;margin-top:22px;padding:18px 20px;border-radius:24px;background:linear-gradient(135deg,rgba(155,99,255,.08),rgba(255,255,255,.94));border:1px solid rgba(115,68,170,.13);box-shadow:0 18px 48px rgba(30,15,50,.09)}
#maxess-results-10.v21-canonical .v21-naya-note img{width:52px;height:52px;border-radius:50%;object-fit:cover;border:2px solid #fff;box-shadow:0 8px 22px rgba(30,15,50,.18)}
#maxess-results-10.v21-canonical .v21-naya-note b{display:block;font-size:9px;letter-spacing:.15em;text-transform:uppercase;color:#7445ad}
#maxess-results-10.v21-canonical .v21-naya-note strong{display:block;margin-top:4px;font-size:17px;color:#17131d}
#maxess-results-10.v21-canonical .v21-naya-note p{margin:6px 0 0;color:#5d5764;font-size:14px;line-height:1.55}
#maxess-results-10.v21-canonical .v21-stage-five{margin-top:18px;display:flex;flex-wrap:wrap;justify-content:center;gap:7px}
#maxess-results-10.v21-canonical .v21-stage-five span{padding:7px 10px;border-radius:999px;border:1px solid rgba(202,168,255,.22);background:rgba(18,10,24,.72);color:rgba(255,255,255,.68);font-size:8px;font-weight:950;letter-spacing:.10em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-stage-five span.v21-active{background:#fff;color:#17131d;border-color:#fff}
#maxess-results-10.v21-canonical .v21-next-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:26px}
#maxess-results-10.v21-canonical .v21-next-card{padding:24px;border-radius:26px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12)}
#maxess-results-10.v21-canonical .v21-next-card .v21-number{font-size:10px;letter-spacing:.14em;font-weight:950;color:#d8baff}
#maxess-results-10.v21-canonical .v21-next-card h3{margin-top:9px;font-size:25px}
#maxess-results-10.v21-canonical .v21-next-card p{margin:8px 0 0;color:rgba(255,255,255,.70);font-size:14px}
#maxess-results-10.v21-canonical .v21-master{transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease}
#maxess-results-10.v21-canonical .v21-master:hover{transform:translateY(-5px);box-shadow:0 28px 60px rgba(0,0,0,.24);border-color:rgba(202,168,255,.40)}
#maxess-results-10.v21-canonical .v21-match{display:inline-flex;margin-bottom:10px;padding:6px 9px;border-radius:999px;background:rgba(202,168,255,.12);border:1px solid rgba(202,168,255,.22);color:#e4d2ff;font-size:8px;font-weight:950;letter-spacing:.12em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-playground-premium{display:grid;grid-template-columns:1.1fr .9fr;gap:22px;align-items:center}
#maxess-results-10.v21-canonical .v21-playground-panel{padding:26px;border-radius:28px;background:#fff;border:1px solid rgba(30,20,40,.09);box-shadow:0 24px 62px rgba(30,15,50,.10)}
#maxess-results-10.v21-canonical .v21-media-host{display:grid;gap:16px;margin-top:18px}
#maxess-results-10.v21-canonical .v21-media-host>video,#maxess-results-10.v21-canonical .v21-media-host>iframe{width:100%;max-width:100%;border-radius:22px;display:block}
#maxess-results-10.v21-canonical .v21-final-note{max-width:760px;margin:18px auto 0;color:rgba(255,255,255,.74)}
@media(max-width:860px){#maxess-results-10.v21-canonical .v21-fingerprint-panel,#maxess-results-10.v21-canonical .v21-playground-premium{grid-template-columns:1fr}#maxess-results-10.v21-canonical .v21-meaning-grid,#maxess-results-10.v21-canonical .v21-next-grid{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v21-canonical .v21-master{transition:none!important}}
@media print{#maxess-results-10.v21-canonical .v21-fingerprint-panel,#maxess-results-10.v21-canonical .v21-naya-note,#maxess-results-10.v21-canonical .v21-next-card,#maxess-results-10.v21-canonical .v21-master{break-inside:avoid;page-break-inside:avoid}}
'''


def main() -> int:
    if not BUILDER.exists():
        raise SystemExit("BUILDER MISSING")

    s = BUILDER.read_text(encoding="utf-8")
    if "/* MAXESS-AAA-FINAL-PRODUCT-CSS */" not in s:
        marker = r"(<style id=\"maxess-results-v21-canonical-css\">.*?</style>)"
        s, n = re.subn(marker, lambda m: m.group(1).replace("</style>", CSS_APPEND + "\n</style>"), s, count=1, flags=re.S)
        if n != 1:
            raise SystemExit(f"CSS ANCHOR NOT FOUND: {n}")

    build_pat = re.compile(r"function build\(r\)\{.*?(?=\n\s*function boot\(\))", re.S)
    build_fn = r'''function build(r){
    var s=score(r), ds=dimensions(r), name=person(r), st=stage(s);
    if(s==null || ds.length!==5){
      root.setAttribute('data-results-state','awaiting');
      root.innerHTML='<section class="v21-section v21-dark"><div class="v21-inner" style="text-align:center;padding-top:120px;padding-bottom:120px"><span class="v21-kicker">MAXESS RESULTS</span><h1 class="v21-section-title" style="margin-top:18px">Your result is not loaded yet.</h1><p class="v21-section-copy" style="margin:18px auto 0;max-width:650px">Complete the MAXESS assessment and return with your Result Contract. This page does not invent a score when real result data is unavailable.</p></div></section>';
      return;
    }

    var sorted=ds.slice().sort(function(a,b){return (b.score||0)-(a.score||0)});
    var strongest=sorted[0], lowest=sorted[sorted.length-1];
    var reportName=name ? escapeHtml(name)+', here is what I see.' : 'Here is what I see.';
    var media=[];
    root.querySelectorAll('video,iframe,#naya-playground,.mx-reading,.mx-section').forEach(function(n){ if(media.indexOf(n)<0) media.push(n); });
    var mastersList=masters();
    var stageLabels=['Supporting','Foundation','Developing','Advancing','Mastering'];
    var stageHTML=stageLabels.map(function(x){return '<span class="'+(x===st?'v21-active':'')+'">'+x+'</span>';}).join('');
    var colorFor=function(v){var x=Math.max(0,Math.min(100,Number(v)||0));return 'hsl('+(178+x*1.05).toFixed(0)+' 78% '+(55+x*.10).toFixed(0)+'%)'};
    var dimensionsCopy=ds.map(function(d){return '<div class="v21-meaning-item"><b>'+escapeHtml(d.name)+'</b><p>'+escapeHtml(d.description||dimCopy(d.name,d.score))+'</p></div>';}).join('');
    var fpPoints=ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5,r=175*(Number(d.score)||0)/100;return (215+Math.cos(a)*r)+','+(215+Math.sin(a)*r)}).join(' ');
    var fpAxes=ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5;return '<line x1="215" y1="215" x2="'+(215+Math.cos(a)*175)+'" y2="'+(215+Math.sin(a)*175)+'" stroke="rgba(30,20,40,.11)"/>'}).join('');
    var fpGrid=[1,2,3,4].map(function(k){var rr=43*k,pts=[];for(var i=0;i<5;i++){var a=-Math.PI/2+i*Math.PI*2/5;pts.push((215+Math.cos(a)*rr)+','+(215+Math.sin(a)*rr))}return '<polygon points="'+pts.join(' ')+'" fill="none" stroke="rgba(30,20,40,.11)"/>'}).join('');
    var fpDots=ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5,r=175*(Number(d.score)||0)/100;return '<circle cx="'+(215+Math.cos(a)*r)+'" cy="'+(215+Math.sin(a)*r)+'" r="7" fill="'+colorFor(d.score)+'" stroke="#fff" stroke-width="3"/>'}).join('');

    root.classList.add('v21-canonical');
    root.innerHTML='<div class="v21-shell">'+
      '<section class="v21-section v21-dark"><div class="v21-inner">'+
        '<div class="v21-naya"><img class="v21-avatar" src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><span class="v21-kicker">NAYA · YOUR AI GUIDE</span><h1 class="v21-naya-title">'+(name?reportName:'Hi. I\'ve looked at your results.')+'</h1><p class="v21-naya-sub">This isn\'t your judgment. <strong>It\'s your map.</strong></p></div><button class="v21-listen" type="button" aria-label="Listen to Naya interpret your MAXESS results">LISTEN TO NAYA <span aria-hidden="true">▶</span></button></div>'+ 
      '</div></section>'+ 
      '<section class="v21-section v21-dark"><div class="v21-inner v21-score-wrap"><span class="v21-kicker">YOUR RESULT</span><div class="v21-score-orb"><div><div class="v21-score-number">'+Math.round(s)+'</div><div class="v21-score-label">MAXESS SCORE</div></div></div><span class="v21-stage">'+st+'</span><div class="v21-stage-five">'+stageHTML+'</div><p class="v21-final-note">Your score is a starting point. The report below explains the shape of your capability and where your next improvement can create the most leverage.</p></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">WHAT YOUR SCORES MEAN</span><h2 class="v21-section-title">The number is useful. The meaning is the value.</h2><p class="v21-section-copy">MAXESS is not here to judge you. It is here to make your current AI capability understandable enough to act on.</p><div class="v21-meaning-grid">'+dimensionsCopy+'</div></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><article class="v21-report"><div class="v21-report-mark"></div><span class="v21-kicker" style="color:#7445ad">YOUR PERSONALIZED REPORT</span><h2>'+reportName+'</h2><span class="v21-report-stage">'+st+'</span><p>Your strongest visible capability is <strong>'+escapeHtml(strongest.name)+'</strong>. Your clearest leverage opportunity is <strong>'+escapeHtml(lowest.name)+'</strong>. Together, those two signals tell us more than the overall number ever could.</p><div class="v21-report-grid"><div class="v21-cell"><span>MAXESS SCORE</span><b>'+Math.round(s)+'</b><small>Your current overall capability signal.</small></div><div class="v21-cell"><span>MASTERY STAGE</span><b>'+st+'</b><small>Supporting → Mastering.</small></div><div class="v21-cell"><span>STRONGEST SIGNAL</span><b>'+escapeHtml(strongest.name)+'</b><small>Protect and compound this capability.</small></div></div><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>Here is what I want you to notice.</strong><p>Your score tells you where you are. Your pattern, strength and lever tell you what to do with that information.</p></div></div></article></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">YOUR AI FINGERPRINT</span><h2 class="v21-section-title">See the shape of your capability.</h2><p class="v21-section-copy">Your five dimensions create a fingerprint. The shape shows where you are balanced, where you are naturally strong, and where focused development can reshape the whole profile.</p><div class="v21-fingerprint-panel"><div class="v21-fingerprint-visual"><svg viewBox="0 0 430 430" role="img" aria-label="Your five-dimension AI capability fingerprint"><defs><radialGradient id="v21FinalFp"><stop offset="0" stop-color="#9b63ff" stop-opacity=".35"/><stop offset="1" stop-color="#44d9ce" stop-opacity=".08"/></radialGradient></defs>'+fpGrid+fpAxes+'<polygon points="'+fpPoints+'" fill="url(#v21FinalFp)" stroke="#7445ad" stroke-width="3"/>'+fpDots+'</svg><div class="v21-fingerprint-core"><div><b>'+Math.round(s)+'</b><span>MAXESS SCORE</span></div></div></div><div class="v21-fp-reading">'+ds.map(function(d){return '<div class="v21-card"><span class="v21-kicker" style="color:#7445ad">'+escapeHtml(d.name)+'</span><h3 style="font-size:34px;margin-top:7px">'+Math.round(d.score||0)+'</h3><p style="margin-top:6px">'+escapeHtml(d.description||dimCopy(d.name,d.score))+'</p></div>';}).join('')+'</div></div></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">YOUR STRENGTH</span><h2 class="v21-section-title">Protect what is already working.</h2><div class="v21-card"><h3>'+escapeHtml(strongest.name)+'</h3><p>You already have meaningful capability here. Compound it deliberately. Your strongest capability is not a trophy—it is the foundation you can build the rest of the system on.</p><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>Keep this. Make it stronger.</strong><p>When you know what you naturally do well, you can stop trying to improve everything at once and start creating leverage.</p></div></div></div></div></section>'+ 
      '<section class="v21-section v21-purple"><div class="v21-inner"><span class="v21-kicker" style="color:#eadcff">YOUR LEVER</span><h2 class="v21-section-title">Build the capability that can move the whole system.</h2><div class="v21-card"><h3>'+escapeHtml(lowest.name)+'</h3><p>Your highest-leverage opportunity is <strong>'+escapeHtml(lowest.name)+'</strong>. This is not a weakness label. It is simply the clearest place to focus one deliberate improvement.</p><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>This is where I would focus next.</strong><p>Protect your strength. Build your lever. Then watch how the shape of your whole profile changes.</p></div></div></div></div></section>'+ 
      '<section class="v21-section v21-dark"><div class="v21-inner"><span class="v21-kicker">YOUR FIVE DIMENSIONS</span><h2 class="v21-section-title">Go one layer deeper.</h2><div class="v21-dims" role="list">'+ds.map(function(d){return '<button class="v21-dim" type="button" role="listitem" aria-label="'+escapeHtml(d.name)+' score '+Math.round(d.score||0)+'"><span class="v21-dim-score">'+Math.round(d.score||0)+'</span><span class="v21-dim-name">'+escapeHtml(d.name)+'</span></button>';}).join('')+'</div><div class="v21-detail"><b>SELECT A DIMENSION</b><p>Choose one of the five orbs to explore the score, meaning and next lever.</p></div></div></section>'+ 
      '<section class="v21-section v21-dark"><div class="v21-inner"><span class="v21-kicker">YOUR PATTERN</span><h2 class="v21-section-title">See the pattern, not just the score.</h2><p class="v21-section-copy">Your strongest capability and your biggest opportunity are not separate facts. They describe the shape of the system you are building with AI.</p><div class="v21-story">'+ds.map(function(d){return '<div class="v21-card"><span class="v21-kicker">'+escapeHtml(d.name)+'</span><h3>'+Math.round(d.score||0)+'</h3><p>'+escapeHtml(d.description || dimCopy(d.name,d.score))+'</p></div>';}).join('')+'</div><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>The pattern is the story between the numbers.</strong><p>Look for what is already supporting the rest of your profile—and what could change the shape if you strengthened it.</p></div></div></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">YOUR NEXT MOVE</span><h2 class="v21-section-title">Three things to do next.</h2><div class="v21-next-grid"><div class="v21-next-card"><div class="v21-number">01 · PROTECT</div><h3>Your strength</h3><p>Use '+escapeHtml(strongest.name)+' in a real AI workflow this week and capture the result.</p></div><div class="v21-next-card"><div class="v21-number">02 · BUILD</div><h3>Your lever</h3><p>Choose one workflow where '+escapeHtml(lowest.name)+' is limiting you and improve it deliberately.</p></div><div class="v21-next-card"><div class="v21-number">03 · REPEAT</div><h3>Create → Score → Improve</h3><p>Do not stop at the first answer. Judge the quality, improve one thing, and repeat.</p></div></div><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>Small actions beat abstract ambition.</strong><p>One good workflow repeated and improved is worth more than a dozen ideas you never use.</p></div></div></div></section>'+ 
      '<section class="v21-section v21-dark"><div class="v21-inner"><span class="v21-kicker">18 NAYA MASTERS</span><h2 class="v21-section-title">Choose the doors that fit your next step.</h2><p class="v21-section-copy">These are not just 18 cards. They are potential pathways. The strongest matches are the ones that can help you build your current lever while compounding your strongest capability.</p><div class="v21-masters">'+(mastersList.length?mastersList.map(function(m,i){var txt=(m.text||'').toLowerCase(),match=(txt.indexOf(String(lowest.name||'').toLowerCase())>=0||txt.indexOf(String(strongest.name||'').toLowerCase())>=0);return '<article class="v21-master">'+(match?'<span class="v21-match">'+(i===0?'BEST MATCH':'STRONG MATCH')+'</span>':'')+(m.href?'<a href="'+escapeHtml(m.href)+'">':'')+'<h3>'+escapeHtml(m.name)+'</h3>'+(m.href?'</a>':'')+'<p>'+escapeHtml(m.text)+'</p></article>';}).join(''):'<article class="v21-master"><h3>Naya Masters</h3><p>Your specialist pathways will appear here when the authoritative library content is available.</p></article>')+'</div></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">PLAYGROUND</span><h2 class="v21-section-title">Understand → Decide → Practice.</h2><div class="v21-playground-premium"><div class="v21-playground-panel"><p>Turn your result into action. Take what you learned, choose one improvement, and practice it on a real task.</p><div class="v21-legacy-wrap" id="v21-playground-host"></div></div><div class="v21-playground-panel"><span class="v21-kicker" style="color:#7445ad">NAYA · IN PRACTICE</span><h3 style="font-size:32px;margin-top:10px">Your report should change what you do next.</h3><p style="margin-top:10px;color:#5d5764">The point of MAXESS is not a score. The point is capability you can use, improve and turn into leverage.</p></div></div></div></section>'+ 
      '<section class="v21-section v21-purple"><div class="v21-inner v21-cta-final"><span class="v21-kicker" style="color:#eadcff">YOUR AI MASTERY JOURNEY</span><h2>Now you know where you are. Let’s turn that into your next level.</h2><p>MAXESS gives you a map. Naya helps you use it.</p><a class="v21-cta-link" href="https://nayanet.xyz/">CONTINUE WITH NAYANET</a></div></section>'+ 
      '</div>';

    var btn=root.querySelector('.v21-listen');if(btn)btn.addEventListener('click',listen);
    var detail=root.querySelector('.v21-detail');root.querySelectorAll('.v21-dim').forEach(function(btn,i){btn.addEventListener('click',function(){var d=ds[i]||{};detail.innerHTML='<b>'+escapeHtml(d.name)+' · '+Math.round(d.score||0)+'</b><p>'+escapeHtml(d.description||dimCopy(d.name,d.score))+'</p>';});});
    var host=root.querySelector('#v21-playground-host');if(host){media.forEach(function(n){if(n && n!==root && n.parentNode!==host)host.appendChild(n);});}
    var orb=root.querySelector('.v21-score-orb');if(orb){orb.style.borderColor=colorFor(s);orb.style.boxShadow='inset 0 0 90px '+colorFor(s)+'33,0 45px 110px rgba(0,0,0,.55),0 0 110px '+colorFor(s)+'22';}
    root.setAttribute('data-results-version','v21-final-aaa');
    root.setAttribute('data-results-data-source','window.MAXESS_RESULT');
    root.setAttribute('data-results-state','ready');
  }'''

    s2, n = build_pat.subn(build_fn, s, count=1)
    if n != 1:
        raise SystemExit(f"BUILD FUNCTION NOT FOUND: {n}")

    BUILDER.write_text(s2, encoding="utf-8")
    print("FINAL MAXESS AAA PRODUCT TRANSFORMATION: APPLIED")
    print("HERO + FINGERPRINT + MEANING + STRENGTH + LEVER + DIMENSIONS + PATTERN + NEXT MOVE + 18 MASTERS + PLAYGROUND + NAYA + CTA: UPDATED")
    print("SOURCE OF TRUTH: window.MAXESS_RESULT")
    print("LOWER-PAGE MEDIA PRESERVATION: ENABLED")
    print("FINAL ARTIFACT VERSION: v21-final-aaa")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
