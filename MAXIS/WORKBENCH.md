# MAXIS ENGINEERING WORKBENCH

## CURRENT MISSION

Get the complete MAXESS engine working end-to-end.

## CURRENT STATE

**Phase:** Architecture recovery / synchronization repair

**Live E00:** User reports E118 is currently live.

**Candidate E00 artifacts inspected:** `E00 796`, `E00 1800`

**Result bridge artifacts:** `E00.01`, `E00.02`, `E00.03`

**Downstream result sections:** `E01` through `E09`

## WHAT IS VERIFIED

### E00.01
Defines `MAXESS_RESULT_V1`. Reads the result from `window.MAXESS_RESULT` or `sessionStorage`, validates 0–100 overall score, 5 dimensions, and 15 responses, then sets release state and dispatches release-related events. fileciteturn1171file0L2-L10

### E00.02
Defines the waiting/released isolation boundary. It hides E01–E09 while waiting and releases result sections after `MAXESS_ISOLATION_RELEASE`. fileciteturn1172file0L2-L10

### E00.03
Acts as a second results controller. It validates a stricter result contract, including `masteryBand`, then issues `MAXESS_ISOLATION_RELEASE`, plus cross-frame messages. fileciteturn1173file0L2-L10

### E01–E04
These sections actively depend on the MAXESS result. E01 hydrates the score/report experience; E02 declares `window.MAXESS_RESULT` authoritative; E03 declares `window.MAXESS_RESULT` authoritative; E04 reads the result and derives Direction. fileciteturn1174file0L1-L2 fileciteturn1175file0L1-L2 fileciteturn1176file0L1-L2 fileciteturn1177file0L2-L2

### E05–E09
These are predominantly presentation/content/offer sections. Their main risk is downstream visibility, layout, and navigation rather than score computation. fileciteturn1178file0L1-L2 fileciteturn1179file0L1-L2 fileciteturn1180file0L1-L2 fileciteturn1181file0L1-L2 fileciteturn1182file0L1-L10

## PRIMARY HYPOTHESIS

The biggest problem is not line count. It is **multiple authorities communicating through partially overlapping contracts and events**.

Observed:

`E00.01` can release.

`E00.03` can release.

`E00.02` controls visual release.

E01–E04 have different recovery paths.

That is enough architectural complexity to create race conditions and “works alone / fails together” behavior.

## TARGET

### Single source of truth

`window.MAXESS_RESULT`

with durable `sessionStorage` recovery.

### Single contract

`MAXESS_RESULT_V1`

### Single release authority

`E00.03`

### Single visual gate

`E00.02`

### Downstream consumers

`E01 → E09`

## PLAN

### Phase 1 — Establish truth

1. Diff E00 796 vs E00 1800.
2. Inspect the actual live E118 code.
3. Identify the exact object E00 produces at Q15.
4. Record the complete result schema.
5. Identify every writer of `window.MAXESS_RESULT`.
6. Identify every writer of `sessionStorage` result state.
7. Identify every result-related event producer/consumer.

### Phase 2 — Collapse authority

8. Select one E00 implementation as the scoring baseline.
9. Make E00 the only scorer/result producer.
10. Make E00.01 an adapter/bridge only.
11. Make E00.03 the only release controller.
12. Make E00.02 the only visual release gate.
13. Normalize all result consumers to the same contract.

### Phase 3 — Make ordering deterministic

14. Ensure result is stored before release events fire.
15. Ensure every consumer can recover current state if it misses an event.
16. Ensure duplicate release is harmless and observable.
17. Ensure cross-frame messaging is consistent and safe.

### Phase 4 — Verify end-to-end

18. Test Q1 → Q15.
19. Test score calculation.
20. Test result contract.
21. Test release.
22. Test E01.
23. Test E02.
24. Test E03.
25. Test E04.
26. Test E05–E09 visibility and continuity.
27. Test refresh / late initialization.
28. Test mobile widths.

### Phase 5 — Preserve and document

29. Record canonical E00.
30. Mark superseded candidates clearly.
31. Update project feed.
32. Create final handoff.

## DO NOT DO

- Do not redesign E01–E09 while the engine is broken.
- Do not add another scoring engine.
- Do not add another result contract.
- Do not solve event ordering with unbounded polling.
- Do not declare success without live-path verification.

## DEFINITION OF DONE

A real 15-question run produces one result object, one release, and every downstream section renders from that same result.
