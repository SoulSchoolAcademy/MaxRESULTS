# MAXESS Clean Repository — Source & Memory Map

## Purpose

This file prevents the new repository from inheriting the old repository's ambiguity.

## Current clean-repo roles

### Active execution path

- `NAYA-OS.md` — compact operating system for Naya/AI execution.
- `docs/NAYA-MAXESS-OPERATING-MANUAL.md` — practical working protocol.
- `docs/MAXESS-RESULTS-PRODUCT-SPEC.md` — consolidated product requirements.
- `docs/RELEASE-CHECKLIST.md` — release gate.
- Future canonical Results artifact — one clearly named production HTML source, established only after its baseline is imported and verified.

### Reference-only knowledge

The original `SoulSchoolAcademy/maxess` repository remains the historical knowledge base until migration is complete. Its `.naya` system contains governance, laws, product specifications, deployment contracts, asset registries, execution directives, memory, smart notes, and historical implementations.

Do not blindly copy every historical artifact into the active path.

## Knowledge classes

### A. Constitutional / execution law

Source files include:

- `00-UNDERSTANDING-FIRST.md`
- `01-PRIME-DIRECTIVE.md`
- `02-LAWS-AND-RULES.md`
- `03-SYSTEM-DESIGN-LAWS.md`
- `04-EXECUTION-PROCEDURE.md`
- `05-QUALITY-AND-OSCAR.md`
- `NAYA-GOVERNANCE.md`
- `NAYA-LAW.md`
- `NAYA-WORK-PROTOCOL.md`

These have been distilled into `NAYA-OS.md`.

### B. Results product specification

Primary sources include:

- `MAXESS-RESULTS-MASTER-INSTRUCTION-SET.md`
- `MAXESS-RESULTS-EXECUTION-DIRECTIVE-V16.md`
- `memory/08-MAXESS-RESULTS-MASTER-SPEC.md`
- `memory/15-MAXESS-10-STAR-RESULTS-EXPERIENCE.md`
- `memory/23-MAXESS-9-9-BUILD-BLUEPRINT.md`
- `memory/28-MAXESS-FINAL-RESULTS-BUILD-DIRECTIVE.md`

Durable product requirements are consolidated into `docs/MAXESS-RESULTS-PRODUCT-SPEC.md`.

Where older documents conflict with the current approved baseline or explicit current user requirements, the current state must be reconciled deliberately rather than copied blindly.

### C. Source/state/deployment governance

Primary sources include:

- `RESULTS-SOURCE-REGISTRY.md`
- `REPOSITORY-OPERATING-MAP.md`
- `GROOVE-DEPLOYMENT-CONTRACT.md`
- `MAXESS-RESULTS-EXECUTION-LOCK.md`
- `MAXESS-RESULTS-SPAGHETTI-PREVENTION-AMENDMENT.md`
- `MAXESS-AAA-DELIVERY-MANIFEST.md`
- `smart-notes/2026-08-16-execution-flow-law.md`

The new repo's operating model incorporates their durable lessons:

1. one authoritative path;
2. explicit baseline/candidate states;
3. write → refetch → diff;
4. no tiny replacement when a complete artifact is required;
5. GitHub change ≠ Groove publication;
6. repeated failures must change the system;
7. complete upstream work even when external publishing is unavailable.

### D. Assets

`MAXESS-RESULTS-ASSET-REGISTRY.md` is the reference for approved Naya/brand assets. Do not substitute random portraits or logos when an approved asset exists.

### E. Historical implementation artifacts

Files such as:

- `MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V2.html` through V6;
- `MAXESS-RESULTS-NAYA-EXPERIENCE-FRAGMENT.html`;
- `maxess-results-v14-personalization.py`;
- `maxess-results-v15-polish.py`;
- `maxess-results-v15-reconstruction.py`;
- older 9.x/10.x Results HTML files;
- duplicate Groove embeds;
- old standalone `results` renderers;

are historical evidence, not active source. Reuse only after inspecting the implementation and proving it is better/compatible with the current architecture.

## Migration rule

The new repository should eventually contain:

```text
ONE canonical Results source
+ compact governance
+ product specification
+ source/state registry
+ deployment contract
+ asset registry
+ QA/release checks
+ durable lessons
```

It should NOT contain:

```text
many competing FINAL files
many patch renderers
old generated duplicates
mystery loaders
unclassified experiments
```

## Current migration status

- Clean repository created: YES
- Governance distilled: YES
- Product spec distilled: YES
- Release gate established: YES
- Historical knowledge mapped: YES
- Canonical production HTML migrated: NOT YET
- Canonical production baseline verified: NOT YET
- V21 implementation in clean repo: NOT YET

This explicit state is intentional. The clean repository must never pretend that the production source has been migrated before it actually has.
