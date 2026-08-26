# MAXESS — Execution Log / AI Handoff Feed

**Project:** MAXESS  
**Canonical repository:** `SoulSchoolAcademy/NayaPOWER`  
**Branch:** `main`  
**Purpose:** Persistent, append-style project continuity so the next AI does not repeat failed approaches or lose the current diagnostic state.

---

## 2026-08-26 — V2 Master Engineering Directive Locked

### Decision
MAXESS V2 is now the active master engineering/design execution standard. V1 remains preserved as lineage.

The rebuild is explicitly moving away from isolated E00/E00.01/E00.02/E00.03 patching as the default strategy.

### Architectural target

**ONE MAXESS APPLICATION → ONE AUTHORITATIVE STATE MACHINE → ONE ASSESSMENT DEFINITION / COMPILER → ONE SCORING ENGINE → ONE VALIDATED `MAXESS_RESULT_V1` CONTRACT → ONE RELEASE PATH → E01–E09 PRESENTATION.**

E00 owns assessment state, completion, scoring, result construction, and result release. E01–E09 remain the nine canonical Results sections and consume the same authoritative result contract.

### Golden assessment
AI Score remains the golden reference: 15 questions, five answers per question, answer values 0–4, five dimensions, deterministic scoring, normalized 0–100 result.

### Dynamic platform direction
The same engine is to become a deterministic, knowledge-driven assessment compiler for supported AI-and-life topics without a mandatory paid runtime LLM API.

**TOPIC → DOMAIN/COVERAGE → KNOWLEDGE → LEARNING OBJECTIVES → CAPABILITIES → QUESTION ARCHETYPES → 0–4 RUBRIC → 15 QUESTIONS → VALIDATE → RUN.**

Advanced topics may be supported when coverage is sufficient. Unsupported or weakly covered topics must be handled honestly.

### Flagship design direction
MAXESS is to be treated as a flagship product: fast, simple, precise, warm, high-tech, premium, alive, accessible, responsive, and resilient. Primary controls are signature jewel-like interactions with intentional material, depth, lighting, motion, and tactile states. Naya is a present human-centered guide, not decoration.

### Execution truth model

```text
🟢 GREEN = implemented AND verified by evidence
🟡 YELLOW = implemented but verification incomplete/ambiguous
🔴 RED = not implemented OR not verified
```

Code existence is not green.

### Smart Note / receipt rule
Meaningful project work must preserve human-readable continuity, AI handoff, canonical event data, verification receipt, current state, and next execution. Human-readable notes are the default human-facing receipt; JSON is optional machine infrastructure.

### Current work performed

- Located and read the canonical Naya Power repository.
- Read the Naya Power README and current governing architecture.
- Read the MAXESS project hub.
- Read the existing MAXESS V1 master directive.
- Read the existing MAXESS execution log.
- Confirmed repository source lineage includes E00 variants, E00.01–E00.03, E01–E09, MAXIS, result bridges, workflows, Smart Note infrastructure, and MAXESS documentation.
- Created `PROJECTS/MAXESS/MAXESS-MASTER-ENGINEERING-DESIGN-DIRECTIVE-V2.md`.
- Updated `PROJECTS/MAXESS/README.md` to make V2 canonical for active execution.
- Created the human-readable V2 Smart Note.
- Created the AI-facing V2 Smart Note.
- Created the canonical V2 Note Event.
- Created the human-readable V2 verification receipt.
- Created the next-execution source/architecture inventory prompt.

### Current status

**DIRECTIVE:** 🟢 GREEN  
**PROJECT HUB:** 🟢 GREEN  
**SMART NOTE + AI NOTE:** 🟢 GREEN  
**HUMAN RECEIPT:** 🟢 GREEN  
**APPLICATION REBUILD:** 🔴 NOT YET VERIFIED  
**LIVE END-TO-END:** 🔴 NOT YET VERIFIED  
**10/10:** 🔴 NOT YET VERIFIED

### Next execution

`PROJECTS/MAXESS/NEXT-EXECUTION-MAXESS-V2-SOURCE-ARCHITECTURE-INVENTORY-2026-08-26.md`

First perform the complete source/architecture inventory. Then establish the unified state/scoring/result map and implement the highest-leverage coherent changes. Do not add another isolated E00 patch unless the inventory and evidence demonstrate that it is the correct architectural action.

---

## 2026-08-26 — Initial Canonical Diagnostic Entry

### Objective
Determine why the MAXESS assessment has not reached a working score/results state after multiple repair attempts, and establish a project memory system that makes every subsequent attempt cumulative rather than repetitive.

### User-observed symptoms

1. Selecting Continue does not visibly advance the assessment as expected.
2. The page may eventually appear to attempt loading, but the intended Results transition does not complete.
3. Four Results blocks have been observed appearing early (`E04`, `E07`, `E08`, `E09`).
4. Results should remain hidden until the assessment is complete and the score has been calculated.
5. The expected final path is E00 assessment → result calculation → E01/E02/E03/E04 Results.

### Repository inspection performed

The repository and the exact user-specified artifact names were checked directly.

### Major discovery

There is a **material source mismatch** inside the repository:

- `E00 118` is currently only a minimal `#maxess-ai-score` shell. It does not contain the actual assessment engine, questions, score matrix, Continue logic, `calculate()`, `buildResult()`, or `publish()`.
- `E00 796` contains the actual assessment engine and the complete terminal scoring/handoff path.

This is the strongest current explanation for the reported behavior if the live embed is using `E00 118`.

### Important source evidence

`E00 796` currently contains:

- `validate()` for 15 questions / 5 dimensions / 15×5 score matrix;
- `save()`;
- `calculate()`;
- `buildResult()`;
- `valid()`;
- `persistResult()`;
- `broadcast()`;
- `renderLocalResults()`;
- `verifyLocalResults()`;
- `releaseResultsSections()`;
- `attemptResultsHandoff()`;
- `publish()`;
- hardened Continue execution;
- `MAXESS_E00_DIAGNOSTICS`.

The score engine is therefore present in source. The missing proof is whether that source is the artifact actually being used by the failing/live assessment.

### Bridge findings

`E00.01` validates `MAXESS_RESULT_V1` and expects:

- overall score 0–100;
- exactly 5 dimensions;
- exactly 15 responses.

`E00.02` explicitly establishes a waiting state and hides E01–E09 until release.

`E00.03` validates the canonical result and coordinates the release event.

Therefore the early visibility of E04/E07/E08/E09 is inconsistent with the intended E00.02 boundary and should be treated as evidence that the isolation layer is not actually active in the failing composition, or that a competing/legacy composition is rendering those sections outside the guarded path.

### Additional concrete inconsistency

`E00 796` currently attempts external Results navigation to:

`results.nayanet.app`

while the `apply-maxess-result-bridge.yml` workflow's static bridge requirements include:

`results.nayanet.xyz`

This is a real configuration/source-generation inconsistency. It may not explain the initial score failure because E00 796 renders and verifies local results before attempting external navigation, but it must be reconciled before release.

---

## Approaches Already Tried / Do Not Blindly Repeat

### 1. Continue-boundary repair
A dedicated workflow exists for E00 796 Continue repair. The current source contains a hardened capture-phase boundary and nested-target handling.

**Conclusion:** Continue logic has been materially hardened in source. Do not perform another generic Continue rewrite until the actual runtime artifact is proven.

### 2. Score-matrix repair
The E00 796 workflow includes a correction for the score matrix guard. Current source validates that `S` is an object with 15 rows and 5 scores per row.

**Conclusion:** The source-level score matrix guard is substantially hardened. Runtime evidence is now more valuable than another blind guard rewrite.

### 3. Results bridge / hydration work
The repository contains multiple bridge, hydration, isolation, terminal, and handoff workflows.

**Conclusion:** The system has accumulated enough repair layers that source reconciliation is now higher leverage than adding another repair layer.

---

## Ranked hypotheses from prior diagnostic cycle

1. **Wrong E00 artifact / source mismatch (`E00 118` vs `E00 796`).**
2. **Live deployment/embedded page points at a different artifact than current `main`.**
3. **E00 796 is not the artifact wired into the production assessment.**
4. **E00.02 isolation code is not executing in the live composition.**
5. **Multiple generations of bridge/controller logic are coexisting.**
6. **Results handoff URL/configuration drift (`.app` vs `.xyz`).**
7. **Runtime failure inside `publish()` despite source implementation being present.**
8. **Runtime data/score-map mismatch despite static validation.**
9. **Event ordering / cross-window release issue.**
10. **External navigation obscures an otherwise successful local result.**

---

## Anti-Loop Rule

A future AI must not retry an approach already recorded as failed unless it can state:

1. what changed;
2. why the previous failure no longer applies;
3. what new evidence justifies the attempt;
4. what observable result will prove or disprove it.

**No new evidence = no repeated experiment.**

---

## Definition of Project Completion

MAXESS reaches project completion only after:

**SOURCE → ASSESSMENT → CONTINUE → SCORE → RESULT CONTRACT → RELEASE → RESULTS → LIVE → REGRESSION → OSCAR → FREEZE**

has been demonstrated with evidence.
