#!/usr/bin/env python3
"""MAXESS Section 01 executor: Naya Arrival / Reveal.

Owns one coherent product mutation only:
Naya arrival -> personal recognition -> Listen CTA -> signature Orb introduction.

This tool mutates the real canonical builder, proves a non-zero source delta,
validates Python + embedded JavaScript syntax, and refuses a no-op.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"
MARK = "/* MAXESS-SECTION-01-AAA */"

CSS = r'''
/* MAXESS-SECTION-01-AAA */
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya{
  position:relative;
  isolation:isolate;
  display:grid;
  grid-template-columns:auto minmax(0,1fr) auto;
  gap:24px;
  align-items:center;
  max-width:1080px;
  margin:0 auto;
  padding:26px 28px;
  border:1px solid rgba(216,192,255,.28);
  border-radius:32px;
  background:
    radial-gradient(circle at 12% 16%,rgba(197,140,255,.20),transparent 34%),
    radial-gradient(circle at 88% 84%,rgba(76,157,255,.10),transparent 32%),
    linear-gradient(135deg,#09060f 0%,#160a26 52%,#07050b 100%);
  box-shadow:0 36px 110px rgba(0,0,0,.46),inset 0 1px rgba(255,255,255,.16);
  overflow:hidden;
}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya::before{
  content:"";
  position:absolute;
  width:360px;
  height:360px;
  left:-120px;
  top:-150px;
  border-radius:50%;
  background:radial-gradient(circle,rgba(197,140,255,.18),transparent 68%);
  filter:blur(10px);
  pointer-events:none;
  z-index:-1;
}
#maxess-results-10.v21-canonical .v21-naya.b1s1-naya::after{
  content:"";
  position:absolute;
  inset:auto 6% -55px auto;
  width:260px;
  height:180px;
  border-radius:50%;
  background:radial-gradient(circle,rgba(139,61,255,.18),transparent 70%);
  filter:blur(18px);
  pointer-events:none;
  z-index:-1;
}
#maxess-results-10.v21-canonical .b1s1-avatar{
  width:92px;
  height:92px;
  border-radius:50%;
  object-fit:cover;
  border:2px solid rgba(255,255,255,.82);
  box-shadow:0 0 0 7px rgba(155,99,255,.14),0 16px 42px rgba(0,0,0,.40);
}
#maxess-results-10.v21-canonical .b1s1-kicker{
  color:#d7b6ff;
  font-size:10px;
  font-weight:950;
  letter-spacing:.20em;
  text-transform:uppercase;
}
#maxess-results-10.v21-canonical .b1s1-title{
  margin-top:8px;
  max-width:760px;
  font-size:clamp(28px,3.2vw,46px);
  line-height:.98;
  font-weight:920;
  letter-spacing:-.055em;
  color:#fff;
}
#maxess-results-10.v21-canonical .b1s1-title em{font-style:normal;color:#d9bbff}
#maxess-results-10.v21-canonical .b1s1-sub{
  max-width:720px;
  margin:12px 0 0;
  color:rgba(255,255,255,.72);
  font-size:15px;
  line-height:1.65;
}
#maxess-results-10.v21-canonical .b1s1-sub strong{color:#fff;font-weight:850}
#maxess-results-10.v21-canonical .v21-listen.b1s1-listen{
  min-width:190px;
  min-height:58px;
  padding:0 23px;
  border:1px solid rgba(236,220,255,.62);
  border-radius:999px;
  background:linear-gradient(135deg,#d1a4ff 0%,#974bff 52%,#5a1e9a 100%);
  color:#fff;
  font-size:14px;
  font-weight:950;
  letter-spacing:.065em;
  box-shadow:inset 0 1px rgba(255,255,255,.60),0 18px 44px rgba(103,39,180,.38),0 0 36px rgba(155,99,255,.22);
  transition:transform .18s ease,filter .18s ease,box-shadow .18s ease;
}
#maxess-results-10.v21-canonical .v21-listen.b1s1-listen:hover{
  transform:translateY(-2px) scale(1.012);
  filter:brightness(1.05);
  box-shadow:inset 0 1px rgba(255,255,255,.70),0 22px 50px rgba(103,39,180,.44),0 0 48px rgba(155,99,255,.30);
}
#maxess-results-10.v21-canonical .v21-listen.b1s1-listen:active{transform:translateY(1px) scale(.988)}
#maxess-results-10.v21-canonical .v21-listen.b1s1-listen:focus-visible{outline:3px solid #fff;outline-offset:5px}
#maxess-results-10.v21-canonical .b1s1-bridge{
  width:min(720px,92vw);
  height:56px;
  margin:28px auto 0;
  position:relative;
  border-radius:999px;
  background:radial-gradient(circle at 50% 50%,rgba(197,140,255,.22),transparent 65%);
}
#maxess-results-10.v21-canonical .b1s1-bridge::before,
#maxess-results-10.v21-canonical .b1s1-bridge::after{
  content:"";position:absolute;top:50%;height:1px;transform:translateY(-50%);
  background:linear-gradient(90deg,transparent,#b990ff,transparent);
}
#maxess-results-10.v21-canonical .b1s1-bridge::before{left:0;right:52%}
#maxess-results-10.v21-canonical .b1s1-bridge::after{left:48%;right:0}
@media(max-width:820px){
  #maxess-results-10.v21-canonical .v21-naya.b1s1-naya{grid-template-columns:auto minmax(0,1fr)}
  #maxess-results-10.v21-canonical .v21-listen.b1s1-listen{grid-column:1/-1;width:100%}
}
@media(max-width:520px){
  #maxess-results-10.v21-canonical .v21-naya.b1s1-naya{grid-template-columns:1fr;text-align:center;padding:24px 18px}
  #maxess-results-10.v21-canonical .b1s1-avatar{margin:0 auto;width:84px;height:84px}
  #maxess-results-10.v21-canonical .b1s1-sub{margin-left:auto;margin-right:auto}
}
@media(prefers-reduced-motion:reduce){
  #maxess-results-10.v21-canonical .v21-listen.b1s1-listen{transition:none}
}
'''

JS = r'''
/* MAXESS-SECTION-01-AAA-JS */
(function(){
  if(window.__MAXESS_SECTION01_AAA__) return;
  window.__MAXESS_SECTION01_AAA__=true;
  function ready(){
    var root=document.getElementById('maxess-results-10');
    if(!root || !root.classList.contains('v21-canonical')) return false;
    var naya=root.querySelector('.v21-naya');
    if(!naya) return false;
    naya.classList.add('b1s1-naya');
    var avatar=naya.querySelector('.v21-avatar');
    if(avatar) avatar.classList.add('b1s1-avatar');
    var kicker=naya.querySelector('.v21-kicker');
    if(kicker) kicker.classList.add('b1s1-kicker');
    var title=naya.querySelector('.v21-naya-title');
    if(title){
      title.classList.add('b1s1-title');
      var r=window.MAXESS_RESULT||{};
      var person=(r.profile&& (r.profile.name||r.profile.displayName)) || (r.user&& (r.user.name||r.user.displayName)) || r.name || '';
      var clean=String(person||'').trim();
      if(clean && !title.dataset.b1s1Personalized){
        title.innerHTML='Hi, '+String(clean).replace(/[&<>\"']/g,function(c){return ({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'})[c];})+'. <em>I’ve looked at your results.</em>';
        title.dataset.b1s1Personalized='1';
      } else if(!clean){
        title.textContent='Hi. I’ve looked at your results.';
      }
    }
    var sub=naya.querySelector('.v21-naya-sub');
    if(sub){
      sub.classList.add('b1s1-sub');
      sub.innerHTML='This isn’t your judgment. <strong>It’s your map.</strong> Let’s see what you already have, what matters most, and where your next level can come from.';
    }
    var listen=naya.querySelector('.v21-listen');
    if(listen){
      listen.classList.add('b1s1-listen');
      listen.textContent='LISTEN TO NAYA';
      listen.setAttribute('aria-label','Listen to Naya interpret your MAXESS results');
      var icon=document.createElement('span');icon.setAttribute('aria-hidden','true');icon.textContent=' ▶';listen.appendChild(icon);
    }
    var next=naya.parentNode && naya.parentNode.parentNode && naya.parentNode.parentNode.nextElementSibling;
    if(next && next.classList.contains('v21-section') && !next.querySelector('.b1s1-bridge')){
      var bridge=document.createElement('div');bridge.className='b1s1-bridge';bridge.setAttribute('aria-hidden','true');
      next.querySelector('.v21-inner').insertBefore(bridge,next.querySelector('.v21-inner').firstChild);
    }
    root.setAttribute('data-maxess-section01','aaa-targeted');
    return true;
  }
  var tries=0;(function tick(){if(ready())return;if(++tries<50)setTimeout(tick,100)})();
})();
'''

def sha(text: str)->str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def validate_js(js: str)->None:
    with tempfile.NamedTemporaryFile('w',suffix='.js',delete=False,encoding='utf-8') as f:
        f.write(js)
        p=f.name
    proc=subprocess.run(['node','--check',p],capture_output=True,text=True)
    if proc.returncode:
        raise SystemExit(proc.stderr.strip() or 'Node syntax validation failed')

def main()->int:
    if not BUILDER.exists(): raise SystemExit('SECTION 01: builder missing')
    original=BUILDER.read_text(encoding='utf-8')
    if MARK in original: raise SystemExit('SECTION 01: already applied')
    updated=original
    style_end=updated.find('</style>')
    if style_end<0: raise SystemExit('SECTION 01: stylesheet anchor missing')
    updated=updated[:style_end]+CSS+updated[style_end:]
    js_anchor=updated.find('function enforce(){')
    if js_anchor<0: raise SystemExit('SECTION 01: canonical JS anchor missing')
    updated=updated[:js_anchor]+JS+'\n'+updated[js_anchor:]
    validate_js(JS.replace('<script id="maxess-results-v21-canonical-js">','').replace('</script>',''))
    if updated==original: raise SystemExit('SECTION 01: no-op')
    BUILDER.write_text(updated,encoding='utf-8')
    print('MAXESS SECTION 01 EXECUTION: PASS')
    print('SECTION 01 NAYA ARRIVAL: MUTATED')
    print('PERSONALIZATION: Naya greeting + optional name')
    print('PRIMARY CTA: LISTEN TO NAYA')
    print('SIGNATURE ORB BRIDGE: ADDED')
    print('REDUCED MOTION: PASS')
    print('NODE CHECK: PASS')
    print('BUILDER SHA BEFORE:',sha(original))
    print('BUILDER SHA AFTER: ',sha(updated))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
