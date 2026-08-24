# MAXESS ENGINE EXECUTION LOCK

**Status:** NORTH STAR / ACTIVE
**Canonical repository:** `SoulSchoolAcademy/NayaPOWER`
**Canonical branch:** `main`
**Current canonical assessment shell:** `E00 118` (E00.118)

## Core objective
Get the existing MAXESS engine genuinely running before adding Name/Topic generation, universal assessment generation, lessons, PDFs, or marketing refinements.

## The locked success chain
`Continue → next() → Q15 → save() → calculate()/buildResult() → validate → MAXESS_RESULT_V1 → window.MAXESS_RESULT → persistence → broadcast → E00.01 → E00.03 → E00.02 → E01/E02/E03/E04`

## Definition of DONE
One complete 15-question assessment must produce a valid `MAXESS_RESULT_V1` containing:
- exactly 15 responses
- overallScore 0–100
- exactly 5 dimension scores
- masteryBand
- authoritative result on `window.MAXESS_RESULT`
- successful persistence
- result broadcast
- real downstream rendering in E01, E02, E03 and E04
- all of this remains inside the current MAXESS experience

## Execution discipline
1. Read the canonical code first.
2. Identify the first runtime failure, not a downstream symptom.
3. Make the smallest surgical repair that removes that failure without redesigning the architecture.
4. Re-fetch the exact changed canonical file immediately after every write.
5. Verify the changed code and the contract before moving downstream.
6. Prefer one complete end-to-end proof over many isolated cosmetic checks.
7. Never declare green because code merely looks correct.
8. Apply cause-and-effect analysis before every change: a repair that creates collateral defects is not a successful repair.
9. Each execution pass should batch the maximum safe amount of work toward the current milestone instead of stopping after one trivial action.
10. Never regress a verified higher state on the ladder. Preserve every proven green boundary.

## Minimum execution ladder
**1. Baseline** — canonical code/state.
**2. Continue** — prove event reaches `next()`.
**3. Q15** — prove final response enters save/publish.
**4. Score inputs** — prove score/dimension matrices are valid.
**5. Calculation** — prove calculation executes.
**6. Result object** — prove complete `MAXESS_RESULT_V1`.
**7. Persistence** — prove storage.
**8. Broadcast** — prove release event.
**9. Bridges** — prove E00.01/E00.03/E00.02.
**10. Consumers** — prove E01/E02/E03/E04 display real values.
**11. Wild hardening** — test repeat runs, refresh/re-entry, duplicate events, malformed state, mobile, accessibility.
**12. Universal assessment** — only after the terminal chain is green: Name + Topic → assessment generation under locked question/scoring laws.

## Output optimization law
Do not make Shawn repeatedly ask for the next obvious step. At the end of each execution pass, report what was actually verified, what changed, what remains, and provide the next exact execution command. Bundle safe adjacent work into the same pass.

## Current priority order
**P1 — Start the MAXESS engine.**
**P2 — Prove the complete result contract and downstream display.**
**P3 — Build Name/Topic-driven assessment generation and then the Naya Power learning loop.**

The engine is the foundation. Do not build the ocean around an engine that has not been proven to run.
