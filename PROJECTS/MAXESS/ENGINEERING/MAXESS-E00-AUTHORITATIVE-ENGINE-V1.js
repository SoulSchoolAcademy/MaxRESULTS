/**
 * MAXESS E00 — Authoritative Assessment Engine V1
 *
 * Pure assessment logic. No DOM. No storage. No timers. No bridges.
 * E01–E09 consume the frozen MAXESS_RESULT_V1 produced here.
 *
 * Scoring and mastery bands come from the assessment definition. The engine
 * supplies the machinery; an assessment supplies the subject-specific truth.
 */
(function (global) {
  'use strict';

  const ENGINE_VERSION = 'MAXESS-E00-ENGINE-V1';
  const RESULT_CONTRACT = 'MAXESS_RESULT_V1';

  function assert(condition, message) {
    if (!condition) throw new Error(message);
  }

  function band(score, bands) {
    const n = Number(score);
    assert(Number.isFinite(n) && n >= 0 && n <= 100, 'Score must be 0–100');
    assert(Array.isArray(bands) && bands.length > 0, 'Assessment mastery bands required');
    const match = bands.find(b => n >= b.min && n <= b.max);
    assert(match, `No mastery band covers score ${n}`);
    return match.id;
  }

  function clone(value) {
    return JSON.parse(JSON.stringify(value));
  }

  function deepFreeze(value) {
    if (!value || typeof value !== 'object' || Object.isFrozen(value)) return value;
    Object.freeze(value);
    Object.keys(value).forEach(key => deepFreeze(value[key]));
    return value;
  }

  function validateDefinition(definition) {
    assert(definition && typeof definition === 'object', 'Assessment definition required');
    assert(Array.isArray(definition.questions), 'Questions array required');
    assert(Array.isArray(definition.dimensions), 'Dimensions array required');
    assert(Array.isArray(definition.bands) && definition.bands.length > 0, 'Mastery bands required');
    assert(definition.questions.length > 0, 'At least one question required');
    assert(definition.dimensions.length > 0, 'At least one dimension required');

    const dimensionIds = new Set(definition.dimensions.map(d => d.id));
    assert(dimensionIds.size === definition.dimensions.length, 'Dimension IDs must be unique');

    const questionIds = new Set();
    definition.questions.forEach((q, qi) => {
      assert(q && typeof q === 'object', `Question ${qi + 1} invalid`);
      assert(typeof q.id === 'string' && q.id, `Question ${qi + 1} ID missing`);
      assert(!questionIds.has(q.id), `Duplicate question ID: ${q.id}`);
      questionIds.add(q.id);
      assert(dimensionIds.has(q.dimensionId), `Question ${q.id} references unknown dimension`);
      assert(Array.isArray(q.answers) && q.answers.length === 5, `Question ${q.id} must have exactly five answers`);
      const answerIds = new Set();
      q.answers.forEach((a, ai) => {
        assert(a && typeof a === 'object', `Question ${q.id} answer ${ai + 1} invalid`);
        assert(typeof a.id === 'string' && a.id, `Question ${q.id} answer ${ai + 1} ID missing`);
        assert(!answerIds.has(a.id), `Duplicate answer ID in ${q.id}: ${a.id}`);
        answerIds.add(a.id);
        assert(Number.isInteger(a.score) && a.score >= 0 && a.score <= 4, `Answer ${q.id}/${a.id} must score 0–4`);
      });
    });

    assert(definition.bands.every(b => Number.isFinite(b.min) && Number.isFinite(b.max) && b.min <= b.max), 'Invalid mastery band range');
    return true;
  }

  function createState(definition) {
    validateDefinition(definition);
    return {
      phase: 'READY',
      questionIndex: 0,
      responses: [],
      selectedAnswerId: null,
      result: null
    };
  }

  function currentQuestion(state, definition) {
    assert(state && definition, 'State and definition required');
    assert(state.phase !== 'RESULT_FINALIZED', 'Assessment already finalized');
    return definition.questions[state.questionIndex] || null;
  }

  function selectAnswer(state, definition, answerId) {
    const question = currentQuestion(state, definition);
    assert(question, 'No active question');
    const answer = question.answers.find(a => a.id === answerId);
    assert(answer, `Answer ${answerId} does not belong to ${question.id}`);
    state.selectedAnswerId = answer.id;
    state.phase = 'ANSWER_SELECTED';
    return answer;
  }

  function commitCurrentAnswer(state, definition) {
    const question = currentQuestion(state, definition);
    assert(question, 'No active question');
    assert(state.selectedAnswerId, 'An answer must be selected before Continue');

    const answer = question.answers.find(a => a.id === state.selectedAnswerId);
    assert(answer, 'Selected answer is invalid for the current question');

    const response = {
      questionId: question.id,
      questionOrder: state.questionIndex + 1,
      dimensionId: question.dimensionId,
      answerId: answer.id,
      score: answer.score
    };

    const existing = state.responses.findIndex(r => r.questionId === question.id);
    if (existing >= 0) state.responses[existing] = response;
    else state.responses.push(response);

    return response;
  }

  function calculate(definition, responses) {
    assert(responses.length === definition.questions.length, 'Incomplete assessment: response count does not match question count');

    const expectedIds = new Set(definition.questions.map(q => q.id));
    const responseIds = new Set(responses.map(r => r.questionId));
    assert(responseIds.size === responses.length, 'Duplicate question responses detected');
    assert(responses.every(r => expectedIds.has(r.questionId)), 'Response references unknown question');

    const dimensions = definition.dimensions.map(dimension => {
      const questions = definition.questions.filter(q => q.dimensionId === dimension.id);
      const maxRaw = questions.length * 4;
      const rows = responses.filter(r => r.dimensionId === dimension.id);
      const raw = rows.reduce((sum, r) => sum + r.score, 0);
      assert(rows.length === questions.length, `Dimension ${dimension.id} is incomplete`);
      const score = Math.round((raw / maxRaw) * 100);
      return {
        id: dimension.id,
        name: dimension.name,
        rawScore: raw,
        maxScore: maxRaw,
        score,
        band: band(score, definition.bands)
      };
    });

    const rawScore = responses.reduce((sum, r) => sum + r.score, 0);
    const maxScore = definition.questions.length * 4;
    const overallScore = Math.round((rawScore / maxScore) * 100);
    const sorted = dimensions.slice().sort((a, b) => b.score - a.score || a.id.localeCompare(b.id));

    return {
      rawScore,
      maxScore,
      overallScore,
      masteryBand: band(overallScore, definition.bands),
      dimensions,
      strongestDimension: sorted[0],
      opportunityDimension: sorted[sorted.length - 1]
    };
  }

  function buildResult(definition, state) {
    const calculation = calculate(definition, state.responses);
    const result = {
      contractVersion: RESULT_CONTRACT,
      engineVersion: ENGINE_VERSION,
      assessmentId: definition.id,
      assessmentVersion: definition.version || '1.0.0',
      topic: clone(definition.topic || { id: definition.id, title: definition.title || definition.id }),
      participant: clone(definition.participant || {}),
      assessment: {
        questionCount: definition.questions.length,
        completedCount: state.responses.length,
        responses: clone(state.responses)
      },
      score: {
        raw: calculation.rawScore,
        max: calculation.maxScore,
        normalized: calculation.overallScore,
        percentage: calculation.overallScore,
        band: calculation.masteryBand
      },
      overallScore: calculation.overallScore,
      masteryBand: calculation.masteryBand,
      dimensions: calculation.dimensions,
      dimensionScores: Object.fromEntries(calculation.dimensions.map(d => [d.id, d.score])),
      strongestDimension: calculation.strongestDimension,
      opportunityDimension: calculation.opportunityDimension,
      responses: clone(state.responses),
      fingerprint: definition.fingerprint || null,
      selectedInterests: clone(definition.selectedInterests || []),
      naya: clone(definition.naya || {}),
      audio: clone(definition.audio || {}),
      integrity: {
        resultVersion: RESULT_CONTRACT,
        scoringVersion: definition.scoringVersion || '0-4-NORMALIZED-V1',
        rubricVersion: definition.rubricVersion || definition.version || '1.0.0'
      },
      completedAt: new Date().toISOString()
    };

    return deepFreeze(result);
  }

  function continueAssessment(state, definition) {
    assert(state.phase === 'ANSWER_SELECTED', 'Continue requires a selected answer');
    commitCurrentAnswer(state, definition);

    if (state.questionIndex === definition.questions.length - 1) {
      state.phase = 'SCORING';
      state.result = buildResult(definition, state);
      state.phase = 'RESULT_FINALIZED';
      state.selectedAnswerId = null;
      return { complete: true, result: state.result };
    }

    state.questionIndex += 1;
    state.selectedAnswerId = null;
    state.phase = 'QUESTION_ACTIVE';
    return { complete: false, question: definition.questions[state.questionIndex] };
  }

  function validateResult(result, definition) {
    assert(result && result.contractVersion === RESULT_CONTRACT, 'Invalid result contract version');
    assert(result.assessmentId === definition.id, 'Result assessment ID mismatch');
    assert(Number.isInteger(result.overallScore) && result.overallScore >= 0 && result.overallScore <= 100, 'Invalid overall score');
    assert(Array.isArray(result.dimensions) && result.dimensions.length === definition.dimensions.length, 'Invalid dimension count');
    assert(Array.isArray(result.responses) && result.responses.length === definition.questions.length, 'Invalid response count');
    assert(new Set(result.responses.map(r => r.questionId)).size === result.responses.length, 'Duplicate result responses');
    result.dimensions.forEach(d => assert(Number.isInteger(d.score) && d.score >= 0 && d.score <= 100, `Invalid dimension score: ${d.id}`));
    return true;
  }

  const API = Object.freeze({
    ENGINE_VERSION,
    RESULT_CONTRACT,
    validateDefinition,
    createState,
    currentQuestion,
    selectAnswer,
    commitCurrentAnswer,
    continueAssessment,
    calculate,
    buildResult,
    validateResult,
    band
  });

  global.MAXESS_E00_ENGINE_V1 = API;
})(typeof window !== 'undefined' ? window : globalThis);
