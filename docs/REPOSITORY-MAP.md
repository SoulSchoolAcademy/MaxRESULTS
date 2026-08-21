# MAXESS / NAYA — REPOSITORY MAP

## Purpose
This is the execution map for AI and humans. Read this after `START-HERE.md` and before consequential work. It prevents source confusion, stale-file selection, duplicated systems, missed QA, semantic guessing, and fragmented memory.

## Canonical identity
- Repository: `SoulSchoolAcademy/MaxRESULTS`
- Governance/reference branch: `main`
- Active Results engineering branch: `maxess-results-v21-working`
- Legacy repository: `SoulSchoolAcademy/maxess` — reference only unless explicitly requested.

**Important:** `main` is authoritative for governance and repository operating rules. The active Results branch is the working engineering state. Neither branch is automatically a human-approved product baseline merely because it exists.

## Canonical MAXESS Results domain
**OFFICIAL PRODUCTION/PUBLIC RESULTS TARGET:** `https://results.nayanet.app/`

`.xyz` is obsolete for the MAXESS Results production target. Every AI, agent, developer, prompt, governance document, deployment instruction, Results navigation reference, redirect, or embed identifying the MAXESS Results public target MUST use `results.nayanet.app`.

Do not perform a blanket replacement of unrelated `.xyz` domains. This rule applies specifically to the MAXESS Results target.

The durable decision is recorded in `docs/smart-notes/2026/08/2026-08-21-canonical-results-app-domain.md` and the deployment boundary is governed by `docs/DEPLOYMENT-CONTRACT.md`.

## Canonical cold-start read order
1. `START-HERE.md` — entry law and activation.
2. `.naya/NAYA-LAW-SYSTEM-PROTOCOL.md` — mandatory execution-integrity protocol and Pre-Action Gate.
3. `docs/REPOSITORY-MAP.md` — this navigation, category, state, and authority map.
4. `NAYA-OS.md` — governing operating laws.
5. `docs/NAYA-LANGUAGE-DICTIONARY.md` — exact project language definitions.
6. `docs/NAYA-SCORECARDING-SYSTEM.md` — general scorecard method and artifact templates.
7. `docs/NAYA-GOVERNANCE-REGISTRY.md` — ownership of recurring governance subjects and duplicate-authority repair.
8. `docs/NAYA-EXECUTIVE-PLAN.md` — North Star, what/why/how, quality hierarchy, human/Naya relationship, and automatic next-action law.
9. `docs/NAYA-NITRO-MODE.md` — execution loop, batching, QA, resistance, and release discipline.
10. `docs/NAYA-EXECUTION-PROMPT-TEMPLATE.md` — reusable master execution contract.
11. `docs/NAYA-SMART-NOTES-SYSTEM.md` — durable memory, aliases, searchability, timestamps, promotion rules, and recall.
12. `docs/NAYA-NITRO-MASTER-BLUEPRINT.md` — Naya Nitro product thesis and user model.
13. `docs/NAYA-MAXESS-OPERATING-MANUAL.md` — practical MAXESS Results operating rules.
14. `docs/MAXESS-RESULTS-PRODUCT-SPEC.md` — current Results product requirements.
15. `docs/SOURCE-AND-MEMORY-MAP.md` — authority, state, and historical lineage.
16. `docs/DEPLOYMENT-CONTRACT.md` — GitHub → Groove → public verification.
17. `docs/RELEASE-CHECKLIST.md` — release gate.
18. `docs/NAYA-NITRO-LEARNING-LOG.md` — durable execution-system lessons when relevant.
19. `docs/smart-notes/INDEX.md` — Smart Note/Naya Note retrieval index.
20. `docs/NAYA-LEAD-EXECUTION-COMMUNICATION-PROTOCOL.md` — mandatory lead-mode communication standard.
21. **If E02 is active:** `docs/MAXESS-E02-EXECUTION-LOCK.md` — mandatory E02 source, scope, visual, self-review, and stop-send contract.
22. Read only additional task-specific documents, scorecards, exemplars, assets, and Smart Notes required by the request.

This read order is intentionally identical to `START-HERE.md`. If the two documents disagree, repair the documentation rather than inventing a third authority.

## NAYA LAW
`.naya/NAYA-LAW-SYSTEM-PROTOCOL.md` is the mandatory execution-integrity layer. It governs consequential MAXESS/Naya/Naya Nitro work and defines the Pre-Action Gate, truth-before-action rule, best-interest rule, source lock, baseline, preservation, verification, regression, Oscar, failure recovery, learning, completion, and stop conditions.

Core rule:

**DO NOT ACT UNTIL YOU UNDERSTAND WHAT YOU ARE ACTING ON, WHY YOU ARE ACTING, WHAT MUST BE PRESERVED, AND HOW SUCCESS WILL BE PROVEN.**

## Terminology aliases
- **Naya Note = Smart Note = durable Naya memory**
- **Max Results / MAX results / MAXESS Results → MaxRESULTS** when referring to this project.
- **Nitro Mode / Naya Nitro Mode → Naya Nitro execution system**.
- **Take the Lead → delegated planning/execution mode; human retains final authority.**
- **AAA → highest practical quality standard for the intended outcome and evidence available.**
- **10/10 → exceptional fitness for purpose with no known material weakness within evaluated scope/evidence.**
- **Scorecard → explicit, weighted, evidence-based evaluation and improvement process.**

## Categories
### GOVERNANCE / EXECUTION
`.naya/NAYA-LAW-SYSTEM-PROTOCOL.md` · `NAYA-OS.md` · `docs/NAYA-LANGUAGE-DICTIONARY.md` · `docs/NAYA-SCORECARDING-SYSTEM.md` · `docs/NAYA-GOVERNANCE-REGISTRY.md` · `docs/NAYA-EXECUTIVE-PLAN.md` · `docs/NAYA-NITRO-MODE.md` · `docs/NAYA-EXECUTION-PROMPT-TEMPLATE.md` · `docs/MAXESS-SECTION-BUILD-LAW.md` · `docs/MAXESS-SECTION-INTEGRITY-GATE.md` · task-specific execution locks.

### MEMORY / LEARNING
`docs/NAYA-SMART-NOTES-SYSTEM.md` · `docs/NAYA-NITRO-LEARNING-LOG.md` · `docs/smart-notes/` — durable Naya Notes / Smart Notes. These preserve learning and context but do not automatically become product law.

### QUALITY / REFERENCES
`docs/NAYA-SCORECARDING-SYSTEM.md` owns general evaluation method. HMC knowledge, approved logos, QMAX/operating-system material, Naya assistant assets, and other designated reference assets are exemplars when explicitly identified; an exemplar informs quality but does not automatically become authority for unrelated artifacts.

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
3. `.naya/NAYA-LAW-SYSTEM-PROTOCOL.md` and `NAYA-OS.md` governing Nitro rules.
4. Current product specification / explicit design directive for the task.
5. Human-approved baseline/candidate state, when one is explicitly identified.
6. Historical notes, learning records, old repositories, and prior implementations.
7. Engineering convenience.

A Smart Note records durable knowledge; it is **not** automatically governance. Promote a lesson deliberately when it becomes a system law.

A working branch, commit, or newer file is **not** automatically an approved baseline.

## Current state
- Governance/reference branch: `main`.
- Active Results engineering branch: `maxess-results-v21-working` exists and is the current working branch for Results engineering.
- **Current public verification target: `https://results.nayanet.app/`.**
- Production/public parity is a separate verification state from GitHub.
- Human-approved AAA baseline: **NOT YET ESTABLISHED for the fresh Section 01 build**.

Do not call any artifact “authoritative production” merely because it is large, current, committed, or visually improved. The only protected element explicitly established by the current Section 01 work is the existing Orb behavior/visual system where the user has said it is approved for preservation.

## Execution law
**GITHUB FIRST → NAYA LAW → READ → MAP → ESTABLISH STATE → SOURCE-LOCK → BASELINE → PLAN → IMPLEMENT IN COHERENT BATCHES → BUILD → REFETCH → DIFF → STATIC QA → BEHAVIOR QA → SCORECARD → OSCAR → REPAIR → RE-VALIDATE → LEARN → FREEZE → DELIVER → NEXT ACTION.**

## Non-negotiables
- Never guess a path, branch, artifact, authority, configuration, or command.
- Never act consequentially before the mandatory Naya Law Pre-Action Gate is satisfied.
- Never use conversation memory when repository evidence exists.
- Never create competing renderers or result sources.
- Never replace a complete working artifact with a tiny test renderer.
- Never call GitHub state live; Groove requires separate public verification.
- Every material failure should produce a root cause and, where practical, a durable guardrail.
- Durable learning should be captured as a Naya Note / Smart Note using the documented structure.
- A Naya Note is not automatically product law; promote durable rules deliberately into governance documents.
- Every consequential execution should end with the next likely action and a copy-and-paste-ready execution prompt.
- Final status must distinguish `IMPLEMENTED`, `VERIFIED`, `LIVE VERIFIED`, `HUMAN REVIEW REQUIRED`, `BLOCKED`, and `UNKNOWN`.

## Product north star
**DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY**

## Naya Nitro north star
**VISION → UNDERSTANDING → RECOMMENDATION → EXECUTION → VERIFICATION → LEARNING → BETTER FUTURE EXECUTION**
