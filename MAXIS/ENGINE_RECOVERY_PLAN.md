# MAXIS ENGINE RECOVERY PLAN

## Objective

Restore deterministic communication across the single-page MAXESS assessment and results system without sacrificing the existing visual work.

## Problem 1 — Multiple E00 candidates

**Observed:** `E00 796` and `E00 1800` are both full E00 implementations with very similar visible architecture. The repository currently also has a user-reported live E118 artifact.

**Solution:** Do not choose by line count. Compare behavior and result-contract output. Select the smallest proven implementation that preserves the required scoring, UX, and result data. If a larger candidate contains required behavior, transplant that behavior into the canonical baseline rather than maintaining two competing E00 engines.

**Decision rule:** correctness > completeness > maintainability > line count.

## Problem 2 — Multiple result-release authorities

**Observed:** E00.01 contains `showResults()` and can set `MAXESS_RESULTS_RELEASED` / dispatch `MAXESS_ISOLATION_RELEASE`; E00.03 also implements `releaseResults()` and emits the same release event. fileciteturn1171file0L2-L10 fileciteturn1173file0L2-L10

**Solution:** E00.03 becomes the sole release authority. E00.01 becomes a bridge/adapter that exposes and validates the canonical result but does not independently release the page.

## Problem 3 — Contract mismatch

**Observed:** E00.01 requires contract version + score + 5 dimensions + 15 responses. E00.03 additionally requires a recognized `masteryBand`. fileciteturn1171file0L2-L10 fileciteturn1173file0L2-L10

**Solution:** Define one `MAXESS_RESULT_V1` schema. The E00 scorer must produce every required field before publication. Every bridge/controller/consumer validates the same contract.

## Problem 4 — Event-ordering risk

**Observed:** E00.03 contains recovery passes because it anticipates initialization-order problems; E00.01 also polls for a result. fileciteturn1171file0L2-L10 fileciteturn1173file0L2-L10

**Solution:** Persist the canonical result first, then emit one release event. Consumers hydrate from both event and current state. Replace broad polling with bounded recovery only where genuinely required.

## Problem 5 — Different consumers use different transport paths

**Observed:** E04 checks current window state, parent/top state, session storage, hash state, result events, storage, pageshow, and message events. fileciteturn1177file0L2-L2

**Solution:** Standardize on:

1. `window.MAXESS_RESULT` for same-document runtime state.
2. `sessionStorage['MAXESS_RESULT_V1']` for same-session recovery.
3. one semantic result-ready event.
4. `postMessage` only when a genuine frame boundary exists.

Hash transport should not be part of the primary architecture.

## Problem 6 — Visual release is mixed with data release

**Observed:** E00.02 is explicitly responsible for hiding/revealing result sections, while E00.01 and E00.03 both participate in result release. fileciteturn1172file0L2-L10

**Solution:** Separate responsibilities:

- E00 = calculate.
- E00.01 = bridge.
- E00.03 = authorize release.
- E00.02 = visually reveal.
- E01–E09 = consume.

## Problem 7 — Downstream sections must not become independent scorers

**Observed:** E02 and E03 identify `window.MAXESS_RESULT` as their runtime authority; E04 derives its Direction value from the result. fileciteturn1175file0L1-L2 fileciteturn1176file0L1-L2 fileciteturn1177file0L2-L2

**Solution:** Preserve this consumer model and make it consistent. No downstream section recalculates overall score or changes the official result.

## Problem 8 — Presentation code is not the immediate blocker

**Observed:** E05–E09 are predominantly content, visual, offer, video, and membership sections. fileciteturn1178file0L1-L2 fileciteturn1179file0L1-L2 fileciteturn1180file0L1-L2 fileciteturn1181file0L1-L2 fileciteturn1182file0L1-L10

**Solution:** Do not spend engineering cycles redesigning these sections until the result contract and release boundary are proven.

## Problem 9 — Cross-frame uncertainty

**Observed:** E00.03 already attempts parent/top `postMessage` notification. E04 also attempts parent/top result reads. fileciteturn1173file0L2-L10 fileciteturn1177file0L2-L2

**Solution:** Determine whether the production page actually uses frames/isolated embeds. If same-document, eliminate unnecessary cross-frame complexity. If frames exist, define a strict message envelope and trusted-origin policy rather than wildcard messaging as the primary transport.

## Problem 10 — Project memory / handoff failure

**Observed:** The project has accumulated multiple candidate artifacts and iterative bridge files without a single discoverable engineering index.

**Solution:** This `MAXIS` folder becomes the project memory layer. Every AI must read it before substantive work and update the feed before handoff.

## Execution order

### Gate A — Source truth

- Inspect current live E118.
- Compare E00 796 and E00 1800.
- Establish the exact result-producing code path.

### Gate B — Contract

- Define exact `MAXESS_RESULT_V1` schema.
- Make producer emit complete schema.
- Remove competing schema interpretations.

### Gate C — Release

- E00.01 bridge only.
- E00.03 sole controller.
- E00.02 sole visual gate.

### Gate D — Hydration

- E01 score.
- E02 dimensions.
- E03 report.
- E04 direction.
- E05–E09 continuity.

### Gate E — Verification

Run the real 15-question path and inspect the browser console/runtime state at each boundary.

## Success signal

The same real result object can be traced from the final E00 answer all the way through E09 without being recreated, overwritten, rejected, or lost.
