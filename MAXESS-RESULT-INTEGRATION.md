# MAXESS One-Page Results Integration Contract

## Status

**ARCHITECTURE LOCKED — ONE WEBFLOW PAGE**

The assessment and Results experience now live on the same Webflow page as separate embed blocks. E00 is the execution authority. E01–E09 are presentation sections that hydrate from the single result contract produced by E00.

## Authoritative flow

`Q1–Q15` → `E00 scoring engine` → `MAXESS_RESULT_V1` → `window.MAXESS_RESULT` → result events → `E01–E09` hydration

There is no Results-page navigation in this one-page architecture. The old external handoff to `results.nayanet.app` is not part of this active flow.

## North Star

When the user answers Question 15 and clicks **Continue once**:

1. the Q15 response is committed;
2. E00 calculates the complete 15-response result;
3. E00 validates the five-dimension result contract;
4. `MAXESS_RESULT_V1` becomes the canonical runtime result;
5. the result is persisted where supported;
6. `MAXESS_RESULT_READY` and `maxess:result-updated` are dispatched;
7. the Results isolation boundary is released;
8. E01–E04 hydrate from the same result;
9. E05–E09 remain present and visible;
10. the user is immediately looking at the Results experience.

No second click. No Q15 dead end. No results navigation. No spinner. No stale stored result is allowed to release the current page before the current assessment completes.

## Authority model

### E00 — EXECUTION AUTHORITY

E00 owns:

- the 15 questions;
- answer capture;
- the score matrix;
- Q15 terminal execution;
- overall score calculation;
- five dimension scores;
- mastery band calculation;
- personalized assessment text;
- `MAXESS_RESULT_V1` construction;
- final contract validation;
- persistence;
- result event broadcast.

E00 is the **only scoring authority**.

### E00.01 — TERMINAL BRIDGE

E00.01 is an execution bridge, not a second scoring engine.

Its V8 terminal path listens for the Q15 `Continue` state (`Assessment Complete`) and calls the existing E00 `window.MAXESS_AISCORE.publish()` authority. This removes the obsolete completion-popup dependency without duplicating scoring logic.

E00.01 intentionally does **not** recover stale sessionStorage on page load. A previous user's result must never release the current assessment page.

### E00.02 — VISUAL ISOLATION

E00.02 owns the visual waiting/released boundary. It hides E01–E09 during assessment and releases them after the authoritative result event.

It does not calculate scores.

### E00.03 — RESULTS CONTROLLER

E00.03 remains a compatibility/controller layer. It validates and relays the already-authoritative E00 result. It does not score the assessment and must never invent a result.

## E01–E04 contract

All four sections consume the same `window.MAXESS_RESULT` object.

- **E01:** overall score / score reveal.
- **E02:** five dimension scores.
- **E03:** personal report / assessment narrative.
- **E04:** Direction capability score and spectrum.

The section code must not redefine the scoring model. E00 supplies the numbers and personalized text; the sections render them.

Current authoritative dimensions:

1. Direction
2. Communication
3. Evaluation
4. Iteration
5. Systems Thinking

## Canonical result payload

`MAXESS_RESULT_V1` must contain at minimum:

- `contractVersion`
- `overallScore` (0–100)
- `masteryBand`
- `dimensions` (exactly 5, each 0–100)
- `dimensionScores`
- `assessmentText`
- `personalizedAssessment`
- `assessment.text`
- `responses` (exactly 15 unique questions)
- `strongestDimension`
- `opportunityDimension`

## Terminal lifecycle

`Q15 answer selected` → `Continue` → `E00.01 terminal bridge` → `window.MAXESS_AISCORE.publish()` → `save()` → `calculate()` → `buildResult()` → `valid()` → persist → broadcast → E01–E09 release/hydration.

The existing E00 publish path already performs the authoritative save, calculation, validation, persistence, broadcast, local release, and result rendering. The repair therefore connects the terminal button to that authority rather than creating another scoring implementation.

## Protected principles

- One scoring engine.
- One canonical result object.
- One terminal click.
- One page.
- No duplicated scoring formulas in E01–E09.
- No stale result auto-release.
- No external Results navigation in the active one-page deployment.
- No obsolete `.xyz` Results implementation.
- No hidden fallback/demo score.

## Verification states

- **IMPLEMENTED:** V8 bridge and one-page contract committed to GitHub.
- **STATIC VERIFIED:** source architecture and terminal path inspected.
- **LIVE VERIFIED:** requires running the published Webflow page through all 15 questions and confirming the real result render.
- **HUMAN REVIEW REQUIRED:** final visual confirmation of E01–E09 in the published Webflow page.
