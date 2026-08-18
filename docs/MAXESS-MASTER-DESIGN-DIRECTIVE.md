# MAXESS MASTER DESIGN DIRECTIVE

Status: AUTHORITATIVE WORKING DESIGN DIRECTIVE
Repository: SoulSchoolAcademy/MaxRESULTS
Branch: maxess-results-v21-working
Purpose: Define the exact experience, visual language, psychological choreography, object behavior, content, interaction, and acceptance standard for the MAXESS Results reference implementation.

This document extends and operationalizes:
- docs/MAXESS-MASTER-CONTRACT.md
- docs/MAXESS-AAA-SECTION-DESIGN-SPEC.md
- docs/AI-DEFINITION-OF-10.md
- docs/AI-PRODUCT-LANGUAGE.md
- docs/NAYA-LEAD-MODE.md
- docs/HMC-MAXIMUS-BUTTON-AND-ICON-SYSTEM.md
- docs/MAXESS-HMC-REFERENCE-PACK.md

The live public baseline was reviewed August 17, 2026 at results.nayanet.xyz. The live page currently communicates a real score, five dimensions, fingerprint, advantage/lever, next chapter, 18 pathways, growth, playground, personalized report, video, and continuation links, but it is still more report-like than signature-product-like. citeturn897819view0

---

# 01 — NORTH STAR

DATA
→ INSIGHT
→ UNDERSTANDING
→ ACTION
→ CAPABILITY

User promise:

“MAXESS helps me understand how I work with AI, recognize what I already do well, see where I can create the most leverage, and know exactly what to do next.”

Emotional target:

SEEN
→ CURIOUS
→ IMPRESSED
→ UNDERSTANDING
→ CAPABLE
→ MOTIVATED
→ INVITED

The page must feel:

PERSONAL
WARM
INTELLIGENT
PREMIUM
CINEMATIC
TACTILE
ALIVE
CLEAR
TRUSTWORTHY
MEMORABLE
USEFUL
CONVERSION-READY

---

# 02 — DEFINITION OF A 10

A 10 is the highest practical quality state in which no material weakness remains relative to purpose, audience, constraints, release environment, and evidence.

MAXESS must satisfy all 20 quality dimensions from docs/AI-DEFINITION-OF-10.md. fileciteturn119file0

A section cannot be frozen merely because it:

- exists;
- builds;
- passes one QA script;
- looks better;
- has more code;
- uses more effects;
- has an AI-generated score of 10.

A section is frozen only when:

PURPOSE
+ CLARITY
+ PERSONALIZATION
+ CONTENT
+ VISUAL DESIGN
+ EMOTIONAL IMPACT
+ UX
+ INTERACTION
+ DATA INTEGRITY
+ RELIABILITY
+ RESPONSIVE
+ ACCESSIBILITY
+ PERFORMANCE
+ MAINTAINABILITY
+ PDF/PRINT when relevant
+ TRUST
+ PRIDE

all have acceptable evidence.

Critical dimensions below 9 prevent a 10 claim.

---

# 03 — EXPERIENCE PRINCIPLE: FLOW LIKE WATER

The page is not a stack of sections.

It is a guided psychological journey.

The correct mental model is:

MOMENT
→ REVEAL
→ TRANSITION
→ DISCOVERY
→ RECOGNITION
→ POSSIBILITY
→ PATHWAY
→ GUIDANCE
→ PRACTICE
→ COMMITMENT

Do not make every section equally loud.

Use ATTENTION BUDGETING:

★★★★★ HERO / REVEAL
★★★★★ SCORE ORB / FIVE MINI-ORB SYSTEM
★★★★ PERSONAL REPORT
★★★★ FINGERPRINT / PATTERN
★★★ STRENGTH
★★★ OPPORTUNITY
★★★ NAYA MASTERS
★★★★ GUIDED MEDIA
★★★ PRACTICE
★★★★★ FINAL NAYA + CTA

If everything glows, nothing glows.

Every scene change must have a reason.

Prefer:

DARK → LIGHT → DARK → LIGHT → PURPLE → DARK

as a rhythm, not as a rigid formula.

---

# 04 — OPTIONAL IDENTITY GATE / PERSONALIZATION ENTRY

Purpose:
Reduce friction while allowing an optional personalized experience.

This is an onboarding enhancement, not a requirement for anonymous access.

Primary message:

“Get a more personal MAXESS experience.”

Supporting line:

“Sign in so Naya can use your name and keep your results connected to your journey.”

Actions:

CONTINUE WITH GOOGLE
CONTINUE WITH FACEBOOK
CONTINUE WITH EMAIL

Secondary text:

“Skip for now”

Rules:

- Never require identity before the user can understand the value of MAXESS unless product strategy later proves a stronger reason.
- The skip action is visible, calm, and easy.
- Social login buttons are B2-style or context variants, not competing conversion CTAs.
- Use approved provider brand icons according to provider rules.
- Email path must be short.
- Authentication UI must not visually overpower the MAXESS experience.
- If identity is known, use it everywhere personalization is meaningful.
- If identity is absent, use neutral language without awkward placeholders.

Psychology:

INVITATION, not GATEKEEPING.

The user should feel:

“This will make my experience better,”
not

“I must give you my information to continue.”

---

# 05 — MASTER VISUAL MATERIAL LANGUAGE

## 5.1 BLACK

Primary value:
AUTHORITY
DEPTH
FOCUS
CINEMATIC SPACE

Base:
#06040B

Deep surface:
#0D0914

Raised surface:
#120C1D

Use black for moments where attention should narrow.

## 5.2 WHITE / WARM LIGHT

Primary value:
CLARITY
READING
RELIEF
EDITORIAL CONFIDENCE

Warm light:
#F7F4FA

Pure white:
#FFFFFF

Use light scenes after visually intense dark scenes to create cognitive relief.

## 5.3 PURPLE

Primary value:
AI
TRANSFORMATION
NAYA
IMAGINATION
POSSIBILITY

Deep purple:
#35106F

Electric purple:
#8B3DFF

Luminous purple:
#C58CFF

Ultra-light purple:
#E9D6FF

## 5.4 GOLD

Primary value:
ACHIEVEMENT
PREMIUM
CELEBRATION
MILESTONE

Gold:
#D8B25C

Warm gold:
#F0D58B

Gold is not a default accent. Reserve it for genuinely earned moments.

## 5.5 DIMENSION COLORS

Direction:
#FF9D3D

Communication:
#FFD84A

Evaluation:
#39DF91

Iteration:
#4C9DFF

Systems Thinking:
#965DFF

These colors have semantic ownership and must remain consistent across Orb, mini-orb, fingerprint, micro-icon, and pathway references.

---

# 06 — TYPOGRAPHY SYSTEM

Use a high-quality modern grotesk/sans family available in the production environment, prioritizing:

- readability;
- optical hierarchy;
- excellent numerals;
- strong weight range;
- strong punctuation;
- clean mobile rendering.

Preferred candidates:
GEIST / INTER / MANROPE / INTER TIGHT class of typography.

Do not depend on a decorative face for core UI.

## Display

Hero headline:
clamp(44px, 7vw, 88px)
font-weight: 800–950
line-height: .92–1.02
letter-spacing: -.055em to -.075em

Section headline:
clamp(34px, 5vw, 64px)
font-weight: 800–900
line-height: .98–1.08
letter-spacing: -.045em to -.065em

Body:
16–19px desktop
15–17px mobile
line-height: 1.55–1.7

Micro-label:
10–12px
font-weight: 800–950
letter-spacing: .14em–.22em
text-transform: uppercase

Score:
clamp(96px, 13vw, 170px)
font-weight: 850–950
line-height: .85–.92
letter-spacing: -.065em

Typography rhythm:

BIG → SMALL → BIG

Use large type to create emotional emphasis, then smaller type to explain, then return to a meaningful visual/data moment.

---

# 07 — GRID / SPACING / COMPOSITION

Content max width:
1120px–1240px depending section.

Desktop side padding:
48–72px.

Tablet:
28–40px.

Mobile:
18–22px.

Major section vertical padding:
96–144px desktop.
72–96px tablet.
56–76px mobile.

Major visual object spacing:
32–56px.

Text measure:
55–75 characters where readable narrative is required.

Do not center every section.

Use:

LEFT-ALIGNED EDITORIAL
+ CENTERED HERO OBJECTS
+ ASYMMETRIC SUPPORTING ELEMENTS

for visual rhythm.

Whitespace is a design element.

---

# 08 — BUTTON MASTER SYSTEM

The authoritative HMC button system defines the semantic families, states, depth, motion, accessibility, and interaction rules. fileciteturn118file0

MAXESS uses those families consistently.

## B1 PRIMARY ACTION

Use when one action clearly matters most.

Geometry:
height 54–60px desktop
48–54px mobile
padding 0 24–30px
radius 999px

Material:
linear-gradient(135deg, #C58CFF 0%, #8B3DFF 52%, #4A187F 100%)

Lighting:
subtle upper highlight
soft outer violet halo
internal lower shadow

Text:
#FFFFFF
15–17px
font-weight 800
letter-spacing .01em

Icon:
16–18px
optically centered

Shadow:
0 12px 28px rgba(125,55,230,.28)

Hover:
translateY(-2px)
scale(1.015)
filter brightness(1.04)
shadow +10–15%

Pressed:
translateY(0)
scale(.985)
shadow contracts

Focus:
3px solid #FFFFFF
outline-offset 5px

Reduced motion:
no transform; preserve contrast and highlight change.

## B4 LISTEN TO NAYA

Primary audio control.

Label:
LISTEN TO NAYA

Icon:
play triangle nested in a soft circular waveform ring.

Idle:
quiet luminous ring.

Hover:
small ring expansion.

Playing:
ring becomes waveform-like pulse.

Paused:
play icon returns, ring remains dimly alive.

Success/end:
brief completion glow, then calm.

The user should understand immediately that this is Naya speaking, not generic media playback.

## B5 PATHWAY ACTION

Label examples:
OPEN MASTER
START THIS PATH
EXPLORE THIS DOOR

Height:
44–50px.

Use compact tactile geometry.

Each pathway action inherits its pathway color but remains subordinate to B1.

## B6 COMMITMENT / CONVERSION

Label examples:
START YOUR FREE TRIAL
START MY JOURNEY
CONTINUE WITH NAYANET

Use only at moments where commitment is appropriate.

Never use B6 to sell before value has been demonstrated.

---

# 09 — ICON / MICRO-ICON SYSTEM

Icons are semantic communication.

One icon family must be used everywhere.

Preferred visual language:

- rounded geometric forms;
- consistent stroke weight;
- optical alignment;
- subtle energy point;
- clean silhouette at 16px;
- recognizable at 24px;
- premium at 40px.

Semantic mapping:

LISTEN = waveform / sound ring
PLAY = play triangle
EXPLORE = compass / spark
OPEN = forward chevron / arrow
INSIGHT = eye / lens / orb
PATTERN = connected constellation
STRENGTH = radiant star / rising node
OPPORTUNITY = upward energy path
ACTION = directional arrow
PATHWAY = door / route
SUCCESS = check / radiant mark
INFO = information circle
AI = intelligence spark

Micro-bullets can use:

mini-orbs
luminous dots
spark marks
checks
small directional arrows
energy dashes

Never use random Unicode glyphs as the final visual system when a designed icon can communicate better.

---

# 10 — MAXESS SIGNATURE ORB

The Orb is the primary signature asset of MAXESS.

It is not a styled circle.

It is a layered digital object.

Object stack from back to front:

1. ATMOSPHERIC FIELD
2. OUTER HALO
3. ORBIT RING
4. SCORE ARC
5. GLASS/LIGHT SHELL
6. INNER ENERGY
7. CORE
8. SCORE
9. MICRO LABEL

## Geometry

Desktop diameter:
320–430px depending hero layout.

Tablet:
260–330px.

Mobile:
210–270px.

## Core

background:
radial-gradient(circle at 35% 28%, #1A1128 0%, #0B0810 45%, #050408 100%)

border:
1px solid rgba(255,255,255,.18)

box-shadow:
inset 0 2px 10px rgba(255,255,255,.10)
0 30px 90px rgba(0,0,0,.46)

## Inner energy

A blurred radial field centered slightly above-left to simulate physical illumination.

## Primary ring

Width:
6–10px desktop
5–8px mobile

Use score percentage to determine energized arc length.

The arc must interpolate continuously with the actual score.

## Secondary orbit

1px line
30–60% opacity
slow rotation 8–12s

## Halo

Large blurred radial field behind the Orb.

Opacity:
15–30%

Blur:
20–50px

## Shell highlight

Upper-left elliptical highlight.

The highlight must remain subtle enough that the score stays dominant.

## Energy arc

One brighter traveling highlight.

Duration:
2.5–4.0s

Repeat:
4–8s interval.

Do not loop continuously at high intensity.

## Particles

Optional 8–20 micro-points.

Slow drift.

Opacity 8–35%.

Never let particles become the visual story.

## Score color

Continuous interpolation based on score bands.

Do not use hard red/orange/green thresholds.

Use a blended spectrum that moves through blue-violet → electric purple → luminous cyan/green as the score increases.

The mapping must be documented and deterministic.

## Voice synchronization

If Naya is speaking, the Orb may respond to the audio/visual event stream with small amplitude changes.

Rule:
VOICE SHOULD WAKE THE ORB, NOT CONTROL THE PAGE.

## Reduced motion

All animation may resolve into a beautiful static Orb with:

- layered light;
- score arc;
- halo;
- depth;
- high contrast.

No essential meaning may depend on motion.

---

# 11 — FIVE MINI-ORB CONSTELLATION

The five dimensions inherit the Orb language.

They are NOT five cards.

They are five living visual nodes connected to the main score.

## Each mini-orb contains

SCORE
NAME

Optional micro-state:
selected / active / strong / developing

Diameter:
88–116px desktop
72–92px mobile

Ring:
3–5px

Halo:
8–15% opacity

Color:
owned dimension color.

## Layout

Desktop:
central MAXESS Orb with five mini-orbs distributed around it in an asymmetric constellation, not a mechanically perfect ring.

The five nodes should have different orbital offsets but remain visually balanced.

Each node connects to the center with a 1px–2px energy path.

On hover:
node rises 2px
halo grows
connection brightens
score slightly enlarges

On selection:
node becomes 1.08–1.12x
connection becomes more visible
shared detail surface appears beneath or beside constellation

## Mobile

Do NOT shrink all five orbs until unreadable.

Use either:

- two rows with an obvious orbital center;
- or a horizontally scrollable orbital strip with the main score retained above.

Touch target around each interactive orb:
44px minimum.

## Psychological purpose

The visual must communicate:

MY SCORE IS MADE OF FIVE CAPABILITIES.

That message should be understandable before the user reads the explanation.

---

# 12 — SECTION 01: HERO / REVEAL

Psychological job:
I AM SEEN.

Exact copy:

NAYA · YOUR AI GUIDE

“Hi, [NAME]. I’ve looked at your results.”

“This isn’t your judgment. It’s your map.”

Optional supporting copy:

“Let’s see what you already have, what matters most, and where your next leap can come from.”

Primary CTA:
LISTEN TO NAYA

Secondary:
EXPLORE MY MAP ↓

The secondary action must not visually compete with Listen.

Visual scene:

background #06040B

At top/upper-left:
Naya portrait 112–132px desktop.

Behind Naya:
subtle purple radial field.

Immediately below/right:
MAXESS Orb.

Orb should begin visually close enough to Naya that the two read as one composition.

Recommended hero composition:
Naya upper-left / center-left
Orb center-right
headline aligned to Naya
CTA directly beneath copy

Mobile:
Naya centered
headline centered
CTA centered
Orb below

Transition out:
Orb ring energy visually resolves into the five mini-orb constellation.

This is the first story connection.

Acceptance:
First-time user knows who Naya is, what the result is, and what to do within roughly 10 seconds.

---

# 13 — SECTION 02: FIVE DIMENSIONS / ORB CONSTELLATION

Psychological job:
I SEE MY SHAPE.

Opening label:
YOUR FIVE DIMENSIONS

Headline:
“Here’s what your MAXESS score is made of.”

Supporting:
“Five capabilities shape the way you work with AI. Tap one to see what yours means.”

Primary visual:
main Orb + five mini-orbs.

The overall score remains visually dominant.

Each dimension mini-orb inherits its color and energy system.

Detail surface exact structure:

DIMENSION NAME
SCORE
ONE-LINE MEANING
WHAT YOU ALREADY DO
WHERE IT CAN GROW
ONE PRACTICE

No long paragraph before interaction.

Transition:
selected mini-orb’s energy path can extend toward the Personal Report section below as a subtle visual line.

---

# 14 — SECTION 03: PERSONAL REPORT / PRINT MASTER

Psychological job:
THIS IS ME.

This is the save-worthy artifact.

It should feel like the user received a personal letter/report.

## Visual metaphor

A premium digital letter / scroll hybrid.

Not a fake antique parchment.

Think:
modern editorial letter
+
premium assessment document
+
personal correspondence

Background:
#F7F4FA

Report surface:
#FFFFFF

Width:
780–900px desktop
calc(100% - 32px) mobile

Border:
1px solid rgba(20,12,30,.10)

Radius:
24–30px

Shadow:
0 30px 90px rgba(32,16,50,.12)

Top accent:
purple-to-gold hairline gradient.

Header:
MAXESS
PERSONAL AI MASTERY REPORT

Personal name:
large editorial name treatment.

Example:

SHAWN

MAXESS SCORE
82

ADVANCING

Then narrative.

## Exact report architecture

1. YOUR RESULT
2. WHAT IT MEANS
3. YOUR FIVE DIMENSIONS
4. YOUR STRONGEST CAPABILITY
5. YOUR MOST USEFUL OPPORTUNITY
6. YOUR PATTERN
7. WHAT NAYA SEES
8. YOUR NEXT MOVE

Each section uses short paragraphs and visual separators.

Use one or two oversized pull-quotes rather than repeated cards.

Naya note:
portrait 72–92px
name
“Naya’s note”
personal interpretation.

Print button:
PRINT / SAVE PDF

Visual:
small printer icon.

This entire report surface becomes the PDF master.

PDF rules:

- intentional page breaks;
- no web-only CTA clutter;
- readable body text;
- preserve Orb, fingerprint, and key data visuals;
- no orphaned headings;
- no clipped content.

---

# 15 — SECTION 04: FINGERPRINT / PATTERN VISUAL

Psychological job:
NOW I UNDERSTAND THE SHAPE.

Primary object:
430–560px fingerprint/radar visual.

Do not put five large score cards beside it.

Use a single visual profile shape with:

- five axes;
- dimension nodes;
- central score;
- one highlighted strongest node;
- one highlighted opportunity node.

Use smooth geometry.

If animated:
profile shape should reveal itself outward from center in 600–900ms.

Supporting sentence:

“Your profile is not five separate scores. It is the shape created by how those capabilities work together.”

The visual should carry most of the explanation.

---

# 16 — SECTION 05: STRENGTH

Psychological job:
I HAVE SOMETHING VALUABLE.

Headline:
“Your strongest capability.”

Sub-label:
NATURAL ADVANTAGE

Dominant object:
one large dimension mini-orb enlarged into a spotlight Orb.

Score:
72–110px.

Naya image:
64–84px.

Copy structure:

WHAT’S ALREADY WORKING

[Capability]

WHY IT MATTERS

[Plain-language interpretation]

COMPOUND IT

[One practical use]

Primary action:
COMPOUND THIS STRENGTH

Use dark background with warm dimension accent plus purple support.

---

# 17 — SECTION 06: OPPORTUNITY

Psychological job:
I SEE WHERE A SMALLER GAP COULD CREATE A BIGGER CHANGE.

This section is conditional.

If the concept cannot be understood in 5 seconds, simplify or remove it.

Preferred headline:
“Where you can create more leverage.”

Visual:
Strength Orb → energy path → Opportunity Orb → impact field.

Example:

COMMUNICATION 91

↓

SYSTEMS THINKING 68

↓

“Turn repeated wins into reusable systems.”

Use an energy pathway visual, not a “weakness” card.

Never use shame, deficit, red warning styling, or language that suggests deficiency as identity.

If no meaningful leverage relationship can be derived from the result contract, omit the section and move directly to the next meaningful chapter.

---

# 18 — SECTION 07: NAYA MASTERS

Psychological job:
THERE ARE DOORS MADE FOR ME.

Opening:
NAYA · YOUR SPECIALIST PATHWAYS

Headline:
“Here are the AI paths that make the most sense for you.”

Supporting:
“Don’t collect tools. Build capability where it matters.”

Naya hero image:
110–140px desktop
80–100px mobile.

18 pathways should flow visually as:

PATHWAY CONSTELLATION

not

18 equal cards in a wall.

Each Master door:

number
custom icon
specialty
one-line outcome
match state
OPEN MASTER →

Door surface:

height 180–230px desktop
150–190px mobile

Border:
1px solid rgba(255,255,255,.10)

Background:
linear-gradient(145deg, rgba(255,255,255,.055), rgba(255,255,255,.015))

Hover:
translateY(-4px)
brightness +4%
icon glow
pathway line illuminates

Recommended matches:
small gold/purple “RECOMMENDED” badge.

Do not show “96%” or similar pathway-fit numbers unless the product has a clearly defined reason the user should see them. Relevance is usually easier to understand as a recommendation state than as another pseudo-score.

---

# 19 — SECTION 08: NAYA + GUIDED EXPERIENCE

Psychological job:
NOW NAYA SHOWS ME HOW.

Headline:
“Now let me show you what you can do with this.”

Naya portrait:
large.

Video frame:
16:9
max-width 1080px
radius 28–36px

Frame:
black/dark shell with purple atmospheric border.

Playback control:
custom MAXESS B4 Listen/Play system.

Below video:

WATCH
UNDERSTAND
TRY

Use three visual micro-steps with icons.

Primary CTA:
WATCH WITH NAYA

The video should feel like a premium guided room, not an iframe stuck into a page.

---

# 20 — SECTION 09: PRACTICE / PLAYGROUND

Psychological job:
I CAN DO SOMETHING WITH THIS NOW.

Headline:
“Ready to try it?”

Supporting:
“Take one thing you learned here and turn it into a real AI result.”

Three practice doors:

NAYA WRITER
NAYA BRAINSTORMER
NAYA

Each door has:
custom icon
one-line outcome
OPEN →

Keep this section visually lighter and more actionable than the report sections.

Practice should be frictionless.

---

# 21 — SECTION 10: FINAL NAYA + CTA

Psychological job:
I WANT TO CONTINUE.

Background:
#06040B

Naya portrait:
104–136px

Headline:
“[NAME], you know where you are. Let’s turn that into what comes next.”

Supporting:
“Your result is a starting point. Naya can help you keep learning, building, and improving.”

Offer:
ONE MEMBERSHIP
Everything Included.

Primary B6 button:
START YOUR FREE TRIAL

Subline:
ZERO COST TO START

Optional support line:
FREE GIFTS INCLUDED

Secondary links should be visually restrained.

Do not end with six equal CTAs.

Primary conversion must be unmistakable.

---

# 22 — VISUAL TRANSITION SYSTEM

Every section must have a transition object or transition behavior.

Examples:

Hero → Dimensions:
Orb energy paths seed mini-orbs.

Dimensions → Report:
mini-orb constellation resolves into a line that becomes the report accent.

Report → Fingerprint:
report data condenses into the fingerprint visual.

Fingerprint → Strength:
strongest node grows into the Strength spotlight.

Strength → Opportunity:
energy path extends from strength to opportunity.

Opportunity → Masters:
pathway line branches into Naya Master doors.

Masters → Guided Experience:
selected pathway visually becomes the bridge into Naya’s guided room.

Guided → Practice:
video ends into three practice doors.

Practice → Final CTA:
activity settles into calm dark invitation.

The page should feel like one continuous visual grammar.

---

# 23 — PERSONALIZATION SYSTEM

When user identity exists:

- use first name in Hero;
- use first name in Personal Report;
- use first name in final Naya invitation;
- personalize Naya copy to goal/context when available;
- use real score/dimensions everywhere;
- rank pathways where supported by data;
- never invent personal facts.

If identity is absent:

Use neutral language gracefully.

The anonymous experience must still feel complete.

Optional sign-in should increase personalization, not gate basic value.

---

# 24 — CONVERSION PSYCHOLOGY

Do not sell first.

Earn trust first.

Sequence:

SEE ME
→ SHOW ME
→ EXPLAIN ME
→ RECOGNIZE ME
→ SHOW ME POSSIBILITY
→ SHOW ME TOOLS
→ LET ME PRACTICE
→ INVITE ME FORWARD

Avoid urgency manipulation.

Use clarity, value, emotional recognition, social proof when genuinely available, and a strong final invitation.

The primary CTA should always be the clearest action in its scene.

---

# 25 — VISUAL MEMORY

The user should remember:

1. Naya’s face.
2. Their MAXESS Orb.
3. Their score.
4. The five living mini-orbs.
5. Their fingerprint shape.
6. Their strongest capability.
7. Their opportunity pathway.
8. Naya’s personal voice.
9. The Naya Masters.
10. The final invitation.

If the user remembers “a bunch of cards,” the visual system failed.

---

# 26 — RENDERING / ENGINEERING RULES

One active visible owner per component.

Repository memory is durable.
Conversation is temporary.

Every component must have:

- owner;
- selector or stable identifier;
- source path;
- editable tokens;
- dependencies;
- preservation rules;
- local QA;
- last verified commit.

Micro edits must use:

LOCATE
→ PATCH
→ VALIDATE
→ PREVIEW
→ COMMIT
→ REPORT

Section edits use:

DEFINE
→ SCORE
→ EDIT ALL RELATED ITEMS
→ LOCAL QA
→ REGRESSION
→ COMMIT
→ FREEZE

Release changes use the full system.

---

# 27 — DATA CONTRACT

Authoritative source:

window.MAXESS_RESULT

Never create a second scoring engine.

Never hard-code production result values.

Derived display values may include:

- overall score;
- mastery stage;
- five dimension scores;
- strongest capability;
- opportunity;
- pattern interpretation;
- pathway relevance where defined.

Missing data must fail gracefully.

---

# 28 — ACCESSIBILITY CONTRACT

Every interactive object:

- has accessible name;
- is keyboard reachable;
- has visible focus;
- has 44px minimum effective touch area;
- does not depend on color alone;
- provides reduced-motion behavior.

Every visual data object has a textual equivalent.

Orb score must have accessible text.
Fingerprint must have accessible description.
Mini-orbs must announce score and name.

---

# 29 — PERFORMANCE CONTRACT

Avoid:

- duplicate renderers;
- repeated initialization;
- runaway MutationObserver loops;
- duplicate event listeners;
- unnecessary third-party libraries;
- excessive animation;
- giant DOM duplication.

Prefer:

- one visible owner;
- CSS animations where sufficient;
- requestAnimationFrame only where needed;
- idempotent initialization;
- local rendering ownership.

---

# 30 — PDF / PRINT CONTRACT

Personal Report is the print master.

The PDF must feel like the same product, not an exported webpage.

Use:

- warm white report page;
- strong typography;
- intentional page breaks;
- Orb/fingerprint visuals preserved;
- Naya note preserved;
- key results emphasized;
- no web-only navigation clutter.

The PDF is a deliverable in its own right.

---

# 31 — SECTION SCORECARD

Every section is rescored on:

PURPOSE
CLARITY
USEFULNESS
HELPFULNESS
PERSONALIZATION
VISUAL IMPACT
WOW FACTOR
EMOTIONAL IMPACT
CONVERSION
INTERACTION
ACCESSIBILITY
RESPONSIVENESS
PERFORMANCE
DATA INTEGRITY
MAINTAINABILITY

Use 0–10.

Priority = IMPACT × GAP × DEPENDENCY.

The highest priority can change as the project changes.

The AI must always work the highest-value unresolved requirement, not merely the easiest edit.

---

# 32 — OSCAR REVIEW

After each complete section batch ask:

- Would a skeptical designer be impressed?
- Would a first-time user understand it instantly?
- Does the visual explain more than the prose?
- Does anything feel generic?
- Is any button unnecessary?
- Is any visual merely decorative?
- Is there duplicate information?
- Is the section personally meaningful?
- Is the transition into the next section obvious?
- Does this section deserve to exist?

If the answer exposes a material weakness:

FIX
→ REBUILD
→ RESCORE

---

# 33 — SECTION FREEZE RULE

Do not freeze a section merely because it is technically complete.

Freeze when:

- all declared requirements are implemented;
- the section earns 9.5+ against its scorecard;
- all critical dimensions are 9+;
- browser evidence exists;
- data evidence exists;
- regression evidence exists;
- responsive evidence exists;
- accessibility evidence exists;
- the next section can safely begin.

---

# 34 — FINAL MAXESS STANDARD

MAXESS is the reference implementation of the AI Product Creation System.

Its purpose is not merely to look good.

It must demonstrate that AI can help a human create something extraordinary while:

- preserving intent;
- reducing iteration;
- increasing clarity;
- maintaining memory;
- creating coherent design;
- making smart edits safely;
- proving its work;
- learning from failures;
- and leading the project toward completion.

The desired user experience is:

“I came here because I wasn’t getting enough from AI.
MAXESS showed me something about myself.
Naya made it personal.
The page felt incredible.
I understood what to do.
And now I want to keep going.”

That is the product.

That is the bar.

That is what every section must earn.
