# MAXESS / NAYA — REPOSITORY MAP

## Purpose
This is the execution map for AI and humans. Read this after `README.md` and before consequential work. It prevents source confusion, stale-file selection, duplicated systems, and missed QA.

## Canonical identity
- Repository: `SoulSchoolAcademy/MaxRESULTS`
- Current Results execution branch: `maxess-results-v21-working`
- Legacy repository: `SoulSchoolAcademy/maxess` — reference only unless explicitly requested.

## Master read order
1. `START-HERE.md` — execution trigger and mandatory read order.
2. `docs/REPOSITORY-MAP.md` — this table of contents and state map.
3. `NAYA-OS.md` — governing execution/product laws.
4. `docs/NAYA-NITRO-MODE.md` — execution loop and QA method.
5. `docs/NAYA-NITRO-MASTER-BLUEPRINT.md` — Naya Nitro product thesis.
6. `docs/NAYA-MAXESS-OPERATING-MANUAL.md` — Results operating rules.
7. `docs/MAXESS-RESULTS-PRODUCT-SPEC.md` — product requirements.
8. `docs/SOURCE-AND-MEMORY-MAP.md` — authority and historical lineage.
9. `docs/DEPLOYMENT-CONTRACT.md` — GitHub → Groove → public verification.
10. `docs/RELEASE-CHECKLIST.md` — release gate.
11. Read only additional task-specific documents required by the request.

## Categories
### GOVERNANCE / EXECUTION
`NAYA-OS.md` · `docs/NAYA-NITRO-MODE.md` · repository lock/entry documents.

### PRODUCT / EXPERIENCE
`docs/MAXESS-RESULTS-PRODUCT-SPEC.md` · `docs/NAYA-MAXESS-OPERATING-MANUAL.md` · relevant MAXESS design/page specifications.

### STATE / HISTORY
`docs/SOURCE-AND-MEMORY-MAP.md` · `docs/MAXESS-CHANGE-LEDGER.md` · baselines/candidate records.

### ENGINEERING / TOOLS
`tools/` — builders, executors, deterministic transforms, and QA scripts. Inspect before use; never assume a named tool exists.

### AUTOMATION
`.github/workflows/` — GitHub Actions. Automation verifies and guards; it must never silently redefine product authority.

### DEPLOYMENT / RELEASE
`docs/DEPLOYMENT-CONTRACT.md` · `docs/RELEASE-CHECKLIST.md`.

### ASSETS / REFERENCES
Root PDFs/images and approved asset registries are reference resources unless explicitly designated production.

## Current main-branch state
Main is the repository governance/reference branch. The active V21 implementation is on `maxess-results-v21-working`. Do not infer production authority from main merely because it is the default branch.

## Execution law
**GITHUB FIRST → READ → MAP → ESTABLISH STATE → SOURCE-LOCK → BASELINE → IMPLEMENT IN COHERENT BATCHES → BUILD → REFETCH → DIFF → STATIC QA → BEHAVIOR QA → OSCAR → REPAIR → RE-VALIDATE → FREEZE → DELIVER.**

## Non-negotiables
- Never guess a path, branch, artifact, or authority.
- Never use conversation memory when repository evidence exists.
- Never create competing renderers or result sources.
- Never replace a complete working artifact with a tiny test renderer.
- Never call GitHub state live; Groove requires separate public verification.
- Every material failure should produce a root cause and, where practical, a durable guardrail.
- Final status must distinguish `IMPLEMENTED`, `VERIFIED`, `LIVE VERIFIED`, and `HUMAN REVIEW REQUIRED`.

## Product north star
**DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY**
