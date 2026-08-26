# MAXESS_RESULT_V1 — Authoritative Result Contract

**Status:** ARCHITECTURE LOCK — V1
**Authority:** E00 authoritative engine
**Consumers:** E01–E09

## Purpose

E00 produces exactly one canonical result object at assessment completion. E01–E09 are presentation consumers. They may derive display-only values, but they may not recalculate score, infer state from DOM, scrape visible text, or wait on timing/bridge choreography.

## Contract

```js
{
  contractVersion: 'MAXESS_RESULT_V1',
  engineVersion,
  assessmentId,
  assessmentVersion,
  topic: { id, title, category?, requestedByUser? },
  participant: { name? },
  assessment: {
    questionCount,
    completedCount,
    responses: [{ questionId, questionOrder, dimensionId, answerId, score }]
  },
  score: { raw, max, normalized, percentage, band },
  overallScore,
  masteryBand,
  dimensions: [{ id, name, rawScore, maxScore, score, band }],
  dimensionScores: { [dimensionId]: score },
  strongestDimension: { id, name, rawScore, maxScore, score, band },
  opportunityDimension: { id, name, rawScore, maxScore, score, band },
  responses: [{ questionId, questionOrder, dimensionId, answerId, score }],
  fingerprint: object | null,
  selectedInterests: [],
  naya: {},
  audio: {},
  integrity: { resultVersion, scoringVersion, rubricVersion },
  completedAt
}
```

## Authority rules

1. E00 is the only scoring authority.
2. E00 is the only completion authority.
3. E00 creates and freezes the result.
4. E01–E09 consume the result; they do not own it.
5. No result consumer may read `localStorage`, session state, DOM text, URL parameters, or legacy globals as an alternate source of score truth.
6. No consumer may poll for a result.
7. No consumer may use `setTimeout`, animation completion, MutationObserver, or load order to establish correctness.
8. The result must validate against `MAXESS_RESULT_V1` before release.
9. A missing or invalid result is an explicit failure state, never a guessed result.

## AI Score golden invariants

- 15 questions.
- 5 answers per question.
- Every answer score is exactly 0, 1, 2, 3, or 4.
- Five dimensions.
- Maximum overall raw score = `15 × 4 = 60`.
- Normalized score = `round(raw / 60 × 100)`.
- Each dimension contains three questions in the canonical AI Score assessment, so each dimension max = 12 and dimension score = `round(raw / 12 × 100)`.
- Mastery-band thresholds are defined by the assessment definition, not by a Results section.

## Release sequence

```text
final valid response
  → deterministic scoring
  → result construction
  → result validation
  → deep freeze
  → single release
  → E01–E09
```

## Dynamic assessment compatibility

The contract intentionally carries `assessmentId`, `assessmentVersion`, `topic`, `rubricVersion`, and `scoringVersion` so AI Score is one configuration-defined assessment rather than a special hard-coded application.

Dynamic topic generation must produce the same assessment-definition interface before E00 runs. The scoring engine does not change when the subject changes.
