# MAXESS Dynamic Assessment Compiler V1

## Purpose

Turn a supported topic into the same configuration contract consumed by E00 without changing the scoring engine.

## Deterministic pipeline

```text
TOPIC → TOPIC RESOLVER → COVERAGE CHECK → KNOWLEDGE SOURCE
→ LEARNING OBJECTIVES → DIMENSION DESIGN → QUESTION ARCHETYPES
→ RUBRIC → ASSESSMENT DEFINITION → E00
```

## Topic request

```js
{ topicId, topicText, participantName, requestedDepth: 'standard' | 'advanced' }
```

## Topic coverage

```js
{ topicId, supported, coverageScore, knowledgeVersion, rubricVersion, sourceIds, limitations: [] }
```

## Assessment definition

```js
{
  id, version, topic,
  dimensions: [{ id, name, objectiveIds }],
  questions: [{ id, dimensionId, order, question,
    answers: [{ id, title, description, score, weight }]
  }],
  scoringVersion, rubricVersion, naya, audio
}
```

## Universal learning rubric

Where appropriate, subject coverage should address:

1. What it is.
2. Why it matters.
3. What problems it solves.
4. Core concepts.
5. How it is used.
6. Common mistakes.
7. Good practice.
8. Recognition/understanding.
9. Application.
10. Limitations and trade-offs.

The final five dimensions are subject-specific, not a hard-coded universal list.

## Knowledge boundary

The system must not invent expertise. If coverage is insufficient:

```text
SUPPORTED = false → TRUTHFUL BOUNDARY MESSAGE → NO ASSESSMENT GENERATED
```

Example: “We're not quite there yet. This topic is beyond our current assessment depth, but we're continually expanding what MAXESS can assess.”

MAXESS aims to be extraordinarily useful to the majority of people; it does not claim to replace elite specialists.

## Runtime principle

The scoring engine is deterministic. Topic compilation may be deterministic when the knowledge/rubric bank is sufficiently complete. A future Naya Power compiler may assist with synthesis, but the final assessment definition must pass validation before E00 can run it.

## Compiler validation

- topic is supported;
- knowledge/rubric versions are identified;
- every dimension has objectives;
- every question references a valid dimension;
- every question has exactly five answers;
- every answer score is 0–4;
- question IDs are unique;
- dimension IDs are unique;
- all questions are covered by the rubric;
- scoring metadata is present;
- assessment version is immutable for the run.

## Golden strategy

AI Score is the first compiled assessment and regression standard. Dynamic-topic generation is not green until the fixed AI Score path is green through E00 → MAXESS_RESULT_V1 → E01–E09.
