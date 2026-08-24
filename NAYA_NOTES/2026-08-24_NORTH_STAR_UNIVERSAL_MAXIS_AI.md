# NAYA SMART NOTE — NORTH STAR: UNIVERSAL MAXIS + NAYA POWER

**Date:** 2026-08-24  
**Owner:** Shawn  
**Canonical spelling:** SHAWN (S-H-A-W-N)  
**Status:** NORTH STAR / PRODUCT DIRECTION  
**System:** Naya Power / MAXIS / CISS

## 1. NORTH STAR

Build MAXIS into a universal, config-driven assessment and mastery engine capable of assessing essentially any user-specified subject or topic, while Naya Power becomes the continuing intelligence/learning relationship that helps the person learn, remember, practice, create, improve, and reassess.

The public experience should be extremely simple:

1. Enter name.
2. Enter the subject/topic.
3. Optionally speak the topic.
4. Start a free assessment.
5. Receive immediate personalized results in the person's name.
6. See score, mastery level, dimensions, and useful feedback.
7. Be invited to use Naya Power to learn and improve the subject.

Core promise:

> Give Naya a subject. She helps you learn it. MAXIS measures where you are. You improve. You can reassess. Your progress compounds.

## 2. PRODUCT STACK

### Naya
The intelligent teacher/companion. She explains, teaches, researches, remembers, guides, adapts, and helps the user create.

### Naya Power
The overall AI relationship/platform: learn, create, grow, remember, and compound intelligence over time.

### MAXIS
The measurement/mastery engine. It generates or consumes assessment configurations, presents questions, captures responses, calculates scores, assigns mastery levels, produces reports, and eventually supports achievement/certificate generation.

### CISS — Compounding Intelligence System
The operating system/methodology connecting learning, memory, assessment, improvement, creation, and repeated growth.

### Naya Power Academy
The learning and achievement/recognition layer, including future certificates of excellence/mastery and verification.

## 3. CURRENT PRODUCT THESIS

The existing AI Score is the lead experience, not the final product.

Current concept:

`AI Score / Assessment -> immediate value -> discover current capability -> invite Naya Power`

North-star concept:

`Choose subject -> Learn with Naya -> Practice -> MAXIS assessment -> Score -> Diagnose -> Improve -> Reassess -> Recognize achievement -> Remember -> Compound`

MAXIS should NOT become a collection of separately hard-coded assessments. It should become one reusable engine capable of consuming generated assessment blueprints for many subjects.

## 4. LANDING PAGE NORTH-STAR UX

Primary above-the-fold interaction should be obvious and minimal:

- **Your name:** [input]
- **What would you like to be assessed on?** [type or speak]
- Primary action: **Start My Free Assessment**

Suggested helper text:

> The more precise you are, the more accurate your assessment can be. Type or speak the subject or topic you want to be assessed on.

Positioning:

> **A free 3-minute assessment. Get immediate results. See your score, your current level, and personalized feedback.**

The user's name is part of the assessment/report identity so the result feels personal rather than generic.

Examples:

- `Jordan — Algebra`
- `Maria — Conversational Spanish`
- `Alex — JavaScript Fundamentals`
- `Sam — World War II`
- `Taylor — Digital Marketing`

The topic field should accept natural language, not require a rigid taxonomy.

## 5. ACCURACY PRINCIPLE

The system should explicitly communicate that specificity improves assessment quality.

Example:

> **Be as specific as you can.** “Physics” gives us a broad target. “High-school introductory mechanics: forces, motion, energy and momentum” gives us a much more precise assessment target.

This is important because arbitrary-topic assessment requires a defined scope. Naya should normalize the user's topic into an assessment specification before MAXIS generates questions.

## 6. REQUIRED ARCHITECTURE

Separate the system into these layers:

`User Input`
`-> Subject Normalization / Scope Definition`
`-> Assessment Blueprint Generator`
`-> MAXIS Assessment Engine`
`-> Response Capture`
`-> Independent Scoring Engine`
`-> Results Contract`
`-> Results UI / Report`
`-> Naya Learning Invitation`

MAXIS must not care whether the subject is mathematics, coding, history, language, music, business, science, etc. It should consume a valid assessment configuration.

Canonical conceptual assessment object:

```text
Assessment
  subject
  scope
  learner
  dimensions[]
  questions[]
    id
    dimensionId
    order
    question
    answers[]
      id
      title
      description
      score
      weight
      accent
    weight
    metadata
  scoringRules
  masteryBands
  version
  metadata
```

Scoring must remain independent of presentation/UI.

## 7. CURRENT CODE FINDINGS — IMPORTANT

The current `E00 118` artifact is a substantial MAXIS assessment UI foundation. It already contains a full visual shell, progress system, Naya interaction, question presentation, answer cards, selection states, continue control, responsive layout, dialogs, and a local results area. The artifact is therefore valuable and should be preserved rather than discarded.

`E00.01` is explicitly acting as a results bridge around `MAXESS_RESULT_V1`. It reads a canonical result from `window.MAXESS_RESULT` or sessionStorage and currently requires:

- integer `overallScore` 0–100
- exactly 5 dimensions
- exactly 15 responses

before releasing results.

`E00.03` independently validates the same result contract and additionally requires a recognized `masteryBand` value. It is deliberately not responsible for scoring; it is a controller/release boundary.

`E00.02` is a visual/isolation boundary: it hides downstream result sections until a valid result is released and then reveals E01–E09.

This architecture is conceptually good because it separates assessment UI from result release. However, it also reveals a major constraint for the universal system: the current result contract is hard-coded around exactly 15 responses and exactly 5 dimensions. That is appropriate for the present assessment but must become configurable or be wrapped by a generalized contract for arbitrary generated assessments.

## 8. MOST IMPORTANT TECHNICAL INVESTIGATION

Before changing the architecture, trace the current E00 scoring pipeline end-to-end and identify the exact failure point:

`answer selection`
`-> selected answer state`
`-> response persistence`
`-> question/dimension association`
`-> score extraction`
`-> weight application`
`-> dimension aggregation`
`-> overall normalization`
`-> mastery band`
`-> MAXESS_RESULT_V1`
`-> E00.01`
`-> E00.03`
`-> E00.02`
`-> E01+

Do not guess why scoring fails. Verify the actual producer of `MAXESS_RESULT`, the scoring function, response structure, and result emission events.

## 9. GENERALIZATION STRATEGY

Do not immediately rewrite the UI. First make the current deterministic assessment reliable.

Then extract a reusable scoring engine:

```text
scoreAssessment(config, responses) -> result
```

Then extract/define a reusable assessment schema:

```text
generateAssessment(subjectSpec) -> assessmentConfig
```

The universal flow becomes:

```text
User enters name + topic
        |
        v
Normalize topic / define scope
        |
        v
Generate assessment blueprint
        |
        v
MAXIS renders assessment
        |
        v
User answers
        |
        v
Independent scoring engine
        |
        v
Personalized result
        |
        v
Naya Power invitation
```

## 10. NAYA VOICE

Do not rely on browser/OS generic “read aloud” as the final Naya voice experience.

The preferred architecture is a TTS abstraction:

`MAXIS/Naya text -> Naya voice adapter -> TTS provider -> audio player`

This allows the product to control voice, pacing, personality, replay, speaking state, and future provider changes without coupling MAXIS to one browser playback implementation.

The current E01 implementation already has an explicit Naya/listen interaction and visual speaking state, which is useful UX groundwork for this future voice layer.

## 11. LEARNING + MASTERY LOOP

The ultimate system should support:

`LEARN -> PRACTICE -> ASSESS -> SCORE -> DIAGNOSE -> IMPROVE -> REASSESS -> RECOGNIZE -> REMEMBER -> COMPOUND`

Failure is not punishment. A user should be able to reassess repeatedly and see growth over time.

Example:

`48 Emerging -> 67 Developing -> 81 Advancing -> 93 Mastering`

The score becomes a measurement of growth, not a judgment of worth.

## 12. FUTURE CERTIFICATION

After assessment and mastery tracking are reliable, add an achievement/certificate layer.

Certificate should be an achievement record, not merely a decorative PDF. Potential fields:

- learner name
- subject
- score
- mastery level
- assessment date
- assessment version
- unique certificate ID
- verification URL / QR code
- Naya Power Academy identity

The system should allow a user to print/share the achievement. Verification should establish provenance; it cannot and should not attempt to prevent every possible forgery.

## 13. BUSINESS/PRODUCT ROLE OF THE FREE ASSESSMENT

The free assessment is the acquisition engine and permanent value demonstration.

The user does not need to pay to receive the assessment experience. The value is delivered first.

Results should naturally lead to:

> You now know where you are. Imagine having Naya beside you to help you improve.

The Naya Power invitation should be integrated into the result journey rather than behaving like an intrusive advertisement.

## 14. COMPETITIVE POSITIONING RULE

Do not claim that no other company has AI tutoring, adaptive learning, generated courses, voice AI, or assessment. Those claims require research and may be false.

The defensible differentiation to investigate is the integrated system:

`AI teacher + persistent learning context + generated assessment + repeated mastery measurement + improvement loop + achievement/verification + continuing AI relationship`

## 15. PRODUCT LANGUAGE

Preferred simple explanation:

> **Choose anything you want to learn. Naya can help you learn it. MAXIS can help you measure it. You can practice, improve, and test yourself again. Your progress compounds.**

Potential category description:

> **An AI-powered personal learning and mastery system.**

CISS is the compounding system/methodology underneath it.

## 16. ENGINEERING PRINCIPLES

1. Preserve what works.
2. Fix and verify current scoring before generalizing.
3. Separate UI, assessment configuration, scoring, results contract, and voice.
4. Make the assessment engine subject-agnostic.
5. Keep GitHub as source of truth for code, schemas, protocols, tests, and canonical artifacts.
6. Do not use GitHub itself as the live runtime database merely because it is the source of truth.
7. Never invent scoring output.
8. Every generated assessment must have an explicit scope and version.
9. Every score must be reproducible from the assessment configuration + responses.
10. Every major architectural change requires tests.

## 17. IMMEDIATE NEXT EXECUTION

### Step 1 — Forensic scoring audit
Inspect E00 118 and all connected E00 bridge/controller logic. Find the exact producer and failure point of the score/result object.

### Step 2 — Make the existing fixed assessment pass
The current 15-question/5-dimension assessment must reliably produce a valid `MAXESS_RESULT_V1` result and downstream Results release.

### Step 3 — Extract generalized scoring
Move scoring into a pure/config-driven engine independent from the UI.

### Step 4 — Define universal assessment schema
Make question count, dimensions, scoring rules, mastery bands, and metadata configuration-driven.

### Step 5 — Build subject-to-assessment generation
User topic -> normalized subject specification -> generated assessment config -> MAXIS.

### Step 6 — Add Naya voice adapter
Replace generic browser playback as the strategic voice path with a controllable Naya TTS layer.

### Step 7 — Add learning/mastery persistence
Connect assessment results to a continuing Naya learning relationship and repeated attempts.

### Step 8 — Add Academy achievement/verification
Only after the measurement foundation is trustworthy.

## 18. DECISION

**THIS IS NOW THE NORTH STAR.**

The current MAXIS AI Score is the seed/lead experience. The product being built is the larger intelligent learning and mastery system around it.

Do not lose this architecture by optimizing only the current static assessment.

**North-star system:**

`NAYA POWER`
`= intelligence + learning + memory + creation + mastery`

`MAXIS`
`= measurement + scoring + assessment + mastery`

`CISS`
`= compounding loop connecting them over time`

`NAYA POWER ACADEMY`
`= achievement + recognition + verification`
