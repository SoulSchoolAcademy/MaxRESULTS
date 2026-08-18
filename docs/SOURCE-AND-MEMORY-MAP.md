# MAXESS Results — Source & Memory Map

## Purpose

This file prevents repository ambiguity by distinguishing current authority, durable memory, historical evidence, and obsolete migration statements.

## Current active roles

### A. Governance / execution

- `NAYA-OS.md` — governing AI execution and product laws.
- `START-HERE.md` — mandatory entry point and execution sequence.
- `NAYA-REPO-LOCK.md` — repository/branch/source-selection lock.
- `docs/NAYA-NITRO-MODE.md` — execution and QA method.

### B. Product / experience

- `docs/MAXESS-RESULTS-PRODUCT-SPEC.md` — consolidated current product requirements.
- `docs/NAYA-MAXESS-OPERATING-MANUAL.md` — practical Results operating rules.
- Relevant current design, section, QA, and implementation specifications identified by `docs/REPOSITORY-MAP.md`.

### C. Source / state / release

- `20260817 912am RESULTS PAGE CODE` — current V21 working artifact on the active branch.
- `BASELINE-WORKING.html` — frozen working baseline.
- `docs/MAXESS-CHANGE-LEDGER.md` — material requirement and state ledger.
- `docs/DEPLOYMENT-CONTRACT.md` — GitHub → Groove → public verification contract.
- `docs/RELEASE-CHECKLIST.md` — release gate.

### D. Durable memory / learning

- `docs/SMART-NOTES.md` — Smart Notes protocol, schema, capture law, retrieval law, and precedence.
- `docs/smart-notes/INDEX.md` — searchable retrieval index.
- `docs/smart-notes/YYYY-MM-DD.md` — chronological durable-learning entries.

Smart Notes preserve valuable project learning from conversations and executions. They are memory, not authority. Current authoritative repository files outrank them.

### E. Engineering / automation

- `tools/` — deterministic builders, executors, and QA scripts.
- `.github/workflows/` — repository integrity and QA automation.

### F. Assets / references

Approved asset registries and reference packs are authoritative only within their documented scope. Random or historical substitutes must not silently become production assets.

## Historical knowledge

The original `SoulSchoolAcademy/maxess` repository remains reference-only unless explicitly requested. Historical governance, memory, smart notes, product specifications, and implementations have informed the clean repository but must not be treated as current source merely because they are older or more extensive.

When a historical lesson remains useful, preserve the durable lesson in current Smart Notes or governance rather than importing an entire obsolete system.

## Knowledge precedence

When sources disagree, use this order:

1. Truth, safety, and platform constraints.
2. Explicit current human requirements.
3. Current governance / execution law.
4. Current product specification and approved source-of-truth records.
5. Current verified baseline / working artifact evidence.
6. Smart Notes and historical records as contextual memory.
7. Engineering convenience.

A Smart Note never silently overrides current source truth.

## Current state — 2026-08-18

- Canonical repository: YES — `SoulSchoolAcademy/MaxRESULTS`
- Active Results branch: YES — `maxess-results-v21-working`
- Governance distilled: YES
- Product specification present: YES
- Release gate present: YES
- V21 implementation present: YES
- Working artifact present: YES
- Frozen baseline present: YES
- Smart Notes system: YES — repository-local and indexed
- Browser rendering verification: NOT YET VERIFIED
- Groove/live parity verification: NOT YET VERIFIED
- Final AAA product quality: NOT YET VERIFIED

Do not reuse the old migration-status language that says the V21 implementation or canonical production HTML is absent. That was an obsolete clean-repo migration statement and is no longer current truth.

## Migration / cleanup rule

The active path should converge toward:

```text
ONE authoritative Results source
+ compact governance
+ current product specification
+ explicit state/lineage
+ durable indexed memory
+ QA/release automation
+ deployment contract
+ validated assets
```

It should not converge toward:

```text
many competing FINAL files
many patch renderers
old generated duplicates
mystery loaders
unclassified experiments
orphan memory notes
```
