# MAXESS / NAYA — ACTIVE BRANCH REPOSITORY MAP

## Purpose

This is the implementation map for the active Results engineering branch. It must not compete with the canonical governance on `main`.

## Canonical governance

The repository is `SoulSchoolAcademy/MaxRESULTS`.

- `main` = canonical governance/reference branch.
- `maxess-results-v21-working` = active Results engineering branch.
- `SoulSchoolAcademy/maxess` = legacy reference only unless explicitly requested.

Canonical operating rules live on `main`:

- `main:START-HERE.md`
- `main:docs/REPOSITORY-MAP.md`
- `main:NAYA-OS.md`
- `main:docs/NAYA-LANGUAGE-DICTIONARY.md`
- `main:docs/NAYA-SCORECARDING-SYSTEM.md`
- `main:docs/NAYA-EXECUTIVE-PLAN.md`
- `main:docs/NAYA-NITRO-MODE.md`
- `main:docs/NAYA-EXECUTION-PROMPT-TEMPLATE.md`
- `main:docs/NAYA-SMART-NOTES-SYSTEM.md`
- `main:docs/NAYA-NITRO-MASTER-BLUEPRINT.md`
- `main:docs/smart-notes/INDEX.md`

If any branch-local document conflicts with current `main` governance, do not guess. Treat `main` governance as authoritative and repair the conflicting branch-local instruction when appropriate.

## Duplicate-authority containment

Earlier execution cycles created branch-local documents with overlapping names and concepts, including language, scorecard, execution-prompt, design-directive, and Nitro operating documents. These remain useful historical/implementation references, but they do **not** create parallel governance.

Examples include:

- `docs/AI-PRODUCT-LANGUAGE.md`
- `docs/AI-DEFINITION-OF-10.md`
- `docs/MAXESS-FAST-EDIT-SCORECARD.md`
- `docs/MAXESS-EXECUTION-PROMPT-TEMPLATE.md`
- older `NITRO-*`, `MAXESS-*`, and design-directive documents

For current project language, quality definitions, scorecard methodology, and reusable execution contracts, use the canonical `main:` documents first. Consult branch-local duplicates only for task-specific implementation context or historical evidence.

## Active branch implementation map

### A. GOVERNANCE BRIDGE
`START-HERE.md` and this file — branch entry and implementation routing back to canonical `main` governance.

### B. PRODUCT / EXPERIENCE
- `docs/MAXESS-RESULTS-PRODUCT-SPEC.md`
- `docs/NAYA-MAXESS-OPERATING-MANUAL.md`
- relevant MAXESS design/page specifications.

### C. STATE / HISTORY
- `docs/SOURCE-AND-MEMORY-MAP.md`
- `docs/MAXESS-CHANGE-LEDGER.md`
- baselines, candidates, restoration references, and current implementation state.

### D. MEMORY / LEARNING
Canonical durable memory lives on `main` under `docs/smart-notes/`.

Use the canonical Smart Notes system and retrieval index. Do not create a second branch-specific memory system.

### E. ENGINEERING / TOOLS
`tools/` — deterministic builders, executors, validators, and QA scripts. Inspect before using; never assume a named tool exists.

### F. AUTOMATION
`.github/workflows/` — GitHub Actions. Automation should inspect, validate, and catch failures. Mutation must be explicitly authorized and must not silently redefine product direction.

### G. DEPLOYMENT / RELEASE
- `docs/DEPLOYMENT-CONTRACT.md`
- `docs/RELEASE-CHECKLIST.md`

GitHub state is never proof of Groove/public state.

## Current implementation state

- Active branch: `maxess-results-v21-working`.
- Working full Results artifact: `20260817 912am RESULTS PAGE CODE`.
- Existing restoration references include `BASELINE-WORKING.html` and `BASELINE-NITRO-20260817.html`.
- Runtime result contract: `window.MAXESS_RESULT`.
- Current Section 01 cycle: **fresh build / refinement — not approved**.
- Protected Section 01 component: **Orb + Orbital Bead core behavior supplied by the human**.
- Current Section 01 surrounding presentation: **working candidate material; open to refinement** unless explicitly protected by the current human instruction.

Do not call any artifact “authoritative production,” “canonical renderer,” or “approved baseline” merely because an older artifact or historical document uses those words.

## Execution law

**READ CANONICAL GOVERNANCE → READ ACTIVE MAP → REVIEW RELEVANT MEMORY → ESTABLISH STATE → SCORE → SOURCE-LOCK → COMPLETE TODO → IMPLEMENT → BUILD → REFETCH → DIFF → STATIC QA → BEHAVIOR QA → RENDER → VISUAL QA → SCORECARD → OSCAR → REPAIR → RE-TEST → REGRESSION → FREEZE ONLY WHEN APPROVED → RECORD DURABLE LEARNING → DELIVER → NEXT ACTION PROMPT.**

## Non-negotiable checks

- Never guess a path, branch, artifact, or authority.
- Never use conversation memory when repository evidence exists.
- Never create a competing renderer or result source.
- Never replace a complete working artifact with a tiny test renderer.
- Never call GitHub state “live.” Groove requires separate public verification.
- Never rely on exact keyword wording for memory retrieval.
- Never create an orphan Smart Note; canonical notes must be indexed.
- Never let Smart Notes override current authoritative sources.
- Every material failure must produce a root cause and, where practical, a durable guardrail.
- Every execution must score the current state, ask **WHY IS THIS NOT A 10?**, write the complete repair list, then execute the full authorized batch.
- Final status must distinguish `IMPLEMENTED`, `VERIFIED`, `LIVE VERIFIED`, `HUMAN REVIEW REQUIRED`, and `UNKNOWN`.

## Product north star

**DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY**

MAXESS measures. The Results experience interprets. Naya guides. The report explains. The dimensions provide evidence. The pattern creates understanding. The strength creates recognition. The lever creates focus. The next move creates action. The Naya Masters provide capability. NayaNET provides continuation.
