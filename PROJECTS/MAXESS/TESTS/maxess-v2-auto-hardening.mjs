import fs from 'node:fs';
const path='PROJECTS/MAXESS/E00 MAXESS V2 — AUTHORITATIVE GROOVE.html';
let s=fs.readFileSync(path,'utf8');
const replacements=[
  [
    '<button class="cont" id="mx-cont" type="button" aria-disabled="true">Continue →</button>',
    '<button class="cont" id="mx-cont" type="button" aria-disabled="true" disabled>Continue →</button>'
  ],
  [
    "$('#mx-cont').setAttribute('aria-disabled','false');",
    "$('#mx-cont').disabled=false;$('#mx-cont').setAttribute('aria-disabled','false');"
  ],
  [
    "$('#mx-cont').setAttribute('aria-disabled',state.phase==='ANSWER_SELECTED'?'false':'true');",
    "const ready=state.phase==='ANSWER_SELECTED';$('#mx-cont').disabled=!ready;$('#mx-cont').setAttribute('aria-disabled',ready?'false':'true');"
  ],
  [
    "function advance(){\n if($('#mx-cont').getAttribute('aria-disabled')==='true')return;",
    "function advance(){\n if(releasedResult)return;\n if($('#mx-cont').disabled)return;"
  ],
  [
    "releasedResult=ENGINE.freezeResult(result);\n window.MAXESS_RESULT=releasedResult;",
    "releasedResult=ENGINE.freezeResult(result);\n $('#mx-cont').disabled=true;$('#mx-cont').setAttribute('aria-disabled','true');\n window.MAXESS_RESULT=releasedResult;"
  ]
];
for(const [from,to] of replacements){
  if(!s.includes(from))throw new Error('Hardening target not found: '+from.slice(0,100));
  s=s.replace(from,to);
}
fs.writeFileSync(path,s);
console.log('GROOVE_HARDENING_APPLIED');
