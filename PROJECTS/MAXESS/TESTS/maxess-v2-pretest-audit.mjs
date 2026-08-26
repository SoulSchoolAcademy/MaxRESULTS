import fs from 'node:fs';
import vm from 'node:vm';

const groovePath='PROJECTS/MAXESS/E00 MAXESS V2 — AUTHORITATIVE GROOVE.html';
const consumerPath='MAXESS-RESULT-CONSUMER-V2.html';
const enginePath='PROJECTS/MAXESS/ENGINEERING/MAXESS-E00-AUTHORITATIVE-ENGINE-V2.js';
const definitionPath='PROJECTS/MAXESS/ENGINEERING/MAXESS-AI-SCORE-DEFINITION-V1.js';

const groove=fs.readFileSync(groovePath,'utf8');
const consumer=fs.readFileSync(consumerPath,'utf8');
const engine=fs.readFileSync(enginePath,'utf8');
const definition=fs.readFileSync(definitionPath,'utf8');
const failures=[];
const warnings=[];
const assert=(ok,msg)=>{if(!ok)failures.push(msg)};
const count=(s,re)=>[...s.matchAll(re)].length;

assert(groove.includes('MAXESS_E00_ENGINE_V2'),'Groove does not load the authoritative E00 engine.');
assert(groove.includes('MAXESS_AI_SCORE_DEFINITION_V1'),'Groove does not load the canonical AI Score definition.');
assert(count(groove,/ENGINE\.continueAssessment\(state,DEFINITION\)/g)===1,'Groove must have exactly one engine Continue path.');
assert(count(groove,/function release\(/g)===1,'Groove must have exactly one result-release function.');
assert(count(groove,/MAXESS_RESULT_READY/g)===1,'Groove must publish exactly one MAXESS_RESULT_READY event path.');
assert(count(groove,/maxess:result-updated/g)===1,'Groove must publish exactly one maxess:result-updated event path.');
assert(!/\bcalculate\s*\(/.test(groove),'Groove contains a competing calculate() implementation/call.');
assert(!/\bsessionStorage\b|\blocalStorage\b/.test(groove),'Groove contains storage result authority.');
assert(!/\bsetTimeout\b|\bsetInterval\b/.test(groove),'Groove contains timer/polling correctness logic.');
assert(!/URLSearchParams|location\.hash|location\.search/.test(groove),'Groove contains URL/hash result authority.');
assert(!/querySelector\([^)]*(score|result)/i.test(groove),'Groove appears to scrape score/result from DOM.');
assert(count(groove,/id="mx-cont"/g)===1,'Groove must contain exactly one Continue control.');
assert(count(groove,/\.addEventListener\('click',advance\)/g)===1,'Groove must contain exactly one Continue click handler.');
assert(groove.includes('ENGINE.validateResult(result,DEFINITION);'),'Groove must validate the engine result before release.');
assert(groove.includes('releasedResult=ENGINE.freezeResult(result);'),'Groove must freeze the released result.');
assert(groove.includes('window.MAXESS_RESULT=releasedResult;'),'Groove must publish the frozen canonical result.');
assert(groove.includes('window.MAXESS_RESULT_V1=releasedResult;'),'Groove must publish MAXESS_RESULT_V1.');
assert(groove.includes('if(releasedResult)return releasedResult;'),'Groove must guard against duplicate result release.');
assert(groove.includes('if(releasedResult)return;'),'Groove must guard duplicate Continue before invoking the finalized engine.');
assert(groove.includes('.disabled=!ready'),'Continue must use the native disabled state, not only aria-disabled.');
assert(engine.includes('Pure deterministic logic'),'Engine source must identify itself as pure deterministic logic.');
assert(!/sessionStorage|localStorage|setTimeout|setInterval|document\.|querySelector|location\./.test(engine),'Authoritative engine contains UI/storage/timer authority.');
assert(!/sessionStorage|localStorage|setTimeout|setInterval|URLSearchParams|location\.hash/.test(consumer),'Active result consumer contains a forbidden alternate authority.');
assert(!/function\s+(payload|decode)\b/.test(consumer),'Active result consumer contains URL payload decoding authority.');
assert(!/setTimeout|setInterval/.test(consumer),'Active result consumer contains polling/timing correctness.');
assert(consumer.includes("window.addEventListener(READY,onResultEvent)"),'Result consumer is not event-driven from MAXESS_RESULT_READY.');
assert(consumer.includes("window.addEventListener(UPDATED,onResultEvent)"),'Result consumer is not event-driven from maxess:result-updated.');

const sandbox={console};
vm.createContext(sandbox);
try{
  vm.runInContext(engine+'\n'+definition,sandbox,{timeout:1000});
  const E=sandbox.MAXESS_E00_ENGINE_V2;
  const D=sandbox.MAXESS_AI_SCORE_DEFINITION_V1;
  assert(!!E,'Authoritative engine did not initialize.');
  assert(!!D,'Canonical AI Score definition did not initialize.');
  if(E&&D){
    E.validateDefinition(D);
    assert(D.questions.length===15,'Canonical definition must contain exactly 15 questions.');
    assert(D.dimensions.length===5,'Canonical definition must contain exactly 5 dimensions.');
    assert(D.questions.every(q=>q.answers.length===5),'Every canonical question must contain exactly 5 answers.');
    assert(D.questions.every(q=>q.answers.every(a=>Number.isInteger(a.score)&&a.score>=0&&a.score<=4)),'Canonical answers must use only 0–4 scores.');
    const canonicalMin=E.createState(D);for(const q of D.questions){const a=q.answers.reduce((m,x)=>x.score<m.score?x:m,q.answers[0]);E.selectAnswer(canonicalMin,D,a.id);E.continueAssessment(canonicalMin,D)}
    const canonicalMax=E.createState(D);for(const q of D.questions){const a=q.answers.reduce((m,x)=>x.score>m.score?x:m,q.answers[0]);E.selectAnswer(canonicalMax,D,a.id);E.continueAssessment(canonicalMax,D)}
    assert(canonicalMin.result?.overallScore===25,'Canonical definition minimum golden result must be 25/100.');
    assert(canonicalMax.result?.overallScore===100,'Canonical definition maximum golden result must be 100.');
    assert(canonicalMin.completionCount===1&&canonicalMax.completionCount===1,'Canonical golden completion must occur exactly once.');
    assert(Object.isFrozen(canonicalMin.result)&&Object.isFrozen(canonicalMax.result),'Canonical golden results must be frozen.');
    assert(canonicalMax.result?.dimensions.every(d=>d.rawScore===d.maxScore&&d.maxScore===12),'Every dimension must max at 12 raw points.');

    const synthetic={...D,questions:D.questions.map(q=>({...q,answers:q.answers.map(a=>({...a,score:0}))}))};
    const zero=E.createState(synthetic);for(const q of synthetic.questions){E.selectAnswer(zero,synthetic,q.answers[0].id);E.continueAssessment(zero,synthetic)}
    const four={...D,questions:D.questions.map(q=>({...q,answers:q.answers.map(a=>({...a,score:4}))}))};
    const sixty=E.createState(four);for(const q of four.questions){E.selectAnswer(sixty,four,q.answers[0].id);E.continueAssessment(sixty,four)}
    assert(zero.result?.overallScore===0,'Engine mathematical minimum golden result must be 0/100.');
    assert(sixty.result?.score?.raw===60&&sixty.result?.overallScore===100,'Engine mathematical maximum golden result must be 60 raw / 100 normalized.');
    try{E.continueAssessment(zero,synthetic);failures.push('Finalized assessment accepted a duplicate Continue.')}catch(_){/* expected */}
  }
}catch(e){failures.push('Executable engine/definition verification failed: '+e.message)}

if(/sessionStorage|localStorage/.test(fs.readFileSync('E01','utf8'))){warnings.push('E01 source still contains legacy persistence helpers; inspected source shows helper definitions but no independently found invocation. Treat this as cleanup debt, not as runtime authority, until browser evidence proves otherwise.');}

console.log('MAXESS V2 STATIC + EXECUTABLE ARCHITECTURE GATE');
console.log('Failures:',failures.length);
failures.forEach(x=>console.log('RED:',x));
console.log('Warnings:',warnings.length);
warnings.forEach(x=>console.log('YELLOW:',x));
if(failures.length)process.exit(1);
console.log('STATIC_GATE=GREEN');
