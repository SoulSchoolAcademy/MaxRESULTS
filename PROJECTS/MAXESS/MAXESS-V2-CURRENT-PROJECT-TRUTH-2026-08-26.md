# MAXESS V2 — Current Project Truth

**Updated:** 2026-08-26

## North Star
One clean human test. The intended experience is: **“OH MY GOD. THIS IS AWESOME.”**

## Current execution state

| Boundary | Status | Evidence |
|---|---|---|
| Engine | GREEN | Prior executable golden evidence |
| Canonical AI Score | GREEN | Prior executable/static evidence |
| Static architecture | GREEN | Run 33002378451 static gate |
| Executable golden | GREEN | Prior executable golden test |
| Result consumer | GREEN | Prior static/executable evidence |
| Groove hardening | GREEN | Run 33002378451 prerequisite |
| Browser | BLOCKED → FIXED IN SOURCE → RERUN REQUIRED | Run 33002378451 evidence |
| Human test | BLOCKED | Must follow browser GREEN |

## Browser defect
Run `33002378451` failed all browser tests because the E00 runtime never published. Evidence showed `hasEngine=true`, `hasDefinition=true`, `hasRuntime=false`.

Root cause: the Groove `$` helper prefixed `#` while callers already supplied `#`, producing invalid selectors such as `##mx-cont`.

## Fix
The authoritative Groove now normalizes selector input rather than changing callers or introducing another authority.

## Required next proof
- Q1 renders.
- Five answers render.
- Continue disabled before selection.
- Continue enables after selection.
- Q1→Q15 exactly once.
- Final commit exactly once.
- `MAXESS_RESULT_V1` frozen.
- Exactly one result-ready event and one result-updated event.
- `completionCount=1`.
- Duplicate Continue remains blocked.
- E01 receives the same result with no rescoring.
- Zero console errors.
- Zero failed requests.
- All required widths pass.

Only an executed post-fix browser run can move Browser to GREEN.
