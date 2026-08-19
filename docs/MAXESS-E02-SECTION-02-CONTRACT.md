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

Section 02 is not a report, dashboard, statistics dump, or sales section.

## 2. HUMAN EXPERIENCE

The user should feel:

- “My score has more depth than one number.”
- “These five things describe how I work with AI.”
- “Those Orbs feel alive and valuable.”
- “I want to know what these numbers mean about me.”

The experience should create curiosity, not explain everything yet.

## 3. VISUAL OBJECTIVE

Move from E01's dark, intimate score reveal into a **premium pearl/white spatial environment**.

The visual hierarchy is:

1. Five living Orbs.
2. Five large, immediately readable scores.
3. Dimension names.
4. Minimal supporting context.
5. A black capability node that feels dimensional and important without becoming a dashboard card.

The composition must feel like a **field of five capability objects**, not five widgets in a grid.

## 4. EXACT TEXT REQUIRED

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

## 5. TEXT FORBIDDEN

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

## 6. FIVE DIMENSIONS

The canonical five dimensions are:

1. Direction
2. Communication
3. Evaluation
4. Iteration
5. Systems Thinking

The renderer consumes the authoritative `window.MAXESS_RESULT` data. It must not become a second scoring engine.

## 7. FIVE LIVING ORBS

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

Do not add orbiting beads, complex particles, floating text, or gratuitous motion unless rendered evidence later proves a material weakness that requires them.

## 8. SCORE HIERARCHY

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

## 9. COLOR SYSTEM

Use five distinct but harmonious MAXESS jewel accents:

- Direction — Purple
- Communication — Magenta/Coral
- Evaluation — Emerald
- Iteration — Electric Blue
- Systems Thinking — Gold/Amber

Colors should be luminous accents within a restrained black/pearl system, not a rainbow dashboard.

## 10. PEARL / WHITE ENVIRONMENT

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

## 11. BLACK CAPABILITY NODE

The node is a visual anchor, not a generic information card.

It must feel:

- dimensional;
- deep;
- premium;
- tactile;
- visually related to the black cores of the Orbs.

It must remain concise.

## 12. SPATIAL COMPOSITION

Desktop target:

**FIVE ORBS IN A SINGLE SPATIAL FIELD**

The composition should not look like five equal dashboard tiles.

Allow:

- atmospheric depth;
- subtle variation in scale/position where it improves spatiality without damaging scanability;
- generous negative space;
- visual connection between the five objects.

Do not sacrifice score readability for spatial effects.

## 13. MOBILE

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

## 14. ACCESSIBILITY

Required:

- semantic section heading;
- accessible name for each dimension and score;
- sufficient contrast;
- score meaning not dependent on color alone;
- keyboard/focus behavior if Orbs are interactive;
- reduced-motion support;
- no hidden score due to animation or visual effects.

## 15. TRANSITION FROM E01

E01 ends with the user's primary AI score reveal.

E02 should feel like the next natural question:

**“What is that score made of?”**

Do not repeat E01's Naya introduction, primary score, Listen control, or explanation.

Do not modify E01 to create the transition.

The transition is created by the beginning of E02 itself.

## 16. ACCEPTANCE CRITERIA

E02 passes only if:

1. E01 source remains unchanged within its protected boundary.
2. E02 exists after E01 in the assembled experience.
3. Exactly five canonical dimensions are presented.
4. Exactly five primary living Orbs are presented.
5. Each Orb has one score.
6. Scores are immediately readable.
7. Scores consume real `window.MAXESS_RESULT` data when available.
8. Missing data fails safely.
9. Pearl/white environment feels premium rather than flat.
10. Black capability node feels dimensional rather than card-like.
11. Five colors feel coherent rather than rainbow-like.
12. Composition feels spatial rather than dashboard-like.
13. Desktop and mobile are intentionally designed.
14. Reduced motion is supported.
15. No unauthorized explanatory/textual clutter appears.
16. E02 creates curiosity about the personal report.
17. E02 feels unmistakably MAXESS.

## 17. FAILURE CONDITIONS

Automatic rejection if any of the following occurs:

- E01 changes;
- E01 CSS changes;
- E01 JS changes;
- E01 copy changes;
- E01 assets change;
- E02 replaces rather than follows E01;
- E02 becomes a standalone page when the assembled experience requires E01 + E02;
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

## 18. IMPLEMENTATION LAW

The active implementation must use:

**LOCKED E01 PREFIX + APPENDED E02**

The E01 protected source must be preserved byte-for-byte through the E01 closing boundary. E02 styles, markup, and script are appended after that protected boundary and must be scoped so they do not alter E01.

Do not rewrite the E01 implementation to make E02 easier.

## 19. VERIFICATION

Required after implementation:

**RE-FETCH → E01 BYTE/BOUNDARY DIFF → STATIC QA → JS QA → RESPONSIVE QA → ACCESSIBILITY QA → RENDER → HUMAN REVIEW → OSCAR → REPAIR → RE-TEST → COMMIT → RE-FETCH → PROVE**

## 20. NORTH STAR

**FIVE DIMENSIONS → FIVE LIVING ORBS → FIVE SCORES → CURIOSITY → DESIRE TO UNDERSTAND THE PERSONAL REPORT**
