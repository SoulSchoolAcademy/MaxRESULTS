# NAYA NOTE — NORTH STAR: DYNAMIC ANY-SUBJECT ASSESSMENT ENGINE

## STATUS
- Status: NORTH STAR / ACTIVE PRODUCT DIRECTION
- Date: 2026-08-24
- Canonical repository: SoulSchoolAcademy/NayaPOWER
- Canonical branch: main
- Human owner: Shawn (S-H-A-W-N)
- Product ecosystem: Naya Power + MAXESS

## CORE INTENT
Naya Power is evolving from a fixed assessment experience into a reusable intelligence-and-assessment system capable of assessing almost any subject a person chooses.

The public entry experience should be extremely simple:
1. Enter name.
2. Enter topic/subject.
3. Start assessment.

The system dynamically creates a high-quality assessment for the requested subject, presents it in the established MAXESS experience, calculates a meaningful score, and returns personalized feedback.

## HUMAN EXPERIENCE
The user should understand the promise immediately:
- "Enter your name."
- "Enter the subject or topic you want to be assessed on."
- More precise topic input produces a more precise assessment.
- The user may type or speak the topic.
- The assessment is free and designed to produce immediate results.
- The result shows a score, capability/mastery level, and personal feedback.
- Naya Power is then presented as the deeper learning/growth system: the place where the user can learn, remember, practice, improve, create, and compound knowledge over time.

## PRODUCT LOOP
DISCOVER → ENTER TOPIC → GENERATE ASSESSMENT → ANSWER → SCORE → PERSONALIZED REPORT → INVITE INTO NAYA POWER → LEARN → PRACTICE → REASSESS → IMPROVE → COMPOUND

## MAXESS ROLE
MAXESS is the scoring/assessment engine. Its existing strengths should be preserved rather than discarded:
- configuration-driven assessment structure
- question/answer presentation
- normalized scoring
- dimension-based results
- result contract and bridge architecture
- personalized results experience
- Naya presence
- responsive/accessibility standards

The new system should generalize the engine rather than hard-code one assessment.

## CURRENT CODE REALITY VERIFIED
E00.01 currently implements a bridge contract named `MAXESS_RESULT_V1` and validates a result containing:
- overallScore: integer 0–100
- exactly 5 dimensions
- exactly 15 responses

Only after that validation does it release the result to downstream result sections through MAXESS result events. This is strong boundary architecture, but it also exposes the key migration requirement: the dynamic engine must generate a result that conforms to a stable contract while allowing the assessment configuration itself to vary by subject.

E00 118 is the active MAXESS AI Score front-end artifact and already contains a substantial premium assessment UI, Naya interaction, progress system, answer cards, and result-release architecture. Preserve this experience and refactor the data/configuration layer rather than rebuilding the visual system unnecessarily.

## TARGET ARCHITECTURE
Separate the system into five concerns:

1. TOPIC INTAKE
   - name
   - topic
   - optional precision/context
   - optional voice input

2. ASSESSMENT GENERATOR
   - converts topic into a structured assessment configuration
   - creates dimensions appropriate to the subject or maps to a canonical scoring framework
   - generates challenging, fair questions and answer choices
   - includes correct/weighted scoring metadata
   - produces a deterministic assessment payload

3. MAXESS RUNTIME
   - renders generated configuration using the existing assessment UI
   - records responses
   - calculates score
   - validates the result contract

4. RESULTS ENGINE
   - overall score
   - dimension scores
   - mastery/capability band
   - personalized interpretation
   - subject-specific strengths and opportunities
   - reassessment path

5. NAYA POWER HANDOFF
   - explain what the score means
   - invite the user to learn the subject with Naya
   - preserve learning history when the user has Naya Power
   - support repeated assessment and compounding improvement

## LEARNING VISION
A user should be able to ask Naya to teach virtually any subject, learn at their own pace, return for reassessment, and use repeated testing as a non-judgmental feedback loop.

The long-term system is not merely a test generator. It is a learning → practice → assessment → feedback → memory → reassessment loop.

## IMPORTANT PRODUCT PRINCIPLE
The public assessment should create value before signup. Naya Power should be the deeper relationship and persistent intelligence layer, not a prerequisite for experiencing the assessment.

## VOICE / NAYA PRESENCE
The assessment should eventually support dynamic Naya narration for questions and results. The current browser playback/TTS should be treated as an implementation detail, not the product identity. The target is a natural Naya voice layer that can speak generated questions, guidance, and reports dynamically.

## TECHNICAL NORTH STAR
Do not create one new hard-coded assessment for every subject. Build one generalized assessment-generation pipeline that outputs the same stable MAXESS runtime contract.

Conceptually:
TOPIC → SUBJECT SPEC → ASSESSMENT CONFIG → MAXESS RUNTIME → RESULT V1 → PERSONALIZED REPORT

The subject-specific intelligence belongs upstream of MAXESS; the scoring/runtime contract remains stable downstream.

## QUALITY BAR
Generated assessments must be:
- relevant to the requested subject
- challenging enough to discriminate levels of understanding
- factually defensible
- internally consistent
- free of answer ambiguity where possible
- reproducible/auditable
- scored from explicit metadata rather than from post-hoc guesswork
- safe to retry without corrupting prior results

## FUTURE RECOGNITION LAYER
The system may eventually support certificates/achievement records based on assessed performance. Recognition should clearly communicate that it is a Naya Power achievement/assessment record, not a government-accredited academic credential unless separately accredited.

## NORTH STAR STATEMENT
"Give anyone, anywhere, the ability to name what they want to learn, be assessed on it immediately, see where they stand, and then use Naya Power to learn, practice, remember, reassess, and grow — again and again."

## EXECUTION PRIORITY
1. Preserve the working MAXESS experience.
2. Isolate and stabilize the scoring/result contract.
3. Define the canonical dynamic assessment schema.
4. Build topic → assessment generation.
5. Validate generated assessments automatically before release.
6. Connect generated configs to MAXESS.
7. Verify scoring with known-answer fixtures.
8. Add dynamic Naya narration.
9. Add persistent learning/reassessment history inside Naya Power.
10. Add achievement/certificate generation after the assessment loop is proven.

## GOVERNANCE
This note is an architectural/product North Star, not permission to bypass verification. Any implementation must follow Naya Power's repository truth, evidence, tests, and documented state rules.
