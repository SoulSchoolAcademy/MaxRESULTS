#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'

s = BUILDER.read_text(encoding='utf-8')

old_result = """  function result(){ return (window.MAXESS_RESULT && typeof window.MAXESS_RESULT==='object') ? window.MAXESS_RESULT : null; }"""
new_result = r'''  function legacyResult(){
    var scoreEl=root.querySelector('.v13-score-number,.mx-score-orb .v13-score-number,.mx-score-orb .mx-score-number,.mx-score-number');
    var scoreText=scoreEl ? (scoreEl.textContent||'').replace(/[^0-9.]/g,'') : '';
    var overall=Number(scoreText);
    if(!Number.isFinite(overall)) return null;
    var dimensions=[];
    var candidates=root.querySelectorAll('.v18-dim-orb,.mx-node,.v13-dimension-card,[data-dimension]');
    candidates.forEach(function(el,i){
      if(dimensions.length>=5) return;
      var raw=(el.textContent||'').replace(/\s+/g,' ').trim();
      var nums=raw.match(/\b(?:100|[0-9]{1,2})\b/g)||[];
      var val=nums.length ? Number(nums[nums.length-1]) : null;
      var nameEl=el.querySelector('.v18-dim-name,.mx-node b,.v13-dimension-name,[data-dimension-name]');
      var name=nameEl ? nameEl.textContent.trim() : (el.getAttribute('data-dimension-name')||'');
      if(name && Number.isFinite(val)) dimensions.push({name:name,score:clamp(val),description:''});
    });
    if(dimensions.length!==5){
      var legacyNames=['Direction','Communication','Evaluation','Iteration','Systems Thinking'];
      var legacyScores=[];
      root.querySelectorAll('#your-fingerprint .mx-node strong,.mx-node strong,.v13-dimension-score').forEach(function(el){
        if(legacyScores.length<5){ var n=Number((el.textContent||'').replace(/[^0-9.]/g,'')); if(Number.isFinite(n)) legacyScores.push(n); }
      });
      if(legacyScores.length===5) dimensions=legacyNames.map(function(n,i){return {name:n,score:clamp(legacyScores[i]),description:''};});
    }
    if(dimensions.length!==5) return null;
    var nameEl=root.querySelector('.mx-name,.v18-naya-copy strong,[data-participant-name]');
    var name=nameEl ? nameEl.textContent.trim() : '';
    return {overallScore:clamp(overall),dimensions:dimensions,profile:{name:name},_migrationSource:'legacy-dom'};
  }

  function result(){
    if(window.MAXESS_RESULT && typeof window.MAXESS_RESULT==='object') return window.MAXESS_RESULT;
    return legacyResult();
  }'''

if old_result not in s:
    raise SystemExit('RESULT FUNCTION MARKER NOT FOUND')
s=s.replace(old_result,new_result,1)

old_boot = """  function boot(){ build(result()); }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot,{once:true}); else boot();"""
new_boot = r'''  var rebuilding=false;
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
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot,{once:true}); else boot();'''

if old_boot not in s:
    raise SystemExit('BOOT FUNCTION MARKER NOT FOUND')
s=s.replace(old_boot,new_boot,1)

# Make the provenance explicit without pretending the migration fallback is production truth.
marker="root.setAttribute('data-results-version','v21-canonical');root.setAttribute('data-results-data-source','window.MAXESS_RESULT');root.setAttribute('data-results-state','ready');"
replacement="root.setAttribute('data-results-version','v21-canonical');root.setAttribute('data-results-data-source',window.MAXESS_RESULT?'window.MAXESS_RESULT':'legacy-dom-migration');root.setAttribute('data-results-state','ready');"
if marker in s:
    s=s.replace(marker,replacement,1)

BUILDER.write_text(s,encoding='utf-8')
print('V21 VISUAL RENDER ACTIVATION COMPLETE')
print('Real MAXESS_RESULT remains authoritative when present')
print('Legacy DOM migration bridge activates only when MAXESS_RESULT is absent')
print('Late boot + mutation recovery enabled')
