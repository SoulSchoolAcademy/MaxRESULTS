(function(g){'use strict';
/*
  MAXESS AI SCORE DEFINITION V2
  V1 answer order is intentionally authored from strongest capability to weakest.
  V2 makes that latent scoring explicit: 4 = strongest evidence, 0 = weakest.
  Presentation layers may deterministically shuffle answers; scoring follows stable IDs.
*/
const base=g.MAXESS_AI_SCORE_DEFINITION_V1;
if(!base) throw new Error('MAXESS_AI_SCORE_DEFINITION_V1 must be loaded before V2');
const questions=base.questions.map(q=>({
  ...q,
  answers:q.answers.map((a,index)=>({...a,score:4-index,weight:1}))
}));
g.MAXESS_AI_SCORE_DEFINITION_V2=Object.freeze({
  ...base,
  version:'2.0.0',
  scoringVersion:'0-4-CAPABILITY-V1',
  rubricVersion:'MAXESS-ASSESSMENT-CONSTRUCTION-RUBRIC-V1',
  questions,
  provenance:{
    previousDefinition:'PROJECTS/MAXESS/ENGINEERING/MAXESS-AI-SCORE-DEFINITION-V1.js',
    constructionRubric:'PROJECTS/MAXESS/ENGINEERING/MAXESS-ASSESSMENT-CONSTRUCTION-RUBRIC-V1.md',
    principle:'Answer quality determines score; presentation position does not.'
  }
});
})(typeof window!=='undefined'?window:globalThis);
