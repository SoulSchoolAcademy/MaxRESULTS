# 🔱 MAXESS Browser Gate 04 — Root Cause Receipt

**Date:** 2026-08-26  
**Run:** `33007579261`  
**Run number:** 23  
**Head SHA tested:** `c906a4fabd269092b057dd6db2a7a933134dbf0e`  
**Artifact:** `maxess-v2-browser-evidence-33007579261`  
**Artifact ID:** `9621240299`  
**Artifact size:** 1,629,335 bytes  
**Status:** ROOT CAUSE IDENTIFIED; CORRECTIVE SOURCE ALREADY PRESENT ON CURRENT MAIN; NEW BROWSER EVIDENCE PENDING

## Executive finding

Browser Gate 04 did **not** fail because the MAXESS scoring engine, assessment definition, or product UI was proven defective.

The uploaded Playwright evidence proves a **test-harness runtime extraction defect**.

The failing harness used a greedy regular expression to extract the authoritative runtime from the composed Groove HTML:

```text
/<script>([\\s\\S]*window\\.MAXESS_E00_V2=[\\s\\S]*?)<\\/script>\\s*$/i
```

Because the expression could begin at an earlier `<script>` block and consume intervening scripts, `harness.runtime` was contaminated with HTML/script markup before it was passed to Playwright `addScriptTag()`.

The actual browser error was:

```text
Failed to execute 'appendChild' on 'Node': Unexpected token '<'
```

The test then waited for the MAXESS globals that could never initialize and timed out at 30 seconds.

## Evidence

The uploaded diagnostics reported:

```json
{
  "url": "about:blank",
  "runtime": {
    "hasEngine": false,
    "hasDefinition": false,
    "hasRuntime": false,
    "phase": null,
    "questionIndex": null,
    "responses": null,
    "result": null
  },
  "runtimeErrors": [],
  "failedRequests": []
}
```

The Playwright trace provides the decisive evidence: the failing `Add script tag` call contained the clean engine code followed by:

```text
</script><script>(function(g){...}
```

Therefore the browser was being handed non-JavaScript markup as script content.

## Classification

**Primary:** TEST HARNESS  
**Secondary:** EVIDENCE / COMPOSITION boundary

**Not proven as:** product scoring defect, browser environment defect, network failure, or MAXESS runtime product failure.

## Corrective action already present on current main

The current `main` browser test no longer uses the retired greedy runtime extraction pattern. It now enumerates script blocks and selects the single script whose own content contains:

```text
window.MAXESS_E00_V2 =
```

It also separately injects the clean engine, definition, and extracted runtime.

The authoritative engine file itself is currently clean and has blob SHA:

`6584e585ed89255581782ae92b0986cad5ca2280`

The current browser test has blob SHA:

`9a73fdbb75f8b6ad00227bdffe3bdd80f6f34044`

## Regression guard added

A new pre-browser workflow step now verifies:

1. the browser harness uses the authoritative script-boundary extraction;
2. the retired greedy extraction pattern is absent;
3. the authoritative engine does not contain embedded `</script><script>` markup.

Commit containing the guard:

`c8f74e7802e5871ae24f1b8bd5ba1c1077d7a1ea`

## What is NOT authorized yet

Do not declare Browser Gate GREEN from this receipt alone.

Do not declare MAXESS human-test-ready.

Do not rewrite Continue, scoring, result authority, or the E01 consumer based on this failure.

## Required next proof

Run the current `main` Browser Gate and obtain a fresh artifact.

The next run must prove at minimum:

- engine initializes;
- definition initializes;
- MAXESS runtime initializes;
- Q1 renders;
- all five answers render;
- Continue state works;
- Q1→Q15 completes exactly once;
- `MAXESS_RESULT_V1` is created and frozen;
- exactly one completion/release event occurs;
- E01 receives the same frozen result;
- no console errors;
- no failed requests;
- required responsive widths pass.

## Continuity lesson

When browser evidence says `about:blank` with no runtime and no request failures, inspect the harness composition and script-boundary construction before changing product code.

**Source → Harness → Browser → Evidence** must be treated as distinct diagnostic layers.

The correct next move is now **fresh Browser Gate evidence**, not another product rewrite.
