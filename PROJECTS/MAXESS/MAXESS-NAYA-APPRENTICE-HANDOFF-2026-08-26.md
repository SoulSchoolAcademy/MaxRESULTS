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
- Golden engine invariants were previously verified.
- Shawn has directly observed the current MAXESS experience working successfully.
- A 10-step pre-test excellence gate has been created to prevent premature human testing.

Source evidence for the current Groove adapter shows the engine and definition are loaded directly, state is created through the engine, answer selection calls the engine, and final result release validates and freezes the engine result before publishing it. 

---

# 4. WHAT IS NOT YET PROVEN

Do not falsely call the following green until executed evidence exists:

- formal browser smoke receipt;
- formal 15-question Groove-loaded integration receipt;
- exact E01 same-result handoff proof;
- responsive matrix evidence;
- final evidence-gate receipt;
- live-test promotion.

Shawn's successful observation is valuable evidence, but it is not a substitute for the formal engineering receipt.

---

# 5. IMPORTANT SOURCE RISK

The repository currently contains both:

- `E00 MAXESS V2 — AUTHORITATIVE GROOVE.html`
- `E00 MAXESS V2 — CANONICAL GROOVE.html`

Treat this as a source-lineage risk.

The intended authoritative runtime is:

`E00 MAXESS V2 — AUTHORITATIVE GROOVE.html`

Before release, determine whether the second artifact is needed, obsolete, or must be clearly labeled/preserved as lineage. Do not let two artifacts become competing live runtimes.

---

# 6. DO NOT REPEAT BLINDLY

Do not return to generic Continue rewrites, score-matrix rewrites, bridge stacking, or legacy choreography without new evidence.

The anti-loop law is:

1. state what changed;
2. explain why the previous failure no longer applies;
3. identify the new evidence;
4. define what observable result will prove the new approach.

**No new evidence = no repeated experiment.**

---

# 7. NEXT CANONICAL EXECUTION

Execute:

`PROJECTS/MAXESS/NEXT-EXECUTION-MAXESS-V2-10-STEP-PRE-TEST-EXCELLENCE-GATE-2026-08-26.md`

Execute it top-to-bottom.

Do not merely summarize it.

The execution must:

1. establish the canonical runtime;
2. audit the Groove as a thin adapter;
3. harden Engine ↔ Groove contracts;
4. run a real Groove-loaded golden integration harness;
5. prove the complete result release chain;
6. execute browser smoke where technically possible;
7. harden responsive/accessibility behavior;
8. prove E01 consumes the same frozen result;
9. create one authoritative evidence receipt;
10. promote the human test only if every gate is green.

If an in-scope defect is discovered, fix it in the same execution and rerun affected verification.

---

# 8. HOW TO THINK

Take the lead.

Think beyond the immediate symptom.

Ask:

- What are the top viable ways to reach the destination?
- What is the root cause rather than the visible symptom?
- What can fail during the human test even if source code looks correct?
- What evidence would eliminate that uncertainty?
- What can be hardened now?
- What good work must be preserved?
- What can be automated so the user never has to think about it again?

Do not expose private chain-of-thought. Preserve the actionable reasoning, evidence, decision, and tradeoffs needed for the team.

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
