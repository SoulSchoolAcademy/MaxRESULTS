# NAYA NITRO — GOVERNANCE REGISTRY

**Purpose:** Make ownership explicit so multiple useful documents do not accidentally become competing authorities.

**Rule:** A document may be valuable without being authoritative. Authority is assigned by subject.

## Canonical owners

| Subject | Canonical owner | Supporting material | Authority status |
|---|---|---|---|
| Repository entry / cold start | `START-HERE.md` | active branch START-HERE | CANONICAL |
| Repository navigation / authority map | `docs/REPOSITORY-MAP.md` | active branch map | CANONICAL |
| Core operating laws | `NAYA-OS.md` | Nitro protocols | GOVERNING |
| **Naya intelligence / reasoning / judgment / problem-solving / verification / learning / useful-action behaviour** | **`docs/NAYA-BRAIN-MASTER-ACTIVATION-SPECIFICATION.md`** | Naya OS, Nitro protocols, Smart Notes, specialist role documents | **CANONICAL BRAIN SPECIFICATION — OFFICIAL 22 AUGUST 2026** |
| **Naya Notes / Smart Notes / durable memory system behaviour** | **`docs/NAYA-NOTES-MASTER-ACTIVATION-SPECIFICATION.md`** | `docs/NAYA-SMART-NOTES-SYSTEM.md`, `docs/smart-notes/`, Learning Log | **CANONICAL NAYA NOTES SPECIFICATION — OFFICIAL 22 AUGUST 2026** |
| **Naya personality / character / voice / relationship behaviour** | **`docs/NAYA-PERSONALITY-MANUSCRIPT-ACTIVATION-PROTOCOL.md`** | Naya Digital Codex, personality exemplars, Awesome Trait Standard | **GOVERNING PERSONALITY SPECIFICATION — HUMAN APPROVED 21 AUGUST 2026** |
| Lead execution / excellence / communication | `docs/NAYA-LEAD-EXECUTION-COMMUNICATION-PROTOCOL.md` | `NAYA-OS.md`, Naya Law, Nitro protocols | GOVERNING LAW |
| Project language / definitions | `docs/NAYA-LANGUAGE-DICTIONARY.md` | branch-local language docs | GOVERNING |
| General scorecarding method | `docs/NAYA-SCORECARDING-SYSTEM.md` | artifact-specific scorecards | GOVERNING |
| Executive North Star / what-why-how | `docs/NAYA-EXECUTIVE-PLAN.md` | Blueprint / Smart Notes | GOVERNING |
| Nitro execution behavior | `docs/NAYA-NITRO-MODE.md` | root/branch Nitro protocols | GOVERNING |
| Reusable execution prompt | `docs/NAYA-EXECUTION-PROMPT-TEMPLATE.md` | older prompt templates | CANONICAL |
| Naya Nitro product thesis | `docs/NAYA-NITRO-MASTER-BLUEPRINT.md` | related product docs | PRODUCT REFERENCE |
| MAXESS Results operating rules | `docs/NAYA-MAXESS-OPERATING-MANUAL.md` | task-specific docs | PRODUCT OPERATING |
| MAXESS Results requirements | `docs/MAXESS-RESULTS-PRODUCT-SPEC.md` | design directives | PRODUCT REQUIREMENTS |
| **Master Designer + Master Coder quality laws** | **`docs/NAYA-MASTER-DESIGN-CODER-LAWS.md`** | HMC/QMAX reference assets; task-specific design specs | **GOVERNING QUALITY LAW** |
| MAXESS section build/integrity law | `docs/MAXESS-SECTION-BUILD-LAW.md` + `docs/MAXESS-SECTION-INTEGRITY-GATE.md` | section-specific locks | GOVERNING |
| Active E02 execution lock | `docs/MAXESS-E02-EXECUTION-LOCK.md` | E02 section contract | CANONICAL TASK GUARDRAIL |
| Source/state/history | `docs/SOURCE-AND-MEMORY-MAP.md` | change ledger / notes | STATE AUTHORITY |
| Deployment truth | `docs/DEPLOYMENT-CONTRACT.md` | release checklist | DEPLOYMENT AUTHORITY |
| Release gate | `docs/RELEASE-CHECKLIST.md` | QA tooling | RELEASE AUTHORITY |
| Durable learning log | `docs/NAYA-NITRO-LEARNING-LOG.md` | Smart Notes | LEARNING RECORD |
| Smart Note retrieval | `docs/smart-notes/INDEX.md` | individual notes | RETRIEVAL INDEX |

## Brain authority law

`docs/NAYA-BRAIN-MASTER-ACTIVATION-SPECIFICATION.md` is the **canonical owner for Naya Brain**: intelligence, contextual reasoning, discernment, judgment, decision-making, problem ownership, problem-solving, persistence, preservation, verification, failure recovery, learning, strategic/creative/leveraged thinking, human-time protection, and useful-action behaviour.

When another document contains Brain-related rules, it is supporting material unless this registry explicitly assigns it authority for a different subject. If Brain-related rules conflict, the Brain specification governs the Brain subject after accounting for higher-priority system, safety, platform, permission, and explicit current human requirements.

`NAYA-OS.md` remains the broader project operating law. It governs the overall operating system and execution environment; it is **not a competing Brain specification**. Where Brain-specific detail is needed, use the canonical Brain document.

## Naya Notes authority law

`docs/NAYA-NOTES-MASTER-ACTIVATION-SPECIFICATION.md` is the **canonical owner for Naya Notes / Smart Notes system behaviour**: durable memory activation, capture, classification, searchability, recall, status, supersession, conflict handling, memory-versus-governance boundaries, automatic durable capture, learning loops, and Naya Notes operating behaviour.

This specification **supersedes any older or competing document that claims to define the Naya Notes / Smart Notes system itself**. Older individual notes remain historical evidence unless explicitly marked `SUPERSEDED`; they are not deleted merely because the system specification changed.

`docs/NAYA-SMART-NOTES-SYSTEM.md` remains valuable supporting material and historical system documentation. It does not compete with the canonical Naya Notes activation specification. Where the two conflict on Naya Notes system behaviour, the canonical activation specification governs.

`docs/smart-notes/INDEX.md` is the retrieval/navigation layer, not an authority layer. Individual dated notes preserve evidence, decisions, discoveries, and historical context; they do not override the canonical system specification or higher-priority governing rules merely because they are newer.

## Supporting-document rule

Documents not listed as canonical owners above may still be used when directly relevant, but they do not override the canonical owner for the subject they discuss.

Examples include older AI language documents, AI definition-of-10 documents, fast-edit scorecards, execution prompt templates, design directives, build protocols, Nitro operating variants, branch-local contracts, historical change reports, and older Smart Notes system documents.

When a supporting document contains a rule useful enough to become permanent, do not silently promote it. Extract the rule, compare it against the canonical owner, consolidate it there if appropriate, and preserve the supporting document as historical/reference material unless it is proven obsolete and safe to remove.

## Duplicate-authority repair law

When a fresh AI discovers two documents that appear to govern the same subject:

1. consult this registry;
2. identify the canonical owner;
3. compare the competing documents for useful differences;
4. determine whether the difference is current, historical, implementation-specific, or contradictory;
5. repair the canonical owner if a missing durable rule is discovered;
6. mark or bridge the duplicate so future AIs do not treat it as independent authority;
7. do not delete historical material merely to make the tree look clean;
8. re-run the cold-start test.

## Branch authority

`main` is the governance/reference branch.

`maxess-results-v21-working` is the active Results engineering branch.

The active branch may contain implementation-specific documents and older directives. It must route back to `main` for governance. Branch divergence does not transfer governance authority.

## Approval authority

The Naya Personality Manuscript was explicitly approved by the project owner on 21 August 2026. The Naya Brain Master Activation Specification was established as the canonical Brain/intelligence authority on 22 August 2026. The Naya Notes Master Activation Specification was established as the canonical Naya Notes/durable-memory authority on 22 August 2026. These approvals govern their respective subjects only and do not override higher-priority system, safety, platform, permission, or repository laws.

## Promotion rule

A rule moves through this path:

**OBSERVATION → LEARNING → CANDIDATE RULE → GOVERNANCE REVIEW → CANONICAL OWNER → VERIFIED USE**

The Naya Personality Manuscript has completed governance review and human approval. The Naya Brain specification is the canonical Brain authority. The Naya Notes specification is the canonical durable-memory-system authority. Runtime behavioural activation remains subject to platform capability and verification.
