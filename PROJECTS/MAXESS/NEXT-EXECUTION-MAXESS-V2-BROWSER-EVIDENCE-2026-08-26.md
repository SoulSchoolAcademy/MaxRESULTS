# 🔱 NEXT EXECUTION — MAXESS V2 BROWSER EVIDENCE GATE

**Priority:** P0
**Status:** READY
**Purpose:** Promote the successful V2 Groove source/runtime path from yellow to green using executable browser evidence.

## Authority

The active MAXESS V2 architecture is:

```text
GROOVE UI
   ↓
MAXESS_E00_ENGINE_V2
   ↓
MAXESS_AI_SCORE_DEFINITION_V1
   ↓
MAXESS_RESULT_V1
   ↓
MAXESS_RESULT_READY
   ↓
E01–E09
```

## Preconditions

- Engine V2: GREEN
- AI Score definition: GREEN
- Groove adapter architecture: GREEN
- Golden engine invariants: GREEN
- No live user testing request until this gate is complete

## Browser execution

### A. Load

- Load the exact deployed/embedded Groove artifact.
- Confirm engine dependency loads.
- Confirm AI Score definition loads.
- Confirm first question renders.
- Capture console output.

### B. Q1–Q15

Run one deterministic assessment journey.

Verify for every question:

- question index is correct;
- exactly five answers render;
- Continue is disabled before selection;
- selecting one answer enables Continue;
- one Continue advances exactly one question;
- response count increases exactly once.

### C. Q15 completion

Verify the exact sequence:

```text
Q15 ANSWER
 ↓
ENGINE COMMIT
 ↓
ENGINE RESULT
 ↓
VALIDATE MAXESS_RESULT_V1
 ↓
FREEZE
 ↓
PUBLISH
 ↓
MAXESS_RESULT_READY
 ↓
E01–E09
```

Capture:

- `window.MAXESS_RESULT`
- `window.MAXESS_RESULT_V1`
- result contract version;
- overall score;
- five dimensions;
- 15 responses;
- frozen-state evidence;
- release-event count.

### D. Duplicate completion

Attempt a duplicate Continue activation after completion.

Required result:

- no second score;
- no second completion;
- no second release event;
- original frozen result remains authoritative.

### E. E01 handoff

Confirm E01 consumes the exact same result object/contract and does not calculate a new score.

### F. Responsive

Smoke-check:

`320, 360, 375, 390, 414, 480, 600, 768, 900, 1024, 1280`

At minimum confirm:

- no horizontal overflow;
- answer controls remain usable;
- Continue remains accessible;
- Naya remains usable;
- result reveal remains usable.

## Evidence package

Store:

1. browser test receipt;
2. console result;
3. result-contract snapshot;
4. release-event count;
5. responsive smoke summary;
6. exact artifact/commit SHA;
7. final green/yellow/red board.

## Promotion rule

Only after all of the above pass may:

- Browser smoke → 🟢
- E01 handoff → 🟢
- Source/live parity → 🟢
- Human live-test gate → 🟢

Then provide Shawn the live-test link and raw Groove code receipt.
