# MAXESS / NAYA — REPOSITORY MAP

## Purpose
This is the execution map for AI and humans. Read this after `README.md` and before consequential work. It prevents source confusion, stale-file selection, duplicated systems, and missed QA.

## Canonical identity
- Repository: `SoulSchoolAcademy/MaxRESULTS`
- Active Results branch: `maxess-results-v21-working`
- Legacy repository: `SoulSchoolAcademy/maxess` — reference only unless explicitly requested.

## Master read order
1. `README.md` — repository overview and entry point.
2. `NAYA-REPO-LOCK.md` — repository/branch/source-selection lock.
3. `NAYA-OS.md` — governing execution and product laws.
4. `docs/NAYA-NITRO-MODE.md` — execution loop and QA method.
5. `docs/NAYA-NITRO-MASTER-BLUEPRINT.md` — Naya Nitro product thesis.
6. `docs/NAYA-MAXESS-OPERATING-MANUAL.md` — Results operating rules.
7. `docs/MAXESS-RESULTS-PRODUCT-SPEC.md` — current product requirements.
8. `docs/SOURCE-AND-MEMORY-MAP.md` — authority and historical lineage.
9. `docs/DEPLOYMENT-CONTRACT.md` — GitHub → Groove → public verification.
10. `docs/RELEASE-CHECKLIST.md` — release gate.
11. Task-specific design, QA, asset, change-ledger, or implementation documents as required.

## Source categories
### A. GOVERNANCE / EXECUTION
`NAYA-REPO-LOCK.md` · `NAYA-OS.md` · `docs/NAYA-NITRO-MODE.md`

### B. PRODUCT / EXPERIENCE
`docs/MAXESS-RESULTS-PRODUCT-SPEC.md` · `docs/NAYA-MAXESS-OPERATING-MANUAL.md` · relevant MAXESS design/page specs

### C. STATE / HISTORY
`docs/SOURCE-AND-MEMORY-MAP.md` · `docs/MAXESS-CHANGE-LEDGER.md` · baselines and candidate records

### D. ENGINEERING / TOOLS
`tools/` — deterministic builders, executors, and QA scripts. Inspect before using; never assume a tool exists because a document names it.

### E. AUTOMATION
`.github/workflows/` — GitHub Actions. Workflows must verify source integrity and QA; automation must never silently redefine product authority.

### F. DEPLOYMENT / RELEASE
`docs/DEPLOYMENT-CONTRACT.md` · `docs/RELEASE-CHECKLIST.md`

### G. ASSETS / REFERENCES
Root PDFs/images and approved asset registries are reference resources, not production source unless explicitly designated.

## Current implementation state
- Working artifact: `20260817 912am RESULTS PAGE CODE`
- Frozen baseline: `BASELINE-WORKING.html`
- Nitro guard: `tools/nitro_aaa_upgrade.py`
- Runtime authority: `window.MAXESS_RESULT`
- Current candidate state: UPDATED EDITED FILE / working branch; not automatically approved.

## Execution law
**READ → MAP → ESTABLISH STATE → SOURCE-LOCK → BASELINE → IMPLEMENT IN COHERENT BATCHES → BUILD → REFETCH → DIFF → STATIC QA → BEHAVIOR QA → OSCAR → REPAIR → RE-TEST → FREEZE → DELIVER.**

## Non-negotiable checks
- Never guess a path, branch, artifact, or authority.
- Never use conversation memory when repository evidence exists.
- Never create a competing renderer or result source.
- Never replace a complete working artifact with a tiny test renderer.
- Never call GitHub state “live.” Groove requires separate public verification.
- Every material failure must produce a root cause and, where practical, a durable guardrail.
- Final status must distinguish `IMPLEMENTED`, `VERIFIED`, `LIVE VERIFIED`, and `HUMAN REVIEW REQUIRED`.

## Product north star
**DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY**

MAXESS measures. The Results experience interprets. Naya guides. The report explains. The user leaves knowing where they are, why it matters, what to improve, and what to do next.
