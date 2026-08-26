# 🔱 NEXT EXECUTION — MAXESS V2 10-STEP PRE-TEST EXCELLENCE GATE

**Date:** 2026-08-26  
**Priority:** P0 / ENGINE → GROOVE → E01  
**Status:** READY TO EXECUTE  
**Purpose:** Make the next execution maximize the probability that the first human test is a **10/10 success**, not merely technically functional.  
**Human test gate:** **LOCKED until every required evidence gate is GREEN.**

---

# MISSION

Take the now-working MAXESS V2 authoritative Groove path and perform one comprehensive pre-test hardening + verification execution.

The objective is not to create another patch cycle.

The objective is to reach this state:

```text
AUTHORITATIVE ENGINE        🟢
        ↓
CANONICAL AI SCORE          🟢
        ↓
THIN GROOVE ADAPTER         🟢
        ↓
15/15 REAL INTEGRATION      🟢
        ↓
FROZEN RESULT V1            🟢
        ↓
SINGLE RESULT RELEASE      🟢
        ↓
E01 SAME RESULT CONTRACT    🟢
        ↓
BROWSER SMOKE               🟢
        ↓
RESPONSIVE QA               🟢
        ↓
EVIDENCE RECEIPT             🟢
        ↓
LIVE TEST LINK               🟢
        ↓
SHAWN TESTS ONCE             🚀
```

**Do not stop at "looks good." Execute evidence.**

**Do not ask Shawn to test until the gate is GREEN.**

---

# SOURCE OF TRUTH — READ FIRST

Before changing anything, read the current `main` state of `SoulSchoolAcademy/NayaPOWER` and establish the exact current truth.

Read, in this order:

1. `PROJECTS/MAXESS/README.md`
2. `PROJECTS/MAXESS/MAXESS-MASTER-ENGINEERING-DESIGN-DIRECTIVE-V2.md`
3. `PROJECTS/MAXESS/NEXT-EXECUTION-MAXESS-V2-GROOVE-AUTHORITATIVE-ADAPTER-2026-08-26.md`
4. `PROJECTS/MAXESS/ENGINEERING/MAXESS-E00-AUTHORITATIVE-ENGINE-V2.js`
5. `PROJECTS/MAXESS/ENGINEERING/MAXESS-AI-SCORE-DEFINITION-V1.js`
6. `E00 MAXESS V2 — AUTHORITATIVE GROOVE.html`
7. the current E01 implementation / result consumer
8. all current MAXESS V2 verification receipts and next-execution documents
9. current Git status / relevant commits / workflow evidence
10. current visual lineage so good UI work is preserved

Do not rely on prior conversation memory when the repository can establish the truth.

---

# TEN EXECUTION STEPS

## 1. ESTABLISH THE CANONICAL RUNTIME

Determine exactly which E00 Groove artifact is intended to be the production/live runtime.

Resolve any duplicate or confusing E00 V2 artifacts that could create source-lineage ambiguity.

Requirements:

- exactly one canonical Groove runtime;
- exactly one authoritative engine;
- exactly one canonical AI Score definition;
- exactly one Result Contract;
- no accidental alternate runtime path;
- preserve the strongest existing visual shell.

If a clearly in-scope lineage defect exists, fix it now.

Do not create another parallel implementation.

---

## 2. AUDIT THE GROOVE AS A TRUE THIN ADAPTER

Perform a static audit of the actual Groove file.

Prove that Groove owns only presentation responsibilities:

- visual shell;
- question rendering;
- answer selection UI;
- Continue control;
- Naya UI/audio hook;
- progress display;
- calls into the authoritative engine;
- result-release adapter.

Prove Groove does NOT own:

- scoring formulas;
- duplicate question state;
- competing result construction;
- localStorage/sessionStorage result authority;
- URL/hash result authority;
- DOM score scraping;
- polling for correctness;
- timer-based completion;
- legacy bridge choreography;
- duplicate completion paths.

Search both positively and negatively. Do not merely inspect by eye.

---

## 3. HARDEN THE ENGINE ↔ GROOVE CONTRACT

Verify every call from Groove into `MAXESS_E00_ENGINE_V2` against the actual engine API.

Verify:

- definition validation occurs;
- state is created once;
- answer selection is engine-owned;
- Continue is engine-owned;
- final Q15 answer is committed through the engine;
- engine result is returned exactly once;
- `MAXESS_RESULT_V1` validation occurs before publication;
- result is frozen before exposure;
- released result cannot be mutated through the public reference;
- repeat completion is rejected/idempotent;
- reset/configuration cannot silently destroy a released result.

If an in-scope contract weakness is discovered, fix it now and retest the full path.

---

## 4. BUILD A REAL GOLDEN INTEGRATION HARNESS

Do not test only the pure engine.

Run the golden cases through the **actual Groove-loaded engine path**.

At minimum verify:

- 15 questions;
- exactly 5 answers each;
- answer scores only 0–4;
- Q1 → Q15 exactly once;
- Continue blocked before selection;
- selecting an answer enables Continue;
- changing selection does not create extra responses;
- Q15 commits exactly once;
- minimum = 0/0;
- maximum raw = 60/60;
- maximum normalized = 100/100;
- each dimension max = 12/12 raw;
- normalized dimension behavior is correct;
- exactly one `MAXESS_RESULT_V1` is released;
- result is frozen;
- duplicate Continue cannot duplicate completion;
- duplicate result events cannot create another result;
- E01 receives the same object/contract values;
- no score is recomputed downstream.

Capture machine-readable output.

---

## 5. VERIFY THE FULL RESULT RELEASE CHAIN

Trace the exact Q15 lifecycle:

```text
Q15 answer
  ↓
ENGINE commit
  ↓
ENGINE result
  ↓
validate MAXESS_RESULT_V1
  ↓
freeze
  ↓
window.MAXESS_RESULT
  ↓
window.MAXESS_RESULT_V1
  ↓
MAXESS_RESULT_READY
  ↓
maxess:result-updated
  ↓
E01–E09 reveal/consume
```

Verify:

- no second scoring call after release;
- no second result construction;
- no result replacement;
- no stale result;
- no race condition;
- no event duplication;
- no downstream recalculation.

Create a receipt containing the exact observed result fingerprint.

---

## 6. BROWSER SMOKE — EXECUTE, DON'T ASSUME

Use the strongest available browser-capable verification route in the environment.

Run the real Groove artifact, not a reconstructed approximation.

Verify visually and behaviorally:

1. Groove loads;
2. no fatal console errors;
3. MAXESS branding renders;
4. Naya control renders;
5. progress renders;
6. Q1 renders;
7. all five answer controls render;
8. no answer selected initially;
9. Continue is visibly disabled;
10. selecting an answer visibly changes state;
11. Continue becomes enabled;
12. Continue advances to Q2;
13. progress updates correctly;
14. Naya dialog opens;
15. Naya dialog closes;
16. Naya audio/TTS hook does not break assessment flow;
17. Q15 completes;
18. result appears;
19. E01 appears;
20. result remains stable after release.

Record console errors/warnings separately from functional failures.

If browser execution is technically unavailable, explicitly mark browser smoke YELLOW rather than claiming GREEN and identify the exact missing capability.

---

## 7. RESPONSIVE + ACCESSIBILITY HARDENING

Before human testing, inspect/test the required widths:

```text
320
360
375
390
414
480
600
768
900
1024
1280
```

Verify:

- no horizontal overflow;
- question remains readable;
- answer cards remain tappable;
- Continue remains accessible;
- Naya control remains accessible;
- progress remains legible;
- modal fits viewport;
- buttons do not overlap;
- result state remains usable;
- keyboard focus is visible;
- Enter/Space operate controls where appropriate;
- Escape closes Naya dialog;
- ARIA state reflects answer selection and disabled/enabled Continue.

Fix clearly in-scope defects now.

---

## 8. E01 HANDOFF PROOF

Do not merely prove that E01 is visible.

Prove that E01 consumes the exact frozen `MAXESS_RESULT_V1` produced by E00.

Verify:

- overall score matches;
- mastery band matches;
- all five dimensions match;
- fingerprint/result identity matches;
- E01 does not invoke its own scoring logic;
- E01 does not reconstruct the result;
- refreshing/duplicating presentation does not create a second authoritative result;
- E02–E09 do not become alternate authorities.

If downstream code violates the Result Contract, fix the clearly in-scope defect now.

---

## 9. EVIDENCE + RELEASE RECEIPT

Produce one authoritative receipt containing:

### Current truth
- canonical branch/commit;
- canonical Groove file;
- engine version;
- score-definition version;
- result-contract version.

### Files changed
Exact paths and reasons.

### Architecture
Before → after summary.

### Tests
Every automated/static/browser/responsive test actually executed.

### Observed results
Actual outputs, not expected outputs.

### Result fingerprint
Include:

- overall score;
- raw total;
- normalized score;
- dimension values;
- mastery band;
- result version;
- release event count;
- result freeze confirmation.

### Board
```text
ENGINE             🟢/🟡/🔴
INTEGRATION        🟢/🟡/🔴
GOLDEN             🟢/🟡/🔴
STATIC             🟢/🟡/🔴
BROWSER            🟢/🟡/🔴
RESPONSIVE         🟢/🟡/🔴
E01 HANDOFF        🟢/🟡/🔴
EVIDENCE           🟢/🟡/🔴
HUMAN TEST         🟢/🔴
```

No green without executed evidence.

---

## 10. FINAL EVIDENCE GATE + NEXT EXECUTION

Only declare the execution successful when:

- engine = 🟢
- integration = 🟢
- golden = 🟢
- static architecture = 🟢
- browser smoke = 🟢
- responsive = 🟢
- E01 handoff = 🟢
- evidence receipt = 🟢

Then:

1. generate the live-test link;
2. provide the raw Groove code receipt;
3. provide a concise human testing script;
4. explicitly state what Shawn should observe;
5. do NOT bury the test steps in a giant explanation;
6. ask for human testing only after the gate is green.

If any gate remains yellow/red:

- do not ask Shawn to test;
- fix every clearly in-scope defect in this execution;
- rerun all affected tests;
- update the receipt;
- define the next execution as the smallest remaining blocker set.

---

# HUMAN TEST SCRIPT — PREPARE IN ADVANCE

Once GREEN, Shawn should only need to do this:

1. Open the supplied live-test link.
2. Confirm MAXESS loads cleanly.
3. Click Naya once and confirm the interaction works.
4. Answer Q1.
5. Confirm Continue becomes enabled.
6. Continue through all 15 questions.
7. On Q15, confirm finalization occurs once.
8. Confirm the result appears.
9. Confirm E01 begins with the same score/result.
10. Report only anything unexpected.

The goal is **one clean human test**, not a debugging session.

---

# NON-NEGOTIABLE LAWS

- GitHub/source authority first.
- Do not guess when repository evidence exists.
- Do not create parallel authorities.
- Do not add patch-on-patch architecture.
- Preserve the strongest visual work.
- Replace fragile implementation instead of layering over it.
- One runtime scorer.
- One state authority.
- One result authority.
- One release path.
- No timers for correctness.
- No polling for correctness.
- No storage authority.
- No URL authority.
- No DOM score scraping.
- No duplicate Continue handlers.
- No duplicate completion path.
- No downstream recalculation.
- No false green.
- No premature human testing.
- Maximize the execution before handing it to Shawn.

---

# DEFINITION OF DONE

The execution is DONE when the next human interaction with MAXESS is expected to feel like:

> **"Oh my God. This is awesome."**

—not:

> **"Okay, we found another thing we need to fix."**

That means the engineering team should proactively eliminate predictable failure modes before requesting the test.

**Execute. Verify. Harden. Re-run. Capture evidence. Then hand it to Shawn.**
