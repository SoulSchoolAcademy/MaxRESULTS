# MAXESS NITRO — SECTION 01 INDEX

Status: ACTIVE SECTION EXECUTION MEMORY
Branch: `maxess-results-v21-working`
Scope: SECTION 01 ONLY

## Purpose

This index exists so future Section 01 executions can locate the exact current instructions, artifact, evidence, and durable memory without relying on conversation history or guessing filenames.

## Section 01 files

- `MAXESS-NITRO-SECTION-01.html` — current UPDATED EDITED FILE for the focused Section 01 deliverable.
- `docs/MAXESS-NITRO-SECTION-01-EXECUTION-REPORT.md` — latest execution evidence and limitations.
- `docs/MAXESS-NITRO-SECTION-01-INDEX.md` — this navigation file.

## Required repository governance

- `README.md`
- `NAYA-OS.md`
- `NAYA-REPO-LOCK.md`

## Product/design references

- `docs/MAXESS-AAA-SECTION-DESIGN-SPEC.md`
- `docs/HMC-MAXIMUS-BUTTON-AND-ICON-SYSTEM.md`
- `docs/MAXESS-COMPONENT-OWNERSHIP-REGISTRY.md`
- `docs/MAXESS-CHANGE-LEDGER.md`
- `docs/MAXESS-SECTION-EXECUTION-WORKFLOW.md`
- `docs/MAXESS-SMART-NOTES.md`
- `docs/MAXESS-FAST-EDIT-SCORECARD.md`
- `docs/DEPLOYMENT-CONTRACT.md`
- `docs/MAXESS-EXECUTION-DEADLOCK-ANALYSIS.md`

## Section 01 owner

Component ownership registry identifies **Naya Arrival / Section 01** as owned by the V21 canonical renderer. The current focused artifact is intentionally kept as a section-level delivery artifact so Section 02+ is not modified by this execution.

## Protected Section 01 behavior

- `window.MAXESS_RESULT.overallScore` is the production score source.
- Explicit `?fixture=demo` is the only demo path.
- Naya uses the existing approved asset reference already present in the current V21 source.
- One primary Listen action.
- Listen delegates to an existing visible listener when available, otherwise emits `maxess:naya-listen` for the containing system.
- Orb breathing remains 6s.
- Orbital Bead remains 14px / 220px / 10s desktop and 11px / 140px mobile.
- Reduced motion disables Orb and Bead animation.
- No `WAITING FOR RESULT`, redundant `RESULT`, `MAXESS SCORE`, or unauthorized `Your score is a map.` presentation copy.

## Execution law

`READ → SCORE → MUTATE → PROVE → BUILD → VERIFY → OSCAR → REPAIR → RETEST`

A GitHub commit is not live deployment. Groove/public verification remains a separate gate.
