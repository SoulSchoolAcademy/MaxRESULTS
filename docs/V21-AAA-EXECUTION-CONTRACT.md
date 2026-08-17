# MAXESS V21 — AAA EXECUTION CONTRACT

## Mission
Complete the existing MAXESS Results experience—not replace it—into one premium, personalized release:
DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY.

## Laws
- `main` is protected known-good baseline.
- Work only on `maxess-results-v21-working` until release passes.
- `window.MAXESS_RESULT` is the only authoritative runtime result source.
- Do not create another competing Results renderer, hero, score source, or uncontrolled patch generation.
- Preserve valuable existing Groove content and working behavior.
- Consolidate obsolete V11/V12/V13/V18/V20 shells/controllers instead of stacking another generation.
- Never hard-code a real user's score.
- Never release on visual inspection alone.

## Canonical visible flow
Naya → LISTEN TO NAYA → MAXESS SCORE → Five Dimensions → Personalized Report → Pattern → Strength → Lever → Next Move → 18 Naya Masters → Playground/ending.

## Required implementation
### Naya
Use:
“Hi. I’ve looked at your results.”
“This isn’t your judgment. It’s your map.”
Exactly one primary Listen CTA. It must be layered: black core, white type, restrained purple accent, depth, hover, pressed and focus states.

### Score
Preserve the successful orb. Center the real score inside it. Default hero text:
SCORE
MAXESS SCORE
Remove “out of 100” unless testing proves it helps comprehension.

### Five dimensions
Exactly five data-driven mini MAXESS orbs sourced from `MAXESS_RESULT.dimensions`. Each shows score + name, inherits the main-orb visual language, is clickable, and updates one shared detail surface. Never hard-code production values.

### Personalized report
Create one premium modern document/letter treatment. Interpret, do not repeat statistics. Include overall result, mastery stage, pattern, strongest capability, highest-leverage area, plain-language meaning, practical next action, and invitation to improve.

Stages:
Supporting → Foundation → Developing → Advancing → Mastering.

### Narrative preservation
Keep useful existing Pattern, Strength, Lever, Next Move, 18 Naya Masters, Playground, media and ending content. Reorder/style it instead of replacing it when safe.

### Naya narration
Interpret what the results mean. Naya is a guide, not a screen reader.

### PDF
Treat PDF as a first-class product. Use dedicated print styles, intentional page/section breaks, readable typography, no clipping/overflow/orphaned headings, and inspect a real generated PDF before release.

### Technical consolidation
One visible controller. One result source. Remove obsolete competing shells and duplicate Listen controls. Resolve duplicate IDs, repeated listeners, mutation loops and race conditions. Preserve result hydration and existing useful functions.

## QA
Test real payload, demo fixture, desktop, tablet, mobile, keyboard, reduced motion, Listen, five dimensions, report, Masters, Playground, Print/Save PDF and malformed/missing-result cases.

Stress score boundaries: 0, 49, 50, 64, 65, 74, 75, 89, 90, 100.

## Release gate
Do not release until syntax, structural checks, browser behavior, responsive behavior and actual PDF output pass. Confirm Naya, single Listen CTA, centered score, five interactive orbs, personalized report, mastery stage, Pattern, Strength, Lever, Next Move, 18 Masters, Playground/ending, no competing renderer, no competing result source, no destructive replacement.

## Execution loop
INSPECT → MAP → IMPLEMENT COHERENT BATCHES → BUILD → STATIC QA → BROWSER QA → PDF QA → FIX ALL FAILURES → QA AGAIN → FREEZE.

Standard:
**A person would be proud to receive this.**
