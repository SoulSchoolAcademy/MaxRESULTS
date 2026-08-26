# 🔱 NEXT EXECUTION — MAXESS V2 E00 INTEGRATION + GOLDEN TEST

**Priority:** P0 / ENGINE FIRST  
**Status:** READY TO EXECUTE

## Mission

Take the newly committed pure E00 engine and integrate it into the strongest existing E00 visual shell. Do not patch E00.01/E00.02/E00.03. Do not create another scoring path.

## Execution order

### 1. Read authority

Read:

- MAXESS Master Directive V2
- Source + Architecture Inventory
- MAXESS_RESULT_V1 contract
- Authoritative Rebuild Map
- E00 796 / 700 / 1800 source lineage

### 2. Build AI Score definition

Create one configuration object containing:

- assessment ID/version;
- five dimensions;
- 15 questions;
- exactly five answers per question;
- answer scores 0–4;
- Naya metadata where needed;
- scoring/rubric versions.

### 3. Integrate engine

Connect the pure engine to the visual E00 shell:

```text
UI
 ↓
ENGINE STATE
 ↓
RESPONSE STORE
 ↓
SCORING
 ↓
RESULT VALIDATION
 ↓
FROZEN MAXESS_RESULT_V1
```

### 4. Remove competing authority

Delete/disable from the live E00 path:

- duplicate scorers;
- duplicate Continue handlers;
- DOM score scraping;
- timing-dependent completion;
- bridge-only state;
- local/session result authority;
- URL result recovery;
- legacy fallback paths.

### 5. Golden automated tests

Prove:

- 15 questions;
- five answers/question;
- every answer score 0–4;
- Q1→Q15 exactly once;
- incomplete Continue is blocked;
- final valid answer creates exactly one result;
- maximum = 60 raw / 100 normalized;
- minimum = 0 / 0;
- dimension max = 12 / 100;
- result contract validates;
- result is frozen;
- duplicate Continue cannot duplicate a response/result.

### 6. Golden live test

Run the actual AI Score assessment from start to finish and capture evidence at:

1. initial state;
2. answer selection;
3. progression;
4. Q15;
5. result finalization;
6. E01 entry.

Do not call the app green merely because automated tests pass.

## Completion gate

This execution is green only when the engine is integrated and the AI Score golden path is both automatically and live verified.

## Required final communication

Return:

1. current truth;
2. source files changed;
3. architecture changes;
4. tests executed;
5. observed results;
6. green/yellow/red board;
7. human-readable receipt;
8. remaining blockers;
9. next execution.

**Lead. Do not ask permission for clearly in-scope, safe, evidence-backed work.**
