# 🧠 MAXESS SMART NOTE — PRE-TEST GATE LEARNINGS

**Date:** 2026-08-26
**Execution:** V2 Pre-Test Excellence Gate

## What we learned

### Result consumer authority
`MAXESS-RESULT-CONSUMER-V2.html` was a genuine architectural defect because it contained storage/URL result recovery. It is now event-driven and presentation-only.

### Duplicate completion
The Groove needed an early finalized-result guard in addition to release freezing. Native `disabled` state was also hardened so accessibility semantics match behavior.

### Scoring truth
The engine's mathematical envelope is 0 raw / 0 normalized through 60 raw / 100 normalized. The current canonical definition's actual minimum is 25/100 because some questions have no zero-score answer. Tests now distinguish mathematical engine invariants from canonical configuration invariants.

### Browser test lesson
The first Playwright attempt failed in the harness before the product rendered Q1 because dependency injection assumed an exact script-tag form. This was a test-harness defect, not evidence that the product failed.

The harness was corrected to inject the engine and definition by script filename pattern and to wait explicitly for the E00 runtime, engine, and definition before interacting.

## Operating lesson

**Never turn a test-harness assumption into a product defect.** First determine whether the observed failure belongs to:

1. product code;
2. test code;
3. environment;
4. deployment/integration;
5. evidence collection.

Then fix the correct layer and rerun.

## Current evidence

Static/executable gate: GREEN in GitHub Actions run `33001382999`.

Browser gate: YELLOW until the corrected harness has an executed green run.

Human test: intentionally blocked until browser smoke + E01 handoff + responsive evidence are green.

## Next AI instruction

Continue from this note. Do not repeat the original browser harness assumption. Run the corrected browser gate against the current `main`, inspect exact logs, fix only the real failing layer, and update the Smart Note + Apprentice Handoff + receipt before promoting any gate.
