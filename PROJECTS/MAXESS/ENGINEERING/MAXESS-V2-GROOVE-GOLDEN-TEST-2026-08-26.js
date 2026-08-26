/* MAXESS V2 Groove golden test. Run with Node from this directory: node MAXESS-V2-GROOVE-GOLDEN-TEST-2026-08-26.js */
'use strict';
require('./MAXESS-E00-AUTHORITATIVE-ENGINE-V2.js');
require('./MAXESS-AI-SCORE-DEFINITION-V1.js');

const E = global.MAXESS_E00_ENGINE_V2;
const D = global.MAXESS_AI_SCORE_DEFINITION_V1;
if (!E || !D) throw new Error('Authoritative engine/definition failed to load');
E.validateDefinition(D);

if (D.questions.length !== 15) throw new Error('Expected 15 questions');
if (D.dimensions.length !== 5) throw new Error('Expected 5 dimensions');
if (!D.questions.every(q => q.answers.length === 5)) throw new Error('Every question must have 5 answers');
if (!D.questions.every(q => q.answers.every(a => Number.isInteger(a.score) && a.score >= 0 && a.score <= 4))) throw new Error('Every answer must score 0–4');

function runAllMax(){
  const s = E.createState(D);
  let continueCount = 0;
  try { E.continueAssessment(s,D); throw new Error('Continue was not blocked before answer'); }
  catch (err) { if (!/selected answer/.test(err.message)) throw err; }
  for(let i=0;i<15;i++){
    const q = E.currentQuestion(s,D);
    const a = q.answers.find(x => x.score === 4);
    if(!a) throw new Error('Canonical question has no score-4 answer: '+q.id);
    E.selectAnswer(s,D,a.id);
    const out = E.continueAssessment(s,D);
    continueCount++;
    if(i < 14 && (out.complete || s.questionIndex !== i+1)) throw new Error('Q progression failed at '+q.id);
    if(i === 14){
      if(!out.complete || s.completionCount !== 1 || !out.result) throw new Error('Q15 completion failed');
      if(out.result.score.raw !== 60 || out.result.score.normalized !== 100) throw new Error('Maximum score mismatch');
      if(out.result.dimensions.some(d => d.maxScore !== 12 || d.score !== 100)) throw new Error('Dimension maximum mismatch');
      if(!Object.isFrozen(out.result)) throw new Error('Result is not frozen');
      if(continueCount !== 15) throw new Error('Expected exactly 15 Continue transitions');
      try { E.continueAssessment(s,D); throw new Error('Duplicate completion accepted'); }
      catch (err) { if(!/selected answer|finalized|Result already exists/.test(err.message)) throw err; }
    }
  }
  return true;
}

function runMinimumMath(){
  const responses = D.questions.map((q,i) => ({questionId:q.id,questionOrder:i+1,dimensionId:q.dimensionId,answerId:q.answers[0].id,score:0}));
  const c = E.calculate(D,responses);
  if(c.rawScore !== 0 || c.maxScore !== 60 || c.normalized !== 0) throw new Error('Minimum 0/0 invariant failed');
}

runAllMax();
runMinimumMath();
console.log('GREEN — MAXESS V2 Groove golden: 15Q/5A/0–4, Q1→Q15 once, Continue blocked before selection, max 60/100, dimension max 12/100, minimum math 0/0, frozen result, duplicate completion blocked.');
