# MAXESS E02 — EXECUTION LOCK + ULTIMATE IMPLEMENTATION PROMPT

**STATUS: HARD LOCK**

**Repository:** `SoulSchoolAcademy/MaxRESULTS`

**Engineering branch:** `maxess-results-v21-working`

**Active artifact:** `E02-SECTION-02-WORKING.html`

**Protected artifact:** `E01-SECTION-01-WORKING.html`

**Protected E01 blob:** `c01ba966c4b1439b8b3e95161c6f8316202736d8`

**Runtime authority:** `window.MAXESS_RESULT`

---

## 1. PURPOSE

Section 02 is a continuation of the Results experience immediately below Section 01.

Its sole product job is:

> **SHOW THE USER THEIR FIVE CAPABILITY DIMENSIONS.**

E02 is intentionally simple. It is a visual reveal, not a second report, second scoring engine, second application, or second interpretation layer.

The experience is:

**SECTION 01 → MEET YOUR RESULT**

↓

**SECTION 02 → SEE YOUR FIVE-DIMENSION CAPABILITY PROFILE**

↓

**SECTION 03 → UNDERSTAND WHAT IT MEANS**

↓

**SECTION 04+ → DISCOVER WHAT TO DO WITH IT**

Do not pull later-section interpretation, marketing, CTAs, report copy, or explanation into E02.

---

# LAW 01 — E01 IS SACRED

`E01-SECTION-01-WORKING.html` is a protected, frozen artifact.

Protected blob:

`c01ba966c4b1439b8b3e95161c6f8316202736d8`

The following are absolutely forbidden:

- editing E01
- rewriting E01
- refactoring E01
- cleaning up E01
- changing E01 HTML
- changing E01 CSS
- changing E01 JavaScript
- changing E01 structure
- changing E01 assets
- changing E01 behavior
- changing E01 copy
- changing E01 spacing
- changing E01 Orb behavior
- changing E01 Orbital Bead behavior
- changing E01 result handling
- copying E01 into another renderer as a substitute for building E02
- using E02 requirements as a reason to alter E01
- making any dependency in E01 on E02

**NOTHING IN E01 MAY BE MODIFIED.**

If E02 needs something, **E02 adapts to E01. Never alter E01 to make E02 easier.**

E01 is the foundation. Build downward from it.

---

# LAW 02 — DO NOT REBUILD THE PAGE

Do not rebuild, reconstruct, duplicate, or replace the Results page to implement E02.

Read the source top-to-bottom and identify where E01 ends. E02 begins immediately after that boundary.

The mental model is:

> **Where does Section 01 end, and what is the next visual experience immediately below it?**

Then implement only that next experience.

Forbidden:

- recreating the E01 shell
- duplicating E01 markup
- duplicating E01 JavaScript
- creating a second application shell
- creating a second Results page
- creating a second scoring engine
- creating a second result object
- creating a competing renderer
- replacing the complete artifact with a tiny renderer
- loading an external Results HTML file
- using an iframe to fake the continuation
- creating a mock or placeholder E02
- restructuring E01 so E02 can fit

E02 is a continuation, not a replacement.

---

# LAW 03 — E02 HAS ONE JOB

E02 exists to display five capability dimensions.

Each dimension consists of exactly these visible essentials:

1. **Dimension name**
2. **Authoritative score** shown as `NN / 100`
3. **Physical MAXESS Orb**
4. **One unique jewel color**
5. **Restrained orbital motion** via a luminous bead

That is the core experience.

Nothing else is required to make E02 complete.

---

# LAW 04 — FIVE OBJECTS, NOT FIVE WIDGETS

The five dimensions must visually read as five physical objects in a capability field.

They must NOT read as:

- cards
- tiles
- dashboard widgets
- charts
- table cells
- generic webpage components
- five miniature app panels
- boxed UI modules

The visual question should be answered instantly:

> **What are these five things inside my capability?**

Not:

> **Okay, here is another dashboard.**

The composition is a **capability constellation / spatial field**.

---

# LAW 05 — ORB VISUAL SPECIFICATION

Each Orb is a physical, jewel-like MAXESS object with:

- deep black physical core
- dimensional internal light
- jewel-colored internal energy/glow
- subtle dimensional outer edge
- soft environmental shadow
- restrained atmospheric glow
- small luminous orbital bead
- subtle breathing/presence
- centered score

The Orb should feel substantial, dimensional, premium, and alive.

It must inherit the established MAXESS Orb language without editing E01.

The Orb is the visual hero of each dimension.

Do not add decorative complexity merely to make the section look busy.

---

# LAW 06 — FIVE-COLOR SYSTEM

Use one distinct jewel identity per dimension:

| Dimension | Jewel identity |
|---|---|
| 1 | Purple |
| 2 | Magenta / Coral |
| 3 | Emerald |
| 4 | Electric Blue |
| 5 | Gold |

The palette must remain controlled and coherent.

Forbidden:

- rainbow treatment
- arbitrary colors
- excessive color mixing
- gradients used everywhere merely for decoration
- color effects that overpower the score
- color as the sole carrier of meaning

Each Orb should clearly belong to the same MAXESS Orb family while retaining its own jewel identity.

---

# LAW 07 — SCORE IS THE HERO

Inside every Orb, the primary content is:

**`NN / 100`**

The score must be immediately readable.

The numeric value is the hero.

`/ 100` is secondary but must remain clearly legible.

Do not bury, miniaturize, obscure, or visually compete with the score.

Do not rely on color alone to communicate the score.

Do not render the score as unnecessary HTML markup when simple deterministic text nodes are sufficient.

The intended visual hierarchy is:

**ORB → SCORE → DIMENSION NAME**

Example:

**PURPLE ORB → 91 / 100 → VISION**

---

# LAW 08 — DIMENSION NAME

Each Orb has exactly one clear dimension name associated with it.

The name appears directly beneath or immediately associated with its Orb, outside the Orb itself unless the current design proves a better equally simple treatment.

The name must be readable and semantically associated with the score.

Do not add descriptions, definitions, paragraphs, badges, explanations, or secondary labels to the Orb object.

---

# LAW 09 — ORBITAL BEAD

Each Orb has one small luminous bead that travels around the Orb.

The bead must:

- continuously orbit the Orb
- remain physically associated with the Orb circumference
- use a dimension-appropriate jewel glow
- move smoothly
- remain visually subordinate to the Orb and score
- never fly away from the Orb
- never visually detach from the object
- never become the focal point
- stop when reduced motion is requested

The orbital radius must be dimension-aware and responsive so the bead remains physically associated with the Orb at every supported size.

Do not use one fixed desktop radius across all mobile sizes.

The orbit is a presence cue, not a spectacle.

---

# LAW 10 — ORB BREATHING

Orb breathing may be used to create subtle physical presence.

It should feel like:

**inhale → hold → exhale**

Very slowly.

The desired effect is **presence**, not obvious animation.

Do not use aggressive scaling, spinning, pulsing, bouncing, flashing, or attention-seeking motion.

Reduced-motion preferences must disable or substantially minimize motion.

---

# LAW 11 — DESKTOP COMPOSITION

Desktop presents five substantial Orbs in one spatial capability field.

Conceptually:

```text
        ORB       ORB       ORB       ORB       ORB
       91/100    76/100    88/100    69/100    94/100
       VISION   CREATION   THINKING   EXECUTION  ADAPTATION
```

The exact names and scores come from the authoritative result data.

The composition must NOT feel like five rigidly identical widgets.

Controlled variation may be used in:

- Orb scale
- vertical position
- glow intensity
- orbit radius
- central emphasis

The center Orb may have slightly greater visual presence.

Variation must remain restrained enough that all five clearly belong to one system.

The objective is **constellation**, not chaos.

---

# LAW 12 — MOBILE COMPOSITION

Mobile must be intentionally composed, not a shrunken desktop dashboard.

Preferred conceptual structure:

```text
       ORB          ORB
      91/100       76/100

       ORB          ORB
      88/100       69/100

             ORB
            94/100
```

The exact dimensions and scores are data-driven.

The fifth Orb is centered.

All five Orbs must remain substantial and recognizable at approximately 390px and 360px widths.

Do not shrink the Orbs until the score becomes weak or the objects become decorative dots.

Do not allow the orbital bead to escape the physical Orb boundary at smaller sizes.

Responsive behavior must be intentional at desktop, tablet, mobile, approximately 430px, and approximately 360px.

---

# LAW 13 — PEARL ENVIRONMENT, NOT DASHBOARD CONTAINER

If a pearl/light environment is used, it should support the five Orbs as an atmospheric spatial plane.

Do not put the Orbs inside a giant white rounded rectangle that makes the section resemble a dashboard.

Avoid:

- giant cards
- boxed Orb collections
- heavy borders
- unnecessary shadows around containers
- UI chrome that competes with the objects

The environment supports the objects.

The objects do not sit inside a dashboard.

---

# LAW 14 — NO UNNECESSARY CONTENT

E02 does NOT need:

- explanatory paragraphs
- capability descriptions
- marketing copy
- giant supporting nodes
- calls to action
- report teasers
- instructional copy
- decorative cards
- dashboard containers
- additional interpretation
- sales language
- solution language
- Naya marketing language
- report analysis
- “what this means” copy
- recommendations
- next-step copy

Personalized interpretation belongs in later sections.

**When in doubt, remove it.**

---

# LAW 15 — E02 MUST NOT THINK

E02 is intentionally a rendering layer.

It does not:

- calculate scores
- score answers
- reinterpret scores
- infer personality
- generate personalized analysis
- create a second result object
- create a second scoring model
- change the authoritative result
- invent fallback scores
- silently substitute fake data

Its job is:

```text
window.MAXESS_RESULT
        ↓
resolve five authoritative dimension values
        ↓
render five Orbs
        ↓
render five scores
        ↓
render five names
```

Nothing more.

Use `window.MAXESS_RESULT` as the authoritative runtime source.

Do not search `window`, `parent`, `top`, unrelated globals, alternate stores, mock objects, or competing result sources for authority.

If authoritative result data is unavailable or incomplete, fail safely and visibly rather than inventing a result.

---

# LAW 16 — EXACTLY FIVE

E02 must generate exactly five canonical capability dimensions.

There must be:

- exactly five Orb objects
- exactly five scores
- exactly five dimension names
- exactly five jewel identities
- exactly five accessible dimension/score relationships

Do not create duplicates.

Do not create a sixth decorative Orb.

Do not omit a dimension.

Do not duplicate a dimension.

Do not hard-code user-specific scores into the visual renderer.

---

# LAW 17 — DATA / PRESENTATION SEPARATION

The result data and presentation must remain separate.

The authoritative result provides the values.

The E02 renderer maps those values to visual objects.

The renderer must not become a second scoring engine.

No duplicated scoring logic is permitted.

No hard-coded user-specific result values are permitted.

---

# LAW 18 — ACCESSIBILITY

E02 must remain accessible without depending solely on color or animation.

Required:

- semantic section structure
- meaningful heading/label structure
- accessible Orb labels
- accessible score labels
- score meaning available in text
- keyboard-safe interaction if any interaction is introduced
- visible focus if any focusable element is introduced
- sufficient contrast
- reduced-motion support
- safe missing-data state

E02 should require no interaction to understand the five dimensions.

---

# LAW 19 — SCOPE DISCIPLINE

Do not add a feature because it is technically possible.

Do not add a feature because the section looks “too simple.”

Do not add a card because there is empty space.

Do not add text because the page could contain more information.

Do not add a CTA because the user will eventually need one.

Do not add a supporting node because it makes the code feel more complete.

**Simple is the intended design.**

The sophistication comes from execution quality:

**five simple objects made extraordinarily well.**

---

# LAW 20 — STOP CONDITION

E02 is complete when all of the following are true:

- five Orbs render
- five authoritative scores render
- five correct dimension names render
- five jewel colors render
- Orb cores are dimensional and premium
- scores are immediately readable
- orbital beads remain physically attached
- orbital motion is restrained
- breathing is restrained
- reduced motion is respected
- desktop composition reads as a constellation
- mobile composition is intentional
- 360–390px remains substantial and readable
- `window.MAXESS_RESULT` is the sole runtime authority
- no second scoring engine exists
- no competing renderer exists
- no unnecessary E02 content remains
- E01 remains byte-for-byte unchanged

When all conditions pass, **STOP.**

Do not expand E02 after it meets the contract.

Freeze E02 and move to Section 03.

---

# LAW 21 — MECHANICAL E01 PROTECTION CHECKPOINTS

Before EVERY E02 mutation:

### CHECKPOINT A — E01 BEFORE

Fetch the current E01 artifact and verify its blob equals:

`c01ba966c4b1439b8b3e95161c6f8316202736d8`

If it does not match, **STOP. Do not modify anything.** Report the mismatch.

### CHECKPOINT B — E02 BEFORE

Fetch the current E02 artifact and record its exact current blob/content state.

### CHECKPOINT C — MUTATION SCOPE

The authorized mutation target is:

`E02-SECTION-02-WORKING.html`

No other file may be modified for the E02 implementation itself.

### CHECKPOINT D — E01 AFTER

After the mutation, refetch E01 and verify the blob still equals:

`c01ba966c4b1439b8b3e95161c6f8316202736d8`

If it differs, the execution is a **FAILURE**, regardless of how good E02 looks.

### CHECKPOINT E — TREE / DIFF

Verify the repository change scope.

Expected implementation mutation:

**E02 only.**

Any E01 mutation is prohibited.

### CHECKPOINT F — QA

Only after the protection checks pass may E02 QA proceed.

---

# LAW 22 — EXECUTION LOOP

For every E02 execution:

**GITHUB FIRST**

→ read canonical governance

→ read active branch map

→ read this E02 execution lock

→ verify E01 protected blob

→ fetch current E02

→ establish actual state

→ identify exact defect(s)

→ score against this contract

→ implement only E02 repairs

→ refetch E02

→ diff E02

→ verify E01 blob again

→ static QA

→ JavaScript QA

→ responsive QA

→ accessibility QA

→ browser/render QA when available

→ Groove/live QA only when actually performed

→ OSCAR ruthless review

→ repair if needed

→ re-test

→ regression-check E01

→ freeze E02 only when the stop condition passes

→ record durable learning when material

→ report explicit verification state

Never claim runtime, Groove, or live verification that did not actually occur.

---

# LAW 23 — VERIFICATION STATES

Use only these states:

- **IMPLEMENTED** — source mutation exists.
- **VERIFIED** — source/test evidence confirms the requirement.
- **LIVE VERIFIED** — actual public/Groove runtime was inspected and confirmed.
- **HUMAN REVIEW REQUIRED** — source is ready but human visual judgment remains necessary.
- **UNKNOWN** — evidence is unavailable.

Do not convert source verification into browser verification.

Do not convert browser verification into Groove verification.

Do not convert a GitHub commit into live verification.

---

# LAW 24 — OSCAR REVIEW

Before declaring E02 complete, ask:

1. Are the five Orbs the first visual thing the eye understands?
2. Do they feel like physical objects rather than UI components?
3. Does the center Orb have appropriate importance without breaking family consistency?
4. Are the scores unmistakable at a glance?
5. Does `/ 100` remain readable?
6. Does the environment feel luxurious rather than like a white webpage/dashboard?
7. Does the composition feel spatial rather than boxed?
8. Are the five colors coherent and restrained?
9. Is the bead physically attached to every Orb at every supported size?
10. Is the motion restrained enough to feel like presence rather than animation?
11. Does mobile still feel premium at 390px and 360px?
12. Is there anything on screen that does not serve the five-Orb reveal?
13. Is there any duplicated scoring or result logic?
14. Did E01 remain byte-for-byte unchanged?
15. Does the section make the user think:

> **“What are these five things inside my capability?”**

rather than:

> **“Okay, here is another dashboard.”**

If any answer is weak, identify the root cause and repair E02 only.

---

# E02 SCORECARD

| Category | Acceptance |
|---|---|
| Structure | Exactly five capability Orbs |
| Data | Exactly five authoritative dimension scores |
| Visual | Five unmistakable physical MAXESS Orbs |
| Color | Five distinct jewel identities |
| Motion | Restrained orbital bead + subtle breathing |
| Readability | Every score immediately readable |
| Responsive | Substantial and readable at 360–390px |
| Architecture | No scoring engine, competing renderer, or duplicate result source |
| Protection | E01 byte-for-byte unchanged |
| Scope | Nothing unnecessary |

Target: **10/10.**

If not 10, ask:

> **WHY IS THIS NOT A 10?**

Then repair the root cause rather than adding superficial decoration.

---

# ULTIMATE COPY-PASTE EXECUTION PROMPT

Use the following prompt when handing E02 to an implementation agent:

---

**NAYA MASTER ON.**

**NAYA LAW ON.**

**NAYA NITRO ON.**

**NAYA LEAD MODE ON.**

# MAXESS E02 — FIVE-DIMENSION ORB EXPERIENCE
## HARD-LOCKED IMPLEMENTATION DIRECTIVE

### GITHUB FIRST — ABSOLUTE

Repository:

`SoulSchoolAcademy/MaxRESULTS`

Engineering branch:

`maxess-results-v21-working`

Read the canonical repository governance and active branch map before acting.

Then read:

`docs/MAXESS-E02-EXECUTION-LOCK.md`

This document is the task-specific source of truth for E02 implementation constraints and acceptance criteria, subject to canonical `main` governance and explicit current human instructions.

Active artifact:

`E02-SECTION-02-WORKING.html`

Protected artifact:

`E01-SECTION-01-WORKING.html`

Protected E01 blob:

`c01ba966c4b1439b8b3e95161c6f8316202736d8`

Runtime authority:

`window.MAXESS_RESULT`

---

## ABSOLUTE PROTECTION LAW

**DO NOT TOUCH E01.**

Before doing anything, fetch E01 and verify its blob is exactly:

`c01ba966c4b1439b8b3e95161c6f8316202736d8`

If it is not, STOP.

During and after execution, E01 must remain exactly that blob.

Do not edit, rewrite, refactor, clean, copy, restructure, restyle, or otherwise mutate E01 for any reason.

If E02 appears to require a change to E01, the correct response is to redesign E02 so it adapts to the existing E01.

**E01 is finished. E01 is sacred. E01 is not an editing zone.**

---

## DO NOT REBUILD THE PAGE

Follow the existing document from top to bottom.

Find where E01 ends.

E02 begins immediately below it.

Build only the E02 continuation.

Do not recreate the page shell.

Do not duplicate E01.

Do not create a second Results application.

Do not create a second scoring engine.

Do not create a second result source.

Do not create a competing renderer.

Do not use an iframe, external HTML loader, mock, placeholder, or tiny replacement renderer.

---

# THE E02 JOB

E02 has one job:

> **SHOW THE USER THEIR FIVE CAPABILITY DIMENSIONS.**

The complete visible concept is:

**five physical Orbs + five scores + five dimension names + five jewel colors + restrained orbital motion.**

Nothing else is necessary.

---

# BUILD THE FIVE ORBS

Create exactly five Orb objects.

Each Orb must be a premium physical object with:

- deep black core
- dimensional internal light
- jewel-colored internal energy
- subtle dimensional edge
- soft shadow
- restrained glow
- luminous orbital bead
- subtle breathing/presence
- centered score

The five Orbs must look like members of one MAXESS Orb family.

They must feel like physical objects, not cards or dashboard widgets.

---

# FIVE COLORS — LOCKED

Dimension 1 = Purple

Dimension 2 = Magenta / Coral

Dimension 3 = Emerald

Dimension 4 = Electric Blue

Dimension 5 = Gold

Keep the palette controlled.

No rainbow treatment.

No unnecessary decorative color system.

---

# SCORE — LOCKED

Inside each Orb, show:

`NN / 100`

The number is the hero.

`/ 100` is secondary but clearly readable.

The score must be immediately understandable without reading instructions.

Do not bury the score.

Do not make `/ 100` microscopic.

Do not use color as the only score signal.

---

# DIMENSION NAME — LOCKED

Place the dimension name directly beneath or immediately associated with its Orb.

No paragraph.

No description.

No secondary explanation.

No interpretation.

The user should understand the object in one glance:

**ORB → SCORE → DIMENSION NAME**

---

# ORBIT — LOCKED

Each Orb receives one small luminous bead.

The bead must orbit continuously around the physical Orb circumference.

It must:

- stay physically attached
- move smoothly
- glow softly
- remain subordinate
- never fly away
- never detach visually
- stop under reduced motion

Use responsive/dimension-aware orbit radii so the bead remains physically associated with the Orb on desktop, tablet, 430px, 390px, and 360px widths.

Do not use one oversized fixed radius across all breakpoints.

---

# BREATHING — LOCKED

Use subtle Orb breathing only.

It should feel like:

**inhale → hold → exhale**

Slowly.

The goal is physical presence, not visible animation.

Reduced motion must disable or minimize it.

---

# DESKTOP — LOCKED COMPOSITION PRINCIPLE

Present five substantial Orbs as one spatial capability constellation.

Conceptually:

```text
        ORB       ORB       ORB       ORB       ORB
       SCORE     SCORE     SCORE     SCORE     SCORE
       NAME      NAME      NAME      NAME      NAME
```

Do not make them five rigidly identical dashboard tiles.

Controlled differences in scale, vertical position, glow, and orbit radius are permitted.

The center Orb may be slightly more prominent.

The result must feel intentional, spatial, premium, and unified.

---

# MOBILE — LOCKED COMPOSITION PRINCIPLE

Do not compress the desktop dashboard into tiny objects.

Use an intentional two-column composition with the fifth Orb centered:

```text
       ORB          ORB

       ORB          ORB

             ORB
```

All five Orbs must remain substantial.

Scores must remain readable.

Names must remain readable.

The Orb/bead relationship must remain physically correct.

Test approximately 390px and 360px explicitly.

---

# REMOVE EVERYTHING UNNECESSARY

Do NOT add:

- explanatory paragraphs
- capability descriptions
- marketing copy
- supporting nodes
- CTA buttons
- report teasers
- instructions
- decorative cards
- dashboard containers
- interpretations
- recommendations
- sales copy
- Naya marketing copy

Section 03 will explain what the five dimensions mean.

E02 is the visual reveal only.

If something is not required for the five-Orb reveal, remove it.

---

# DATA — LOCKED

Read only from:

`window.MAXESS_RESULT`

Do not calculate scores.

Do not score answers.

Do not reinterpret results.

Do not create another result object.

Do not search parent/top/window fallbacks.

Do not invent missing values.

Resolve exactly five canonical dimension scores and render them.

If the authoritative result is unavailable or incomplete, fail safely rather than fabricating data.

---

# IMPLEMENTATION DISCIPLINE

Before mutation:

1. Verify E01 blob.
2. Fetch current E02.
3. Establish exact current state.
4. Identify only the defects relevant to this contract.
5. Implement only E02 changes.

After mutation:

1. Refetch E02.
2. Diff E02.
3. Verify E01 blob again.
4. Confirm E01 is unchanged.
5. Confirm the implementation mutation is E02 only.
6. Run static QA.
7. Run JS/data QA.
8. Run responsive QA.
9. Run accessibility QA.
10. Render/browser-test if available.
11. Groove-test only if actually available.
12. Run OSCAR review.
13. Repair remaining defects.
14. Re-test.

Never claim verification that did not happen.

---

# COMPLETION GATE

E02 is DONE only when:

- exactly five Orbs exist
- exactly five authoritative scores render
- exactly five names render
- exactly five jewel colors are applied
- the Orbs look physical and premium
- scores are unmistakable
- `/ 100` is readable
- beads orbit correctly
- beads remain physically associated at mobile sizes
- breathing is subtle
- reduced motion works
- desktop feels like a constellation
- mobile feels intentional
- 360px and 390px remain readable
- `window.MAXESS_RESULT` is the sole result authority
- no scoring engine exists in E02
- no competing renderer exists
- no unnecessary content remains
- E01 blob is still exactly `c01ba966c4b1439b8b3e95161c6f8316202736d8`

Then STOP.

Do not add more.

Freeze E02.

Move to Section 03.

---

# OSCAR — FINAL QUESTION

Do not ask whether the code is clever.

Ask:

> **Does the user instantly see five beautiful physical objects representing five dimensions of their capability?**

And:

> **Does it feel like MAXESS rather than a dashboard?**

And:

> **Did we achieve it without changing one byte of E01?**

If not, repair E02 only.

**WHY IS THIS NOT A 10?**

Find the root cause.

Repair it.

Verify again.

---

# REQUIRED FINAL REPORT

Return:

## CURRENT STATE

What actually exists in GitHub now.

## WHAT WAS FOUND

The exact source-level state and defects.

## WHAT CHANGED

Only E02 changes, with exact file/blob evidence.

## E01 PROTECTION

Explicitly report the before/after E01 blob and whether they match.

## QA

Static / JS / responsive / accessibility / browser / Groove status, each explicitly classified.

## OSCAR

What still prevents a 10, if anything.

## RECOMMENDATION

The single highest-value next action.

## EXACT NEXT ACTION

One concrete action.

## VERIFICATION STATUS

Use only:

`IMPLEMENTED` · `VERIFIED` · `LIVE VERIFIED` · `HUMAN REVIEW REQUIRED` · `UNKNOWN`

Never guess.

---

# FINAL PRINCIPLE

**We do not make E02 impressive by adding more.**

We make it impressive by making five simple things extraordinarily good.

**Five Orbs.**

**Five colors.**

**Five numbers.**

**Five names.**

**Five living physical objects.**

That is Section 02.

Then we move on.

**SECTION 01 — MEET YOUR RESULT.**

**SECTION 02 — SEE YOUR FIVE-DIMENSION CAPABILITY PROFILE.**

**SECTION 03 — UNDERSTAND WHAT IT MEANS.**

**SECTION 04+ — DISCOVER WHAT TO DO WITH IT.**

**Protect scope. Preserve E01. Build downward. Simplify intelligently. Ship the five-Orb experience.**
