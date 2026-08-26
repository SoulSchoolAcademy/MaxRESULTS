# 🔱 MAXESS POST-GATE RECONCILIATION — 2026-08-26

## STATE

**Project:** MAXESS / Naya Hub front-end core

**Current main SHA at reconciliation:** `b1658830e82a9999208440994b3b7c359d5bbfb1`

**Last successful Browser Gate run:** `33024152158`

**Successful run tested SHA:** `ebf65026c45abc8ba92a4f0dc05ab02336fe753d`

**Current main differs from tested SHA:** YES. Two subsequent commits were made after the successful run:

1. `6a0769d6bf64c486f0a9395455d9640f5b4fed0d` — automated MAXESS hardening commit.
2. `4baf8979938738c358d5c456e736bab1a26bf52e` — CI hardening made idempotent and duplicate Continue assignments guarded.
3. `b1658830e82a9999208440994b3b7c359d5bbfb1` — successful-browser-evidence preservation added to the workflow.

The current `main` therefore must not be called browser-verified solely from run `33024152158` because that run executed `ebf65026...`, not `b1658830...`.

## FINDINGS

### 1. Browser Gate 04 root cause is proven

Run `33007579261` was a **TEST HARNESS / SCRIPT-COMPOSITION boundary** failure. The old greedy runtime extraction consumed multiple script blocks and injected `</script><script>` markup into JavaScript, causing `Unexpected token '<'` and preventing MAXESS globals from initializing.

The root-cause receipt is authoritative for that diagnosis.

### 2. Browser correction succeeded

Run `33024152158` completed successfully with all three defined Playwright tests passing:

- canonical minimum golden path;
- maximum golden path + duplicate Continue guard;
- required mobile-width usability.

The workflow log proves the static gate, browser source-boundary guard, Playwright browser execution, and all three tests passed.

### 3. The successful run did not preserve success artifacts

The workflow attempted to upload `test-results/**` and `playwright-report/**`, but the Playwright invocation used the line reporter and produced no files on success. The job log explicitly states that no artifacts were found and no artifacts were uploaded.

This is an **evidence-preservation gap**, not a browser failure.

### 4. Automated hardening was not actually idempotent

Commit `6a0769d6...` added another `$('#mx-cont').disabled=false;` assignment. The diff proves the automated hardening step had accumulated a duplicate assignment.

The hardening script was subsequently changed so the answer-selection unlock is normalized to exactly one assignment and the script throws if more than one remains.

This is source-quality / CI hygiene, not evidence of a product defect.

### 5. Current evidence state

There is **no fresh Browser Gate run ID yet for current main `b1658830...` visible through the available workflow-run lookup**.

Therefore the correct gate is:

**Browser corrected + prior browser run GREEN + current-main verification PENDING.**

Do not promote current main to final Browser GREEN until a run executes the current head and its evidence is preserved.

## EXACT TESTS PASSED IN RUN 33024152158

### Test 1 — minimum golden

Proven by assertions:

- result score = 25;
- contract = `MAXESS_RESULT_V1`;
- 15 responses;
- result frozen;
- exactly one `MAXESS_RESULT_READY` event observed;
- exactly one `maxess:result-updated` event observed;
- `completionCount = 1`;
- E01 displays score 25;
- no failed requests;
- no runtime/console errors.

### Test 2 — maximum golden + duplicate Continue

Proven by assertions:

- result score = 100;
- contract = `MAXESS_RESULT_V1`;
- 15 responses;
- result frozen;
- exactly one ready event;
- exactly one updated event;
- `completionCount = 1`;
- two additional synthetic Continue clicks do not increase completion count;
- result remains 100;
- no failed requests;
- no runtime/console errors.

### Test 3 — responsive widths

Proven at:

`320, 360, 375, 390, 414, 480, 600, 768, 900, 1024, 1280`

The test verified no document/Groove horizontal overflow, Q1 presence, and five answers at every width.

## ACCEPTANCE SCORECARD

| Criterion | State | Evidence |
|---|---|---|
| 1. Q1 renders | VERIFIED | Test 1/2 browser execution |
| 2. Five answers render | VERIFIED | Test loop asserts count 5 |
| 3. Continue disabled before selection | VERIFIED | Test loop asserts disabled |
| 4. Continue enables after selection | VERIFIED | Test loop asserts enabled |
| 5. Q1→Q15 exactly once | PARTIALLY VERIFIED | 15-step progression is exercised; exact render-count telemetry is not asserted |
| 6. Final answer commits once | PARTIALLY VERIFIED | `completionCount=1` proves one completion, but no dedicated final-answer commit counter exists |
| 7. `MAXESS_RESULT_V1` contract | VERIFIED | Both golden tests assert contract |
| 8. Result frozen | VERIFIED | Both golden tests assert `Object.isFrozen` |
| 9. Exactly one completion | VERIFIED | `completionCount=1` |
| 10. Exactly one `MAXESS_RESULT_READY` | VERIFIED | `ready=1` |
| 11. Exactly one `maxess:result-updated` | VERIFIED | `updated=1` |
| 12. `completionCount=1` | VERIFIED | Both golden tests |
| 13. Duplicate Continue cannot create completion | VERIFIED | Synthetic double-click guard |
| 14. E01 receives same result | VERIFIED for score | E01 score equals authoritative score; exact object identity not asserted |
| 15. No downstream rescoring | PARTIALLY VERIFIED | E01 consumes released result and static architecture guard passes; no explicit mutation/rescore sentinel asserted |
| 16. No console errors | VERIFIED | Runtime/console error arrays equal empty |
| 17. No failed requests | VERIFIED | Failed-request arrays equal empty |
| 18. Required mobile widths usable | VERIFIED | All 11 widths pass |

## CURRENT MAXESS GATE

**Machine browser path:** GREEN on the tested SHA `ebf65026...`.

**Current-main browser path:** PENDING fresh verification.

**Human test:** BLOCKED until current-main machine evidence is green and the remaining acceptance gaps are closed or explicitly accepted.

**10/10:** NOT VERIFIED.

## EXECUTED IN THIS RECONCILIATION

### A. Fixed CI hardening idempotency

Updated:

`PROJECTS/MAXESS/TESTS/maxess-v2-auto-hardening.mjs`

The hardening pass now:

- normalizes the answer-selection Continue unlock to one assignment;
- fails if more than one unlock assignment exists;
- preserves all existing hardening invariants.

### B. Fixed evidence preservation

Updated:

`.github/workflows/maxess-v2-pretest.yml`

The workflow now:

- emits a Playwright JSON report;
- creates a machine-readable run receipt even on successful tests;
- uploads browser evidence with `if-no-files-found: error`;
- retains the evidence for 14 days.

This makes a successful browser run durable evidence rather than a disappearing green check.

## PROTECTED ASSETS

- MAXESS V2 authoritative E00 Groove implementation.
- MAXESS authoritative V2 engine.
- MAXESS AI Score definition.
- `MAXESS_RESULT_V1` contract.
- E01–E09 premium result assets.
- No-historical-rescoring rule.
- Browser harness source-boundary correction.
- Browser root-cause receipt.
- Existing premium visual language and Naya/orb experience.
- One authoritative scoring/result path.

## OPEN / RISKS

1. Fresh Browser Gate for current `main` is required.
2. Success evidence must be downloaded/inspected after the new run.
3. Exact question-render-count / final-answer-commit / downstream-rescore telemetry should be strengthened if safely possible without changing product behavior.
4. Existing `.app` / `.xyz` results-navigation drift remains a release-reconciliation item unless current E01 handoff evidence proves the relevant path is no longer active.
5. Human test remains blocked.
6. Hub implementation remains downstream of the MAXESS machine gate.

## NEXT ACTION

**Run the Browser Gate against current `main` after the idempotency/evidence-preservation changes. Inspect the new artifact. If GREEN, strengthen only the remaining machine-verification gaps and then advance to the human-test-readiness gate. If RED, diagnose the first new evidence-backed divergence and repair only that boundary.**

## NEXT NAYA PROMPT

```text
🔱 NAYA EXECUTION MODE — CONTINUE FROM MAXESS POST-GATE RECONCILIATION

SOURCE OF TRUTH:
SoulSchoolAcademy/NayaPOWER / main

CURRENT MAIN:
b1658830e82a9999208440994b3b7c359d5bbfb1

LAST SUCCESSFUL BROWSER RUN:
33024152158

TESTED SHA:
ebf65026c45abc8ba92a4f0dc05ab02336fe753d

IMPORTANT:
The successful run is real evidence, but it tested ebf65026..., not current main. Do not call current main Browser GREEN until a fresh run proves it.

PROVEN ROOT CAUSE:
The previous Browser Gate failure was a TEST HARNESS / SCRIPT-COMPOSITION boundary defect caused by greedy runtime extraction. The correction is already proven on ebf65026....

EXECUTED SINCE SUCCESS:
1. Hardened maxess-v2-auto-hardening.mjs so CI normalization cannot accumulate duplicate Continue unlock assignments.
2. Added a hard failure if more than one Continue unlock assignment remains.
3. Updated maxess-v2-pretest.yml to emit and preserve a Playwright JSON report and machine-readable browser-run receipt on successful runs.
4. Changed evidence upload from silent ignore to explicit error when the evidence-preservation path itself fails.

PROTECTED:
MAXESS authoritative E00, authoritative engine, AI Score definition, MAXESS_RESULT_V1, E01–E09, existing visual implementation, Naya/orb, one scorer/result authority, no historical rescoring.

FIRST ACTION:
Locate the fresh MAXESS V2 Pre-Test Excellence Gate run triggered by the current-main changes.

THEN:
1. Verify the run's head SHA equals the current main SHA or record any new post-run automation commit explicitly.
2. Inspect job logs.
3. Download/inspect the preserved browser artifact.
4. Confirm the three browser tests pass.
5. Confirm the JSON receipt exists.
6. Confirm no browser artifacts are missing.
7. Reconcile current source against tested source.
8. Update the acceptance scorecard.

IF GREEN:
Close the remaining machine-verification gaps safely:
- exact Q1→Q15 render/progression telemetry;
- final-answer commit exactly once;
- downstream no-rescore sentinel;
- exact E01 frozen-result equivalence where safely testable.
Do not rewrite scoring, Continue, or result authority.

THEN:
Run the complete MAXESS regression/OSCAR readiness path.
Only after machine evidence is complete may Shawn be invited for one clean human test.

IF RED:
Classify the first new divergence PRODUCT / HARNESS / ENVIRONMENT / INTEGRATION / EVIDENCE and repair only that boundary.

AFTER EXECUTION RETURN:
STATE
FINDINGS
DECISIONS
EXECUTED
VERIFIED
UNVERIFIED
EVIDENCE
OPEN / RISKS
MAXESS SCORECARD
CURRENT MAIN SHA
TESTED SHA
NEXT ACTION

Then leave a new complete executable Naya prompt.

READ → UNDERSTAND → LEAD → EXECUTE → VERIFY → SCORE → PRESERVE → HANDOFF → CONTINUE
```
