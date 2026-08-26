# 🔱 MAXESS V2 — SOURCE + ARCHITECTURE INVENTORY

**Date:** 2026-08-26  
**Authority:** MAXESS Master Engineering Design Directive V2  
**Truth standard:** green means proven, not promised

## Executive finding

The repository contains excellent visual/product work and substantial working assessment logic, but the current system is **not one machine**. It is a lineage of E00 variants plus multiple result bridges/consumers and repair workflows. The correct move is a coherent re-architecture, not another patch.

The three main E00 variants are useful source material:

- `E00 796` — strongest current assessment UX/interaction lineage and direct result release.
- `E00 700` — compact flow with deterministic 15-question scoring.
- `E00 1800` — strongest teaching/completion narrative, but it retains a separate terminal gate.

`E00.01`, `E00.02`, and `E00.03` are bridge/isolation/controller experiments. They are valuable forensic evidence, but should not remain runtime authorities after unified E00 integration.

The Results lineage contains strong section design, but E01/E02/E09 and the V2 result consumer contain fallback/polling/storage logic. That is precisely the architecture the V2 directive forbids.

## Source matrix

| Source | Best value | Problem discovered | Rebuild decision |
|---|---|---|---|
| E00 796 | Best current UX, 15×0–4 config, dimension scoring, progress, answer interaction | UI/state/engine mixed; persistence and legacy handoff | Primary design source; reimplement against pure engine |
| E00 700 | Clean compact flow and scoring | Page-owned state and release assumptions | Reuse interaction ideas |
| E00 1800 | Teaching context and terminal concepts | Separate terminal completion gate | Reuse teaching; remove gate as authority |
| E00.01 | Bridge/handoff diagnostics | Cross-document/timing dependency | Retire runtime authority |
| E00.02 | Runtime isolation experiment | Workaround for competing state | Retire after unified E00 |
| E00.03 | Controller/diagnostic knowledge | Creates another authority layer | Convert useful diagnostics to tests |
| E01 | Premium score reveal | Polling/fallback result acquisition | Keep visual; direct contract only |
| E01-SECTION-01-WORKING | Strong Section 01 baseline | Consumer should not own acquisition | Preserve visual/reference lineage |
| E02 | Strong dimension presentation | Polling + duplicate consumer logic | Keep visual; direct contract only |
| E03 | Personalized analysis | Consumer-side hydration concerns | Keep presentation; direct contract |
| E04 | Capability/direction experience | Must not derive score | Keep presentation; direct contract |
| E05 | Solution/insight presentation | Mostly static | Keep and harden boundary |
| E06 | Excellent Naya/Supercharger presentation | Needs deterministic result context | High-value visual asset; rewire |
| E07 | Conversion/continuation experience | Not a result authority | Keep product flow; contract boundary |
| E08 | NayaNET/ecosystem continuation | Presentation-only | Keep visual/product work |
| E09 | Final CTA/continuation | Legacy consumer/fallback behavior | Keep UX; strip alternate acquisition |
| MAXESS-RESULT-INTEGRATION.md | Useful bridge documentation | Bridge exists because authority is missing | Reference; replace bridge authority |
| MAXESS-RESULT-CONSUMER-V1/V2 | Useful hydration experiments | Multiple fallback sources, polling | Retire after direct contract integration |
| MAXESS-RESULTS-INTEGRATED-V1 | Large integrated Results source | Monolith + mixed consumer assumptions | Preserve as source/visual lineage, not authority |

## Mathematical truth

The canonical AI Score model is already correct and should remain the golden regression:

```text
15 questions
× maximum answer value 4
= 60 maximum raw points

normalized = round(raw / 60 × 100)
```

There are five dimensions with three questions each, so each dimension has a maximum of 12.

The problem is **not the mathematics**. The problem is **where authority lives**.

## Competing authority discovered

The source lineage contains multiple possible sources of truth:

- E00 page-local state;
- E00 result construction;
- E00.01 bridge state;
- E00.02 isolated runtime state;
- E00.03 controller state;
- result-consumer fallbacks;
- localStorage/sessionStorage;
- URL/query state;
- polling;
- legacy `window.MAXESS_RESULT` globals;
- Results-side hydration;
- repair workflows for Continue, terminal state, handoff, and bridges.

These are evidence of an architectural gap, not independent product features.

## Authoritative target

```text
TOPIC / ASSESSMENT DEFINITION
        ↓
E00 STATE MACHINE
        ↓
QUESTION RENDERER
        ↓
ANSWER CAPTURE
        ↓
RESPONSE STORE
        ↓
SCORING ENGINE
        ↓
RESULT VALIDATOR
        ↓
FROZEN MAXESS_RESULT_V1
        ↓
ONE RELEASE
        ↓
E01 → E02 → E03 → E04 → E05 → E06 → E07 → E08 → E09
```

No downstream section becomes a second engine.

## E00 state target

```text
READY
  ↓
QUESTION_ACTIVE
  ↓
ANSWER_SELECTED
  ↓
QUESTION_ACTIVE
  ↓
...
  ↓
ANSWER_SELECTED (Q15)
  ↓
SCORING
  ↓
RESULT_FINALIZED
```

The final valid answer completes the assessment. No second scoring authority and no timing-dependent terminal choreography.

## Result contract

`MAXESS_RESULT_V1` is now explicitly locked as the assessment → Results interface. It carries assessment identity/version, topic, participant, responses, overall score, mastery band, dimensions, strongest/opportunity dimensions, fingerprint, interests, Naya/audio metadata, integrity versions, and completion time.

Full contract: `PROJECTS/MAXESS/ENGINEERING/MAXESS-RESULT-V1-CONTRACT.md`.

## First coherent implementation

A pure E00 engine core now exists at:

`PROJECTS/MAXESS/ENGINEERING/MAXESS-E00-AUTHORITATIVE-ENGINE-V1.js`

It intentionally contains no DOM, storage, URL scraping, timers, polling, or bridges. It provides configuration-driven questions/dimensions, deterministic 0–4 validation, response storage, scoring, result construction, validation, and deep-frozen result output.

This is the **architectural core**, not yet the final live Groove embed.

## Dynamic assessment finding

The universal assessment vision fits the engine, but one truth must remain explicit:

**A deterministic zero-LLM scoring engine is straightforward. Arbitrary-topic assessment generation is not magically possible without a source of knowledge/rubric material for that topic.**

Therefore dynamic compilation must separate:

```text
TOPIC
→ COVERAGE
→ KNOWLEDGE SOURCE
→ LEARNING OBJECTIVES
→ DIMENSIONS
→ QUESTION ARCHETYPES
→ RUBRIC
→ ASSESSMENT DEFINITION
→ E00
```

AI Score is the golden assessment. A dynamic topic is green only when sufficient trusted knowledge/rubric coverage exists. Unsupported or excessively advanced topics must return an explicit “not there yet” state rather than fabricate content.

## Design/performance findings

The strongest existing visual assets include jewel-like answer controls, premium purple/black treatment, dimensional cards, Naya presence, score/orb treatment, strong section storytelling, responsive patterns, and motion feedback.

The flagship design pass should **unify** these strengths rather than copy nine divergent component systems. Visual effects must never become correctness dependencies.

## Repair-workflow finding

The number of repair workflows for Continue, terminal state, handoff, hydration, isolation, and integrated Results is itself diagnostic evidence. Future changes should converge on the authoritative engine and contract. Historical workflows remain valuable forensic evidence and regression clues.

## Status

### 🟢 Proven

- E00 and E01–E09 canonical artifacts exist.
- AI Score is 15 × 0–4 with five dimensions.
- Results contain substantial reusable design value.
- Universal-assessment/knowledge-bank direction exists.
- Pure E00 engine core exists.
- MAXESS_RESULT_V1 is documented.

### 🟡 Needs integration/verification

- Connect engine to canonical E00 visual shell.
- Build AI Score definition against engine.
- Replace consumer hydration/polling with direct contract injection.
- Rewire E01–E09 to the contract.
- Verify Q1→Q15→E01→E09.
- Complete responsive/accessibility/performance QA.

### 🔴 Not green

- Live end-to-end application.
- Production E00 replacement.
- Complete E01–E09 contract integration.
- Dynamic topic runtime.
- 10/10 visual/product verification.

## Authoritative rebuild decision

**Do not choose one old E00 file as the winner.** Build the new E00 from the strongest combined lineage:

- E00 796 → current interaction/UX;
- E00 700 → compact flow;
- E00 1800 → teaching concepts;
- E00.01–03 → failure knowledge/diagnostics;
- E01–E09 → Results presentation;
- MAXESS/Naya design laws → flagship visual system.

The old artifacts remain preserved as source material and forensic lineage. The new engine and contract become the authority.
