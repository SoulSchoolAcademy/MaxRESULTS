# SMART NOTE — MAXESS EXECUTION READINESS + AIRTIGHT BUILD PLAN

**Status:** CANONICAL EXECUTION PLAN
**Owner:** Shawn + Naya
**Spelling lock:** SHAWN = S-H-A-W-N. Never Sean.
**North Star:** Turn the current MAXESS assessment experience into a deterministic, reusable assessment engine that can accept a name + topic/subject, create or load a controlled assessment, score it correctly, publish one canonical result contract to E01–E04, deliver a ten-star personalized experience, and then connect the user to Naya Power.

## 1. READINESS VERDICT

### What is already strong

- E00.118 contains a strong, polished assessment experience and the core 15-question / 5-answer interaction model.
- E00.118 already contains a deterministic score matrix, response persistence, dimension aggregation, overall score calculation, result construction, validation, storage, broadcast, and a result handoff URL.
- E00.01 already defines a `MAXESS_RESULT_V1` bridge contract and validates the minimum result shape before release.
- E00.02 establishes a results-isolation/release boundary.
- E00.03 establishes a controller that validates the canonical result and issues the release event.
- E01–E04 already consume the canonical result instead of inventing independent scores.
- The repository already contains a canonical source-map note and prior North Star notes.

### What is NOT yet airtight

1. The current scoring engine is hard-coded to the AI Mastery assessment. It is not yet topic-driven.
2. The score engine and assessment definition are embedded together instead of being cleanly separated into reusable configuration + engine layers.
3. E00.02 has a concrete version mismatch: it looks for `#maxess-e02-v3`, while the current E02 artifact uses `#maxess-e02-v2`. This means E02 is not consistently owned by the isolation/release system.
4. E00.118 currently calculates and validates the result, then immediately attempts navigation to `https://results.nayanet.app/#maxess-result=...`. That external navigation competes with the same-page E01–E04 release architecture and can prevent the intended sections from hydrating on the original page.
5. The current Naya speech experience uses browser `speechSynthesis`; it is a hook, not a canonical Naya voice pipeline.
6. Dynamic assessment generation does not yet have a locked generation schema, subject normalization policy, question-quality validator, difficulty-balancing rule, or deterministic fallback path.
7. There is no demonstrated automated regression harness proving all 15 answer paths and the result contract in a browser/runtime environment from this repository alone.
8. The current contract contains the information needed for today's fixed assessment, but future universal/topic assessments need explicit subject/topic metadata and assessment versioning.
9. Cost controls, caching, rate limiting, and provider abstraction must be designed before public dynamic generation is opened at scale.

**Conclusion:** We have enough to begin immediately. We do NOT need to rebuild the house. We need to repair the result boundary, extract the scoring engine, then generalize the assessment definition. That is the fastest safe route.

---

# 2. THE 12-PHASE EXECUTION PATH

## PHASE 1 — STABILIZE THE EXISTING RESULT PIPELINE

**Goal:** Make today's MAXESS score unquestionably work before adding intelligence.

Actions:

- Keep E00.118's visual structure.
- Preserve the existing deterministic score matrix while it is validated.
- Repair the E00.02 E02 selector/version mismatch (`v3` → current `v2`).
- Remove the automatic external redirect from the normal success path. The canonical path is now:

`Q15 SAVE → CALCULATE → BUILD MAXESS_RESULT_V1 → VALIDATE → STORE → BROADCAST → E00.01/E00.03 → E00.02 RELEASE → E01 → E02 → E03 → E04`

- Keep the encoded results URL available as a fallback/deep-link mechanism, but do not navigate away from the canonical same-page result experience unless explicitly required.
- Verify that E01, E02, E03, and E04 all hydrate from the same object.

**Exit condition:** One completed 15-question assessment produces one canonical result object and all four result sections show the correct values without independent recalculation.

## PHASE 2 — MAKE THE SCORE ENGINE A REAL ENGINE

Extract the mathematical engine from the UI.

Canonical responsibilities:

`responses → dimension scores → overall score → mastery band → strongest dimension → opportunity dimension → result contract`

The engine must be pure/deterministic wherever possible.

It must never know about DOM elements, buttons, animations, page layout, or navigation.

**Exit condition:** The same input responses always produce the exact same output, independent of UI.

## PHASE 3 — LOCK THE MAXESS ASSESSMENT CONTRACT

Create a reusable assessment configuration model:

- assessmentId
- assessmentVersion
- title
- subject
- topic
- participant name
- five dimensions
- 15 questions
- five answers per question
- answer IDs
- answer scores/weights
- question difficulty metadata
- dimension assignment
- question intent/type
- validation metadata
- narrative/report metadata

The UI renders configuration. It does not contain assessment logic that should belong to configuration.

**Exit condition:** A second fixed assessment can run through the same engine without rewriting the scoring engine.

## PHASE 4 — LOCK THE 15-QUESTION ASSESSMENT PROTOCOL

Every generated assessment follows the same disciplined method.

### Step A — Define the subject

Precisely identify what is being assessed.

### Step B — Identify the five most important capability dimensions

The dimensions must collectively represent the subject rather than merely five random categories.

### Step C — Build three questions per dimension

15 questions total.

Each dimension receives:

- one foundational understanding question
- one applied/decision question
- one integration/evaluation question

### Step D — Build five answer levels

Answers must represent an ordered capability spectrum without making the correct/highest answer obvious merely from wording.

### Step E — Balance difficulty

The assessment should test meaningful understanding, not trivia.

### Step F — Validate

Reject assessments that have:

- duplicate questions
- overlapping questions
- trivial questions
- ambiguous questions
- multiple obviously correct answers
- no meaningful distinction between answer levels
- dimension imbalance
- unsupported claims
- answer patterns that reveal the score

**Exit condition:** Every generated assessment passes the protocol before a user sees Q1.

## PHASE 5 — ADD NAME + TOPIC ENTRY

The lead experience becomes intentionally simple.

### Primary headline

**WHAT'S YOUR SCORE?**

### Inputs

- Your name
- Enter any topic or subject

### Guidance

"The more precise you are, the more accurate your assessment can be. Type or speak your topic."

### Promise

"Free 3-minute assessment. Instant results. Personalized report."

### Suggested starting topics

- What's your AI Score?
- What's your ChatGPT Score?
- What's your MAXESS Score?
- Life / Human Maximus topics

The user should never need to understand the architecture.

**Exit condition:** A user can enter their name + subject and launch an assessment with one obvious action.

## PHASE 6 — ADD CONTROLLED ASSESSMENT GENERATION

Use a provider abstraction rather than hard-coding the entire product to one AI vendor.

Preferred architecture:

`MAXESS UI → secure server endpoint → cache/database lookup → generation provider only when needed → schema validation → assessment cache → MAXESS engine`

First implementation can use a single provider, but the interface must allow another provider later.

### Cost-control rules

- Normalize topic strings.
- Cache generated assessments by normalized subject/topic + protocol version.
- Reuse validated assessments when appropriate.
- Never expose provider secrets in client code.
- Rate-limit generation.
- Log generation failures without storing unnecessary personal data.
- Separate generation cost from scoring cost.
- Make scoring itself zero-provider-cost whenever possible.

**Exit condition:** A new subject can produce a valid assessment through the controlled pipeline.

## PHASE 7 — BUILD THE RESULTS EXPERIENCE AROUND THE CANONICAL CONTRACT

E01–E04 remain presentation layers.

They must not calculate separate scores.

Canonical flow:

`MAXESS_RESULT_V1`
→ E01 overall score
→ E02 five dimensions
→ E03 personalized report
→ E04 capability/direction spectrum

The participant's name and subject must flow through the contract so the result feels genuinely personal.

**Exit condition:** Changing the subject changes the content and interpretation, not the underlying result plumbing.

## PHASE 8 — BUILD DYNAMIC PERSONALIZED REPORTING

E03 becomes subject-aware.

The report should explain:

1. what the person demonstrated
2. where they are strongest
3. where their biggest opportunity is
4. what the score means in plain language
5. what to do next
6. how Naya Power could help them improve

The writing should be human-first, warm, useful, and specific to the subject.

**Exit condition:** Two different subjects produce two meaningfully different reports while using the same engine.

## PHASE 9 — NAYA VOICE

Do not attempt to hijack browser playback as the long-term architecture.

Use the current browser `speechSynthesis` only as the immediate fallback/prototype.

Long-term:

`result narrative → Naya speech service → audio stream/file → player → speaking events → visual Naya state`

The voice provider should be abstracted so the system can change providers without rebuilding MAXESS.

**Exit condition:** Naya can naturally read the question/report dynamically, with a stable voice experience and graceful fallback when audio is unavailable.

## PHASE 10 — NAYA POWER HANDOFF

After the user receives real value, the result experience becomes the bridge to Naya Power.

The message is simple:

**You just discovered where you are. Now imagine having Naya beside you every day to help you learn, remember, create, improve, and grow.**

The assessment is free value. Naya Power is the compounding relationship.

**Exit condition:** The user understands the difference between a score and having Naya as an ongoing master/partner.

## PHASE 11 — CERTIFICATE / RECOGNITION SYSTEM

After Naya Power + learning is established, connect MAXESS to mastery validation.

Flow:

`Learn with Naya → choose subject → practice → request MAXESS assessment → repeat → improve → achieve desired score → generate verified certificate artifact`

Certificates should contain:

- participant name
- subject
- score
- capability level
- assessment version
- unique certificate ID
- issue date
- Naya Power Academy identity
- verification mechanism

This is recognition of demonstrated assessment performance, not a claim of government/accredited educational equivalence.

**Exit condition:** A user can produce a consistent, verifiable recognition artifact from a completed assessment.

## PHASE 12 — COMPOUNDING INTELLIGENCE SYSTEM

The final system connects learning, memory, assessment, improvement, creation, and recognition.

`VISION → LEARN → PRACTICE → CREATE → ASSESS → SCORE → REFLECT → REMEMBER → IMPROVE → REPEAT`

Naya Power becomes the ongoing intelligence relationship.

MAXESS becomes the measurement/validation engine.

The assessment is the doorway, not the destination.

**Exit condition:** The system can support repeated learning and assessment across multiple subjects while preserving the user's chosen knowledge/memory and progress.

---

# 3. ENGINEERING LAWS

1. **One canonical result object.**
2. **One scoring authority.**
3. **No result component recalculates scores independently.**
4. **No client-side secret keys.**
5. **No dynamic assessment reaches the user before schema validation.**
6. **No patching around a broken contract; repair the contract boundary.**
7. **Preserve E00.118's proven UX unless there is a measured reason to change it.**
8. **Configuration drives questions; engine drives scoring; UI drives presentation.**
9. **Every generated assessment is versioned.**
10. **Every release path is observable and testable.**
11. **Every failure becomes a regression test or explicit engineering rule.**
12. **Build the smallest complete vertical slice before expanding the system.**

---

# 4. CURRENT TECHNICAL DIAGNOSIS

## What the current code already proves

E00.118 already has a real deterministic score path. It defines five dimensions, 15 questions, five answers per question, a score matrix, response storage, dimension aggregation, overall normalization to 0–100, mastery band calculation, result-contract construction, validation, session/local storage, event broadcasting, and local result rendering. fileciteturn282file0L21-L100

The terminal publish path explicitly saves Q15, calculates the result, validates `MAXESS_RESULT_V1`, persists and broadcasts it, renders local results, verifies them, releases result sections, and then attempts an external results navigation. fileciteturn282file0L101-L200

E00.01 is designed as a release bridge and requires a valid `MAXESS_RESULT_V1` with an overall score, five dimensions, and 15 responses. fileciteturn284file0L2-L6

E00.03 explicitly defines itself as a controller rather than a scorer and releases a validated canonical result to the visual isolation layer. fileciteturn286file0L2-L6

E01 consumes `MAXESS_RESULT_V1` and refuses to invent a score when the result is missing. fileciteturn287file0L2-L2

## Highest-confidence current failure points

### Failure A — Result navigation conflicts with same-page release

The current E00 terminal path calls `attemptResultsHandoff(result)` immediately after same-page release. That function navigates to `results.nayanet.app` with the encoded result. This is unnecessary if E01–E04 are already present on the canonical page and creates a race/architecture conflict. fileciteturn282file0L101-L200

### Failure B — E02 isolation selector is stale

E00.02 looks for `#maxess-e02-v3`, while the current E02 artifact is `#maxess-e02-v2`. Therefore the isolation controller cannot reliably mark/release the current E02 section. fileciteturn285file0L2-L6 fileciteturn288file0L2-L6

These are concrete code-level defects, not speculation.

---

# 5. OSCAR SELF-REVIEW

### What would make this plan fail?

- Trying to generalize the current hard-coded Q/S matrix before proving the fixed pipeline.
- Continuing to patch E00/E01/E02/E03/E04 independently.
- Allowing two different result paths to become authoritative.
- Generating questions without schema validation.
- Calling an expensive provider on every user interaction.
- Putting API credentials into the browser.
- Building Naya voice before the assessment/result contract is stable.
- Building certificates before assessment integrity is stable.
- Expanding to every possible subject before the two highest-value domains are proven.

### Oscar verdict

**Do not rebuild. Do not broaden yet. Repair the boundary first, extract the engine second, generalize third.**

That is the highest-leverage path from the current state to the North Star.

---

# 6. IMMEDIATE EXECUTION ORDER

**NOW:**

1. Repair E00.02's E02 selector mismatch.
2. Stop automatic external navigation from interrupting the same-page result release.
3. Verify the canonical result reaches E01, E02, E03, and E04.
4. Add a deterministic regression path for all 15 responses.
5. Extract the scoring engine from E00.118.
6. Convert the current AI Mastery assessment into a configuration using that engine.
7. Add name + topic input.
8. Add the controlled 15-question generation protocol.
9. Add secure provider/cache infrastructure only where generation requires it.
10. Add dynamic subject-aware reporting.
11. Add Naya voice.
12. Add Naya Power handoff, then certificate/mastery loop.

**Priority rule:** Nothing downstream is allowed to distract from making the score/result pipeline unquestionably reliable first.

---

# 7. SUCCESS DEFINITION

We are successful when a stranger can:

1. open MAXESS;
2. enter their name;
3. enter a topic/subject;
4. start immediately;
5. answer 15 intelligent questions in about three minutes;
6. press Continue through the final question;
7. receive one verified score;
8. see the score appear correctly in E01–E04;
9. receive a personalized report about their actual subject;
10. understand their strongest capability and biggest opportunity;
11. optionally hear Naya explain the result;
12. understand why Naya Power is the next logical step;
13. later return to Naya and continue learning/compounding that subject.

**That is the product. MAXESS is the measurement engine. Naya Power is the compounding intelligence relationship.**
