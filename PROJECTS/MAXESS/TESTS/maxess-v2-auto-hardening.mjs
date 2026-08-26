import fs from 'node:fs';

const path='PROJECTS/MAXESS/E00 MAXESS V2 — AUTHORITATIVE GROOVE.html';
let s=fs.readFileSync(path,'utf8');

// Idempotent hardening: the workflow may run against the original Groove or
// against a Groove already hardened by an earlier successful execution.
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

const required=[
  'disabled>Continue →</button>',
  "return ROOT.querySelector(selector)||document.querySelector(selector);",
  "$('#mx-cont').disabled=false;",
  "const ready=state.phase==='ANSWER_SELECTED';$('#mx-cont').disabled=!ready;",
  'if(releasedResult)return releasedResult;',
  "if($('#mx-cont').disabled)return;",
  "$('#mx-cont').disabled=true;$('#mx-cont').setAttribute('aria-disabled','true');"
];
for(const marker of required){
  if(!s.includes(marker))throw new Error('Required Groove hardening invariant missing: '+marker);
}

fs.writeFileSync(path,s);
console.log('GROOVE_HARDENING_VERIFIED');