# MAXESS Smart Note — Browser Gate Selector Defect

**Date:** 2026-08-26
**Status:** FIXED IN SOURCE; EXECUTED RERUN REQUIRED

## Finding
GitHub Actions run `33002378451` executed the browser gate and failed all three browser tests before assessment execution. The exact browser diagnostics showed:

- `hasEngine = true`
- `hasDefinition = true`
- `hasRuntime = false`
- Q1 shell rendered, but question text and answers did not populate.

Inspection of the executed Groove source identified the product defect:

```js
const $=id=>ROOT.querySelector('#'+id);
```

while the authoritative Groove consistently calls the helper with IDs that already include `#`, for example:

```js
$('#mx-cont')
$('#mx-q')
$('#mx-answers')
```

That produced selectors such as `##mx-cont`, causing the authoritative Groove bootstrap to fail before `MAXESS_E00_V2` was published.

## Classification
**PRODUCT DEFECT — authoritative E00 Groove bootstrap selector resolution.**

Not an environment failure and not merely a Playwright harness defect.

## Fix
The helper now accepts either form without changing state authority:

```js
const $=id=>ROOT.querySelector(id.charAt(0)==='#'?id:'#'+id);
```

No new scorer, state authority, result authority, bridge, or replacement Continue implementation was introduced.

## Verification target
The next Actions execution must prove:

1. E00 runtime publishes.
2. Q1 renders.
3. Five answers render.
4. Continue is disabled before selection.
5. Continue enables after selection.
6. Q1→Q15 occurs exactly once.
7. Final answer commits once.
8. `MAXESS_RESULT_V1` is frozen.
9. Exactly one `MAXESS_RESULT_READY` and one `maxess:result-updated` occur.
10. `completionCount = 1`.
11. Duplicate Continue cannot create a second completion.
12. E01 receives the same result without rescoring.
13. No console errors or failed requests.
14. Required widths remain usable.

## Learning
A static architecture gate can pass while a browser bootstrap path is dead. Browser evidence must be treated as a separate executable truth boundary, and diagnostics must distinguish dependency loading from runtime publication.
