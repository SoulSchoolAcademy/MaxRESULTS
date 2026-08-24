# NAYA NOTE — CISS / MAXIS UNIVERSAL ASSESSMENT SYSTEM

**Date:** 2026-08-24
**Human:** Shawn (S-H-A-W-N)
**System:** Naya Power / MAXIS / CISS
**Status:** Strategic product direction — candidate North Star

## 1. Core Decision
Naya Power is being evolved from a fixed assessment experience into a general-purpose **Compounding Intelligence System (CISS)** in which a person can choose virtually any subject, learn it with Naya, assess their knowledge through MAXIS, receive a capability score/report, repeat assessment indefinitely, and retain/retrieve the learning history through Naya Power.

MAXIS is therefore not merely an AI-score quiz. It is the **assessment/scoring engine** of a larger learning → practice → assessment → feedback → recognition → compounding loop.

## 2. Product Architecture Concept
The intended public experience has two complementary entry points:

1. **AI Score:** the existing MAXIS lead experience that assesses AI capability.
2. **Any Subject:** a user enters any subject/topic they want assessed on; the system dynamically generates an assessment using the MAXIS question/answer/scoring architecture.

The universal assessment flow should be:

USER SUBJECT → SUBJECT VALIDATION/FRAMING → ASSESSMENT BLUEPRINT → QUESTIONS + ANSWERS → USER TAKES TEST → SCORING ENGINE → DIMENSIONS/LEVEL → REPORT → OPTIONAL CERTIFICATE/RECOGNITION → NAYA POWER INVITATION → LEARN/IMPROVE → RETEST → COMPOUND.

## 3. Intended Learning Loop
Naya Power should function as an always-available master-teacher relationship:

VISION/GOAL → ASK NAYA TO TEACH → LEARN → PRACTICE/CREATE → ASSESS → IDENTIFY GAPS → IMPROVE → RETEST → REMEMBER → CONTINUE.

The system should support both knowledge acquisition and creation: learning a subject, building an app, website, image, document, project, or other artifact.

## 4. MAXIS Generalization Requirement
MAXIS must become **configuration/data driven rather than topic-hardcoded**. The existing architecture already points toward this model: questions, answers, dimensions, scores, weights, metadata, progress, state, and results are separable concerns.

For a new subject, the system should generate a structured assessment configuration conforming to a canonical schema. The scoring engine should not care whether the topic is mathematics, history, programming, biology, business, AI, music, or another domain.

The system should preserve a stable scoring model while allowing subject-specific dimensions and question content.

## 5. Assessment Quality Rules
Dynamic assessments must not be shallow trivia generators. They should be deliberately constructed to test meaningful understanding, with a range of difficulty and coverage of the subject's important concepts.

The user may retake an assessment without a punitive mindset. The objective is measurement, feedback, learning, and growth—not judgment.

Capability bands discussed:
- EMERGING
- FOUNDATION / DEVELOPING (exact naming to be finalized)
- DEVELOPING
- ADVANCING
- MASTERING

The exact canonical band taxonomy must be locked before implementation.

## 6. Recognition / Certificate Concept
After assessment, the system can generate a report and allow the user to produce a **Naya Power Academy Certificate of Excellence / Mastery** based on an achieved score.

Important distinction: this is intended as a recognition artifact of demonstrated learning within the Naya Power system, not a claim of accredited academic credentials unless accreditation is separately obtained.

Potential certificate integrity features:
- unique serial/credential ID
- verification mechanism
- Naya Power Academy mark/stamp
- subject
- learner
- date
- achieved score/level
- assessment version
- optional QR/link verification

Users may print or share the certificate.

## 7. Business / Growth Loop
The public assessment can remain a high-value lead experience. The user receives immediate value even without Naya Power membership. The result then naturally demonstrates the value of Naya Power:

GET ASSESSED FREE → SEE CURRENT LEVEL → DISCOVER GAPS → INVITATION TO LEARN WITH NAYA → 5-DAY EXPERIENCE/CHALLENGE → CONTINUED LEARNING + RETESTING + MEMORY + CREATION.

The assessment becomes a persistent, relevant invitation rather than a generic advertisement.

## 8. Naya Voice / Audio Requirement
The assessment should eventually support Naya reading questions, instructions, feedback, and results dynamically in Naya's voice rather than relying on generic robotic browser text-to-speech.

Architecture should separate **content generation** from **voice rendering**:
CONTENT → TTS/VOICE SERVICE → AUDIO STREAM/BUFFER → PLAYBACK CONTROLS.

The existing browser/web speech playback can remain a fallback/prototype, but should not be treated as the final Naya voice architecture.

## 9. Technical Integration Direction
Do NOT make the public MAXIS frontend directly dependent on GitHub as if GitHub were the runtime intelligence engine.

Preferred architecture:
- Frontend: existing MAXIS/Naya Power experience.
- Backend/orchestration: secure API/service.
- LLM: structured generation of assessment blueprints/questions/reports.
- Scoring: deterministic application-side scoring engine.
- Persistence: database/storage for assessment instances, results, versions, and user history.
- GitHub: source of truth for code, schemas, canonical prompts/specifications, versioned artifacts—not a public client-side database for sensitive/user runtime data.

If an early prototype uses GitHub to store configuration, it must be treated as a temporary controlled architecture and never expose credentials or privileged write access in browser code.

## 10. Existing NayaPOWER Code Insight
The active E00 118 artifact already demonstrates a strong visual/interaction shell: responsive MAXIS UI, progress, answer cards, Naya interaction, dialogs, local results, and a premium dark/purple visual system. It is a strong foundation rather than something to discard.

The strategic move is to preserve the proven UX and refactor the underlying assessment contract so generated subject assessments can enter the same engine.

## 11. Critical Engineering Principle
The universal system should have one canonical assessment contract. Subject generation creates an instance of that contract. The MAXIS renderer consumes it. The scoring engine scores it. The result engine interprets it. This prevents creating a separate app for every subject.

CANONICAL CONTRACT → ANY SUBJECT → SAME ENGINE.

## 12. CISS Definition
CISS = **Compounding Intelligence System**.

Working definition:
A system in which learning, memory, assessment, feedback, creation, and progress reinforce one another over time so that each interaction can improve the value of the next.

CISS is best treated as the **system/architecture and operating model**, while Naya Power is the product/ecosystem and MAXIS is the assessment/scoring subsystem.

## 13. North-Star Product Statement
Working statement:
**Naya Power gives anyone with a phone or computer an always-available AI learning partner who can help them learn, create, practice, remember, assess, and grow in virtually any subject—and MAXIS gives them a way to measure and demonstrate that growth.**

This is a strategic statement, not yet a final marketing claim. Claims about speed, mastery, cost, accreditation, or superiority over all existing education must be validated before public use.

## 14. Immediate Build Sequence
1. Freeze the canonical MAXIS assessment schema.
2. Audit the current E00/E00.x/E01–E04 code paths and identify the actual scoring failure.
3. Separate generated assessment data from renderer/UI logic.
4. Build a subject-input entry experience.
5. Build secure subject → assessment generation endpoint.
6. Validate generated assessments against schema before rendering.
7. Feed validated assessments into existing MAXIS renderer.
8. Make scoring deterministic and independently testable.
9. Build dynamic results/report generation.
10. Add certificate generation + verification.
11. Add Naya voice architecture.
12. Connect the learning/reassessment loop to Naya Power.
13. Instrument analytics and abuse/cost controls.
14. QA across mobile/desktop and multiple subjects.

## 15. Governance
This note is an AI-oriented intelligent brief. Future Naya agents should preserve the distinction between:
- CISS = overarching compounding system
- Naya Power = product/ecosystem
- MAXIS = assessment/scoring engine
- Naya = AI learning/creation partner
- Certificate = recognition/verification artifact

Do not collapse these names into one technical component.
