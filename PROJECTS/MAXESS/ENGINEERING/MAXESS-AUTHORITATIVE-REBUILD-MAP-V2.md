# 🔱 MAXESS V2 — AUTHORITATIVE REBUILD MAP

## Target

Replace the patchwork assessment/results handoff with one authoritative assessment machine and one immutable Results contract while preserving the best existing UX/design work.

## Architecture

```text
ASSESSMENT DEFINITION
   ↓
E00 ENGINE
   ├─ state
   ├─ questions
   ├─ answers
   ├─ responses
   ├─ scoring
   └─ result validation
   ↓
MAXESS_RESULT_V1 (frozen)
   ↓
RESULTS RELEASE
   ↓
E01–E09 presentation consumers
```

## Work packages

### WP1 — Engine
- Integrate `MAXESS-E00-AUTHORITATIVE-ENGINE-V1.js` into the final E00 shell.
- Supply AI Score as configuration.
- Remove duplicate score functions from the E00 shell.
- Remove competing Continue listeners.
- Remove DOM scraping and timing-based completion.

### WP2 — Contract
- Validate every release against `MAXESS_RESULT_V1`.
- Release exactly once after Q15.
- Freeze the result before Results presentation.

### WP3 — Results consumers
- Refactor E01–E09 to receive the result directly.
- Remove polling.
- Remove local/session fallback.
- Remove URL/result scraping.
- Remove duplicate global consumers.
- Keep display-only derivation local to each section.

### WP4 — Visual flagship
- Preserve the strongest jewel controls, Naya presence, orb/score treatment, motion, typography, spacing, and color rhythm.
- Unify components instead of maintaining divergent versions.
- Make hover/press/selected/focus states tactile and premium.
- Keep motion independent from correctness.

### WP5 — Dynamic foundation
- Define deterministic assessment-definition interfaces.
- AI Score is the first compiled definition.
- Topic support requires sufficient trusted knowledge/rubric coverage.
- Unsupported topics produce a truthful boundary message.

### WP6 — QA/evidence
- Unit: scoring, normalization, dimensions, validation, progression, result creation.
- Integration: E00 → contract → E01–E09.
- E2E: Q1 → Q15 → final result → E01 → E09.
- Responsive: 320, 360, 375, 390, 414, 480, 600, 768, 900, 1024, 1280.
- Accessibility: keyboard, focus, labels, live regions, contrast, touch targets.
- Performance: no unnecessary polling/timers/listener duplication.
- Live evidence required before green.

## Completion gates

1. **Engine green:** pure engine tests pass.
2. **AI Score green:** 15×0–4 and expected score math reproduced.
3. **Contract green:** every required result field is present and valid.
4. **Results green:** E01–E09 render from the same frozen contract.
5. **Journey green:** one complete live run succeeds.
6. **Design green:** flagship critique has no material P0/P1 defects.
7. **Evidence green:** automated + live evidence stored.
8. **Final green:** Oscar challenge passes and state is frozen.

## Explicit retirement list after integration

- E00.01 as runtime bridge authority.
- E00.02 as competing assessment runtime.
- E00.03 as competing controller authority.
- Result consumer polling.
- local/session fallback result authority.
- DOM score scraping.
- URL-based score recovery.
- timing hacks used for correctness.
- duplicate scoring functions.
- duplicate completion paths.

Historical artifacts are preserved; runtime authority is not.
