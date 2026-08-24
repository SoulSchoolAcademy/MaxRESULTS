# SMART NOTE — MAXESS CANONICAL SOURCE MAP

**Status:** CANONICAL REFERENCE MAP
**Purpose:** Preserve the exact source artifacts Shawn identified as the working foundation for MAXESS / Naya Power assessment development so they can be retrieved quickly without relying on conversation history.
**Owner:** Shawn + Naya
**Spelling lock:** SHAWN = S-H-A-W-N. Never Sean.

## NORTH STAR

Build MAXESS into a reusable, reliable scoring engine that can assess a user on a selected topic/subject, calculate the score correctly, generate the complete results experience, and eventually support dynamically generated assessments under a controlled assessment-generation protocol.

The existing artifacts are valuable source material. They are not automatically the final architecture. Preserve what works, learn from failures, and build the final system deliberately rather than patching disconnected pieces together.

## CANONICAL SOURCE ARTIFACTS

### 1. E00.118 — CURRENT FRONT-END / PRIMARY EXPERIENCE

This is the primary active front-end artifact Shawn identified as the most valuable structural reference for the current assessment experience.

https://github.com/SoulSchoolAcademy/NayaPOWER/blob/main/E00%20118

### 2. E00.01 — BRIDGE / ASSESSMENT FLOW ARTIFACT

https://github.com/SoulSchoolAcademy/NayaPOWER/blob/main/E00.01

### 3. E00.02 — RESULTS / FLOW SUPPORT ARTIFACT

https://github.com/SoulSchoolAcademy/NayaPOWER/blob/main/E00.02

### 4. E00.03 — RESULTS / FLOW SUPPORT ARTIFACT

https://github.com/SoulSchoolAcademy/NayaPOWER/blob/main/E00.03

### 5. E01 — RESULTS COMPONENT / SCORE OUTPUT

https://github.com/SoulSchoolAcademy/NayaPOWER/blob/main/E01

### 6. E02 — RESULTS COMPONENT / SCORE OUTPUT

https://github.com/SoulSchoolAcademy/NayaPOWER/blob/main/E02

### 7. E03 — PERSONALIZED REPORT / TEXT OUTPUT

https://github.com/SoulSchoolAcademy/NayaPOWER/blob/main/E03

### 8. E04 — RESULTS COMPONENT / SCORE OUTPUT

https://github.com/SoulSchoolAcademy/NayaPOWER/blob/main/E04

## HOW TO USE THIS MAP

When MAXESS work resumes:

1. Read this note first.
2. Open E00.118 first to understand the current experience and protected structure.
3. Inspect E00.01, E00.02, and E00.03 for the bridge/flow architecture.
4. Inspect E01–E04 together to understand the intended result outputs.
5. Do not assume any artifact is correct merely because it exists.
6. Verify scoring, state flow, persistence, result construction, and rendering before modifying architecture.
7. Preserve working UX and visual structure wherever possible.
8. Treat failures as engineering evidence and convert them into explicit rules/tests.

## TARGET FLOW

USER NAME + TOPIC/SUBJECT
→ CREATE/LOAD ASSESSMENT
→ 15 QUESTIONS
→ ANSWER EACH QUESTION
→ CONTINUE
→ SCORE ENGINE CALCULATES
→ 4 RESULT OUTPUTS (3 numeric/result components + 1 personalized report component)
→ VALIDATE RESULT
→ DISPLAY COMPLETE RESULTS EXPERIENCE
→ INVITE USER TO NAYA POWER

## FUTURE DYNAMIC ASSESSMENT FLOW

USER ENTERS NAME + TOPIC/SUBJECT
→ ASSESSMENT GENERATION PROTOCOL IDENTIFIES SUBJECT
→ EXTRACTS THE MOST PERTINENT KNOWLEDGE AREAS
→ BUILDS A BALANCED 15-QUESTION ASSESSMENT
→ BUILDS ANSWER SETS + SCORING WEIGHTS
→ VALIDATES QUESTION QUALITY / DIFFICULTY / COVERAGE
→ RUNS THE SAME MAXESS SCORING ENGINE
→ GENERATES PERSONALIZED RESULTS
→ OPTIONALLY PROVIDES NAYA VOICE / AUDIO
→ INVITES USER TO NAYA POWER

## CRITICAL ENGINE REQUIREMENT

The scoring engine must become deterministic and independently testable.

For every answered question, the system must reliably preserve:

- question ID
- selected answer ID
- subject/topic
- dimension/category
- answer score
- answer weight, if applicable
- accumulated dimension score
- overall score state
- completion state

On the final Continue action, the system must calculate and validate the final result before publishing it to E01–E04.

No result screen should depend on guessed, missing, stale, or independently recomputed scoring values.

## REFERENCE PRINCIPLE

**E00.118 is the experience reference. The final MAXESS engine is the system of record.**

The objective is not to preserve bugs. The objective is to preserve valuable design, flow, and lessons while creating a correct, reusable scoring architecture.

## RETRIEVAL RULE

If Shawn says:

> "Pull the MAXESS source files."

or

> "Open the E00/E01–E04 source."

start with this map and use the exact links above.

## LASTING RULE

Do not let these links disappear into conversation history. This note exists specifically so Naya can recover the canonical source set quickly and continue the work from verified repository artifacts.
