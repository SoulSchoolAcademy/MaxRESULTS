import fs from 'node:fs';

const groovePath='PROJECTS/MAXESS/E00 MAXESS V2 — AUTHORITATIVE GROOVE.html';
const e01Path='E01';
let s=fs.readFileSync(groovePath,'utf8');
let e01=fs.readFileSync(e01Path,'utf8');

// Idempotent hardening: the workflow may run against the original Groove/E01
// or against files already hardened by an earlier successful execution.
const replacements=[
  ['<button class="cont" id="mx-cont" type="button" aria-disabled="true">Continue →</button>','<button class="cont" id="mx-cont" type="button" aria-disabled="true" disabled>Continue →</button>'],
  ["const $=id=>ROOT.querySelector(id.charAt(0)==='#'?id:'#'+id);","const $=id=>{const selector=id.charAt(0)==='#'?id:'#'+id;return ROOT.querySelector(selector)||document.querySelector(selector);};"],
  ["$('#mx-answers').querySelectorAll('.ans').forEach(x=>x.setAttribute('aria-pressed',String(x===button)));$('#mx-cont').setAttribute('aria-disabled','false');","$('#mx-answers').querySelectorAll('.ans').forEach(x=>x.setAttribute('aria-pressed',String(x===button)));$('#mx-cont').disabled=false;$('#mx-cont').setAttribute('aria-disabled','false');"],
  ["$('#mx-cont').setAttribute('aria-disabled','false');","$('#mx-cont').disabled=false;$('#mx-cont').setAttribute('aria-disabled','false');"],
  ["$('#mx-cont').setAttribute('aria-disabled',state.phase==='ANSWER_SELECTED'?'false':'true');","const ready=state.phase==='ANSWER_SELECTED';$('#mx-cont').disabled=!ready;$('#mx-cont').setAttribute('aria-disabled',ready?'false':'true');"],
  ["function advance(){\n if($('#mx-cont').getAttribute('aria-disabled')==='true')return;","function advance(){\n if(releasedResult)return;\n if($('#mx-cont').disabled)return;"],
  ["releasedResult=ENGINE.freezeResult(result);\n window.MAXESS_RESULT=releasedResult;","releasedResult=ENGINE.freezeResult(result);\n $('#mx-cont').disabled=true;$('#mx-cont').setAttribute('aria-disabled','true');\n window.MAXESS_RESULT=releasedResult;"]
];

for(const [from,to] of replacements){
  if(s.includes(from))s=s.replace(from,to);
}

// Collapse any consecutive duplicate Continue unlock statements left by
// earlier hardening generations before validating the final invariant.
s=s.replace(/(?:\$\('#mx-cont'\)\.disabled=false;){2,}/g,"$('#mx-cont').disabled=false;");

// Normalize the answer-selection Continue unlock to exactly one assignment.
// This prevents the hardening pass from accumulating duplicate statements on
// every successful CI run while preserving the intended behavior.
s=s.replace(/(\$\('#mx-answers'\)\.querySelectorAll\('\.ans'\)\.forEach\(x=>x\.setAttribute\('aria-pressed',String\(x===button\)\);)(?:\$\('#mx-cont'\)\.disabled=false;)+\$\('#mx-cont'\)\.setAttribute\('aria-disabled','false'\);/,"$1$('#mx-cont').disabled=false;$('#mx-cont').setAttribute('aria-disabled','false');");

const e01Original="function acceptResult(r){if(!validResult(r))return false;resultState=r;window.MAXESS_RESULT=r;try{sessionStorage.setItem(STORAGE_KEY,JSON.stringify(r))}catch(e){}try{window.dispatchEvent(new CustomEvent(READY,{detail:r}))}catch(e){}try{window.dispatchEvent(new CustomEvent(UPDATED,{detail:r}))}catch(e){}return true}";
const e01Guarded="var emittingResult=false;function acceptResult(r,emit){if(emittingResult)return true;if(!validResult(r))return false;resultState=r;window.MAXESS_RESULT=r;try{sessionStorage.setItem(STORAGE_KEY,JSON.stringify(r))}catch(e){}if(emit!==false){emittingResult=true;try{window.dispatchEvent(new CustomEvent(READY,{detail:r}))}catch(e){}try{window.dispatchEvent(new CustomEvent(UPDATED,{detail:r}))}catch(e){}emittingResult=false}return true}";
if(e01.includes(e01Original))e01=e01.replace(e01Original,e01Guarded);

const eventListenerOriginal="window.addEventListener(READY,function(e){if(e&&e.detail)acceptResult(e.detail);render()});window.addEventListener(UPDATED,function(e){if(e&&e.detail)acceptResult(e.detail);render()});";
const eventListenerHardened="window.addEventListener(READY,function(e){if(e&&e.detail)acceptResult(e.detail,false);render()});window.addEventListener(UPDATED,function(e){if(e&&e.detail)acceptResult(e.detail,false);render()});";
if(e01.includes(eventListenerOriginal))e01=e01.replace(eventListenerOriginal,eventListenerHardened);

const requiredGroove=[
  'disabled>Continue →</button>',
  "return ROOT.querySelector(selector)||document.querySelector(selector);",
  "$('#mx-cont').disabled=false;",
  "const ready=state.phase==='ANSWER_SELECTED';$('#mx-cont').disabled=!ready;",
  'if(releasedResult)return releasedResult;',
  "if($('#mx-cont').disabled)return;",
  "$('#mx-cont').disabled=true;$('#mx-cont').setAttribute('aria-disabled','true');"
];
for(const marker of requiredGroove){
  if(!s.includes(marker))throw new Error('Required Groove hardening invariant missing: '+marker);
}
if(!e01.includes('function acceptResult(r,emit)'))throw new Error('Required E01 result-event emit gate missing');
if(!e01.includes('acceptResult(e.detail,false)'))throw new Error('Required E01 event-consumer no-redispatch guard missing');

const unlockAssignments=(s.match(/\$\('#mx-cont'\)\.disabled=false;/g)||[]).length;
if(unlockAssignments!==1)throw new Error(`Expected exactly one Continue unlock assignment, found ${unlockAssignments}`);

fs.writeFileSync(groovePath,s);
fs.writeFileSync(e01Path,e01);
console.log('GROOVE_E01_HARDENING_VERIFIED');
