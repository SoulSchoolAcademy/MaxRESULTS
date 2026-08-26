# 🔱 MAXESS — MASTER ENGINEERING + DESIGN DIRECTIVE V2

**Status:** ACTIVE / CANONICAL / MASTER EXECUTION STANDARD  
**Date:** 2026-08-26  
**Project:** MAXESS  
**Repository:** `SoulSchoolAcademy/NayaPOWER`  
**Authority:** Human-approved MAXESS North Star + Naya Power governing law  
**Role:** Principal Architect + Principal Engineer + Master Designer  
**Apprentice:** Any AI, engineer, designer, QA agent, or future Naya executing MAXESS work

> **This directive supersedes V1 for execution. V1 remains preserved as historical lineage.**

---

## 0. MASTER COMMAND

**STOP PATCHING SYMPTOMS. BUILD THE INTENDED MACHINE.**

Do not keep modifying isolated `E00`, `E00.01`, `E00.02`, or `E00.03` variants simply because they are the newest artifacts.

Do not preserve broken architecture because it already exists.

Do not create another competing scorer, state model, result object, bridge, completion path, or timing workaround.

Study everything that came before. Harvest what is proven. Understand every failure. Preserve valuable behavior. Remove fragile architecture. Rebuild the authoritative path so it is simpler, deterministic, beautiful, fast, extensible, and testable.

**The existing files are source material and evidence—not architectural prison.**

The objective is not to make yesterday's code coexist forever. The objective is to create the MAXESS machine that should have existed all along.

---

# 1. NORTH STAR

MAXESS is a **learning-first capability assessment machine for AI and life-related knowledge**.

The user experience is:

**ENTER TOPIC → UNDERSTAND → LEARN → ASSESS → SCORE → DISCOVER → IMPROVE → CONTINUE.**

The flagship entry point is:

> **What's Your AI / ChatGPT Score?**

AI Score is the golden reference assessment and the first proof that the architecture works.

The platform must ultimately support a user entering an appropriate topic and receiving a useful assessment compiled from structured Naya Power / Digital Codex / Human Maximus knowledge and deterministic rules, without requiring a paid runtime LLM API as a mandatory dependency.

MAXESS optimizes for extraordinary usefulness to the majority of people. It does **not** claim to replace elite specialists or possess perfect depth in every field.

If coverage is insufficient, MAXESS says so honestly. Unknown is legitimate; fabricated authority is not.

---

# 2. FLAGSHIP EXPERIENCE STANDARD

MAXESS must feel like:

> **A beautiful heart built an extraordinarily powerful machine.**

It must be simultaneously:

- intelligent;
- high-tech;
- precise;
- fast;
- powerful;
- premium;
- warm;
- human;
- inviting;
- trustworthy;
- simple;
- alive;
- delightful.

The human should experience simplicity even though the machine underneath is sophisticated.

The emotional sequence should be:

**CURIOSITY → WELCOME → ENGAGEMENT → DISCOVERY → RECOGNITION → CLARITY → EMPOWERMENT → NEXT ACTION.**

Never make the user feel judged, tricked, confused, or responsible for understanding the implementation.

---

# 3. ARCHITECTURAL NORTH STAR

Converge toward exactly this authority model:

```text
ONE MAXESS APPLICATION
        ↓
ONE AUTHORITATIVE STATE MACHINE
        ↓
ONE ASSESSMENT DEFINITION / COMPILER
        ↓
ONE SCORING ENGINE
        ↓
ONE VALIDATED RESULT CONTRACT
        ↓
ONE RELEASE / NAVIGATION PATH
        ↓
MANY RESULTS PRESENTATION SECTIONS
```

`E00` is the authoritative assessment application/runtime.

`E01–E09` remain the nine canonical Results sections and remain separately maintainable because the complete Results Experience is intentionally modular.

**E01–E09 are consumers, never competing authorities.**

They may interpret and beautifully present the result. They may not calculate a second result.

---

# 4. E00 RE-ENGINEERING RULE

The physical existence of:

- `E00 796`;
- `E00 700`;
- `E00 1800`;
- `E00.01`;
- `E00.02`;
- `E00.03`

is historical implementation lineage.

Do not assume any one artifact is authoritative merely because it is newer, larger, named FINAL, or previously deployed.

The rebuild must first inventory them and extract:

1. what works;
2. what failed;
3. what is reusable;
4. what is duplicated;
5. what is fragile;
6. what is only a workaround;
7. what belongs in the final architecture.

Then build **one authoritative E00**.

If a beautiful behavior exists in a legacy artifact but its implementation is fragile, **reimplement the behavior correctly rather than preserving the fragility.**

---

# 5. IMMUTABLE RESULT CONTRACT

The most important interface in the Results system is the result contract.

The authoritative result is `MAXESS_RESULT_V1` unless a deliberately versioned successor is introduced.

Conceptually:

```js
{
  contractVersion,
  assessmentId,
  assessmentVersion,
  assessmentType,
  topic: {
    id,
    title,
    category,
    requestedByUser
  },
  participant: {
    name
  },
  assessment: {
    questionCount,
    completedCount,
    responses
  },
  score: {
    raw,
    max,
    normalized,
    percentage,
    masteryBand
  },
  dimensions: [
    {
      id,
      name,
      rawScore,
      maxScore,
      normalizedScore,
      percentage,
      band
    }
  ],
  strongestDimension,
  opportunityDimension,
  fingerprint,
  selectedInterests,
  nayaMetadata,
  audioMetadata,
  completedAt,
  integrity: {
    scoringVersion,
    rubricVersion,
    resultVersion
  }
}
```

The exact field set must be reconciled against the canonical existing Results consumers before implementation is frozen.

### Absolute result laws

- E00 creates the authoritative result.
- E00 validates it before release.
- E01–E09 receive the same result authority.
- E01–E09 do not rescore.
- No DOM scraping.
- No parsing visible score text.
- No guessing from UI state.
- No timer-based result creation.
- No section-to-section score calculation.
- No competing result objects presented as authoritative.
- If the result cannot be validated, Results do not falsely release.

**DATA → ENGINE → RESULT OBJECT → PRESENTATION.**

Never:

**DOM → SCRAPE → PARSE → GUESS → RESCORE.**

---

# 6. DETERMINISTIC SCORING LAW

The flagship AI Score assessment remains:

- 15 questions;
- 5 answers per question;
- answer values exactly `0, 1, 2, 3, 4`;
- five dimensions;
- deterministic aggregation;
- normalized overall score `0–100`.

For the canonical 15 × 0–4 model:

```text
MAX RAW = 15 × 4 = 60
OVERALL = round(raw / 60 × 100)
```

With three questions per dimension:

```text
DIMENSION MAX RAW = 3 × 4 = 12
DIMENSION SCORE = round(dimensionRaw / 12 × 100)
```

The exact existing mastery-band thresholds and dimension mapping must be read from the canonical source and centrally defined. Do not invent a new threshold system during the rebuild.

Scoring must be:

- deterministic;
- mathematically auditable;
- configuration-driven;
- independent of presentation;
- independently unit-testable;
- reproducible from the same inputs.

---

# 7. STATE MACHINE LAW

E00 owns one state machine.

Minimum conceptual states:

```text
IDLE
 ↓
INTRO
 ↓
QUESTION
 ↓
ANSWERED
 ↓
ADVANCING
 ↓
QUESTION
 ↓
...
 ↓
COMPLETE
 ↓
RESULT_READY
 ↓
RESULTS
```

Recoverable failure may branch to:

```text
ERROR / RECOVERABLE
```

Rules:

- valid question required before answer save;
- valid answer required before Continue;
- answer must belong to current question;
- each question contributes exactly once;
- Q15 answer must be persisted before scoring;
- score calculation occurs once for a completed assessment;
- result is frozen before Results release;
- Results release is a state transition, not a race;
- failed external navigation must not destroy a valid local result;
- refresh/recovery behavior must be explicit rather than accidental.

---

# 8. CONTINUE BUTTON LAW

Continue is a state-transition control, not decoration.

Before an answer is selected:

**DISABLED.**

After a valid answer is selected:

**ENABLED.**

On activation:

1. validate current question;
2. validate selected answer;
3. prevent duplicate submission;
4. persist the response exactly once;
5. update authoritative state;
6. if not final, advance to next question;
7. if final, enter completion/scoring pipeline;
8. never depend on animation timing.

On Q15:

```text
ANSWER
 ↓
VALIDATE
 ↓
SAVE
 ↓
FINALIZE
 ↓
CALCULATE
 ↓
VALIDATE RESULT
 ↓
FREEZE RESULT
 ↓
RELEASE RESULTS
```

No “advance to nowhere.” No timeout as correctness mechanism.

---

# 9. NO TIMING DEPENDENCY LAW

Timers may animate.

Timers may **never** establish correctness.

Never use timing as the authority for:

- scoring;
- completion;
- result creation;
- release;
- handoff;
- section readiness;
- state synchronization.

Avoid architectural dependence on:

- arbitrary `setTimeout` delays;
- animation completion callbacks as logic authority;
- polling;
- MutationObserver hacks;
- DOM mutation races;
- cross-frame timing assumptions;
- retry loops whose purpose is to hide missing state.

Correct order:

**LOGIC → STATE → RESULT → PRESENTATION → ANIMATION.**

---

# 10. CONFIGURATION-DRIVEN ASSESSMENT MODEL

The engine must not hard-code assessment questions into UI logic.

Conceptual question model:

```js
{
  id,
  dimensionId,
  order,
  question,
  label,
  answers: [
    {
      id,
      title,
      description,
      score,
      weight
    }
  ],
  helperText,
  metadata
}
```

The assessment definition should conceptually contain:

```js
{
  id,
  version,
  topic,
  title,
  description,
  dimensions,
  questions,
  scoring,
  resultProfile,
  coverage
}
```

The runtime engine should not care whether the subject is AI, prompting, agents, productivity, quantum computing, or another supported topic.

It cares that it receives a valid assessment definition.

---

# 11. DYNAMIC ASSESSMENT COMPILER

MAXESS must be architected for:

```text
USER TOPIC
 ↓
TOPIC RESOLUTION
 ↓
DOMAIN / COVERAGE RESOLUTION
 ↓
STRUCTURED KNOWLEDGE MAP
 ↓
LEARNING OBJECTIVES
 ↓
CAPABILITY / DIMENSION SELECTION
 ↓
QUESTION ARCHETYPES
 ↓
0–4 RUBRIC CONSTRUCTION
 ↓
15-QUESTION ASSESSMENT CONFIG
 ↓
VALIDATION
 ↓
E00 RUNTIME
```

Runtime generation must not require a paid LLM API as a mandatory dependency.

The preferred model is deterministic compilation from structured knowledge and rules maintained by Naya Power.

The knowledge layer should encode, where useful:

- concepts;
- relationships;
- definitions;
- applications;
- limitations;
- common misunderstandings;
- learning objectives;
- aliases;
- difficulty;
- capability levels;
- evidence/coverage confidence;
- question-generation rules.

The system should store enough knowledge to compile strong assessments; it does not need to pre-store every possible question.

---

# 12. UNIVERSAL CAPABILITY MODEL

A reusable capability framework may include:

1. **UNDERSTAND** — explain core ideas.
2. **CONTEXTUALIZE** — know why, where, and when it matters.
3. **APPLY** — use knowledge in practical situations.
4. **EVALUATE** — judge quality, evidence, limitations, tradeoffs, risks, and errors.
5. **CREATE / IMPROVE** — build, diagnose, transform, or improve something.

The engine selects the most meaningful five capabilities for the subject when the assessment specification calls for five dimensions.

For the flagship AI Score, preserve the established dimensions:

**Direction · Communication · Evaluation · Iteration · Systems Thinking.**

Universal methodology does not mean every topic gets identical dimension names.

---

# 13. QUESTION ARCHETYPE LAW

Use a mixture of capability-testing forms:

**DEFINE · EXPLAIN · DISTINGUISH · IDENTIFY · APPLY · DIAGNOSE · COMPARE · SEQUENCE · CHOOSE · EVALUATE · DESIGN · IMPROVE.**

Questions must be:

- relevant;
- understandable;
- unambiguous;
- fair;
- educational;
- appropriately challenging;
- answerable from supported knowledge;
- capable of distinguishing meaningful capability levels.

Do not use trick wording or obscure trivia merely to create difficulty.

The goal is **learning + measurement**, not humiliation.

---

# 14. 0–4 RUBRIC LAW

Every question has five defensible capability levels:

```text
0 = no meaningful demonstrated capability
1 = beginning awareness
2 = functional/basic capability
3 = strong practical capability
4 = advanced capability within supported scope
```

These are internal capability values, not arbitrary confidence ratings.

Answer wording must be topic-specific and logically defensible.

The user should be able to understand why an answer represents a higher capability level.

---

# 15. LEARNING-FIRST ASSESSMENT

MAXESS is not a gotcha test.

Its purpose is to help people learn faster and more effectively, then understand where they stand.

The experience should turn:

**NUMBER → UNDERSTANDING → CAPABILITY → OPPORTUNITY → NEXT ACTION.**

Teaching and assessment must be balanced so feedback increases understanding without corrupting the integrity of the measurement.

Results should reveal:

- strengths;
- opportunities;
- capability patterns;
- practical implications;
- next best learning action.

---

# 16. TOPIC COVERAGE LAW

Before attempting to compile a topic, classify coverage.

Suggested states:

**STRONG · GOOD · DEVELOPING · LIMITED · UNSUPPORTED.**

For limited/unsupported topics, MAXESS must not fabricate expertise.

Use a clear message such as:

> **We're not quite there yet. This topic is beyond our current assessment depth, but we're continually expanding what MAXESS can assess.**

Advanced topics such as quantum computing may be supported when the knowledge and rubric are strong enough. The goal is not to pretend to be an elite quantum physicist. The goal is to be extremely useful to ordinary learners within honest scope.

Feedback that identifies weaknesses in the system should become improvement input where appropriate.

---

# 17. E01–E09 RESULTS LAW

E01–E09 remain the canonical nine Results sections.

Each section must have a clearly documented responsibility and consume the same authoritative result contract.

Conceptually:

```js
renderE01(result)
renderE02(result)
renderE03(result)
...
renderE09(result)
```

Actual orchestration may differ, but authority may not.

Every section must answer:

- what data does this section consume?
- what is it allowed to derive for display?
- what must it never recalculate?
- what happens if the result is missing or invalid?

A presentation can derive display labels from already-authoritative data if that derivation is defined centrally. It must not create a competing score truth.

---

# 18. NAYA PRESENCE LAW

Naya is part of the experience, not a decorative mascot.

She should feel:

**PRESENT · ATTENTIVE · WARM · INTELLIGENT · ENCOURAGING · TRUSTWORTHY.**

Her visual presence should be beautiful, intentional, and subordinate to the user's task.

Useful interaction states may include:

**IDLE · ATTENTIVE · SPEAKING · LISTENING · CELEBRATING.**

Her communication should answer:

> What is happening?

> Why does it matter?

> What should I do next?

She should feel like someone is genuinely helping—not like a chatbot sticker has been placed on the interface.

---

# 19. SIGNATURE JEWEL CONTROL SYSTEM

Primary answer controls and important actions are signature MAXESS objects.

They should feel like:

> **jewelry + precision technology + energy**

Each major interactive control must be intentionally designed for:

**PURPOSE · MATERIAL · GEOMETRY · TYPOGRAPHY · LIGHTING · DEPTH · IDLE · HOVER · FOCUS · PRESSED · SELECTED · DISABLED · MOTION · ACCESSIBILITY.**

Interaction psychology:

- **HOVER = INVITATION**
- **PRESS = PHYSICALITY**
- **SELECT = CONFIRMATION**
- **TRANSITION = PROGRESS**
- **SCORE REVEAL = DISCOVERY**

The control should visibly come alive without becoming noisy.

Avoid:

- generic flat primary buttons;
- arbitrary Unicode pretending to be premium iconography;
- uncontrolled neon;
- excessive blur;
- gratuitous animation;
- effects that reduce contrast or speed.

Every effect must earn its performance cost.

---

# 20. VISUAL DESIGN LAW

Foundation:

- deep black / near-black;
- white typography;
- premium luminous purple;
- magenta / blue / green / yellow as intentional semantic rhythm;
- restrained gold where earned milestones justify it.

Use the established visual rhythm when appropriate:

**MAGENTA → PURPLE → BLUE → GREEN → YELLOW.**

Never use low-contrast purple-on-purple text.

Every scene must make it immediately obvious:

**WHERE AM I? → WHAT IS BEING ASKED? → WHAT DO I DO? → WHAT HAPPENED? → WHAT NEXT?**

Use the hierarchy:

**HEADLINE → SUPPORTING STATEMENT → DETAIL.**

Use the Maximus layering principle:

**CAKE → ICING → ICE CREAM → CHERRY → CARAMEL → WHIPPED CREAM → SPRINKLES.**

Additional layers must improve delight, not create clutter.

---

# 21. TYPOGRAPHY + SPACING LAW

Typography must be intentional at every viewport.

Audit:

- hierarchy;
- line length;
- weight;
- letter spacing;
- line height;
- text wrapping;
- icon/text alignment;
- card padding;
- button spacing;
- section spacing;
- whitespace;
- safe-area behavior.

Do not repair spacing by randomly accumulating margins.

Establish coherent visual tokens and relationships.

---

# 22. PERFORMANCE LAW

MAXESS must feel immediate.

Optimize:

- runtime dependencies;
- DOM size;
- JavaScript execution;
- event listeners;
- storage writes;
- repeated calculations;
- asset loading;
- animation cost;
- memory use;
- responsive rendering.

Prefer:

- event delegation where appropriate;
- transform/opacity animation;
- lazy/non-blocking asset work;
- deterministic computation;
- one-time result calculation;
- no polling;
- no unnecessary bridge layers.

**Beautiful + fast is the standard.**

---

# 23. RESPONSIVE LAW

Required target widths:

**320 · 360 · 375 · 390 · 414 · 480 · 600 · 768 · 900 · 1024 · 1280px.**

Do not merely shrink desktop.

Design the responsive composition intentionally.

Verify:

- no horizontal overflow;
- readable text;
- accessible controls;
- stable layout during state changes;
- Naya remains present without crowding the task;
- answer controls remain easy to touch;
- results remain legible;
- no critical content disappears.

---

# 24. ACCESSIBILITY LAW

Required:

- semantic controls;
- keyboard navigation;
- visible focus;
- meaningful labels;
- correct ARIA state;
- live regions where state changes need announcement;
- sufficient contrast;
- adequate touch targets;
- reduced-motion support;
- no interaction that exists only through pointer hover.

Accessibility is core engineering quality, not final icing.

---

# 25. FAILURE + RECOVERY LAW

Handle explicitly:

- missing topic;
- unsupported topic;
- malformed assessment configuration;
- incomplete assessment;
- invalid answer;
- duplicate Continue activation;
- missing result;
- malformed result;
- missing dimension;
- corrupted local state;
- unexpected navigation;
- failed external handoff;
- stale/legacy source.

Never silently produce a false success.

A valid local result must remain recoverable even if external navigation fails.

---

# 26. SOURCE INVENTORY — FIRST EXECUTION

Before making major architectural changes, inventory:

### Assessment

- `E00 796`
- `E00 700`
- `E00 1800`
- `E00.01`
- `E00.02`
- `E00.03`

### Results

- `E01`
- `E02`
- `E03`
- `E04`
- `E05`
- `E06`
- `E07`
- `E08`
- `E09`
- `E01-SECTION-01-WORKING.html`
- existing Results consumer/integration artifacts

### Governance / knowledge

- `PROJECTS/MAXESS/README.md`
- `PROJECTS/MAXESS/MAXESS-EXECUTION-LOG.md`
- prior MAXESS directives and change ledgers;
- Naya Power Smart Notes/CIS laws;
- Naya Master Coder/Designer laws;
- Superbrain/SOM(E)/Oscar standards;
- AI/Life knowledge-bank material;
- HMC/MAXIS button and icon specifications.

Create a source matrix:

| Artifact | Proven Good | Failure / Risk | Reusable | Replace / Remove | Evidence |
|---|---|---|---|---|---|

Do not select a canonical implementation until this inventory has been performed.

---

# 27. REBUILD ORDER

Execute in this order unless evidence justifies a change:

```text
01. READ CANONICAL GOVERNANCE
02. INVENTORY SOURCE MATERIAL
03. MAP GOOD / BAD / REUSABLE / OBSOLETE
04. DEFINE UNIVERSAL DATA MODEL
05. DEFINE STATE CONTRACT
06. DEFINE SCORING CONTRACT
07. DEFINE MAXESS_RESULT_V1 CONTRACT
08. BUILD AUTHORITATIVE E00 ENGINE
09. VERIFY E00 IN ISOLATION
10. CONNECT E01–E09 AS CONSUMERS
11. VERIFY END-TO-END DATA FLOW
12. MAKE AI SCORE THE GOLDEN REGRESSION TEST
13. BUILD DYNAMIC TOPIC COMPILER FOUNDATION
14. PROVE A SECOND SUPPORTED TOPIC
15. PERFORM FLAGSHIP VISUAL PASS
16. PERFORMANCE PASS
17. ACCESSIBILITY PASS
18. RESPONSIVE PASS
19. OSCAR 10/10 CHALLENGE
20. AUTOMATED QA
21. LIVE END-TO-END QA
22. CAPTURE EVIDENCE
23. WRITE HUMAN + AI SMART NOTE
24. WRITE HUMAN-READABLE VERIFICATION RECEIPT
25. UPDATE PROJECT STATE
26. ISSUE NEXT EXECUTION
27. RE-VERIFY AFTER ANY FIX
28. FREEZE ONLY WHAT IS ACTUALLY GREEN
```

---

# 28. GREEN / RED EXECUTION SYSTEM

Every execution must maintain a visible status register.

```text
🟢 GREEN = implemented AND verified by evidence
🔴 RED   = not implemented OR not verified
🟡 YELLOW = implemented but verification incomplete / ambiguous
```

**Critical rule:** code existence is not green.

A requirement becomes green only when the required behavior has been executed and observed successfully.

When a phase is fully green, move to the next phase. When red/yellow remains, work the highest-leverage blocker first.

Never hide uncertainty behind optimistic wording.

---

# 29. TESTING LAW

Every meaningful requirement should map to:

**REQUIREMENT → IMPLEMENTATION → TEST → OBSERVED RESULT → EVIDENCE → VERIFICATION → DOCUMENTED STATE.**

### Unit / logic

Test:

- answer validation;
- progression;
- response persistence;
- scoring;
- normalization;
- dimension aggregation;
- result construction;
- result validation.

### Integration

Test:

**E00 → MAXESS_RESULT_V1 → E01–E09.**

### UI

Test:

- selection;
- Continue;
- progress;
- keyboard interaction;
- Naya;
- animations;
- result release;
- responsive behavior.

### End-to-end

Run the complete assessment from first load through E09.

---

# 30. GOLDEN AI SCORE TEST

The canonical regression test must prove:

- exactly 15 questions;
- exactly 5 answers per question;
- answer values exactly 0–4;
- five expected dimensions;
- all expected responses saved;
- correct raw score;
- correct normalized 0–100 score;
- correct mastery band;
- correct dimension scores;
- correct fingerprint where specified;
- valid `MAXESS_RESULT_V1`;
- E01–E09 consume that same result;
- no downstream rescoring;
- final Results release occurs only after valid completion.

Test minimum, maximum, middle, and representative mixed-response scenarios.

---

# 31. EDGE CASE TESTS

Explicitly test:

- lowest possible score;
- highest possible score;
- middle score;
- every answer option;
- answer selection changes before Continue where supported;
- rapid repeated Continue;
- keyboard selection;
- mobile touch;
- refresh/recovery where applicable;
- incomplete assessment;
- direct Results access;
- missing result contract;
- malformed result contract;
- duplicate completion;
- failed external handoff;
- unsupported topic;
- advanced/limited topic.

---

# 32. LIVE EVIDENCE LAW

A claim that “it works” is not evidence.

Evidence must demonstrate the actual journey:

```text
START
 ↓
QUESTION 1
 ↓
ANSWER
 ↓
QUESTION 2
 ↓
...
 ↓
QUESTION 15
 ↓
SCORE
 ↓
E01
 ↓
E02
 ↓
...
 ↓
E09
 ↓
FINAL RESULT
```

Where possible capture meaningful checkpoints and automated test output.

Source code alone does not prove live behavior.

---

# 33. SOURCE / BUILD / LIVE PARITY LAW

The following are distinct facts:

1. source contains the code;
2. build/embed contains the code;
3. deployed/live product runs the code;
4. live behavior succeeds.

Do not collapse them into one claim.

Required release evidence:

**SOURCE → BUILD/EMBED → LIVE CHECK → OBSERVED RESULT → EVIDENCE.**

A public URL does not establish source authority.

---

# 34. OSCAR 10/10 LAW

Before declaring completion, challenge the work independently:

### ENGINEERING
Is it deterministic?

### ARCHITECTURE
Is there one authority?

### SCORING
Can the mathematics be reproduced?

### STATE
Can every transition be explained?

### UX
Can a new user understand it instantly?

### DESIGN
Does it look extraordinary rather than merely acceptable?

### INTERACTION
Do controls feel alive and tactile?

### NAYA
Does she feel present and helpful?

### PERFORMANCE
Does visual quality remain fast?

### RESPONSIVE
Is it excellent at every required width?

### ACCESSIBILITY
Can people actually use it?

### RESILIENCE
What happens when something fails?

### MAINTAINABILITY
Can another AI understand it tomorrow?

### EXTENSIBILITY
Can it support another assessment without rewriting the engine?

### EVIDENCE
Can every important claim be proven?

If any critical answer is no, it is not finished.

---

# 35. SMART NOTE LAW — DEFAULT BEHAVIOR

Meaningful MAXESS mastermind/project work is durable project knowledge.

When a session produces future-value learning, capture it automatically as a canonical Note Event.

Record meaningful:

- decisions;
- discoveries;
- lessons;
- design principles;
- architecture insights;
- failures;
- safeguards;
- performance insights;
- UX insights;
- corrections;
- next actions.

Do not preserve conversational noise merely to create volume.

Every meaningful Smart Note delivery must have:

### HUMAN NOTE
Human-readable explanation of what happened, what was decided, why it matters, and what comes next.

### AI NOTE
Operational handoff explaining what another AI needs to know to continue correctly.

### OPTIONAL JSON
Machine-readable representation where useful.

### HUMAN-READABLE RECEIPT
Proof that the note was created, stored, and verified.

**Never send a JSON-only URL as the human Smart Note receipt.**

The default human link is the human-readable note.

---

# 36. CONTINUITY LAW

Assume tomorrow:

- a new chat starts;
- a different AI takes over;
- an engineer joins;
- the human forgets exactly where work stopped.

The project must still explain itself.

Preserve:

**CURRENT STATE → WHAT CHANGED → WHY → EVIDENCE → WHAT IS GREEN → WHAT IS RED/YELLOW → NEXT EXECUTION.**

We never go below the verified line.

**LEVEL UP, NEVER LEVEL DOWN.**

---

# 37. EXECUTION COMMUNICATION LAW

The lead AI must take control of the process.

Do not make the human repeatedly manage the project.

For each execution:

1. state the current truth;
2. identify the highest-leverage work;
3. execute as much as safely possible in the current output;
4. verify what was changed;
5. classify green/yellow/red;
6. preserve the learning;
7. issue the next execution prompt.

Do not stop at “I found X.”

Move from discovery to solution whenever the work is in scope and evidence-backed.

---

# 38. MAXIMUM-OUTPUT RULE

Within a single execution, maximize useful throughput without sacrificing verification.

Batch related safe operations together.

Do not create artificial micro-executions when one coherent execution can:

- inspect multiple artifacts;
- reconcile contracts;
- implement related changes;
- run related tests;
- update documentation;
- create receipts;
- prepare the next execution.

But never trade verification for speed.

**Effective efficiency = maximum verified progress per execution.**

---

# 39. NO PERMISSION STALLING

If an issue is:

- clearly in scope;
- safe;
- necessary;
- evidence-backed;

fix it without unnecessary permission requests.

Ask only when a decision genuinely cannot be inferred from the canonical source, project contract, or user-approved North Star.

---

# 40. CHANGE DISCIPLINE

Before modifying a canonical artifact:

1. verify its current source;
2. understand what it does;
3. identify what depends on it;
4. preserve a recoverable version where required by project law;
5. make the smallest coherent change that solves the architectural problem;
6. test it;
7. update evidence and state.

Do not create a patch merely to make a failing symptom disappear.

---

# 41. DEFINITION OF DONE

MAXESS is not done when source code exists.

It is done when evidence proves:

- the authoritative E00 assessment runs;
- all 15 AI Score questions work;
- every answer can be selected;
- responses are saved exactly once;
- Q15 completes deterministically;
- scoring is correct;
- `MAXESS_RESULT_V1` is valid;
- E01–E09 consume the same result authority;
- no competing score/result authority remains;
- a second supported topic can compile and run;
- unsupported/advanced coverage boundaries are honest;
- Naya is present and useful;
- jewel controls feel premium and alive;
- performance is fast;
- responsive checks pass;
- accessibility checks pass;
- source/live parity is proven;
- Oscar finds no unresolved critical defect;
- Smart Notes are captured;
- a human-readable verification receipt exists;
- the next execution state is documented.

---

# 42. MASTER APPRENTICE COMMAND

> **Do not try to make the old architecture survive. Make the intended system succeed.**
>
> Study everything. Learn from every failure. Preserve proven value. Remove fragile complexity. Establish one state authority. Establish one scoring authority. Establish one result contract. Make E01–E09 deterministic consumers. Build the dynamic assessment foundation now so AI Score is the golden first assessment rather than the permanent architectural limit.
>
> Then make the machine beautiful. Make the controls feel alive. Make Naya feel present. Make the interface powerful but simple. Make it fast, accessible, responsive, resilient, maintainable, and understandable.
>
> Ask at every meaningful boundary:
>
> **Can this be faster? Can this be simpler? Can this be clearer? Can this be more beautiful? Can this feel more alive? Can Naya feel more present? Can this be warmer? Can this be more trustworthy? Can this be more accessible? Can this be more resilient? Can this be more effortless? What would make this a 10?**
>
> Then test the answer.
>
> Do not say it works because the code looks correct.
>
> **Show the evidence.**
>
> Do not say it is 10/10 because it is impressive.
>
> **Interrogate it until the important weaknesses are gone.**
>
> The goal is not yesterday's code.
>
> **The goal is the MAXESS flagship machine.**

---

# 43. MASTER EXECUTION LOOP

```text
READ
 ↓
UNDERSTAND
 ↓
INVENTORY
 ↓
DECIDE
 ↓
BUILD
 ↓
TEST
 ↓
OBSERVE
 ↓
VERIFY
 ↓
DOCUMENT
 ↓
RECEIPT
 ↓
NEXT EXECUTION
 ↓
LEARN
 ↓
IMPROVE
 ↓
REPEAT
```

### Status loop

```text
🔴 RED / 🟡 YELLOW
        ↓
EXECUTE
        ↓
TEST
        ↓
🟢 GREEN
        ↓
NEXT GATE
        ↓
FINAL VALIDATION
        ↓
FREEZE ONLY AFTER PROOF
```

**This is the operating standard for every MAXESS AI and human collaborator.**
