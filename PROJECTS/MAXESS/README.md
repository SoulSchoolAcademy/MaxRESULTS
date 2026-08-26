# PROJECT MAXESS — Canonical Project Hub

**Project:** MAXESS — AI Mastery Assessment / Results Engine  
**Repository:** `SoulSchoolAcademy/NayaPOWER`  
**Branch:** `main`  
**Status:** ACTIVE / ENGINE BLOCKED / SOURCE-RECONCILIATION REQUIRED  
**Created:** 2026-08-26  
**North Star:** Make the complete MAXESS journey reliably calculate the user's real result and release the correct Results experience, with no hidden source confusion and with every future AI able to restore the exact current state.

## 1. Immediate North Star

**E00 assessment → answer selection → Continue → 15 responses saved → score calculated → MAXESS_RESULT_V1 created → result validated → Results released → E01/E02/E03/E04 hydrate → live experience verified.**

The first engineering objective is not visual polishing. It is proving the terminal result path works end-to-end.

## 2. Canonical Terminology

- Product name: **MAXESS**
- Assessment: **MAXESS AI Mastery Assessment**
- Main assessment artifact currently containing the full executable engine: **`E00 796`**
- `E00 118` currently exists but is only a minimal shell and is **not** a complete assessment engine.
- Bridge layers: **E00.01, E00.02, E00.03**
- Result sections: **E01–E09**
- Result contract: **`MAXESS_RESULT_V1`**

## 3. Critical Source Finding — 2026-08-26

The repository contains two materially different E00 artifacts.

### `E00 118`
Current content is only the `#maxess-ai-score` shell plus minimal CSS and closes immediately. It contains no question data, scoring matrix, `save()`, `calculate()`, `buildResult()`, `publish()`, or Continue execution path.

### `E00 796`
Current content contains the actual MAXESS assessment engine, including:

- 15-question structure validation;
- 5 dimensions;
- 15×5 score matrix validation;
- answer selection;
- response saving;
- score calculation;
- `MAXESS_RESULT_V1` construction;
- result validation;
- persistence;
- event broadcast;
- local result rendering;
- Results-section release;
- external Results handoff;
- hardened Continue boundary;
- diagnostics API.

**Therefore the first source-of-truth question is now explicit: which E00 artifact is actually embedded/deployed?** If the live assessment is using `E00 118`, the current observed Continue/scoring failure is immediately explained by a source/artifact mismatch.

## 4. Current Architecture

```text
E00 assessment
   ↓
E00.01 — result bridge / result validation
   ↓
E00.03 — results controller
   ↓
E00.02 — visual isolation / release gate
   ↓
E01 → E09 — Results experience
```

The intended result contract is `MAXESS_RESULT_V1`.

## 5. Relevant Artifacts

### Assessment / Engine
- [`E00 796`](../../E00%20796) — full executable assessment engine; highest-priority inspection target.
- [`E00 118`](../../E00%20118) — minimal shell; must be classified as shell/non-canonical unless deployment evidence proves otherwise.

### Bridge / Release
- [`E00.01`](../../E00.01) — validates the result contract and releases results when valid.
- [`E00.02`](../../E00.02) — hides E01–E09 until release and controls visual isolation.
- [`E00.03`](../../E00.03) — canonical results controller / release coordinator.

### Results
- [`E01`](../../E01) — score reveal.
- [`E02`](../../E02) — five dimensions.
- [`E03`](../../E03) — personal report.
- [`E04`](../../E04) — direction/capability spectrum.
- `E05`–`E09` — additional Results sections; inspect only after the terminal bridge is proven.

### Execution / Repair Workflows
- [`patch-e00-continue.yml`](../../.github/workflows/patch-e00-continue.yml) — hardened E00 796 Continue boundary and score-matrix repair.
- [`apply-maxess-result-bridge.yml`](../../.github/workflows/apply-maxess-result-bridge.yml) — deterministic Results bridge workflow.
- [`repair-e00-796-continue.yml`](../../.github/workflows/repair-e00-796-continue.yml) — E00 796 Continue repair workflow.
- [`repair-e00-results-handoff-v2.yml`](../../.github/workflows/repair-e00-results-handoff-v2.yml) — Results handoff repair.
- [`repair-e00-results-handoff.yml`](../../.github/workflows/repair-e00-results-handoff.yml) — earlier handoff repair.
- [`repair-e00-terminal-state.yml`](../../.github/workflows/repair-e00-terminal-state.yml) — terminal-state repair.
- [`maxess-result-hydration.yml`](../../.github/workflows/maxess-result-hydration.yml) — result hydration workflow.
- [`maxess-step3-diagnostic.yml`](../../.github/workflows/maxess-step3-diagnostic.yml) — diagnostic workflow.
- [`maxess-step3-runtime.yml`](../../.github/workflows/maxess-step3-runtime.yml) — runtime workflow.

## 6. Ranked Root-Cause Investigation

Rank is based on repository evidence plus the reported symptoms. This is a hypothesis ranking, not a claim that every item has been proven.

| Rank | Hypothesis | Why it matters | Status |
|---:|---|---|---|
| **1** | **Wrong E00 artifact / source mismatch (`E00 118` vs `E00 796`)** | `E00 118` is only a shell while `E00 796` contains the actual engine. If the live embed uses 118, Continue/scoring cannot work. | **STRONGEST** |
| **2** | **Live embed/deployment points to a different artifact than `main`** | Repository state alone does not prove the live page uses the intended file. | **UNVERIFIED** |
| **3** | **E00 796 is not the artifact actually wired into the production assessment** | The repo contains several historical/repair paths, creating a real source-chaos risk. | **UNVERIFIED** |
| **4** | **Results isolation code is not executing in the live composition** | E00.02 explicitly hides E01–E09; if E04/E07/E08/E09 visibly appear before completion, the isolation boundary is not operating as intended. | **LIKELY SYMPTOM / NEEDS LIVE PROOF** |
| **5** | **Multiple generations of bridge/controller logic are coexisting** | E00.01, E00.02, E00.03, plus legacy/hardened paths create event-order and authority risk if more than one version is injected. | **PLAUSIBLE** |
| **6** | **Result handoff URL/configuration drift** | E00 796 currently uses `results.nayanet.app`, while the bridge workflow's static requirements include `results.nayanet.xyz`. This is a concrete configuration inconsistency. | **CONFIRMED IN SOURCE / NOT TERMINAL SCORE ROOT CAUSE** |
| **7** | **Continue terminal path fails during `publish()`** | The engine has a full publish path, but runtime evidence is still required to identify the exact thrown error. | **UNVERIFIED** |
| **8** | **Score matrix / dimension data mismatch** | E00 796 now validates the score object and dimension structure; a runtime data mismatch would throw before result publication. | **PARTIALLY HARDENED** |
| **9** | **Cross-document event timing/order issue** | E00.01, E00.03, and E00.02 communicate through custom events and parent/top-window messaging. Incorrect composition can break release without breaking scoring. | **PLAUSIBLE** |
| **10** | **External navigation masks a successful local result** | E00 796 renders/verifies local results before attempting external handoff, so this should not prevent local scoring; it can still obscure the final user journey if navigation fails. | **SECONDARY** |

## 7. Known Evidence

### E00 796 already contains the core score engine
The current source includes `save()`, `calculate()`, `buildResult()`, `valid()`, `publish()`, `renderLocalResults()`, `verifyLocalResults()`, `releaseResultsSections()`, and `attemptResultsHandoff()`.

### E00 796 already contains a hardened Continue boundary
The current source uses a capture-phase Continue boundary with `closest('#continueButton')`, state guards, and an execution error boundary. The repository also contains a workflow specifically created to repair this boundary.

### E00.01 expects a complete result
It requires `MAXESS_RESULT_V1`, an overall score 0–100, exactly five dimensions, and exactly fifteen responses before release.

### E00.02 explicitly owns visual isolation
It marks the root state as `waiting`, hides E01–E09, and releases them only when the release event arrives.

### E00.03 is intended to coordinate the release
It validates the canonical result and emits `MAXESS_ISOLATION_RELEASE` once.

## 8. Current State

**ENGINE:** Not proven live-working.  
**SOURCE:** Not fully reconciled.  
**SCORING:** Implemented in E00 796, not yet live-verified.  
**CONTINUE:** Hardened in source, not yet live-verified.  
**RESULT CONTRACT:** Implemented.  
**RESULT ISOLATION:** Implemented in source, not yet live-verified.  
**LIVE PARITY:** Not proven.  
**10/10:** No — not yet.

## 9. Next Execution Order

1. **Prove the live source artifact.** Determine exactly which E00 file is embedded in the failing assessment.
2. If it is `E00 118`, stop debugging the bridge and restore the correct executable assessment source first.
3. If it is `E00 796`, run a runtime diagnostic against the actual live artifact and capture the first thrown error / state transition.
4. Verify the E00.02 isolation state before and after completion.
5. Verify the exact `MAXESS_RESULT_V1` object at Q15.
6. Verify E01/E02/E03/E04 hydration from the same result object.
7. Resolve the `results.nayanet.app` vs `results.nayanet.xyz` configuration mismatch.
8. Remove or quarantine competing legacy artifacts only after source authority is proven.
9. Perform end-to-end live verification.
10. Record the result, lesson, safeguard, and next state in this project log.

## 10. Anti-Loop Rule

**No AI may repeat an already-failed approach without first reading this project hub and adding a new reason for why the next attempt differs.**

Before every material attempt, record:

- current hypothesis;
- evidence supporting it;
- what has already been tried;
- why this attempt is different;
- expected observable result;
- actual result;
- conclusion;
- next hypothesis.

This is the project memory loop:

**TRY → OBSERVE → RECORD → LEARN → CHANGE APPROACH → TRY AGAIN**

## 11. Definition of Done

MAXESS is not done when the source contains a scoring function.

It is done when:

- all 15 questions can be answered;
- Continue advances through all questions;
- Q15 saves the final answer;
- the score is calculated correctly;
- `MAXESS_RESULT_V1` is valid;
- the result is persisted/broadcast;
- E01/E02/E03/E04 display the real result;
- E05–E09 remain hidden until release;
- the live result path works;
- source/live parity is proven;
- regression checks pass;
- Oscar finds no unresolved critical defect;
- the verified state is frozen and documented.

---

**Current project rule:** Resolve **SOURCE → LIVE PARITY** before performing another blind scoring/Continue rewrite. That is now the highest-leverage move.
