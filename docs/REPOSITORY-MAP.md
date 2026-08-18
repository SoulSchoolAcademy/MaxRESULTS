# MAXESS / NAYA — REPOSITORY MAP

## Purpose
This is the execution map for AI and humans. Read this after `START-HERE.md` and before consequential work. It prevents source confusion, stale-file selection, duplicated systems, missed QA, and fragmented memory.

## Canonical identity
- Repository: `SoulSchoolAcademy/MaxRESULTS`
- Governance/reference branch: `main`
- Active Results engineering branch: `maxess-results-v21-working`
- Legacy repository: `SoulSchoolAcademy/maxess` — reference only unless explicitly requested.

**Important:** `main` is authoritative for governance and repository operating rules. The active Results branch is the working engineering state. Neither branch is automatically a human-approved product baseline merely because it exists.

## Canonical cold-start read order
1. `START-HERE.md` — entry law and activation.
2. `docs/REPOSITORY-MAP.md` — this navigation, category, state, and authority map.
3. `NAYA-OS.md` — governing operating laws.
4. `docs/NAYA-EXECUTIVE-PLAN.md` — North Star, what/why/how, quality hierarchy, human/Naya relationship, and automatic next-action law.
5. `docs/NAYA-NITRO-MODE.md` — execution loop, batching, QA, resistance, and release discipline.
6. `docs/NAYA-EXECUTION-PROMPT-TEMPLATE.md` — reusable master execution contract.
7. `docs/NAYA-SMART-NOTES-SYSTEM.md` — durable memory, aliases, searchability, timestamps, promotion rules, and recall.
8. `docs/NAYA-NITRO-MASTER-BLUEPRINT.md` — Naya Nitro product thesis and user model.
9. `docs/NAYA-MAXESS-OPERATING-MANUAL.md` — practical MAXESS Results operating rules.
10. `docs/MAXESS-RESULTS-PRODUCT-SPEC.md` — current Results product requirements.
11. `docs/SOURCE-AND-MEMORY-MAP.md` — authority, state, and historical lineage.
12. `docs/DEPLOYMENT-CONTRACT.md` — GitHub → Groove → public verification.
13. `docs/RELEASE-CHECKLIST.md` — release gate.
14. `docs/NAYA-NITRO-LEARNING-LOG.md` — durable execution-system lessons when relevant.
15. `docs/smart-notes/INDEX.md` — Smart Note/Naya Note retrieval index.
16. Read only additional task-specific documents and Smart Notes required by the request.

This read order is intentionally identical to `START-HERE.md`. If the two documents disagree, repair the documentation rather than inventing a third authority.

## Terminology aliases
- **Naya Note = Smart Note = durable Naya memory**
- **Max Results / MAX results / MAXESS Results → MaxRESULTS** when referring to this project.
- **Nitro Mode / Naya Nitro Mode → Naya Nitro execution system**.
- **Take the Lead → delegated planning/execution mode; human retains final authority.**

## Categories
### GOVERNANCE / EXECUTION
`NAYA-OS.md` · `docs/NAYA-EXECUTIVE-PLAN.md` · `docs/NAYA-NITRO-MODE.md` · `docs/NAYA-EXECUTION-PROMPT-TEMPLATE.md` · repository entry/map documents.

### MEMORY / LEARNING
`docs/NAYA-SMART-NOTES-SYSTEM.md` · `docs/NAYA-NITRO-LEARNING-LOG.md` · `docs/smart-notes/` — durable Naya Notes / Smart Notes. These preserve learning and context but do not automatically become product law.

### PRODUCT / EXPERIENCE
`docs/MAXESS-RESULTS-PRODUCT-SPEC.md` · `docs/NAYA-MAXESS-OPERATING-MANUAL.md` · relevant MAXESS design/page specifications.

### STATE / HISTORY
`docs/SOURCE-AND-MEMORY-MAP.md` · `docs/MAXESS-CHANGE-LEDGER.md` when present · baselines/candidate records.

### ENGINEERING / TOOLS
`tools/` — builders, executors, deterministic transforms, and QA scripts. Inspect before use; never assume a named tool exists.

### AUTOMATION
`.github/workflows/` — GitHub Actions. Automation verifies and guards; it must never silently redefine product authority.

### DEPLOYMENT / RELEASE
`docs/DEPLOYMENT-CONTRACT.md` · `docs/RELEASE-CHECKLIST.md`.

### ASSETS / REFERENCES
Root PDFs/images and approved asset registries are reference resources unless explicitly designated production.

## Authority hierarchy
Use this hierarchy to resolve competing information:

1. Truth, safety, and platform/tool constraints.
2. Explicit current human requirements.
3. `NAYA-OS.md` and governing Nitro rules.
4. Current product specification / explicit design directive for the task.
5. Human-approved baseline/candidate state, when one is explicitly identified.
6. Historical notes, learning records, old repositories, and prior implementations.
7. Engineering convenience.

A Smart Note records durable knowledge; it is **not** automatically governance. Promote a lesson deliberately when it becomes a system law.

A working branch, commit, or newer file is **not** automatically an approved baseline.

## Current state
- Governance/reference branch: `main`.
- Active Results engineering branch: `maxess-results-v21-working` exists and is the current working branch for Results engineering.
- Current public verification target: `https://results.nayanet.xyz/`.
- Production/public parity is a separate verification state from GitHub.
- Human-approved AAA baseline: **NOT YET ESTABLISHED for the fresh Section 01 build**.

Do not call any artifact “authoritative production” merely because it is large, current, committed, or visually improved. The only protected element explicitly established by the current Section 01 work is the existing Orb behavior/visual system where the user has said it is approved for preservation.

## Execution law
**GITHUB FIRST → READ → MAP → ESTABLISH STATE → SOURCE-LOCK → BASELINE → PLAN → IMPLEMENT IN COHERENT BATCHES → BUILD → REFETCH → DIFF → STATIC QA → BEHAVIOR QA → OSCAR → REPAIR → RE-VALIDATE → LEARN → FREEZE → DELIVER → NEXT ACTION.**

## Non-negotiables
- Never guess a path, branch, artifact, or authority.
- Never use conversation memory when repository evidence exists.
- Never create competing renderers or result sources.
- Never replace a complete working artifact with a tiny test renderer.
- Never call GitHub state live; Groove requires separate public verification.
- Every material failure should produce a root cause and, where practical, a durable guardrail.
- Durable learning should be captured as a Naya Note / Smart Note using the documented structure.
- A Naya Note is not automatically product law; promote durable rules deliberately into governance documents.
- Every consequential execution should end with the next likely action and a copy-paste-ready execution prompt.
- Final status must distinguish `IMPLEMENTED`, `VERIFIED`, `LIVE VERIFIED`, `HUMAN REVIEW REQUIRED`, and `UNKNOWN`.

## Product north star
**DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY**

## Naya Nitro north star
**VISION → UNDERSTANDING → RECOMMENDATION → EXECUTION → VERIFICATION → LEARNING → BETTER FUTURE EXECUTION**
