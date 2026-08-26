import fs from 'node:fs';

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
assert(count(groove,/MAXESS_RESULT_READY/g)===1,'Groove must publish exactly one MAXESS_RESULT_READY event definition/dispatch path.');
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
assert(engine.includes('Pure deterministic logic'),'Engine source must identify itself as pure deterministic logic.');
assert(!/sessionStorage|localStorage|setTimeout|setInterval|document\.|querySelector|location\./.test(engine),'Authoritative engine contains UI/storage/timer authority.');
assert((definition.match(/score:\d/g)||[]).length>=15,'Canonical definition does not expose the expected answer scoring structure.');
assert(!/sessionStorage|localStorage|setTimeout|setInterval|URLSearchParams|location\.hash/.test(consumer),'Active result consumer contains a forbidden alternate authority.');
assert(!/function\s+(payload|decode)\b/.test(consumer),'Active result consumer contains URL payload decoding authority.');
assert(!/setTimeout|setInterval/.test(consumer),'Active result consumer contains polling/timing correctness.');
assert(consumer.includes("window.addEventListener(READY,onResultEvent)"),'Result consumer is not event-driven from MAXESS_RESULT_READY.');
assert(consumer.includes("window.addEventListener(UPDATED,onResultEvent)"),'Result consumer is not event-driven from maxess:result-updated.');
if(/sessionStorage|localStorage/.test(fs.readFileSync('E01','utf8'))){warnings.push('E01 source still contains legacy persistence helpers; static search shows the helper definitions are not independently invoked in the inspected source. Keep this as a cleanup risk and do not treat it as a second authority without execution evidence.');}

console.log('MAXESS V2 STATIC ARCHITECTURE GATE');
console.log('Failures:',failures.length);
failures.forEach(x=>console.log('RED:',x));
console.log('Warnings:',warnings.length);
warnings.forEach(x=>console.log('YELLOW:',x));
if(failures.length)process.exit(1);
console.log('STATIC_GATE=GREEN');
