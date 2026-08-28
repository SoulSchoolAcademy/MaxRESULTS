# 🔱 2026-08-28 — MAXIS + NayaPOWER Execution Failures and Repairs

## Purpose

Preserve the exact failures discovered during the first real execution of the current Team Naya doctrine so the next Naya does not rediscover them.

## NayaPOWER finding

The existing cold-start runtime gate failed before Smart Brain validation because the canonical Human Capability & Mastery protocol did not contain the exact machine-checked phrase:

`ready-to-run **NEXT EXECUTION**`

This was a governance/documentation-to-runtime contract drift, not a product failure.

### Repair

Added the exact enforcement phrase to:

`.naya/codex/HUMAN-CAPABILITY-AND-MASTERY-OPERATING-PROTOCOL.md`

### Lesson

If a runtime validator checks a contractual phrase, that phrase is part of the executable contract. Human-readable equivalence is insufficient.

## MAXIS finding #1

The first current-source MAXIS Quality run failed at TypeScript parsing after the guest-Hub repair.

### Root cause

Malformed JSX was introduced in:

- `app/hub/page.tsx`
- `app/maxess/page.tsx`

### Repair

Both files were structurally rewritten and the next verification run proved:

- typecheck: PASS
- build: PASS
- front-door contract: 24/24 PASS
- current-HEAD production server startup: PASS

## MAXIS finding #2

The current-source QMAX golden-path test then failed with:

`QMAX GOLDEN PATH FAILED: next action to Hub is missing`

### Root cause

The product now correctly exposes two legitimate Hub continuations:

1. authenticated save/claim → Hub;
2. guest continuation → Guest Hub.

The old test assumed exactly one link whose accessible name contained `Hub`, so it rejected the correct two-path design.

### Repair

The golden-path contract was strengthened rather than weakened. It now requires:

- exactly one explicit `Continue to Guest Hub` action;
- exactly one `Save result & enter Hub` member continuation.

This makes the test encode the actual product truth instead of hiding the second legitimate path.

## Current evidence

At commit `dde0aaa470485738a18bfbef3d87a169494b8dc6` the MAXIS Quality run demonstrated:

- typecheck PASS;
- build PASS;
- QMAX front-door contract 24/24 PASS;
- current-HEAD production server startup PASS;
- QMAX golden path reached the result and authoritative result checks before failing only on the outdated Hub-link assertion.

The test was then repaired in commit:

`e4919112bb5fe8ec734af7d5c2202e23f1633f12`

A fresh MAXIS Quality run is queued/in progress for that commit.

## Production boundary

Vercel production remains on an older READY deployment and has not yet been observed at the latest source SHA. Therefore exact production/source parity remains UNKNOWN.

## Non-negotiable next move

Do not polish the UI.

Do not add another architecture.

Do not claim the golden path green.

First obtain a green MAXIS Quality run for the repaired test, deploy that exact verified source, then execute the real interactive guest journey and the optional identity/claim journey.
