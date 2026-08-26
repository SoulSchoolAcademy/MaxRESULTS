# 🔱 MAXESS — NAYA APPRENTICE HANDOFF / BROWSER GATE 02

**Date:** 2026-08-26
**Canonical repository:** `SoulSchoolAcademy/NayaPOWER`
**Current branch:** `main`
**Current handoff commit:** `4229d3ce39bd653e6f536b42dd3cdcbf54716e6c` at the moment of browser execution start

## Destination

Reach the first clean human MAXESS test:

**SOURCE → ASSESSMENT → CONTINUE → SCORE → RESULT CONTRACT → RELEASE → RESULTS → LIVE → REGRESSION → OSCAR → FREEZE**

Human testing remains blocked until executed evidence is green.

## Authoritative architecture

- E00 owns state, answer commitment, scoring, result construction and result release.
- `MAXESS_E00_ENGINE_V2` is the scoring authority.
- `MAXESS_AI_SCORE_DEFINITION_V1` is the canonical assessment definition.
- `MAXESS_RESULT_V1` is the result authority.
- E01–E09 consume the result and never rescore.
- `MAXESS-RESULT-CONSUMER-V2.html` is presentation-only and event-driven.

## What just changed

### Hardening automation
`maxess-v2-auto-hardening.mjs` was made idempotent. It can now run against both unhardened and already-hardened Groove source and verifies the final hardening invariants.

### Browser harness
The Playwright harness now captures request failures, page errors, failure screenshots, traces and a machine-readable diagnostics JSON. Duplicate completion is tested with programmatic click events.

### CI
The pre-test workflow now uploads browser evidence artifacts even when the browser gate fails.

## Current evidence

Run `33002378451` is the current browser evidence execution at the latest known observation.

Its prerequisites have passed:

- checkout;
- Node;
- deterministic hardening;
- static architecture gate;
- Playwright installation.

The browser evidence step is the remaining active gate at handoff time.

## Prior evidence

Run `33001382999` failed at browser evidence after static/executable prerequisites passed. The old workflow did not preserve artifacts, so the exact browser failure could not be responsibly diagnosed from the run metadata alone.

## Do not repeat blindly

Do not rewrite Continue again without new evidence.
Do not replace the authoritative engine.
Do not introduce a second scorer.
Do not add another bridge.
Do not turn a test failure into a product failure without classification.
Do not call green because source looks correct.

## Next exact action

Inspect the completed result of run `33002378451`.

If GREEN:

1. inspect the verified hardened Groove source;
2. prove E01 receives the exact frozen result;
3. verify responsive evidence;
4. update the final evidence receipt;
5. only then open the human test gate.

If RED:

1. download/read the uploaded browser artifact;
2. inspect `maxess-browser-diagnostics.json`;
3. inspect screenshot/trace if present;
4. classify the failure as product, harness, environment, integration, or evidence;
5. fix the correct layer;
6. rerun the affected gate;
7. update this handoff and the Smart Note.

## Ten-star standard

The next AI is joining an active team, not starting a new project.

Protect what works. Use evidence. Explain the decision. Fix the root cause. Verify the fix. Leave the next AI better prepared.

The user should receive a clean experience, not a debugging assignment.
