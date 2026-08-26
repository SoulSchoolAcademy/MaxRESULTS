# MAXIS — PROJECT SOURCE OF TRUTH

**Project:** MAXESS / MAXIS Assessment Engine + Results Experience
**North Star:** Make the complete E00 → E09 experience function as one coherent page, with one authoritative result contract and deterministic handoffs.
**Status:** RECOVERY / ENGINEERING MODE
**Canonical live E00:** User states the currently live code is E118. Do not replace it blindly.

## Source artifacts

The current root-level source artifacts supplied for this project are:

- `E00 1800` — E00 assessment candidate
- `E00 796` — E00 assessment candidate
- `E00.01` — results bridge / result release bridge
- `E00.02` — isolation CSS + visual release controller
- `E00.03` — results controller / handoff controller
- `E01` — score reveal / personal report
- `E02` — five dimensions
- `E03` — personal report letter
- `E04` — direction spectrum
- `E05` — AI friction / familiarity
- `E06` — Naya Supercharger / 9-node + boards experience
- `E07` — cinematic conversion / video CTA
- `E08` — Human Maximus Codex ecosystem
- `E09` — membership preview

## Important architecture rule

These are **not independent pages**. They form one runtime system. The critical dependency chain is:

`E00 scoring → canonical MAXESS_RESULT_V1 → release boundary → E01–E09 hydration/reveal`

The immediate engineering priority is therefore **contract and communication correctness**, not visual redesign.

## Current verified observations

- `E00.01` defines contract `MAXESS_RESULT_V1` and validates `overallScore`, exactly 5 dimensions, and exactly 15 responses before releasing results. It can read from `window.MAXESS_RESULT` or `sessionStorage`. fileciteturn1171file0L2-L10
- `E00.02` establishes a `waiting/released` document state and hides E01–E09 while waiting. It listens for `MAXESS_ISOLATION_RELEASE` and then releases result sections. fileciteturn1172file0L2-L10
- `E00.03` defines itself as the results controller and requires `MAXESS_RESULT_V1`, a valid 0–100 score, a recognized mastery band, 5 dimensions, and 15 responses before issuing `MAXESS_ISOLATION_RELEASE`. fileciteturn1173file0L2-L10
- `E01` is a substantial self-contained result-reveal section and is explicitly designed to hydrate from the result. fileciteturn1174file0L1-L2
- `E02` explicitly declares `window.MAXESS_RESULT` as its runtime authority. fileciteturn1175file0L1-L2
- `E03` explicitly declares `window.MAXESS_RESULT` as runtime authority and prohibits demo/fallback results. fileciteturn1176file0L1-L2
- `E04` reads `window.MAXESS_RESULT`, parent/top windows, session storage, and result events; it derives a Direction score from the result. fileciteturn1177file0L2-L2
- `E05` is primarily content/presentation and is not presently the critical scoring bridge. fileciteturn1178file0L1-L2
- `E06` is primarily presentation/content with its own large visual system. fileciteturn1179file0L1-L2
- `E07` is primarily a cinematic conversion/video section. fileciteturn1180file0L1-L2
- `E08` is primarily the Human Maximus ecosystem/offer section. fileciteturn1181file0L1-L2
- `E09` is primarily a membership preview/CTA section. fileciteturn1182file0L1-L10

## Primary engineering diagnosis

The system currently has **multiple result-release authorities and multiple communication paths**. That is the strongest architectural risk.

In particular:

1. E00.01 can release results itself.
2. E00.03 also acts as a release controller.
3. E00.01 validates a smaller contract than E00.03.
4. E00.02 owns visual release but depends on an event emitted elsewhere.
5. E04 can independently read several result locations/events.
6. Different sections therefore have different ideas about how the authoritative result arrives.

This creates ordering, contract-shape, duplicate-event, and cross-embed synchronization risk.

## Target architecture

There must be exactly **one canonical result producer**, exactly **one canonical result contract**, and exactly **one release boundary**.

Recommended target:

`E00 → MAXESS_RESULT_V1 → E00.03 Controller → E00.02 Release Gate → E01–E09`

E00.01 should become a bridge/adapter only. It should not compete with E00.03 as an independent release authority.

## Working rule

Do not make broad visual changes until the engine passes the full communication chain. Preserve the existing visual work wherever possible; repair the smallest architectural surface that makes the system deterministic.

**Next execution:** diff E00 candidates, establish the exact result schema emitted by E00, normalize the controller contract, then test E00 → E00.01 → E00.03 → E00.02 → E01–E09.