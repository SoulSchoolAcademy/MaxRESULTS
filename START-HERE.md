# MAXESS / NAYA — START HERE

## Canonical repository

`SoulSchoolAcademy/MaxRESULTS`

## Branch model

This branch, `maxess-results-v21-working`, is the **active Results engineering branch**.

The repository `main` branch is the **canonical governance/reference branch**. The current cold-start operating system, Naya Nitro rules, Smart Notes rules, authority hierarchy, and reusable execution contract are maintained there.

**Do not create a second governance system on this branch.**

When a branch-local document conflicts with the current governance on `main`, the current `main` governance wins unless the human explicitly changes the rule.

## Mandatory cold-start sequence

### A. Read canonical governance on `main`

1. `main:START-HERE.md`
2. `main:docs/REPOSITORY-MAP.md`
3. `main:NAYA-OS.md`
4. `main:docs/NAYA-EXECUTIVE-PLAN.md`
5. `main:docs/NAYA-NITRO-MODE.md`
6. `main:docs/NAYA-EXECUTION-PROMPT-TEMPLATE.md`
7. `main:docs/NAYA-SMART-NOTES-SYSTEM.md`
8. `main:docs/NAYA-NITRO-MASTER-BLUEPRINT.md`
9. `main:docs/smart-notes/INDEX.md`

### B. Then inspect this active branch

10. `START-HERE.md` — this branch-specific implementation entry point.
11. `docs/REPOSITORY-MAP.md` — active branch implementation map.
12. Relevant active source, tools, QA, deployment, and release documents.
13. Relevant recent/topic Smart Notes from `main`.

**Never substitute branch-local history for canonical governance.**

## Activation

Treat `Naya Read GitHub`, `Naya MAX Mode`, `Naya Nitro Mode`, and `Naya Nitro` as explicit activation commands.

## Every consequential execution

**GITHUB FIRST.** Resolve repository, governance branch, active branch, and current artifact before acting.

Establish:

**WHERE ARE WE → WHAT ARE WE BUILDING → WHAT IS PROTECTED → WHAT WORKS → WHAT FAILED → WHAT MUST NOT REGRESS → WHAT IS UNKNOWN → WHAT HAPPENS NEXT.**

Then:

**READ → MAP → REVIEW MEMORY → SCORE → SOURCE-LOCK → PLAN COMPLETE TODO → IMPLEMENT → BUILD → TEST → RENDER → VISUAL QA → OSCAR → REPAIR → RE-TEST → RECORD LEARNING → REPORT → NEXT ACTION PROMPT.**

## Current Section 01 authority rule

The current Section 01 cycle is a fresh build/refinement cycle.

Do **not** describe the current presentation artifact as “authoritative code,” “canonical renderer,” or “approved baseline” unless the human explicitly promotes it.

The **Orb + Orbital Bead core behavior supplied by the human is protected** for this cycle. Its specified visual behavior, score mapping, breathing, orbit, sizes, timing, reduced-motion behavior, and MAXESS visual language must be preserved unless the human explicitly changes them.

Everything surrounding that protected Orb behavior is working candidate material and may be refined according to the current human direction.

## Smart Notes / Naya Notes

**Naya Notes = Smart Notes = durable project memory.**

The canonical Smart Notes system lives on `main` under `docs/smart-notes/` and is governed by `main:docs/NAYA-SMART-NOTES-SYSTEM.md`.

At the end of every project conversation or consequential execution, identify durable learning that would make future work better, safer, faster, clearer, or more correct. Record it by default when durable value exists.

Do not store raw transcripts, temporary chatter, guesses, secrets, or duplicates.

Search by concepts, synonyms, aliases, dates, section names, and failure modes — never only by exact original wording.

Smart Notes are **memory, not authority**. Current human requirements and current repository governance outrank historical notes.

## Product chain

`15 answers → scoring → Result Contract → window.MAXESS_RESULT → Results → interpretation → Naya guidance → next action`

## Verification law

Code written is not completion.

A GitHub commit is not live deployment.

Use explicit states:

`IMPLEMENTED` · `VERIFIED` · `LIVE VERIFIED` · `HUMAN REVIEW REQUIRED` · `UNKNOWN`

Never claim a test, browser result, visual inspection, Groove result, or deployment that did not actually occur.

**Never guess. Preserve what works. Fix root causes. Add guardrails. Ask: WHY IS THIS NOT A 10?**

## Required ending

Every consequential execution must end with:

- CURRENT STATE
- WHAT WAS FOUND
- RECOMMENDATION
- EXACT NEXT ACTION
- COPY-PASTE EXECUTION PROMPT
- OPTIONS A/B/C only when genuinely useful
- VERIFICATION STATUS
