# 🔱 NEXT EXECUTION — MAXESS V2 GROOVE AUTHORITATIVE ADAPTER

**Priority:** P0 / ENGINE → GROOVE  
**Status:** READY TO EXECUTE  
**Gate:** Do not request live user testing until this execution passes.

## Mission

Turn the strongest MAXESS E00 visual shell into a thin presentation adapter around the already-verified authoritative E00 engine.

## Non-negotiable architecture

```text
Groove UI
   ↓
MAXESS_E00_ENGINE_V2
   ↓
MAXESS_AI_SCORE_DEFINITION_V1
   ↓
response state
   ↓
deterministic scoring
   ↓
validated + frozen MAXESS_RESULT_V1
   ↓
MAXESS_RESULT_READY
   ↓
E01–E09
```

There must be exactly one runtime scoring authority.

## Execution order

### 1. Read authority

Read:
- Master Engineering Directive V2
- Source/Architecture Inventory
- Result Contract V1
- Authoritative E00 engine V2
- AI Score definition V1
- Golden test V2
- current E00 visual lineage

### 2. Inspect current Groove artifact

Identify and remove:
- embedded duplicate scoring;
- embedded duplicate question state;
- competing result construction;
- local/session result authority;
- URL result authority;
- timing-based completion;
- polling used to compensate for missing authority;
- legacy bridge choreography.

### 3. Rebuild the Groove runtime adapter

The Groove file should contain:
- visual shell;
- question renderer;
- answer selection UI;
- Continue control;
- Naya UI/audio hook;
- thin calls into `MAXESS_E00_ENGINE_V2`;
- result release adapter.

The Groove layer may read state for presentation. It may not calculate scores.

### 4. Result release

On Q15:
1. commit the final answer through the engine;
2. receive the engine result;
3. validate `MAXESS_RESULT_V1`;
4. freeze it;
5. publish `window.MAXESS_RESULT` and `window.MAXESS_RESULT_V1`;
6. dispatch `MAXESS_RESULT_READY` and `maxess:result-updated`;
7. reveal E01–E09;
8. never calculate again.

### 5. Static verification

Prove:
- one scorer in the live Groove path;
- one state authority;
- no `setTimeout`/polling for correctness;
- no DOM score scraping;
- no storage result authority;
- no duplicate Continue handlers;
- no URL/hash result authority;
- no duplicate completion path.

### 6. Golden integration verification

Run the golden cases against the actual Groove-loaded engine:
- 15 questions;
- 5 answers each;
- 0–4 scores;
- Q1→Q15 once;
- Continue blocked without answer;
- 0/0 minimum;
- 60/100 maximum;
- 12/100 dimension maximum;
- exactly one result;
- frozen result;
- duplicate Continue cannot duplicate completion.

### 7. Browser/static artifact QA

Verify:
- Groove renders;
- first question renders;
- answer selection visibly works;
- Continue enables only after selection;
- progress advances;
- Naya opens;
- Q15 finalizes;
- E01 receives the same result contract;
- no console errors;
- required mobile widths remain usable.

### 8. Evidence gate

Do NOT ask Shawn to test until:

- engine = 🟢
- integration = 🟢
- automated golden = 🟢
- static architecture = 🟢
- browser smoke = 🟢
- E01 handoff = 🟢

Then produce the live-test link and raw Groove code receipt.

## Required final communication

Return:
1. current truth;
2. files changed;
3. architecture changes;
4. tests run;
5. observed results;
6. green/yellow/red board;
7. human-readable receipt;
8. remaining blockers;
9. next execution.

## Leadership rule

Maximize the execution. If a clearly in-scope architectural defect is found, fix it in the same execution rather than creating another patch cycle. Preserve good visual work; replace fragile implementation. Do not call something green without executed evidence.
