# MAXESS ASSESSMENT CONSTRUCTION RUBRIC V1

**Status:** LOCKED METHODOLOGY
**Authority:** NayaPOWER
**Purpose:** Define how MAXESS assessments are conceived, constructed, scored, taught, and improved.

## 1. NORTH STAR

MAXESS must provide value while measuring the person.

Core loop:

`MEASURE → MEANING → MASTERY → MEASURE AGAIN`

An assessment is not a trivia test. It is an intelligence experience designed to help a person understand where they are, learn something useful while answering, discover opportunity, and know what to do next.

## 2. SOURCE-OF-TRUTH ORDER

When constructing an assessment, use this order:

1. NayaPOWER governing law and relevant Codex knowledge.
2. The authoritative subject knowledge bank.
3. The MAXESS assessment contract and engine.
4. This rubric.
5. Product UX and presentation constraints.

If a conflict appears, stop and resolve it against the higher authority. Never silently invent subject truth.

## 3. QUESTION DESIGN LAW

Every question must satisfy all of these:

- Measures a meaningful capability, behavior, judgment, or understanding.
- Helps the participant notice something useful about the subject.
- Is understandable without specialist language unless the subject requires it.
- Has one defensible strongest answer and one defensible weakest answer.
- Avoids trick wording, deception, shame, or gotcha construction.
- Avoids making the correct answer obvious through length, positivity, jargon, or position.
- Produces useful differentiation between developing levels of capability.
- Can support a meaningful explanation in the final report.

Ask the smallest number of questions that can produce a useful signal. Do not add questions merely to increase question count.

## 4. THE FIVE-ANSWER MODEL

Default MAXESS configuration:

- 5 answers per question.
- Latent capability scores: `4, 3, 2, 1, 0`.
- `4` = strongest evidence of the target capability.
- `0` = weakest evidence of the target capability.

The score belongs to the answer's demonstrated capability, **not its visual position**.

Answer choices should be presented in a deterministic but non-patterned order so participants cannot infer scoring from position.

Do not use a visible A=4, B=3, C=2, D=1, E=0 pattern.

## 5. SWEET-SPOT DIFFICULTY

Questions must live between trivial and obscure.

Too easy:
- correct answer is obviously the most positive sentence
- distractors are silly or clearly inferior
- participant can score without understanding the subject

Too hard:
- requires specialist knowledge unrelated to the intended capability
- multiple answers are equally defensible
- wording is ambiguous
- participant is punished for terminology rather than understanding

Sweet spot:

> The participant must think about what they actually do, but a knowledgeable person can recognize the stronger behavior without guessing the test-maker's intention.

## 6. DISTRACTOR / ANSWER QUALITY LAW

All five answers should be plausible.

Each answer must represent a real behavior or mental model a person could reasonably have.

The weaker answers should not be insulting or caricatures. They should describe genuine developmental stages.

The strongest answer should be clearly best **after reflection**, not instantly obvious from tone.

## 7. TEACHING-VALUE LAW

Every question should teach at least one useful idea through:

- the question itself,
- the answer descriptions,
- a brief Naya explanation,
- a micro-lesson after selection, or
- the resulting report.

The participant should be able to finish an assessment knowing more than when they began, even before entering the paid product.

## 8. DIMENSION LAW

Dimensions must represent distinct but connected capabilities.

For the current AI Mastery assessment:

- Direction
- Communication
- Evaluation
- Iteration
- Systems Thinking

Questions may measure one primary dimension. The final report may explain how the dimensions interact as a pattern.

Do not create five disconnected mini-tests.

## 9. SCORING LAW

Scoring must be deterministic, inspectable, repeatable, and independent from presentation.

For the standard 15-question assessment:

- maximum raw score = `15 × 4 = 60`
- normalized score = `round(raw / 60 × 100)`
- dimension score = `round(dimensionRaw / dimensionMax × 100)`

Mastery bands remain authoritative wherever defined by the result contract:

- `0–49` EMERGING
- `50–74` DEVELOPING
- `75–89` ADVANCING
- `90–100` MASTERING

## 10. ANSWER-ORDER RANDOMIZATION

Presentation order must not reveal scoring.

Use a deterministic shuffle based on question ID / assessment version, or another reproducible mechanism. The same assessment version must produce the same answer order so results remain explainable and testable.

The engine must retain the answer's stable ID and latent score.

## 11. REPORT-VALUE LAW

The report should answer:

- Where am I?
- What does this result mean?
- What am I naturally good at?
- Where is my strongest opportunity?
- What did I learn from taking this?
- What should I do next?
- What would mastery look like?

A score without interpretation is arithmetic.

## 12. TOPIC GENERATION LAW

Future subject assessments may be generated from a subject knowledge bank, but generated content must pass the same construction rubric before becoming authoritative.

Pipeline:

`SUBJECT → KNOWLEDGE RETRIEVAL → CAPABILITY MAP → DIMENSIONS → QUESTION BLUEPRINTS → ANSWERS → LATENT SCORING → TEACHING VALUE → QA → AUTHORITATIVE CONFIG → ASSESSMENT`

The generator must never invent subject truth merely to fill a question slot.

## 13. KNOWLEDGE-BANK REQUIREMENT

A future dynamic assessment generator should retrieve relevant source knowledge before generating questions.

Each generated assessment should retain provenance sufficient to answer:

- Which knowledge informed this question?
- Which capability is being measured?
- Why is this answer stronger than the alternatives?
- What teaching point does the question provide?

## 14. QUALITY GATE

Before an assessment is released:

`CONSTRUCT → SCORE → SIMULATE → REVIEW → VERIFY → LOCK`

Test at minimum:

- all questions render
- all five answers render
- each answer has a valid latent score
- exactly one 4 and one 0 exist per question
- all score values are within 0–4
- no duplicate question IDs
- no duplicate answer IDs within a question
- every question maps to a valid dimension
- maximum/minimum score math is correct
- answer order does not reveal score order
- report receives complete provenance

## 15. HUMAN VALUE STANDARD

The ultimate question is:

> **Did this assessment create more human value than it consumed?**

If not, improve it.

MAXESS should make a person think:

> “I learned something about myself and the subject just by taking this.”

That is the standard.
