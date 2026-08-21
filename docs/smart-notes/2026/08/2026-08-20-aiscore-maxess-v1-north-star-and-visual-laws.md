# MAXESS AIScore V1 North Star, Visual DNA, and Naya Supercharger Operating Direction

- Timestamp: 2026-08-20 19:53 PDT
- Category: DECISION
- Status: ACTIVE
- Scope: PRODUCT
- Keywords: AIScore, MAXESS, visual DNA, Naya, Naya Supercharger, Naya Power, Lead Mode, buttons, orb, assessment, three-minute experience, AAA, smart memory, GitHub
- Aliases: MAXESS AIScore, AI Score, clean V1, MAXESS assessment, Naya-powered assessment, premium assessment
- Related: `docs/MAXESS-AISCORE-CLEAN-V1-MASTER-EXECUTION-PROMPT.md`, `docs/NAYA-SMART-NOTES-SYSTEM.md`, `START-HERE.md`, `NAYA-OS.md`, `docs/NAYA-NITRO-MODE.md`

## Context

Shawn explicitly established that GitHub should function as Naya's durable project brain: memory, notebook, decision log, learning system, source map, and execution record. Naya should not depend on conversation memory when repository evidence can preserve the knowledge. The current AIScore/MAXESS build is being elevated from an existing strong assessment into a premium, warm, human, highly readable three-minute personal discovery experience.

The user wants Naya Supercharger / Naya Power / Lead Mode behavior applied to the work: independently inspect, think through alternatives, identify improvements, preserve what is excellent, challenge weak decisions, and pursue the best outcome for the participant and the product rather than merely satisfying the literal request.

## What We Decided

### 1. North Star

Take the existing MAXESS intelligence and visual DNA and turn it into an elite three-minute human experience.

The participant journey is:

**Naya welcomes me → I understand what I'm being asked → the answer choices are incredibly easy to read → the interface feels beautiful to interact with → I learn something after every question → I finish quickly → my answers actually mean something → my score feels earned → my profile feels like me → Naya speaks directly to where I am → I know what I should do next.**

The participant should barely notice the sophisticated machinery underneath.

### 2. MAXESS Visual Preservation Law

**Do not redesign MAXESS from scratch.**

Treat the existing MAXESS board, answer cards, icons, button construction, depth, glow, typography hierarchy, and interaction language as established visual DNA.

- Preserve what is already excellent.
- Improve what is weak.
- Never replace a strong interaction merely because a newer implementation is technically cleaner.
- The goal is not “new.”
- The goal is **better**.

Every redesign must answer:

- Is this clearer?
- Is this easier to use?
- Is this more beautiful?
- Does this feel more premium?
- Does this preserve MAXESS identity?

If not, do not change it.

### 3. MAXESS Button Law

Primary buttons must feel physical, premium, dimensional, and immediately actionable.

Use layered construction, subtle borders, controlled shadows, depth, refined purple illumination, strong typography, and sophisticated hover/focus states.

The interaction should create the impression that the button rises slightly from the surface and becomes illuminated when engaged.

Do not use flat generic CSS buttons. Do not over-glow. Do not make them look like gaming UI.

Desired feeling:

**luxury interface + physical object + intelligent technology**

Buttons must remain exceptionally clear on mobile and accessible by keyboard.

The existing `LET'S GO` treatment and the purple illuminated/depth behavior of the existing Continue button are approved visual references to preserve and elevate.

### 4. Answer Presentation

The existing icon + bold answer + supporting-information pattern is strong and should be preserved.

Answer choices must be immediately scannable. The participant should be able to understand the distinction between options without decoding dense UI.

Use strong labels and concise supporting text. Do not make the “AI communication”/dimension label small pink decoration. The dimension/title hierarchy should be larger, cleaner, bolder, and easier to understand while remaining subordinate to the actual question.

Never visually reward the high-scoring answer.

### 5. Naya Guidance

Naya's job during the assessment is to help the participant understand what the question is really asking, not to lecture, coach, or reveal the preferred answer.

Use a short popup structure:

**NAYA**

**WHAT THIS QUESTION IS REALLY ASKING**

One concise plain-English explanation.

**PLAY NAYA**

The popup must be easy to read. No walls of text. Do not repeat the entire question. Do not expose scoring. Do not reveal the best answer.

When `PLAY NAYA` is clicked:

**popup closes → actual question remains visible → audio plays → Naya orb activates → audio ends → orb returns to inactive.**

No automatic audio. No orb activation without actual playback.

### 6. Naya Orb

The assessment orb is a small, premium, restrained representation of Naya speaking. It should feel alive without competing with the question or answer cards.

It may subtly pulse/breathe and, where technically feasible, respond to real audio amplitude. It must represent actual audio state rather than fake speech.

State model:

`IDLE → PLAYING → ENDED`

and, if supported:

`IDLE → PLAYING → PAUSED → PLAYING → ENDED`

Respect reduced motion. Audio failure must not break the assessment.

Results will use a larger, more cinematic version of the same visual language.

### 7. Four Final Naya Audio Reports

After wording is finalized, Shawn will record four overall Naya narratives. The architecture must exist before the recordings.

Score bands:

- `< 50` → Foundation
- `50–74` → Developing
- `75–89` → Advancing
- `90+` → Mastery

Centralized configuration only:

`foundation: null`
`developing: null`
`advancing: null`
`mastery: null`

Later, public audio URLs may be supplied, likely from Google Drive. URLs must be stored in one centralized configuration location and tested for actual browser playback before claiming they work. Never scatter audio URLs through the code.

### 8. Measurement Truth

Each response is an authoritative value from `0, 1, 2, 3, 4`. Answer position is never equivalent to score.

There are 15 questions and a maximum raw score of 60.

`overallScore = round((totalRawScore / 60) × 100)`

Each dimension has three questions and a maximum raw score of 12.

`dimensionScore = round((dimensionRawScore / 12) × 100)`

Band boundaries are explicit:

`score < 50` → Foundation
`score >= 50 && score < 75` → Developing
`score >= 75 && score < 90` → Advancing
`score >= 90` → Mastery

Do not normalize or “repair” the supplied answer-value mappings merely because a question contains repeated values.

### 9. Results Relationship

AIScore and Results are separate artifacts.

AIScore collects, teaches, scores, validates, constructs `MAXESS_RESULT_V1`, and hands the result to `https://results.nayanet.app/`.

Results owns presentation, report, print/PDF, personalized interpretation, final Naya result experience, CTA, and continuation.

Never embed the Results renderer in AIScore.

### 10. GitHub as Project Brain

Durable knowledge must be captured in MaxRESULTS.

Naya should proactively create Smart Notes when a conversation produces a material decision, design law, learning, failure/root cause, solution, product requirement, or reusable operating rule.

Do not save conversational noise.

Do not create duplicate memory systems.

Naya Notes = Smart Notes = durable Naya memory.

When a note becomes a true governing law, promote it deliberately into the correct governance/product document; a Smart Note is evidence/memory, not automatically authority.

### 11. Self-Improving Lead Mode

Naya should not ask Shawn whether it is acceptable to think of a better solution when that improvement is within scope and does not override an explicit product decision.

For each meaningful design/engineering choice, proactively ask:

- What is the obvious solution?
- What is the better solution?
- What would make this feel extraordinary?
- What is the simplest way to achieve that?
- What could go wrong?
- What can be preserved from the existing system?
- What alternative presentation would improve comprehension?
- How will this behave on mobile?
- How will accessibility work?
- How will the user experience feel, not merely function?

Then choose the best evidence-supported path and verify it.

### 12. Product Philosophy

The assessment is itself proof of the claim it makes.

If MAXESS/Naya promises exceptional AI-assisted outputs, the assessment must visibly demonstrate exceptional output quality. The product must earn trust through the experience rather than through claims.

The experience should provide real value even if the participant never purchases anything.

The sequence is:

**CURIOSITY → HONEST SELF-REFLECTION → 15 SMALL AHAs → PERSONALIZED SCORE → CLEAR DIAGNOSIS → SPECIFIC NEXT STEP → OPTIONAL DEEPER NAYA EXPERIENCE**

The North Star is not conversion at any cost. The North Star is extraordinary human value, which creates trustworthy conversion when the deeper solution genuinely fits.

## Why It Matters

This is a product-quality and execution-system decision, not merely a design preference. Future Naya must be able to reconstruct the intent behind the build without asking Shawn to repeat it. The repository therefore becomes the durable memory layer for the assessment's visual DNA, interaction standards, Naya behavior, measurement truth, audio architecture, Results boundary, and quality philosophy.

## Required Behavior

For future AIScore/MAXESS work:

1. Read GitHub before acting.
2. Retrieve this note and the task-specific master execution contract when relevant.
3. Preserve approved MAXESS visual DNA.
4. Improve rather than replace strong work.
5. Treat buttons as premium physical interface objects.
6. Keep question readability and answer clarity paramount.
7. Make Naya helpful, concise, optional, and non-coaching.
8. Make the orb represent real audio state.
9. Keep four score-band audio slots centralized.
10. Use the authoritative 0–4 scoring model and explicit formulas.
11. Keep AIScore/Results separation intact.
12. Use GitHub for durable memory and learning.
13. Take the lead: inspect, critique, innovate, implement, verify, Oscar-review, repair, and learn.
14. Never claim AAA/10/10 without evidence.

## Evidence / Source

Source: Shawn's explicit product and engineering direction in the 2026-08-20 MAXESS AIScore V1 design/engineering discussion, including the supplied assessment content, scoring map, Naya narratives, audio architecture, Results bridge requirements, existing MAXESS visual references, and explicit MAXESS Visual Preservation/Button Laws.

Repository governance confirms that MaxRESULTS is the canonical project brain and that Smart Notes are the durable memory layer. See `START-HERE.md`, `.naya/NAYA-LAW-SYSTEM-PROTOCOL.md`, `docs/NAYA-SMART-NOTES-SYSTEM.md`, and `docs/smart-notes/INDEX.md`.

## Follow-up

Execute `docs/MAXESS-AISCORE-CLEAN-V1-MASTER-EXECUTION-PROMPT.md` against the actual repository evidence before implementation.
