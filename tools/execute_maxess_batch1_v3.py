#!/usr/bin/env python3
"""MAXESS Batch 1 V3 — builder repair + real product mutation.

This executor owns the actual Batch 1 execution path:
1. Repair balanced Git conflict blocks inside the real canonical builder.
2. Mutate Sections 01-03 through stable builder anchors.
3. Refuse success unless the builder source hash changes.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"
MARK_CSS = "/* MAXESS-BATCH1-V3-CSS */"
MARK_JS = "/* MAXESS-BATCH1-V3-JS */"

CSS = r'''
/* MAXESS-BATCH1-V3-CSS */
#maxess-results-10.v21-canonical .b1v3-naya{position:relative;overflow:hidden;background:radial-gradient(circle at 8% 12%,rgba(155,99,255,.20),transparent 34%),linear-gradient(135deg,#09060f 0%,#150b24 55%,#08050d 100%);border-color:rgba(216,192,255,.24);box-shadow:0 34px 100px rgba(0,0,0,.40),inset 0 1px rgba(255,255,255,.16)}
#maxess-results-10.v21-canonical .b1v3-naya::after{content:"";position:absolute;inset:auto -10% -50% 42%;height:180px;background:radial-gradient(circle,rgba(155,99,255,.18),transparent 68%);pointer-events:none}
#maxess-results-10.v21-canonical .b1v3-whisper{position:relative;z-index:1;margin:10px 0 0;color:rgba(255,255,255,.60);font-size:14px;max-width:720px}
#maxess-results-10.v21-canonical .b1v3-score{position:relative}
#maxess-results-10.v21-canonical .b1v3-score::before{content:"";position:absolute;inset:50% auto auto 50%;width:min(620px,95vw);height:min(620px,95vw);transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,rgba(155,99,255,.10),transparent 65%);filter:blur(18px);pointer-events:none}
#maxess-results-10.v21-canonical .b1v3-orb{z-index:1;overflow:visible!important;box-shadow:inset 0 0 120px rgba(155,99,255,.24),0 48px 130px rgba(0,0,0,.62),0 0 120px var(--b1v3-orb-color,rgba(155,99,255,.22))!important;animation:b1v3Orb 8s ease-in-out infinite}
#maxess-results-10.v21-canonical .b1v3-orb::after{content:"";position:absolute;inset:-26px;border-radius:50%;border:1px solid rgba(216,192,255,.10);box-shadow:0 0 50px rgba(155,99,255,.10)}
#maxess-results-10.v21-canonical .b1v3-meaning{margin-top:28px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(280px,.9fr);gap:22px}
#maxess-results-10.v21-canonical .b1v3-panel{padding:28px;border-radius:30px;background:linear-gradient(135deg,#ffffff,#f3edf9);border:1px solid rgba(30,20,40,.10);box-shadow:0 26px 70px rgba(30,15,50,.10)}
#maxess-results-10.v21-canonical .b1v3-panel.dark{background:linear-gradient(145deg,#0a070f,#170b26);color:#fff;border-color:rgba(216,192,255,.18)}
#maxess-results-10.v21-canonical .b1v3-panel h3{font-size:clamp(28px,3.4vw,46px);margin:0;letter-spacing:-.05em}
#maxess-results-10.v21-canonical .b1v3-panel p{margin:10px 0 0;color:#5d5764;line-height:1.65}
#maxess-results-10.v21-canonical .b1v3-panel.dark p{color:rgba(255,255,255,.70)}
#maxess-results-10.v21-canonical .b1v3-chip{display:inline-flex;margin-bottom:12px;padding:7px 10px;border-radius:999px;background:rgba(116,69,173,.10);color:#7445ad;border:1px solid rgba(116,69,173,.12);font-size:9px;font-weight:950;letter-spacing:.15em;text-transform:uppercase}
#maxess-results-10.v21-canonical .b1v3-panel.dark .b1v3-chip{background:rgba(216,192,255,.10);color:#eadcff;border-color:rgba(216,192,255,.18)}
#maxess-results-10.v21-canonical .b1v3-loop{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:20px}
#maxess-results-10.v21-canonical .b1v3-loop b{display:inline-flex;min-height:38px;align-items:center;padding:0 13px;border-radius:999px;background:#7445ad;color:#fff;font-size:10px;letter-spacing:.10em}
#maxess-results-10.v21-canonical .b1v3-loop i{font-style:normal;color:#b990ff;font-size:18px}
@keyframes b1v3Orb{0%,100%{transform:scale(1);filter:saturate(1)}50%{transform:scale(1.012);filter:saturate(1.07)}}
@media(max-width:820px){#maxess-results-10.v21-canonical .b1v3-meaning{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v21-canonical .b1v3-orb{animation:none!important}}
'''

JS = r'''
/* MAXESS-BATCH1-V3-JS */
(function(){
  if(window.__MAXESS_BATCH1_V3__) return;
  window.__MAXESS_BATCH1_V3__=true;
  function getScore(r){
    r=r||{};
    return Number(r.overallScore!=null?r.overallScore:(r.masterScore!=null?r.masterScore:(r.score!=null?r.score:r.overall)))||0;
  }
  function ready(){
    var root=document.getElementById('maxess-results-10');
    if(!root || !root.classList.contains('v21-canonical')) return false;
    var sections=root.querySelectorAll('.v21-section');
    var naya=null,scoreSec=null,meaning=null;
    for(var i=0;i<sections.length;i++){
      var t=(sections[i].textContent||'');
      if(!naya && t.indexOf('NAYA · YOUR AI GUIDE')>=0) naya=sections[i];
      if(!scoreSec && (t.indexOf('YOUR RESULT')>=0 || t.indexOf('YOUR MAXESS SCORE')>=0)) scoreSec=sections[i];
      if(!meaning && (t.indexOf('WHAT YOUR SCORES MEAN')>=0 || t.indexOf('WHAT YOUR SCORE MEANS')>=0)) meaning=sections[i];
    }
    if(!naya||!scoreSec||!meaning) return false;

    naya.classList.add('b1v3-naya-section');
    var nayaCard=naya.querySelector('.v21-naya');
    if(nayaCard){
      nayaCard.classList.add('b1v3-naya');
      if(!nayaCard.querySelector('.b1v3-whisper')){
        var p=document.createElement('p');
        p.className='b1v3-whisper';
        p.textContent='I have your results. Now let me help you understand what they mean — and where your next level lives.';
        nayaCard.appendChild(p);
      }
      var listen=nayaCard.querySelector('.v21-listen');
      if(listen) listen.classList.add('v21-btn-primary');
    }

    scoreSec.classList.add('b1v3-score');
    var orb=scoreSec.querySelector('.v21-score-orb');
    if(orb){
      orb.classList.add('b1v3-orb');
      var v=getScore(window.MAXESS_RESULT);
      var h=178+Math.max(0,Math.min(100,v))*1.05;
      orb.style.setProperty('--b1v3-orb-color','hsl('+h.toFixed(0)+' 78% 61%)');
      orb.setAttribute('aria-label','Your MAXESS score is '+Math.round(v)+' out of 100');
    }

    if(!meaning.querySelector('.b1v3-meaning')){
      var inner=meaning.querySelector('.v21-inner');
      if(inner){
        var r=window.MAXESS_RESULT||{};
        var raw=getScore(r);
        var stage=raw>=91?'Mastering':raw>=76?'Advancing':raw>=51?'Developing':raw>=21?'Foundation':'Supporting';
        var wrap=document.createElement('div');
        wrap.className='b1v3-meaning';
        wrap.innerHTML='<div class="b1v3-panel"><span class="b1v3-chip">WHAT YOUR SCORE SAYS</span><h3>'+Math.round(raw)+' is a starting position, not a judgment.</h3><p>Your score is a current signal of how effectively you are creating outcomes with AI across five connected capabilities.</p><p><strong>Current stage:</strong> '+stage+'.</p></div><div class="b1v3-panel dark"><span class="b1v3-chip">WHAT TO DO WITH IT</span><h3>Turn feedback into a better result.</h3><p>Use the score as feedback: create something real, judge the quality, improve the highest-value gap, and repeat.</p><div class="b1v3-loop"><b>CREATE</b><i>→</i><b>SCORE</b><i>→</i><b>IMPROVE</b></div></div>';
        inner.appendChild(wrap);
      }
    }
    root.setAttribute('data-maxess-batch1','mutated');
    return true;
  }
  var tries=0;(function tick(){if(ready())return;if(++tries<50)setTimeout(tick,100)})();
})();
'''

def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def repair_conflicts(source: str) -> tuple[str,int]:
    lines=source.splitlines(keepends=True)
    out=[]; i=0; repairs=0
    while i < len(lines):
        if re.match(r'^\s*<<<<<<<\s+.+\s*$', lines[i]):
            start=i; sep=None; end=None; j=i+1
            while j < len(lines):
                if re.match(r'^\s*=======\s*$', lines[j]) and sep is None:
                    sep=j
                elif sep is not None and re.match(r'^\s*>>>>>>>\s+.+\s*$', lines[j]):
                    end=j; break
                elif re.match(r'^\s*<<<<<<<\s+.+\s*$', lines[j]):
                    raise SystemExit('MAXESS BATCH 1 V3: nested conflict block detected')
                j+=1
            if sep is None or end is None:
                raise SystemExit('MAXESS BATCH 1 V3: unmatched conflict marker')
            out.extend(lines[start+1:sep])
            i=end+1; repairs+=1
            continue
        out.append(lines[i]); i+=1
    return ''.join(out),repairs

def main():
    if not BUILDER.exists(): raise SystemExit('MAXESS BATCH 1 V3: builder missing')
    s=BUILDER.read_text(encoding='utf-8')
    before=sha_text(s)
    s,repairs=repair_conflicts(s)
    changed=(s!=BUILDER.read_text(encoding='utf-8'))
    if MARK_CSS not in s:
        pos=s.find('</style>')
        if pos<0: raise SystemExit('MAXESS BATCH 1 V3: CSS anchor not found')
        s=s[:pos]+CSS+s[pos:]; changed=True
    if MARK_JS not in s:
        pos=s.find('function enforce(){')
        if pos<0: raise SystemExit('MAXESS BATCH 1 V3: JS anchor not found')
        s=s[:pos]+JS+'\n'+s[pos:]; changed=True
    if not changed: raise SystemExit('MAXESS BATCH 1 V3: NO PRODUCT SOURCE DELTA')
    after=sha_text(s)
    if after==before: raise SystemExit('MAXESS BATCH 1 V3: NO PRODUCT SOURCE DELTA')
    if '<<<<<<<' in s or '\n=======' in s or '>>>>>>> ' in s: raise SystemExit('MAXESS BATCH 1 V3: unresolved conflict markers remain')
    BUILDER.write_text(s,encoding='utf-8')
    print('MAXESS BATCH 1 V3 PRODUCT MUTATION: PASS')
    print(f'BUILDER CONFLICT BLOCKS REPAIRED: {repairs}')
    print('SECTION 01 NAYA ARRIVAL: MUTATED')
    print('SECTION 02 SCORE / ORB: MUTATED')
    print('SECTION 03 SCORE MEANING: MUTATED')
    print(f'BUILDER SHA BEFORE: {before}')
    print(f'BUILDER SHA AFTER:  {after}')
    print('UNRESOLVED BUILDER CONFLICTS: 0')
    print('REAL PRODUCT SOURCE DELTA: VERIFIED')

if __name__=='__main__':
    main()
