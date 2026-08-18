# MAXESS AAA SECTION DESIGN SPECIFICATION

Status: AUTHORITATIVE WORKING DESIGN SPECIFICATION
Version: V21 AAA Reference Implementation
Repository: SoulSchoolAcademy/MaxRESULTS
Branch: maxess-results-v21-working

## Purpose

Define what an extraordinary MAXESS Results experience looks like before implementation. This document is the visual/editorial/interaction specification that implementation must follow.

The public baseline currently communicates real value through score, fingerprint, five dimensions, advantage, next chapter, 18 pathways, growth, playground, and Naya continuation, but the experience is still primarily a linear information presentation. The next quality jump is not simply more content. It is stronger visual storytelling, hierarchy, personalization, tactility, section composition, and transition design. The baseline currently presents an 82 score, five dimension scores, an advantage/lever interpretation, 18 pathways, growth actions, and Naya continuation. [Current public baseline verified August 17, 2026.]

## AAA definition for MAXESS

AAA means every material part earns its place and works together as one human experience.

A 10 means:

- the human purpose is unmistakable;
- the first screen earns attention immediately;
- the experience feels personal, not templated;
- numbers become understandable insight;
- visuals communicate relationships faster than paragraphs;
- the Orb and fingerprint become signature assets;
- buttons and icons feel proprietary, tactile, and premium;
- typography and contrast are exceptional and readable;
- every section has one clear cognitive job;
- every transition changes the user's mental state intentionally;
- interactions reward exploration;
- mobile is designed, not merely compressed;
- accessibility is designed in;
- real result data controls personalization;
- existing working functionality survives;
- the whole page feels coherent from first pixel to final CTA;
- PDF/print is intentionally designed;
- the public artifact is stable enough to trust.

## Master visual language

Core palette:

- BLACK: authority, depth, focus, cinematic space.
- WHITE: clarity, breathing room, reading, reset.
- PURPLE: intelligence, transformation, Naya identity, AI energy.
- GOLD: achievement, premium moments, milestones, celebration.

Optional support colors must be subordinate and used for meaning, not decoration.

Visual principles:

1. One dominant visual idea per major section.
2. Prefer organic geometry, orbs, rings, pathways, energy fields, and connected forms over repeated rectangles.
3. Use cards only when they improve scanability or interaction.
4. Use visual contrast as a cognitive tool.
5. Use depth sparingly but intentionally: glow, inset light, elevation, layered gradients, scale, and atmosphere.
6. Avoid generic dashboard grids, excessive glassmorphism, noisy neon, giant shadows, decorative clutter, and visual effects that reduce readability.
7. Favor editorial composition: asymmetric balance, large type, deliberate whitespace, visual anchors, and scene changes.
8. Every major section should feel like a new chapter, not another component row.

## Typography

- Use a high-quality, highly legible primary sans-serif for body and controls.
- Use a strong editorial display face for major headings only when contrast and readability remain excellent.
- Use restrained uppercase micro-labels for chapter markers.
- Use optical rather than purely mathematical spacing around large scores and headings.
- Never use a decorative display face for core actions.
- Body copy should remain readable at comfortable line lengths.

## Button and icon standard

All controls use `docs/HMC-MAXIMUS-BUTTON-AND-ICON-SYSTEM.md`.

Buttons must feel:

CLEAR + TACTILE + PREMIUM + PROPRIETARY + ALIVE + ACCESSIBLE

Preferred interaction:

REST → HOVER → FOCUS → PRESSED → SUCCESS

No control should exist without a clear action meaning.

Icons are semantic communication, not decoration. Micro-icons and bullets can use sparks, mini-orbs, checks, directional marks, waveform marks, pathway markers, or other coherent symbols from the HMC visual family.

## Section-by-section target experience

### 01 — NAYA ARRIVAL / ORIENTATION

Current-state problem:
The current public baseline opens with a headline and supporting copy, but the emotional contract is not yet strong enough to feel like Naya has personally entered the experience. The current opening is also visually structured like a presentation panel rather than a signature arrival.

AAA target:
A cinematic Naya arrival that feels like a trusted guide has stepped into the room.

User question:
“Does Naya understand me and my result?”

Primary visual:
Naya profile image integrated into an atmospheric dark scene, with subtle purple energy, depth, and one clear focal point.

Text target:
“Hi, [Name]. I’ve looked at your results.”
“This isn’t your judgment. It’s your map.”

Primary action:
LISTEN TO NAYA.

Design:
- Naya visual large enough to feel human.
- One primary CTA only.
- CTA uses HMC primary/listen treatment.
- Background should create depth without competing with Naya.
- Personalized headline should become more specific when result identity exists.

Interaction:
- Listen action has visible hover/focus/pressed state.
- Optional subtle waveform/activity response.
- Keyboard and touch equivalent.

Evidence:
Source selector + one CTA + screenshot/browser review + responsive review.

Priority: 10/10, weight 100.

### 02 — MAXESS SCORE / SIGNATURE ORB

Current-state problem:
The public page currently shows the score clearly, but the score treatment is not yet a truly distinctive signature asset. The Orb should carry much more of the product's visual identity.

AAA target:
The most recognizable visual element on the page.

User question:
“What is my score?”

Primary visual:
Large layered Orb with depth, rings, energy field, subtle motion, and score-reactive color.

Design:
- score centered and dominant;
- layered radial energy;
- inner glow and outer halo;
- subtle rings/orbit lines where useful;
- score-based smooth color interpolation;
- motion tied to energy rather than novelty;
- reduced-motion state remains beautiful;
- no competing hero visual.

Interaction:
The Orb may react to hover, scroll progression, or Naya speaking, but must remain performant and not become a distraction.

Evidence:
Real result source + visual inspection + reduced-motion test + desktop/mobile test.

Priority: 10/10, weight 100.

### 03 — WHAT YOUR SCORE MEANS

Current-state problem:
The current page explains dimension scores well, but the overall score's meaning should become more prominent and easier to understand before the user is asked to interpret the details.

AAA target:
Translate the number into useful self-understanding.

User question:
“What does this score mean for me?”

Content:
- mastery stage;
- plain-language meaning;
- what the score indicates;
- what it does not indicate;
- what the user can do with the result;
- Create → Score → Improve principle;
- brief Naya commentary.

Visual:
Use a visual mastery continuum rather than another generic card grid.

Priority: 10/10, weight 95.

### 04 — PERSONALIZED REPORT

Current-state problem:
The report currently exists, but it reads partly like a conventional summary block. The target is a save-worthy editorial artifact.

AAA target:
A personal “this is me” report that a user would screenshot or save.

Content:
Overall result → stage → strongest capability → highest-leverage opportunity → pattern → meaning → next move.

Visual:
Editorial report composition, strong typography, one hero statement, selected data, Naya note, visual hierarchy. Use cards only for data that benefits from comparison.

Priority: weight 95.

### 05 — AI FINGERPRINT

Current-state problem:
The live page has a textual five-dimension fingerprint but it needs a more signature visual system.

AAA target:
The user can understand the shape of their capability in one glance.

Visual:
Five-axis radar/fingerprint with coherent Orb language, central overall score, animated or static profile shape, labels, and accessible textual equivalent.

Principle:
Visual relationship first; explanation second.

Priority: weight 95.

### 06 — FIVE DIMENSIONS DEEP DIVE

Current-state problem:
The five dimensions are substantive, but the current presentation is still mostly score + text. The mini-orbs should become one of the defining visual devices of the report.

AAA target:
Five beautiful interactive mini-orbs that explain the user's capabilities without feeling like a dashboard.

Dimensions:
Direction / Communication / Evaluation / Iteration / Systems Thinking.

Each mini-orb needs:
- score;
- visual state;
- name;
- meaning;
- behavioral interpretation;
- practical opportunity;
- selected state;
- accessible text equivalent.

Priority: weight 95.

### 07 — YOUR PATTERN

Current-state problem:
The public baseline describes the five scores, but the pattern must explain their relationships rather than restating them.

AAA target:
A visual relationship story.

Visual:
Connected arcs, pathways, constellation-like links, or another relationship model showing how the five capabilities support or constrain one another.

Copy:
Short interpretation followed by one “what this means” paragraph.

Priority: weight 90.

### 08 — YOUR STRENGTH

Current-state problem:
Recognition exists, but it should feel more emotionally powerful and visually specific.

AAA target:
“I already have something valuable here.”

Visual:
One dominant capability spotlight, score, icon/orb, Naya recognition note, and one compounding action.

Priority: weight 90.

### 09 — YOUR BIGGEST LEVER

Current-state problem:
The opportunity is clear, but the presentation can feel like a weakness callout unless carefully framed.

AAA target:
“This is an opportunity I can actually use.”

Visual:
A visual lever metaphor, energy path, or before/after capability representation.

Copy:
Not a weakness. A leverage point.

Action:
One concrete improvement workflow.

Priority: weight 90.

### 10 — YOUR NEXT MOVE

Current-state problem:
Current action guidance is useful but should become more individualized and decisive.

AAA target:
The user knows exactly what to do next.

Three actions:
1. Protect your strength.
2. Build your lever.
3. Create → Score → Improve one real AI workflow.

Each action needs a compact visual marker, action icon, concise text, and clear CTA behavior.

Priority: weight 95.

### 11 — 18 NAYA MASTERS

Current-state problem:
The live experience can feel like a pathway library rather than 18 personally relevant doors.

AAA target:
“Here are the AI paths that make the most sense for me.”

Requirements:
- all 18 retained;
- best-match ranking;
- strong/next-match states;
- concise descriptions;
- pathway identity;
- useful CTA behavior;
- connection to Strength, Lever, and Next Move.

Visual:
Use a flowing pathway/constellation system rather than a flat 18-card wall.

Priority: weight 85.

### 12 — NAYA IN PRACTICE / MEDIA

Current-state problem:
The lower page has historically suffered from loading/ownership issues, and media can feel appended rather than integrated.

AAA target:
The user sees Naya’s guidance become a lived experience.

Requirements:
- video loads reliably;
- walkthrough preserved;
- Naya commentary is contextual;
- media has a visual frame that belongs to MAXESS;
- no disappearing lower-half content.

Priority: weight 85.

### 13 — PLAYGROUND / PRACTICE

Current-state problem:
The Playground can feel like a separate tool rather than the natural action bridge.

AAA target:
UNDERSTAND → DECIDE → PRACTICE.

Requirements:
- one clear practice moment;
- preserved useful legacy function;
- tactile controls;
- strong CTA hierarchy;
- mobile-first interaction;
- clear tie to the user's Strength/Lever.

Priority: weight 85.

### 14 — CLOSING NAYA

Current-state problem:
The current page moves toward conversion/continuation, but the final Naya moment should feel personal rather than like a generic sales transition.

AAA target:
“I know what my next chapter is.”

Visual:
Naya + calm premium dark scene + concise personal statement.

Priority: weight 80.

### 15 — FINAL CONTINUATION CTA

Current-state problem:
The final CTA currently relies heavily on conventional links and a membership-oriented close.

AAA target:
A decisive, visually premium transition into the next experience.

CTA family:
HMC B6 commitment/conversion system.

Copy should emphasize the user's next capability, not generic selling.

Priority: weight 80.

## Global quality layers

These are not separate sections. They apply to every section.

### Visual communication

Prefer visual explanation over prose whenever a concept can be understood spatially.

Examples:
- score → Orb;
- five scores → mini-orbs + fingerprint;
- pattern → connected visual;
- strength → spotlight;
- lever → focused pathway;
- next move → action path;
- Masters → capability doors.

### Contrast

Use high contrast for hierarchy. Preserve readability. Purple and gold are accents, not body-text compromises.

### Tactility

Controls should feel pressable. Use optical depth, restrained elevation, clear state changes, and meaningful icons.

### Motion

Motion must communicate state, energy, progress, or attention. Avoid motion without meaning.

### Responsive

Design each section across widescreen, desktop, tablet, and mobile. Do not merely allow wrapping.

### Accessibility

Every visual state needs a non-color equivalent. Every interactive control needs an accessible name, keyboard path, visible focus, and touch-friendly size.

### Performance

No repeated renderers, runaway MutationObservers, duplicate listeners, or unnecessary libraries.

### Data integrity

All scores and personalization derive from `window.MAXESS_RESULT`.

## Section freeze standard

A section becomes FROZEN only when:

- visual review passes;
- functional review passes;
- responsive review passes;
- accessibility review passes;
- data review passes;
- regression review passes;
- source evidence exists;
- no critical Master Contract requirement remains open for that section.

## Re-score loop

After each complete batch:

1. inspect the real page;
2. score each section 0–10;
3. identify the largest gap;
4. update the priority weights;
5. execute the highest-value next improvement;
6. repeat.

The scorecard must never replace human judgment; it organizes it.
