# SMART NOTE — MAXESS TERMINAL FORENSICS, LESSONS & RECOVERY PLAN

## Purpose
Prevent repeated debugging loops and preserve the accumulated evidence, failed approaches, lessons, ranked hypotheses, and execution discipline for the MAXESS terminal engine.

## Locked Objective
The immediate objective is singular:

`E00.118 Q15 Continue → next() → save() → publish() → calculate/buildResult() → validate → MAXESS_RESULT_V1`

No Name/Topic generation. No E01–E04 changes until E00 itself produces the authoritative result.

## What We Tried / What It Taught Us

### 1. Full E00→E04 integration runs
**Outcome:** Repeatedly stopped at Q15.
**Lesson:** Reproduces the symptom but is too large a debugging surface. Do not use full integration as the first diagnostic anymore.

### 2. Parent/iframe harness work
**Outcome:** Genuine iframe integration infrastructure was established, but it still reproduced the Q15 terminal stall.
**Lesson:** The harness can observe the problem, but it cannot substitute for proving the production E00 terminal boundary.

### 3. GitHub Actions browser proof
**Outcome:** Browser automation reproduced the same Q15 stopping point.
**Lesson:** The defect is not merely Shawn's manual browser environment. Automated reproduction is valuable evidence, but Q15 completion is not result success.

### 4. Downstream E01–E04 inspection
**Outcome:** No downstream consumer can display a result that E00 never publishes.
**Lesson:** Downstream debugging before authoritative-result production is premature.

### 5. Repeated reruns of substantially similar proofs
**Outcome:** More evidence of the same symptom without crossing the terminal boundary.
**Lesson:** Repeating the same experiment is not progress. When the result is unchanged, change the boundary being interrogated.

### 6. Static inspection of the button/terminal path
**Outcome:** We have strong reason to investigate DOM/event lifecycle, but static code alone has not yet proven the exact first runtime failure.
**Lesson:** Do not promote a hypothesis to fact. Instrument the exact runtime boundary and let the first missing checkpoint determine the repair.

### 7. Broad architectural/integration thinking
**Outcome:** Too much time was spent considering the whole system while the engine remained unable to produce its first result.
**Lesson:** Shrink the problem until the failure becomes deterministic.

## Oscar Review — What Was Wrong With the Previous Reasoning

1. We optimized for coverage instead of information gain.
2. We treated reproduction as if it were diagnosis.
3. We sometimes moved downstream before proving the upstream contract.
4. We allowed the integration harness to become the debugging target instead of the production engine.
5. We did not force a strict first-failure checkpoint early enough.
6. We repeated experiments that had already produced the same information.
7. We did not sufficiently separate hypotheses from verified facts.
8. We optimized for architectural completeness before achieving the smallest executable success.
9. We allowed the ladder to advance and retreat instead of locking each proven rung.
10. We need to change strategy whenever two materially similar attempts produce the same failure.

## Top 10 Current Hypotheses — Highest Probability First

### 1. Continue event is not reaching the intended `next()` handler
Possible causes: listener lifecycle, stale DOM instance, listener attached before Groove replacement, or event delegation boundary.

### 2. Continue button is being replaced after the listener is attached
The visible button may not be the same DOM node that received the original listener.

### 3. Button state and event state are out of sync
`updateContinue()` may visually/semantically enable the button while the actual executable path remains unavailable, or vice versa.

### 4. Another event handler or lifecycle layer intercepts the click
A capture/bubble ordering issue, `preventDefault`, `stopPropagation`, or competing handler may prevent the terminal listener from executing.

### 5. A JavaScript exception occurs before or during terminal event binding
The page can remain visually functional while the terminal binding path has failed.

### 6. `next()` is entered but its Q15 branch does not execute as expected
The click problem would then be a symptom, not the root cause.

### 7. Q15 save state is invalid or incomplete
The terminal calculation may be correctly gated against an invalid 15-response state.

### 8. `publish()` is not reached after Q15 save
A control-flow or guard condition may terminate the chain.

### 9. Result construction/validation rejects the terminal state
The scoring engine may run but fail before producing a valid `MAXESS_RESULT_V1`.

### 10. Groove/iframe lifecycle changes the runtime context at the terminal boundary
The code may execute in a context different from the one expected by the result/persistence/broadcast path.

## Execution Order — Do Not Skip Ahead

### A. Fetch and inspect
Fetch the complete canonical E00.118 and locate the exact implementations of:
`continueButton`, `updateContinue()`, event binding, `next()`, Q15 branch, `save()`, `publish()`, `calculate/buildResult()`, validation, persistence and broadcast.

### B. Instrument only E00 terminal execution
Use deterministic checkpoints:
`CLICK_RECEIVED → NEXT_ENTERED → Q15_BRANCH → SAVE_COMPLETE → PUBLISH_ENTERED → CALCULATE_COMPLETE → RESULT_VALID → RESULT_PUBLISHED`

### C. Run E00 alone
Complete Q1–Q15. The first absent checkpoint is the first failure.

### D. Repair the first failure only
Make the smallest surgical change. Do not redesign scoring or downstream architecture.

### E. Re-fetch and verify the exact committed code
Never ask for human testing of an unverified version.

### F. Repeat E00 from zero
Require:
- exactly 15 responses
- valid `MAXESS_RESULT_V1`
- overallScore
- five dimension scores
- masteryBand

### G. Lock E00 green
Only after the authoritative result exists may the system move downstream.

### H. Reconnect E01–E04
Then prove the existing result contract through the four consumers.

## Ground Rules

- No repeated experiment without a new question it answers.
- No static inspection declared as runtime proof.
- No downstream repair for an upstream failure.
- No architectural redesign to solve a local event defect.
- No Name/Topic work until E00→E04 is genuinely green.
- Every repair must be re-fetched and verified.
- Every successful rung becomes protected evidence.
- If two attempts produce the same failure, change the debugging boundary.
- Cause-and-effect review is mandatory before every change: identify the intended benefit and possible collateral effects.

## Success Definition
The engine is not considered started because the button looks enabled, Q15 appears selected, or a test runner reaches Q15.

The first true success is:

`15 responses → calculation → valid MAXESS_RESULT_V1 → overallScore + 5 dimensions + masteryBand`

Then, and only then:

`MAXESS_RESULT_V1 → E01 → E02 → E03 → E04`

## Operating Mantra
**Find the first failure. Fix the first failure. Prove the repair. Lock the rung. Move forward. Never loop backward without new evidence.**

Optimize. Maximize. Synergize. Equalize.
