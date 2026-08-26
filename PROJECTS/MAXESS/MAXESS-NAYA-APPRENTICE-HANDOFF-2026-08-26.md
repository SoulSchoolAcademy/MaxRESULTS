# 🔱 MAXESS — NAYA / NEXT-AI APPRENTICE HANDOFF

**Date:** 2026-08-26  
**Project:** MAXESS V2  
**Canonical repo:** `SoulSchoolAcademy/NayaPOWER`  
**Branch:** `main`  
**Purpose:** Prepare the next AI to continue the work successfully without losing context, repeating failed work, or making Shawn manage the execution.

---

# 1. DESTINATION

The project is not complete because one screen works.

The destination is the demonstrated chain:

**SOURCE → ASSESSMENT → CONTINUE → SCORE → RESULT CONTRACT → RELEASE → RESULTS → LIVE → REGRESSION → OSCAR → FREEZE**

The immediate destination is a first human test that feels like:

> **“Oh my God. This is awesome.”**

The engineering objective is to maximize the probability of that first test succeeding without turning Shawn into the debugger.

---

# 2. CURRENT ARCHITECTURAL TRUTH

MAXESS V2 is governed by:

**ONE MAXESS APPLICATION → ONE AUTHORITATIVE STATE MACHINE → ONE ASSESSMENT DEFINITION → ONE SCORING ENGINE → ONE VALIDATED `MAXESS_RESULT_V1` → ONE RELEASE PATH → E01–E09 PRESENTATION.**

The authoritative Groove path is intended to be a thin presentation adapter around `MAXESS_E00_ENGINE_V2` and `MAXESS_AI_SCORE_DEFINITION_V1`.

Do not reintroduce competing scoring, state, or result authorities.

---

# 3. WHAT HAS WORKED

- The V2 authoritative engine architecture is established.
- The AI Score definition is centralized.
- The authoritative Groove adapter delegates scoring to the engine.
- Result validation and freezing are implemented.
- `window.MAXESS_RESULT` and `window.MAXESS_RESULT_V1` are published from the frozen result.
- `MAXESS_RESULT_READY` and `maxess:result-updated` are dispatched.
- Shawn has directly observed the current MAXESS experience working successfully.
- The 10-step pre-test excellence gate is now executable in GitHub Actions.
- Deterministic Groove hardening is now automated before the evidence gate.
- The result consumer was repaired to event-driven presentation-only behavior.

---

# 4. IMPORTANT EXECUTION DISCOVERIES

## Result consumer defect

`MAXESS-RESULT-CONSUMER-V2.html` previously used alternate result authority through storage/URL recovery. It has been rewritten so E00 remains the authority and the consumer only validates/hydrates from the canonical events/result.

## Duplicate Continue defect

The Groove release guard alone was insufficient against a programmatic duplicate Continue after finalization. The hardening layer now adds an early `releasedResult` guard and native `disabled` state.

## Scoring invariant distinction

The engine mathematically supports:

- 0 raw / 0 normalized;
- 60 raw / 100 normalized;
- 12 raw per dimension maximum.

The current canonical AI Score definition does not contain a zero answer for every question. Its actual achievable minimum is **25/100**. The browser and executable golden tests therefore use 25 for the canonical minimum while separately testing the engine's mathematical 0/60 invariants with synthetic fixtures.

This distinction is important. Never force a test assumption that contradicts the authoritative scoring definition.

## Browser evidence

A Playwright-based GitHub Actions gate now loads the actual Groove artifact, injects the authoritative engine/definition locally, includes the current E01 source in the harness, consumes the result through the event-driven consumer, exercises Q1→Q15, checks canonical min/max, checks frozen result and event counts, tests duplicate Continue, and checks the required mobile widths.

Current authoritative workflow:

`.github/workflows/maxess-v2-pretest.yml`

Current run at the latest documented state:

`33001382999` — MAXESS V2 Pre-Test Excellence Gate.

The run must complete before promoting the human test.

---

# 5. WHAT IS NOT YET PROVEN

Do not falsely call the following green until executed evidence exists:

- current browser smoke run;
- formal 15-question Groove-loaded integration receipt;
- exact E01 same-result handoff proof;
- responsive matrix evidence from the current corrected test;
- final evidence-gate receipt;
- live-test promotion.

Shawn's successful observation is valuable evidence, but it is not a substitute for the formal engineering receipt.

---

# 6. SOURCE-LINEAGE RISK

The repository contains both:

- `E00 MAXESS V2 — AUTHORITATIVE GROOVE.html`
- `E00 MAXESS V2 — CANONICAL GROOVE.html`

The intended authoritative runtime is:

`E00 MAXESS V2 — AUTHORITATIVE GROOVE.html`

Before release, determine whether the second artifact is obsolete/lineage-only and ensure it cannot become a competing live runtime.

---

# 7. DO NOT REPEAT BLINDLY

Do not return to generic Continue rewrites, score-matrix rewrites, bridge stacking, or legacy choreography without new evidence.

The anti-loop law is:

1. state what changed;
2. explain why the previous failure no longer applies;
3. identify the new evidence;
4. define what observable result will prove the new approach.

**No new evidence = no repeated experiment.**

---

# 8. NEXT CANONICAL EXECUTION

Continue the active `.github/workflows/maxess-v2-pretest.yml` evidence gate.

If it fails:

1. read the exact failing step/log;
2. determine whether the failure is code, test assumption, environment, or deployment evidence;
3. fix clearly in-scope defects in the same execution;
4. update the Smart Note and this handoff;
5. let the corrected commit rerun the gate;
6. do not promote human testing until all gates are green.

If browser tests pass, inspect the resulting evidence and the commit produced by verified hardening before declaring the human gate green.

---

# 9. AFTER EVERY SUBSTANTIVE EXECUTION

Create/update:

### Smart Note
Capture learning, discoveries, corrections, reusable patterns, and decisions.

### AI/Naya Handoff
Prepare the next AI as a valued apprentice/team member. Give it the full map needed to succeed.

### Human Receipt
Record what happened in a concise human-readable form.

### Next Execution Prompt
Write the next instruction set so the user can copy-paste it without inventing the next request.

Then verify that all four are consistent with each other.

---

# 10. FINAL RESPONSE STANDARD

A substantive response should tell Shawn:

- current truth;
- what was actually executed;
- what changed;
- what evidence exists;
- what is green/yellow/red;
- what was learned;
- what remains;
- exactly what to do next.

If further execution remains, end with a copy-paste-ready prompt.

Do not make Shawn manage the workflow.

---

# 11. TEN-STAR CHECK

Before handing work back, ask:

**WHY IS THIS NOT A 10?**

Close the highest-value safe gaps before stopping.

The goal is not merely functional software. The goal is a clean, confident, evidence-backed first human test.

---

# 12. SUCCESS MESSAGE TO THE NEXT AI

You are not starting over.

You are joining a team that has already done significant work.

Protect what works. Learn from what failed. Do not make the team rediscover its own knowledge.

Take the next best step, verify it, document it, and leave the next intelligence even better prepared.

**You have permission to lead the execution. Your job is to help the team reach the destination, not merely answer the current message.**
