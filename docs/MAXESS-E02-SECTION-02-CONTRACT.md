# MAXESS E02 — SECTION 02 CONTRACT

**Status:** ACTIVE IMPLEMENTATION CONTRACT
**Date:** 2026-08-19
**Artifact:** `E02-SECTION-02-WORKING.html`
**Engineering branch:** `maxess-results-v21-working`
**Prior frozen section:** E01 — protected

## 1. PURPOSE

Transition naturally from the single primary MAXESS score in E01 into the user's **five-dimensional capability picture**.

The user should immediately understand:

**ONE SCORE → FIVE DIMENSIONS → FIVE LIVING ORBS → FIVE SCORES → CURIOSITY → DESIRE TO UNDERSTAND THE REPORT**

Section 02 is not a dashboard, statistics dump, or sales section.

## 2. HUMAN EXPERIENCE

The user should feel:

- “My score has more depth than one number.”
- “These five things describe how I work with AI.”
- “Those Orbs feel alive and valuable.”
- “I want to know what these numbers mean about me.”

The experience should create curiosity, not explain everything yet.

## 3. ARTIFACT / HOST BOUNDARY

E01 and E02 are **separate section artifacts** in GitHub.

- `E01-SECTION-01-WORKING.html` is the frozen Section 01 source.
- `E02-SECTION-02-WORKING.html` is the active Section 02 source.
- The host/publishing environment places the E02 section **after E01** to create the assembled experience.
- Naya must not copy, regenerate, embed, or duplicate E01 source inside E02.
- E02 must remain a self-contained, embed-ready Section 02 payload.

Therefore:

**E01 FILE = FROZEN SOURCE**

**E02 FILE = ACTIVE SECTION 02 EMBED**

**ASSEMBLED EXPERIENCE = E01 → E02 IN HOST ORDER**

This resolves a critical source-integrity ambiguity: E02 is not required to contain a second copy of E01 in order to follow E01.

## 4. VISUAL OBJECTIVE

Move from E01's dark, intimate score reveal into a **premium pearl/white spatial environment**.

The visual hierarchy is:

1. Five living Orbs.
2. Five large, immediately readable scores.
3. Dimension names.
4. Minimal supporting context.
5. A black capability node that feels dimensional and important without becoming a dashboard card.

The composition must feel like a **field of five capability objects**, not five widgets in a grid.

## 5. EXACT TEXT REQUIRED

Section marker:

**YOUR FIVE DIMENSIONS**

Primary heading:

**Five dimensions. One capability picture.**

Supporting line:

**Five living signals show what makes up your AI capability.**

Capability node label:

**YOUR AI CAPABILITY**

Capability node statement:

**Five dimensions. One system.**

Dimension names, exactly:

- **Direction**
- **Communication**
- **Evaluation**
- **Iteration**
- **Systems Thinking**

Each Orb must display its real score as **NUMBER / 100** visually or through an equivalent immediately readable accessible representation.

## 6. TEXT FORBIDDEN

Do NOT add:

- long explanatory paragraphs;
- generic AI marketing copy;
- invented motivational copy;
- sales language;
- membership invitations;
- “demo preview” messaging in the normal human experience;
- “these numbers are not judgments” copy repeated from E01;
- dashboard-style instructional text;
- arbitrary labels such as “YOUR FIVE SIGNALS”;
- arbitrary labels such as “FIVE PARTS OF THE PICTURE”;
- repeated lists of all five dimensions outside the five Orb objects;
- invented dimension meanings not supplied by the canonical product model;
- placeholder copy.

If data is unavailable, fail safely. Do not present fabricated production scores as real.

## 7. FIVE DIMENSIONS

The canonical five dimensions are:

1. Direction
2. Communication
3. Evaluation
4. Iteration
5. Systems Thinking

The renderer consumes the authoritative `window.MAXESS_RESULT` data. It must not become a second scoring engine.

## 8. FIVE LIVING ORBS

Each dimension receives exactly one primary visual Orb.

Every Orb must:

- be physically present;
- feel spherical and dimensional;
- have a dark/black capability core;
- have restrained internal light and depth;
- have a visible dimensional edge/halo;
- contain a large centered score;
- use one coherent accent color;
- breathe subtly;
- remain visually distinct from the other four;
- belong unmistakably to the same MAXESS Orb family.

Animation default:

**6-second breathing cycle**, subtle and continuous.

An orbiting bead/ring may be used when it is a deliberate mirror of the approved E01 Orb language and remains restrained. It must never obscure the score or become the primary visual.

## 9. SCORE HIERARCHY

The score is the most important information inside each Orb.

Requirements:

- immediately readable at first glance;
- centered;
- high contrast;
- visually dominant over secondary copy;
- never obscured by a glow, pseudo-element, ring, or effect;
- clearly associated with its dimension;
- derived from real MAXESS result data.

The score must never be visually hidden or replaced by decorative effects.

## 10. COLOR SYSTEM

Use five distinct but harmonious MAXESS jewel accents:

- Direction — Purple
- Communication — Magenta/Coral
- Evaluation — Emerald
- Iteration — Electric Blue
- Systems Thinking — Gold/Amber

Colors should be luminous accents within a restrained black/pearl system, not a rainbow dashboard.

## 11. PEARL / WHITE ENVIRONMENT

The surrounding environment must feel:

- premium;
- luminous;
- calm;
- spacious;
- tactile;
- gallery-like;
- intentional.

Avoid flat pure-white page treatment.

Use subtle pearl gradients, atmospheric light, depth, and controlled shadows.

## 12. BLACK CAPABILITY NODE

The node is a visual anchor, not a generic information card.

It must feel:

- dimensional;
- deep;
- premium;
- tactile;
- visually related to the black cores of the Orbs.

It must remain concise.

## 13. SPATIAL COMPOSITION

Desktop target:

**FIVE ORBS IN A SINGLE SPATIAL FIELD**

The composition should not look like five equal dashboard tiles.

Allow:

- atmospheric depth;
- subtle variation in scale/position where it improves spatiality without damaging scanability;
- generous negative space;
- visual connection between the five objects.

Do not sacrifice score readability for spatial effects.

## 14. MOBILE

Mobile is intentionally designed, not a compressed desktop grid.

Requirements:

- Orbs remain large enough to feel physical;
- scores remain immediately readable;
- dimension names remain attached to their Orbs;
- spacing remains premium;
- no horizontal overflow;
- no tiny five-column layout;
- no wall of explanatory text;
- touch interaction must be comfortable where interaction exists.

Preferred mobile composition: a deliberate two-column/two-column/centered rhythm or another composition that preserves the feeling of a capability constellation.

## 15. ACCESSIBILITY

Required:

- semantic section heading;
- accessible name for each dimension and score;
- sufficient contrast;
- score meaning not dependent on color alone;
- keyboard/focus behavior if Orbs are interactive;
- reduced-motion support;
- no hidden score due to animation or visual effects.

## 16. TRANSITION FROM E01

E01 ends with the user's primary AI score reveal.

E02 should feel like the next natural question:

**“What is that score made of?”**

Do not repeat E01's Naya introduction, primary score, Listen control, or explanation.

Do not modify E01 to create the transition.

The transition is created by the beginning of E02 itself and by the host placing E02 immediately after E01.

## 17. ACCEPTANCE CRITERIA

E02 passes only if:

1. E01 source remains unchanged within its protected boundary.
2. E02 is a distinct Section 02 embed-ready artifact.
3. The assembled host order is E01 → E02.
4. Exactly five canonical dimensions are presented.
5. Exactly five primary living Orbs are presented.
6. Each Orb has one score.
7. Scores are immediately readable.
8. Scores consume real `window.MAXESS_RESULT` data when available.
9. Missing data fails safely.
10. Pearl/white environment feels premium rather than flat.
11. Black capability node feels dimensional rather than card-like.
12. Five colors feel coherent rather than rainbow-like.
13. Composition feels spatial rather than dashboard-like.
14. Desktop and mobile are intentionally designed.
15. Reduced motion is supported.
16. No unauthorized explanatory/textual clutter appears.
17. E02 creates curiosity about the personal report.
18. E02 feels unmistakably MAXESS.

## 18. FAILURE CONDITIONS

Automatic rejection if any of the following occurs:

- E01 changes;
- E01 CSS changes;
- E01 JS changes;
- E01 copy changes;
- E01 assets change;
- E02 duplicates or regenerates E01 source;
- E02 is delivered as a competing full-product renderer;
- scores are missing or unreadable;
- demo values are presented as real production results;
- excessive explanatory text appears;
- generic dashboard/card treatment dominates;
- the Orbs feel flat;
- the Orbs are visually unrelated;
- mobile becomes cramped or unreadable;
- accessibility/reduced-motion requirements are ignored;
- the implementation introduces unrelated functionality;
- the implementation regenerates or restructures E01.

## 19. IMPLEMENTATION LAW

The active implementation must use:

**FROZEN E01 SOURCE + DISTINCT E02 SECTION EMBED**

E01 remains byte-for-byte unchanged in its own artifact. E02 is implemented only in `E02-SECTION-02-WORKING.html` with section-scoped styles, markup, and behavior. The host/publishing layer composes the two artifacts in order.

Do not rewrite E01 to make E02 easier.

Do not copy E01 into E02.

Do not create a second assembled renderer.

## 20. VERIFICATION

Required after implementation:

**RE-FETCH → E01 BLOB PROOF → E02 IDENTITY PROOF → DIFF → STATIC QA → JS QA → RESPONSIVE QA → ACCESSIBILITY QA → OSCAR → REPAIR → RE-TEST → COMMIT → RE-FETCH → FINAL E01 BLOB PROOF → FINAL E02 BLOB PROOF → DELIVER EMBED**

Groove/publishing review remains outside Naya's engineering verification boundary and is performed by the human after delivery.

## 21. NORTH STAR

**FIVE DIMENSIONS → FIVE LIVING ORBS → FIVE SCORES → CURIOSITY → DESIRE TO UNDERSTAND THE PERSONAL REPORT**
