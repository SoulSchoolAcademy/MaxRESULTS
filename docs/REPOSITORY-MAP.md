# MAXESS / NAYA — ACTIVE BRANCH REPOSITORY MAP

## Purpose

This is the implementation map for the active Results engineering branch. It must not compete with the canonical governance on `main`.

## Canonical governance

The repository is `SoulSchoolAcademy/MaxRESULTS`.

- `main` = canonical governance/reference branch.
- `maxess-results-v21-working` = active Results engineering branch.
- `SoulSchoolAcademy/maxess` = legacy reference only unless explicitly requested.

Canonical operating rules live on `main` and outrank branch-local history.

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

### E. ENGINEERING / TOOLS
`tools/` — deterministic builders, executors, validators, and QA scripts. Inspect before using; never assume a named tool exists.

### F. AUTOMATION
`.github/workflows/` — GitHub Actions. Automation should inspect, validate, and catch failures. Mutation must be explicitly authorized and must not silently redefine product direction.

### G. DEPLOYMENT / RELEASE
- `docs/DEPLOYMENT-CONTRACT.md`
- `docs/RELEASE-CHECKLIST.md`

GitHub state is never proof of public/live state.

## Current implementation state

- Active branch: `maxess-results-v21-working`.
- **E01 active working source:** `E01-SECTION-01-WORKING.html`.
- **Retired monolithic source:** `20260817 912am RESULTS PAGE CODE` — deleted from the active branch and must not be recreated or routed as an E01 source.
- Existing restoration references remain `BASELINE-WORKING.html` and `BASELINE-NITRO-20260817.html`; they are historical/restoration references, not the active E01 source.
- Runtime result contract: `window.MAXESS_RESULT`.
- Production score authority for E01: `window.MAXESS_RESULT.overallScore` only.
- Current Section 01 cycle: **fresh build / refinement — not approved**.
- Protected Section 01 component: **Orb + Orbital Bead core behavior supplied by the human**.
- Current Section 01 surrounding presentation: **new working implementation; open to refinement** unless explicitly protected by the current human instruction.

### E01 source-of-truth rule

There is exactly one active E01 working source: `E01-SECTION-01-WORKING.html`.

Historical, baseline, candidate, generated, and retired artifacts must not be treated as the active E01 implementation source.

The E01 working source is **not yet approved/canonical production**. Human approval is required before promotion.

## Execution law

**READ CANONICAL GOVERNANCE → READ ACTIVE MAP → ESTABLISH STATE → SOURCE-LOCK → IMPLEMENT → BUILD → REFETCH → DIFF → STATIC QA → BEHAVIOR QA → RENDER → VISUAL QA → SCORECARD → OSCAR → REPAIR → RE-TEST → REGRESSION → FREEZE ONLY WHEN APPROVED → RECORD DURABLE LEARNING → DELIVER.**

## Non-negotiable checks

- Never guess a path, branch, artifact, or authority.
- Never use conversation memory when repository evidence exists.
- Never create a competing renderer or result source.
- Never replace a complete working artifact with a tiny test renderer.
- Never call GitHub state “live.” Public deployment requires separate verification.
- Every material failure must produce a root cause and, where practical, a durable guardrail.
- Every execution must ask **WHY IS THIS NOT A 10?** and repair safely repairable weaknesses.
- Final status must distinguish `IMPLEMENTED`, `VERIFIED`, `LIVE VERIFIED`, `HUMAN REVIEW REQUIRED`, and `UNKNOWN`.

## Product north star

**DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY**

MAXESS measures. The Results experience interprets. Naya guides. The report explains. The dimensions provide evidence. The pattern creates understanding. The strength creates recognition. The lever creates focus. The next move creates action. The Naya Masters provide capability. NayaNET provides continuation.
