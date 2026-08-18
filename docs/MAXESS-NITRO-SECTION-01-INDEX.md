# MAXESS NITRO — SECTION 01 INDEX

Status: ACTIVE SECTION EXECUTION MEMORY
Branch: `maxess-results-v21-working`
Scope: SECTION 01 ONLY

## Primary artifact

- `NITRO/SECTION-01-NAYA-WELCOME-ORBSCORE.html` — current Section 01 working artifact.

## Execution memory

- `docs/MAXESS-NITRO-SECTION-01-EXECUTION-REPORT.md` — latest evidence/state.
- `docs/MAXESS-NITRO-SECTION-01-GUARDRAILS.md` — durable Section 01 rules.
- `docs/MAXESS-SECTION-01-AAA-BUILD-PROMPT.md` — existing Section 01 build prompt.
- `docs/MAXESS-SECTION-01-LOCKED-BUILD-CONTRACT.md` — existing Section 01 contract.
- `docs/SMART-NOTE-2026-08-18-SECTION-01-VISUAL-QA.md` — latest Section 01 visual QA memory.

## Required governance

- `README.md`
- `NAYA-OS.md`
- `NAYA-REPO-LOCK.md`
- `docs/MAXESS-MASTER-CONTRACT.md`
- `docs/MAXESS-AAA-SECTION-DESIGN-SPEC.md`
- `docs/MAXESS-COMPONENT-OWNERSHIP-REGISTRY.md`
- `docs/MAXESS-CHANGE-LEDGER.md`
- `docs/MAXESS-SECTION-EXECUTION-WORKFLOW.md`
- `docs/MAXESS-SMART-NOTES.md`
- `docs/HMC-MAXIMUS-BUTTON-AND-ICON-SYSTEM.md`
- `docs/DEPLOYMENT-CONTRACT.md`

## Section 01 owner

The component ownership registry identifies Naya Arrival / Section 01 as a V21-owned component. This execution remains section-scoped and does not modify Section 02+.

## Protected behavior

- `window.MAXESS_RESULT.overallScore` is the production score source.
- Explicit `?fixture=demo` is the only demo path.
- Naya uses the approved asset already referenced by the current V21/Nitro implementation.
- One primary Listen action; no second audio system.
- Orb breathing remains 6s.
- Orbital Bead remains 14px / 220px / 10s desktop and 11px / 140px mobile.
- Reduced motion disables Orb + Bead animation.
- No `WAITING FOR RESULT`, redundant `RESULT`, `MAXESS SCORE`, or `Your score is a map.` presentation copy.

## Execution law

`READ → SCORE → MUTATE → PROVE → BUILD → VERIFY → OSCAR → REPAIR → RETEST`

GitHub commit state and Groove/live state are separate verification gates.
