# MAXESS — MASTER ENGINEERING + DESIGN DIRECTIVE V1

**Status:** ACTIVE / CANONICAL FOR THE MAXESS REBUILD
**Date:** 2026-08-26
**Project:** MAXESS / Naya Power
**Authority:** Human-approved North Star + Naya Power governing law
**Purpose:** Give every engineer, designer, AI, QA system, and future Naya the same complete understanding of what MAXESS is, how it must be built, and what 10/10 means.

---

## 01 — THE NORTH STAR

MAXESS is a universal capability-assessment and learning machine for AI and life-related knowledge.

A person should be able to:

**ENTER A TOPIC → RECEIVE A FAIR ASSESSMENT → LEARN WHILE TAKING IT → GET A REAL SCORE → UNDERSTAND THE RESULT → KNOW WHAT TO IMPROVE → CONTINUE LEARNING.**

The flagship example is **AI Score / AI Mastery Assessment**. It remains the golden reference assessment with its existing 15 questions, five dimensions, five answers per question, and 0–4 scoring values. The dynamic engine must reproduce that assessment exactly before the AI Score is considered migrated.

MAXESS may eventually assess many subjects within the supported AI/life knowledge universe, including advanced technical topics such as quantum computing. MAXESS does not claim to replace domain experts or achieve perfect depth in every specialized field. It optimizes for extraordinary usefulness to the majority of people, honest coverage boundaries, fair assessment, learning value, and continuous improvement.

---

## 02 — THE HUMAN EXPERIENCE

The product must feel like a **beautiful heart built an extraordinarily powerful machine**.

It must simultaneously feel:

- high-tech;
- intelligent;
- precise;
- fast;
- powerful;
- premium;
- alive;
- warm;
- human;
- inviting;
- encouraging;
- trustworthy;
- simple to use.

The desired emotional sequence is:

**CURIOSITY → WELCOME → ENGAGEMENT → DISCOVERY → RECOGNITION → CLARITY → EMPOWERMENT → NEXT ACTION.**

The user must never feel judged, tricked, overwhelmed, or forced to understand the underlying technology.

---

## 03 — ONE MACHINE, NOT A COLLECTION OF PATCHES

E00, E00.01, E00.02, E00.03, and E01–E09 are source material and lessons, not sacred implementation boundaries.

Preserve their proven behavior and knowledge. Do not preserve unnecessary complexity merely because it already exists.

The rebuild should converge toward:

**ONE MAXESS APPLICATION → ONE AUTHORITATIVE STATE MACHINE → ONE ASSESSMENT ENGINE → ONE SCORING ENGINE → ONE RESULT CONTRACT → ONE RELEASE PATH → MANY PRESENTATION SECTIONS.**

No competing scorers. No competing result authorities. No timing-dependent handshakes. No unnecessary retry loops. No duplicated completion paths. No multiple components independently deciding that an assessment is complete.

`MAXESS_RESULT_V1` remains the stable result interface unless a deliberately versioned successor is introduced.

---

## 04 — SOURCE MATERIAL TO HARVEST

The rebuild must inspect and learn from:

- `E00 796` — current full executable assessment engine;
- `E00.01` — result validation, bridge, terminal lessons;
- `E00.02` — isolation/release lessons;
- `E00.03` — result-controller/release lessons;
- `E01`–`E09` — results experience and presentation;
- `E01-SECTION-01-WORKING.html` — working Section 01 reference;
- `MAXESS-RESULT-CONSUMER-V1.html` and V2;
- `MAXESS-RESULT-INTEGRATION.md`;
- `MAXESS-RESULTS-INTEGRATED-V1.html`;
- existing MAXESS directives, change ledger, execution logs, smart notes, and recovery notes;
- Naya Power knowledge banks and universal assessment material;
- HMC/MAXIS button and icon specifications;
- Naya Master Coder and Designer laws;
- Superbrain/SOM(E)/Oscar verification laws.

The rule is:

**LEARN FROM EVERYTHING → KEEP THE GOOD → REMOVE THE FRAGILE → UNIFY THE AUTHORITY → VERIFY.**

---

## 05 — DYNAMIC ASSESSMENT COMPILER

Runtime assessment generation must not require an LLM API as a mandatory dependency.

The primary model is deterministic, rules-based compilation from structured knowledge.

Pipeline:

**TOPIC INPUT
→ DOMAIN RESOLUTION
→ KNOWLEDGE MAP
→ LEARNING OBJECTIVES
→ DIMENSION SELECTION
→ QUESTION ARCHETYPES
→ RUBRIC CONSTRUCTION
→ 15-QUESTION ASSESSMENT CONFIG
→ VALIDATION
→ RUNTIME.**

The knowledge bank should describe concepts, relationships, common misunderstandings, applications, limitations, learning objectives, aliases, difficulty, and coverage confidence.

The engine should not attempt to store every possible question. It should store enough structured domain knowledge and question-generation rules to produce strong assessments deterministically.

---

## 06 — UNIVERSAL CAPABILITY MODEL

MAXESS uses reusable capability dimensions rather than a separate scoring architecture for every topic.

Candidate universal capabilities include:

1. **UNDERSTAND** — explain the subject and core concepts.
2. **CONTEXTUALIZE** — understand why it matters, where it fits, and when it applies.
3. **APPLY** — use the knowledge in practical situations.
4. **EVALUATE** — judge quality, limitations, tradeoffs, errors, risks, and evidence.
5. **CREATE / IMPROVE** — use the knowledge to build, transform, diagnose, or improve something.

The engine selects the five most useful dimensions for the requested topic. Existing AI Score dimensions remain authoritative for the flagship assessment:

**Direction · Communication · Evaluation · Iteration · Systems Thinking.**

A topic may therefore have different dimension names while retaining the same underlying capability/scoring framework.

---

## 07 — QUESTION ARCHETYPES

Use multiple assessment forms so the product tests capability rather than self-confidence alone.

Approved archetypes include:

**DEFINE · EXPLAIN · DISTINGUISH · IDENTIFY · APPLY · DIAGNOSE · COMPARE · SEQUENCE · CHOOSE · EVALUATE · DESIGN · IMPROVE.**

A 15-question assessment should deliberately cover the chosen dimensions and learning objectives. Questions should be understandable to ordinary people while still discriminating meaningfully between capability levels.

Questions must be:

- relevant;
- unambiguous;
- answerable from the supported knowledge scope;
- fair;
- non-trick-based unless the objective specifically requires misconception detection;
- concise;
- educational;
- capable of distinguishing levels of understanding.

---

## 08 — THE 0–4 RUBRIC

Every question has five scored answer states:

**0 · 1 · 2 · 3 · 4**

The numbers are internal capability values, not arbitrary confidence labels.

General interpretation:

- **0** — no meaningful demonstrated capability;
- **1** — beginning awareness;
- **2** — functional/basic capability;
- **3** — strong practical capability;
- **4** — advanced/mastery-level capability within the assessment scope.

The exact answer wording must be topic-specific. Each answer must represent a logically defensible capability level.

Scoring must remain deterministic and mathematically auditable.

---

## 09 — SCORE NORMALIZATION

The canonical normalized output is **0–100**.

For the flagship 15×0–4 model:

**maximum raw score = 60**

**overallScore = round(rawScore / 60 × 100)**

Each of five dimensions contains three questions:

**dimensionScore = round(dimensionRaw / 12 × 100)**

No score may be invented, manually injected, or generated from presentation code.

Mastery-band thresholds must be centrally defined and used consistently across the engine and results experience.

---

## 10 — STATE MACHINE

The runtime must have one explicit state machine.

Minimum states:

**IDLE → INTRO → QUESTION → ANSWERED → ADVANCING → COMPLETE → RESULT_READY → RESULTS → ERROR/RECOVERABLE.**

Rules:

- an answer cannot be saved without a valid question and valid answer;
- Continue cannot advance without a selected answer;
- each question can contribute exactly once to the final response set;
- Q15 completion must save the answer before result calculation;
- completion is a state transition, not a timing race;
- result calculation occurs exactly once per assessment completion;
- result validation occurs before release;
- results consume the same authoritative result object;
- failed handoff must not erase a valid local result.

---

## 11 — RESULT CONTRACT

`MAXESS_RESULT_V1` is the authoritative result contract.

Minimum authoritative fields:

- contractVersion;
- assessmentId;
- assessmentVersion;
- completedAt;
- overallScore;
- masteryBand;
- five dimensions with scores;
- dimensionScores;
- strongestDimension;
- opportunityDimension;
- responses;
- selectedInterests where applicable;
- Naya interpretation metadata;
- audio metadata where applicable.

The contract must be validated structurally and semantically before Results release.

Results must never create a second score.

---

## 12 — NAYA PRESENCE

Naya is a participant in the experience, not decoration.

She should feel:

**PRESENT · ATTENTIVE · WARM · INTELLIGENT · ENCOURAGING · TRUSTWORTHY.**

Use approved Naya imagery from the project. Do not substitute arbitrary portraits.

Her visual treatment should include controlled depth, lighting, and presence without becoming distracting.

Naya interaction states should distinguish, where useful:

**IDLE · ATTENTIVE · SPEAKING · LISTENING · CELEBRATING.**

Her copy must help the user understand what is happening and why it matters.

---

## 13 — SIGNATURE JEWEL INTERACTION SYSTEM

The MAXESS answer buttons are signature brand objects.

They must feel like luminous jewelry or precision-crafted controls rather than generic web buttons.

Each major interactive object must define:

**PURPOSE · MATERIAL · GEOMETRY · TYPOGRAPHY · LIGHTING · DEPTH · IDLE · HOVER · FOCUS · PRESSED · SELECTED · DISABLED · MOTION · ACCESSIBILITY.**

Required interaction psychology:

- **hover = invitation**;
- **press = physicality**;
- **selection = confirmation**;
- **transition = progress**;
- **score reveal = discovery**.

The selected jewel should visibly come alive: controlled luminance, depth, edge definition, and subtle motion. Effects must remain restrained enough to preserve clarity and performance.

Do not ship flat primary controls, arbitrary Unicode as premium iconography, uncontrolled neon, excessive blur, or decorative effects that compete with the task.

---

## 14 — VISUAL SYSTEM

Foundation:

**deep black · white typography · electric/luminous purple · semantic dimension accents · controlled gold for earned milestones.**

Visual hierarchy must always answer:

**WHERE AM I? → WHAT IS BEING ASKED? → WHAT DO I DO? → WHAT HAPPENED? → WHAT NEXT?**

Every major scene has one primary attention owner.

Use the existing MAXESS principles of:

**HEADLINE → SUPPORTING STATEMENT → DETAIL**

and:

**CAKE → ICING → ICE CREAM → CHERRY → CARAMEL → WHIPPED CREAM → SPRINKLES.**

The additional layers must earn their place. More does not automatically mean better.

---

## 15 — PERFORMANCE LAW

Performance is part of design quality.

Optimize for:

- minimal runtime dependencies;
- minimal unnecessary DOM;
- deterministic state transitions;
- event delegation where appropriate;
- no polling;
- no arbitrary timer-based correctness;
- no redundant storage writes;
- no repeated computation when results are already known;
- CSS transform/opacity for animation;
- efficient asset loading;
- responsive rendering;
- reduced-motion support;
- graceful failure.

The user should feel that MAXESS responds immediately.

The machine must do complexity internally so the human experiences simplicity.

---

## 16 — RESPONSIVE + ACCESSIBLE BY DEFAULT

Design and test for at least:

**320 · 360 · 375 · 390 · 414 · 480 · 600 · 768 · 900 · 1024 · 1280px.**

Required:

- keyboard navigation;
- visible focus;
- semantic controls;
- correct ARIA state;
- screen-reader meaningful labels;
- sufficient contrast;
- reduced-motion behavior;
- touch targets appropriate for mobile;
- no horizontal overflow;
- no critical information hidden by viewport constraints.

Accessibility is not a final patch.

---

## 17 — TOPIC COVERAGE AND HONEST LIMITS

MAXESS must classify topic coverage before attempting an assessment.

Coverage states may include:

**STRONG · GOOD · DEVELOPING · LIMITED · UNSUPPORTED.**

For limited/unsupported topics, do not fabricate authority. Give the user an honest message explaining that MAXESS is still developing depth in that area.

The product may continue improving its coverage over time. New knowledge and successful assessment patterns become reusable system knowledge.

---

## 18 — LEARNING-FIRST ASSESSMENT DESIGN

The assessment is not merely a measurement instrument.

It should help the user learn while taking it.

Each question should ideally provide enough context, wording, feedback, or Naya explanation to increase understanding without compromising the integrity of the assessment.

The final experience should produce:

**MEASURE → UNDERSTAND → LEARN → IMPROVE.**

Results should identify strengths, opportunities, capability patterns, and the next best learning action.

---

## 19 — SMART NOTES ARE DEFAULT PROJECT BEHAVIOR

Every meaningful MAXESS mastermind/work session should be evaluated for durable learning.

When valuable, record:

**DECISION · DISCOVERY · LESSON · DESIGN PRINCIPLE · FAILURE · SAFEGUARD · PERFORMANCE INSIGHT · UX INSIGHT · ARCHITECTURE INSIGHT · NEXT ACTION.**

Do not record conversational noise. Do record durable knowledge that another AI could use to make a better decision later.

The canonical memory architecture remains the Naya Power Note Event system. Project context must connect:

**WORK → DECISIONS → DISCOVERIES → LESSONS → ARTIFACTS → RECEIPTS → NEXT ACTIONS.**

Every meaningful execution should leave a **NEXT EXECUTION** continuation artifact.

---

## 20 — OSCAR 10/10 CHALLENGE

Before declaring any major component complete, independently ask:

> **WHY IS THIS NOT A 10?**

Challenge:

- correctness;
- completeness;
- source authority;
- scoring validity;
- state transitions;
- edge cases;
- performance;
- visual hierarchy;
- button quality;
- Naya presence;
- copy quality;
- accessibility;
- responsive behavior;
- security;
- maintainability;
- live parity;
- evidence quality.

A 10 may not be claimed merely because the code looks good.

---

## 21 — EVIDENCE LAW

MAXESS is complete only when evidence demonstrates the actual product works.

Acceptance chain:

**REQUIREMENT → IMPLEMENTATION → TEST → OBSERVED RESULT → EVIDENCE → VERIFICATION → DOCUMENTED STATE.**

Minimum flagship evidence:

1. initial load;
2. Naya arrival;
3. Q1 answer selection;
4. Continue transition;
5. all 15 questions;
6. every answer can be selected;
7. exactly 15 responses saved;
8. Q15 terminal transition;
9. correct raw and normalized score;
10. valid `MAXESS_RESULT_V1`;
11. Results release;
12. E01–E09 consume the same result;
13. AI Score reproduces the known golden assessment;
14. dynamic secondary topic compiles successfully;
15. unsupported/advanced topic boundary behaves honestly;
16. responsive checks pass;
17. accessibility checks pass;
18. no competing result authority remains;
19. live/browser behavior matches source;
20. receipt and current state are documented.

---

## 22 — BUILD ORDER

Do not polish blindly before architecture is correct.

Build in this order:

**A. SOURCE + KNOWLEDGE INVENTORY**

**B. UNIVERSAL SCHEMA**

**C. DYNAMIC ASSESSMENT COMPILER**

**D. SINGLE STATE MACHINE**

**E. SINGLE SCORING ENGINE**

**F. RESULT CONTRACT + VALIDATION**

**G. FLAGSHIP AI SCORE GOLDEN TEST**

**H. PREMIUM RUNTIME UI**

**I. NAYA PRESENCE + TEACHING**

**J. RESULTS EXPERIENCE**

**K. QUANTUM COMPUTING / SECOND-DOMAIN TEST**

**L. PERFORMANCE + ACCESSIBILITY + RESPONSIVE PASS**

**M. OSCAR PASS**

**N. LIVE END-TO-END VERIFICATION**

**O. RECEIPT + FREEZE + NEXT EXECUTION.**

---

## 23 — REFACTOR DECISION RULE

When choosing between keeping a legacy component and replacing it, ask:

1. Does it contain proven behavior worth preserving?
2. Does it create duplicated authority?
3. Does it introduce timing/order dependency?
4. Can the behavior be represented more simply?
5. Will replacement improve reliability without losing required behavior?
6. Can the replacement be tested more completely?

If a unified implementation is materially better, **replace it**. The objective is successful, verified product behavior—not historical code preservation.

---

## 24 — DEFINITION OF 10/10

MAXESS reaches the 10/10 target when the evidence supports all of the following:

**INTELLIGENCE** — useful, coherent, fair assessments.

**ARCHITECTURE** — one clear authority model with no unnecessary competing paths.

**CORRECTNESS** — deterministic scoring and validated results.

**PERFORMANCE** — fast, responsive, efficient.

**UX** — obvious, effortless, low cognitive load.

**VISUAL** — extraordinary, elegant, intentional, premium.

**INTERACTION** — tactile, luminous, alive, rewarding.

**NAYA** — present, warm, human, helpful.

**ACCESSIBILITY** — usable by the broadest practical audience.

**RESPONSIVENESS** — excellent from phone through desktop.

**TRUST** — honest about evidence and limitations.

**LEARNING** — users gain understanding, not merely a number.

**EXTENSIBILITY** — new topics can be assessed without rebuilding the engine.

**MAINTAINABILITY** — future AIs can understand and safely improve it.

**CONTINUITY** — meaningful learning is preserved in Naya Power memory.

**VERIFICATION** — completion is backed by receipts and observed evidence.

---

## 25 — THE MASTER QUESTIONS

Every engineer and designer should continuously ask:

> **Can this be faster?**
>
> **Can this be simpler?**
>
> **Can this be clearer?**
>
> **Can this be more beautiful?**
>
> **Can this interaction feel more alive?**
>
> **Can Naya feel more present?**
>
> **Can this be warmer?**
>
> **Can this be more trustworthy?**
>
> **Can this be more accessible?**
>
> **Can this be more resilient?**
>
> **Can this feel more effortless?**
>
> **What would make this a 10?**
>
> Then test the answer.

---

## 26 — MASTER OPERATING LOOP

**READ → MAP → SOURCE-LOCK → INVENTORY → DEFINE → ARCHITECT → BUILD → TEST → OSCAR → FIX → RETEST → VERIFY → RECEIPT → LEARN → PRESERVE → IMPROVE.**

And system-wide:

**SYNERGIZE → OPTIMIZE → MAXIMIZE → EQUALIZE → VERIFY → LEARN → SYNERGIZE AGAIN.**

---

## 27 — FINAL DIRECTIVE

Build MAXESS as though billions of people could eventually use it.

Do not optimize for the current workaround.

Do not optimize for preserving legacy code.

Do not optimize for impressive source size.

Optimize for:

**HUMAN VALUE + RELIABILITY + SPEED + BEAUTY + SIMPLICITY + LEARNING + TRUST + EXTENSIBILITY + VERIFIED EXCELLENCE.**

The machine may be sophisticated.

The experience must be simple.

The technology may be powerful.

The human experience must be warm.

The interface may be extraordinary.

The claims must remain truthful.

**Make the machine magnificent. Make the experience effortless. Make the result trustworthy. Make the learning useful. Then prove it works.**
