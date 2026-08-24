# NAYA NOTE — UNIVERSAL MAXIS / NAYA POWER NORTH STAR

**Date:** 2026-08-24
**Status:** LOCKED NORTH STAR
**Human:** Shawn (S-H-A-W-N)
**System:** Naya Power / MAXIS

## Core Decision
MAXIS is no longer merely a fixed AI Mastery assessment. The product direction is a **universal, configuration-driven assessment engine** that can assess a person on essentially any valid subject or topic they choose.

The user experience should become:

1. Enter your name.
2. Enter or speak the subject/topic you want assessed on.
3. MAXIS generates a rigorous, balanced 15-question assessment for that subject.
4. The user completes the assessment in roughly three minutes.
5. MAXIS calculates a 0–100 score and meaningful dimension scores.
6. MAXIS returns immediate, personalized feedback in the user's name.
7. The experience recommends Naya Power as the ongoing learning/growth system.

Primary landing-page promise:

> **Enter your name. Enter any subject. Get your score.**
>
> The more precise your topic, the more accurately MAXIS can tailor your assessment. Type or speak your topic. Your personalized assessment is generated immediately.

## Product Vision
The assessment is the **front door / lead experience**. Naya Power is the larger system behind it.

Naya Power's long-term promise is that a person can choose what they want to learn, create, build, remember, or accomplish; Naya can act as an always-available master teacher/partner; learning can compound over time; and MAXIS can repeatedly assess progress.

The intended loop is:

**CHOOSE → LEARN WITH NAYA → PRACTICE → ASSESS WITH MAXIS → SCORE → UNDERSTAND GAPS → LEARN AGAIN → REASSESS → COMPOUND**

The system should support repeated assessment without shame or penalty. The goal is learning and growth, not merely producing a one-time score.

## Current Codebase Reality
The current repository is the starting point, not something to discard.

Known structure:
- E00 = assessment experience.
- E00.118 = current active E00 frontend.
- E00.01 = result bridge/contract layer.
- E00.02 / E00.03 = additional result-flow components.
- E01–E04 = core app/result experience.
- E05–E09 = primarily static Naya Power pages.

The existing E00.118 already contains substantial premium UI, responsive behavior, question/answer presentation, Naya presence, result UI, and local assessment mechanics. Preserve what works.

The existing E00.01 establishes a `MAXESS_RESULT_V1` contract and validates:
- `contractVersion === MAXESS_RESULT_V1`
- `overallScore` integer 0–100
- exactly 5 dimensions
- exactly 15 responses

That contract is a valuable architectural boundary and should remain authoritative while topic-specific assessment configuration is generated upstream.

## Critical Architectural Principle
**Do not make the scoring engine responsible for generating its own questions.**

Separate the system into:

**INPUT → ASSESSMENT GENERATOR → NORMALIZED ASSESSMENT CONFIG → MAXIS RUNTIME → SCORING ENGINE → RESULT CONTRACT → RESULTS EXPERIENCE**

The generated assessment must conform to a deterministic schema before the runtime consumes it.

The runtime should remain stable while the generated content changes.

## Universal 15-Question Model
Every generated assessment should identify the most important knowledge/capability areas of the requested subject and distribute questions across a stable set of dimensions appropriate to that subject.

The question generator should optimize for:
- relevance to the exact topic
- factual accuracy
- coverage of fundamentals and important concepts
- conceptual understanding rather than trivia
- application/problem solving
- differentiation between shallow recognition and genuine understanding
- fair difficulty
- unambiguous wording
- one defensible best answer where multiple-choice is used
- balanced answer positions
- useful diagnostic value

Difficulty should target a productive middle: challenging enough to reveal knowledge gaps, but not so obscure that the test becomes a trivia contest.

The five dimensions should be **semantically generated for the subject when appropriate**, while preserving the five-dimension scoring architecture and 0–100 normalization. The engine scores normalized evidence; the generator supplies subject-specific dimensions, questions, answers, weights, and metadata.

## Canonical Assessment Config
Conceptually:

```text
AssessmentConfig
  assessmentId
  subject
  topic
  userName
  generatedAt
  dimensions[5]
  questions[15]
    id
    dimensionId
    order
    question
    answers[5]
      id
      title
      description
      score
      weight
    weight
    metadata
  difficultyProfile
  source/grounding metadata
  generatorVersion
```

The generated config must be validated before rendering.

## Scoring Boundary
Preserve the existing MAXESS runtime boundary:

**Q15 SAVE → assert 15 responses → calculate → five dimensions → build `MAXESS_RESULT_V1` → validate → store → broadcast → render results**

The generator may change the assessment configuration; it must not silently change the scoring contract or result consumers.

## Results
Results should be personalized using the user's name and requested subject.

Minimum result value:
- overall 0–100 score
- five meaningful dimension scores
- mastery band (for example Emerging / Foundation / Developing / Advancing / Mastering)
- strongest area
- opportunity area
- concise explanation of what the score means
- actionable next step
- invitation to continue learning with Naya Power

The result should feel like an immediate reward, not an error report or academic judgment.

## Naya Voice / Audio
The current system can use browser speech playback, but the robotic voice is not the final experience.

Architecture should isolate narration behind a small TTS adapter:

`NarrationService.speak(text, voiceProfile)`

This allows the current browser speech implementation to remain a working fallback while a higher-quality Naya voice can later be plugged in without rewriting the assessment engine.

Naya should be able to dynamically narrate:
- question introduction
- selected question text
- result summary
- personalized feedback
- next-step invitation

Voice generation is an experience layer, not a scoring dependency.

## Naya Power Conversion
The public MAXIS experience can provide immediate assessment value without requiring full Naya Power access. The conversion point is the realization:

> **You just discovered where you are. Naya Power helps you learn, remember, practice, and grow from here.**

The assessment is therefore both a useful standalone experience and a permanent invitation into the larger system.

## Long-Term Learning Loop
Naya Power should eventually maintain an intentional memory/learning record for users who choose it:
- what they wanted to learn
- what they studied
- what they learned
- assessments taken
- scores over time
- identified gaps
- important notes/memories they intentionally save
- progress and achievements

This creates the Compounding Intelligence System concept: knowledge, experience, and reflection can accumulate instead of disappearing between sessions.

## Execution Doctrine
Build from the existing code with the smallest coherent architectural change.

1. Freeze the working E00 visual/runtime behavior.
2. Extract/define the assessment configuration schema.
3. Build a validated assessment-generation boundary.
4. Generate one subject-specific assessment at a time.
5. Feed the normalized config into the existing E00 runtime.
6. Preserve the current scoring/result contract.
7. Make result content topic-aware and personalized.
8. Add speech through an isolated narration adapter.
9. Add robust validation/fallback behavior for malformed AI output.
10. Test with several unrelated subjects before broadening.
11. Only then expand memory, learning history, certificates, and deeper Naya Power integration.

## Non-Negotiables
- Preserve working UI and scoring behavior unless a change is required by the new architecture.
- Never let arbitrary AI output directly control the DOM or scoring logic.
- Never accept malformed assessment configs silently.
- Never claim a score is meaningful when the generated assessment failed validation.
- Keep scoring deterministic and auditable.
- Keep the user experience extremely simple.
- Optimize for immediate value and a memorable experience.
- Treat the human as the decision-maker; the system assists rather than manipulates.

## North Star
**MAXIS should make it possible for a person to say, “I want to know where I stand on this subject,” and receive a fast, personalized, fair, meaningful assessment—then Naya Power can help them learn, remember, practice, and come back to measure their growth.**

This is the current product direction and should be treated as the canonical North Star until explicitly changed by Shawn.
