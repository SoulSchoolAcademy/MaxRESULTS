# MAXESS NITRO — SECTION 01 INDEX

**Status:** ACTIVE SECTION EXECUTION MEMORY + DELIVERY LOCK  
**Branch:** `maxess-results-v21-working`  
**Scope:** SECTION 01 ONLY

## PRIMARY DELIVERY ARTIFACT — HARD LOCK

`E01-SECTION-01-WORKING.html` is the **single active Section 01 engineering source AND the exact Groove handoff payload**.

**Naya edits this file. GitHub stores this file. Naya verifies this file. Shawn copies this file into Groove.**

There is no translation step between engineering and Groove handoff.

`NITRO/SECTION-01-NAYA-WELCOME-ORBSCORE.html` is preserved as a prior Section 01 implementation/reference artifact. It is not an independent active source and must not become a competing renderer or delivery payload.

## NON-NEGOTIABLE EXECUTION LOOP

`READ → FETCH ACTIVE FILE → ESTABLISH BASELINE SHA → BUILD COMPLETE CHECKLIST → MUTATE SAME FILE → RE-FETCH SAME FILE → INSPECT ACTUAL CHANGES → DIFF → STATIC QA → BEHAVIOR/REGRESSION QA → COMMIT → RAW LINK → HUMAN GROOVE DEPLOYMENT`

**A commit is not proof. A version bump is not proof. A successful write is not proof. A plan is not proof. The re-fetched artifact containing the requested changes is proof of implementation.**

## SELF-INSTRUCTION / LEAD MODE

At the end of every execution, before responding, Naya must ask herself:

> **Did I actually change the active delivery file? Did I re-fetch the same file after the write? Can I point to the requested edits inside that re-fetched source? Does the raw link point to that exact file? If not, I am not done. Continue execution or report the exact blocker.**

Do not return a prompt asking the human to tell Naya to finish work that Naya has already been instructed to execute. **Take the lead and execute.**

## EXECUTION MEMORY

- `docs/MAXESS-NITRO-SECTION-01-EXECUTION-REPORT.md` — latest evidence/state from prior focused Section 01 mutation.
- `docs/MAXESS-NITRO-SECTION-01-GUARDRAILS.md` — durable hard rules and delivery lock.
- `docs/MAXESS-SECTION-01-AAA-BUILD-PROMPT.md` — existing Section 01 build prompt.
- `docs/MAXESS-SECTION-01-LOCKED-BUILD-CONTRACT.md` — existing Section 01 contract.
- `docs/SMART-NOTE-2026-08-18-SECTION-01-VISUAL-QA.md` — latest Section 01 visual QA memory.

## REQUIRED GOVERNANCE

Canonical governance is on `main` and must be read first:

- `main:START-HERE.md`
- `main:.naya/NAYA-LAW-SYSTEM-PROTOCOL.md`
- `main:docs/REPOSITORY-MAP.md`
- `main:NAYA-OS.md`
- `main:docs/NAYA-LANGUAGE-DICTIONARY.md`
- `main:docs/NAYA-SCORECARDING-SYSTEM.md`
- `main:docs/NAYA-EXECUTIVE-PLAN.md`
- `main:docs/NAYA-NITRO-MODE.md`
- `main:docs/NAYA-EXECUTION-PROMPT-TEMPLATE.md`
- `main:docs/NAYA-SMART-NOTES-SYSTEM.md`

Then inspect active-branch implementation sources, including `START-HERE.md`, `NAYA-REPO-LOCK.md`, `NITRO-MASTER-EXECUTION-PROTOCOL.md`, `docs/MAXESS-AAA-SECTION-DESIGN-SPEC.md`, `docs/MAXESS-COMPONENT-OWNERSHIP-REGISTRY.md`, `docs/MAXESS-CHANGE-LEDGER.md`, `docs/MAXESS-NITRO-SECTION-01-GUARDRAILS.md`, and `docs/DEPLOYMENT-CONTRACT.md`.

## PROTECTED BEHAVIOR

- `window.MAXESS_RESULT.overallScore` is the production score source.
- Explicit `?fixture=demo` is the only demo path.
- Naya uses the approved asset already referenced by the current V21/Nitro implementation.
- One primary Listen action; no second audio system.
- Orb breathing remains 6s.
- Orbital Bead remains 14px / 220px / 10s desktop and 11px / 140px mobile.
- Reduced motion disables Orb + Bead animation.
- No hard-coded production result.
- Missing/invalid production data fails safely rather than inventing a score.

## CURRENT SECTION 01 HIERARCHY

**NAYA PRESENCE → NAYA MESSAGE → LISTEN → YOUR AI SCORE → SCORE REVEAL → ORB/BEAD → SCORE CONTEXT**

The surrounding presentation remains open to refinement until rendered review and applicable release/freeze gates pass.

## GROOVE ROLE BOUNDARY

Naya does **not** need Groove editor access for this workflow and must not treat it as an engineering blocker.

- **Naya:** engineering, editing, verification, GitHub commit, raw-code handoff.
- **Shawn:** Groove deployment/paste and rendered human review.

Do not send an unverified public/Groove link as though it were updated.

## SOURCE-OF-TRUTH REPAIR RULE

If any older document disagrees with this index, resolve the disagreement through current governance and the latest explicit human-approved state. Do not silently create or use a second active renderer.

## COMPLETION STATES

- **IMPLEMENTED:** requested edits exist in the active artifact.
- **VERIFIED:** active artifact was re-fetched after mutation and inspected for the requested edits.
- **LIVE VERIFIED:** public/Groove deployment independently fetched and confirmed.
- **HUMAN REVIEW REQUIRED:** rendered visual/interaction review remains with Shawn.
- **UNKNOWN:** evidence is unavailable; never convert UNKNOWN into success language.

## EXECUTION LAW

`READ → SCORE → MUTATE → PROVE → BUILD → VERIFY → OSCAR → REPAIR → RETEST`

**No report-only completion. No stale-link completion. No version-number completion. No commit-only completion.**
