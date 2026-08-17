#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'

s = BUILDER.read_text(encoding='utf-8')

# Replace result() by structure, not brittle literal matching.
result_pattern = re.compile(r"\n  function result\(\)\{.*?\n  \}\n  function person", re.S)
result_replacement = r'''
  function legacyResult(){
    var scoreEl=root.querySelector('.v13-score-number,.mx-score-orb .v13-score-number,.mx-score-orb .mx-score-number,.mx-score-number');
    var scoreText=scoreEl ? (scoreEl.textContent||'').replace(/[^0-9.]/g,'') : '';
    var overall=Number(scoreText);
    if(!Number.isFinite(overall)) return null;
    var dimensions=[];
    root.querySelectorAll('.v18-dim-orb,.mx-node,.v13-dimension-card,[data-dimension]').forEach(function(el){
      if(dimensions.length>=5) return;
      var raw=(el.textContent||'').replace(/\s+/g,' ').trim();
      var nums=raw.match(/\b(?:100|[0-9]{1,2})\b/g)||[];
      var val=nums.length ? Number(nums[nums.length-1]) : null;
      var nameEl=el.querySelector('.v18-dim-name,.mx-node b,.v13-dimension-name,[data-dimension-name]');
      var name=nameEl ? nameEl.textContent.trim() : (el.getAttribute('data-dimension-name')||'');
      if(name && Number.isFinite(val)) dimensions.push({name:name,score:clamp(val),description:''});
    });
    if(dimensions.length!==5){
      var names=['Direction','Communication','Evaluation','Iteration','Systems Thinking'];
      var vals=[];
      root.querySelectorAll('.mx-node strong,.v13-dimension-score').forEach(function(el){
        if(vals.length<5){var n=Number((el.textContent||'').replace(/[^0-9.]/g,''));if(Number.isFinite(n))vals.push(n);}
      });
      if(vals.length===5) dimensions=names.map(function(n,i){return {name:n,score:clamp(vals[i]),description:''};});
    }
    if(dimensions.length!==5) return null;
    var nameEl=root.querySelector('.mx-name,.v18-naya-copy strong,[data-participant-name]');
    var name=nameEl ? nameEl.textContent.trim() : '';
    return {overallScore:clamp(overall),dimensions:dimensions,profile:{name:name},_migrationSource:'legacy-dom'};
  }
  function result(){
    return (window.MAXESS_RESULT && typeof window.MAXESS_RESULT==='object') ? window.MAXESS_RESULT : legacyResult();
  }
  function person'''
s2, n = result_pattern.subn(result_replacement, s, count=1)
if n != 1:
    raise SystemExit(f'RESULT BLOCK PATCH FAILED: {n}')
s = s2

# Five-stage mastery model.
stage_pattern = re.compile(r"\n  function stage\(s\)\{.*?\n  \}\n  function dimCopy", re.S)
stage_replacement = r'''
  function stage(s){
    if(s==null) return '';
    return s>=91?'Mastering':s>=76?'Advancing':s>=51?'Developing':s>=21?'Foundation':'Supporting';
  }
  function dimCopy'''
s2, n = stage_pattern.subn(stage_replacement, s, count=1)
if n != 1:
    raise SystemExit(f'STAGE BLOCK PATCH FAILED: {n}')
s = s2

# Replace boot() through the end of the IIFE in a controlled way.
boot_pattern = re.compile(r"\n  function boot\(\)\{.*?\n  if\(document\.readyState===['\"]loading['\"]\).*?\n\}\)\(\);", re.S)
boot_replacement = r'''
  var rebuilding=false;
  function authoritativeResult(){
    return (window.MAXESS_RESULT && typeof window.MAXESS_RESULT==='object') ? window.MAXESS_RESULT : legacyResult();
  }
  function renderNow(){
    if(rebuilding) return;
    var r=authoritativeResult();
    if(!r) return;
    rebuilding=true;
    try{ build(r); }
    finally{ rebuilding=false; }
  }
  function boot(){
    renderNow();
    setTimeout(renderNow,80);
    setTimeout(renderNow,250);
    setTimeout(renderNow,700);
    if(window.MutationObserver){
      var observer=new MutationObserver(function(){
        if(rebuilding) return;
        if(!root.querySelector('.v21-shell') || !root.classList.contains('v21-canonical')) renderNow();
      });
      observer.observe(root,{childList:true});
    }
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot,{once:true}); else boot();
})();
'''
s2, n = boot_pattern.subn(boot_replacement, s, count=1)
if n != 1:
    raise SystemExit(f'BOOT BLOCK PATCH FAILED: {n}')
s = s2

# Clean visible /100 presentation in the canonical result UI.
s, n1 = re.subn(r"Math\.round\(s\)\+' / 100</b>", "Math.round(s)+'</b>", s, count=1)
s, n2 = re.subn(r"Math\.round\(d\.score\|\|0\)\+' / 100</b>", "Math.round(d.score||0)+'</b>", s, count=1)
s, n3 = re.subn(r"Math\.round\(d\.score\|\|0\)+' / 100</b>", "Math.round(d.score||0)+'</b>", s, count=1)

BUILDER.write_text(s, encoding='utf-8')
print('V21 PRODUCT PACKET 1 SOURCE PATCH COMPLETE')
print(f'Result migration bridge: {n}')
print(f'Mastery cleanup: {1 if "Supporting" in s and "Mastering" in s else 0}')
print(f'Removed /100 occurrences: {n1+n2+n3}')
print('Late boot + MutationObserver recovery: ENABLED')
