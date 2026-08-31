# NayaNET Public Page — AAA Visual / UX Lock

**Date:** 2026-08-31  
**Status:** LOCKED — preserve this version unless a deliberate change is explicitly requested.

## Decision
The current NayaNET public-facing page is approved by Shawn as the preferred visual and experiential baseline. Preserve the current look, feel, hierarchy, cinematic video treatment, Academy presentation, jewel/insight-card language, spacing, contrast, and overall premium experience.

## Canonical positioning
**NayaNET — Create. Connect. Grow with Us**  
**Master AI and Be Your MAX!**  
**AAA Excellence is our mission and goal for AI and Humans — together in one network, a private new internet portal called NayaNET. Meet Naya.**

## Quality bar
The page is treated as an AAA/premium reference, not a prototype. Future changes must preserve:
- premium, cinematic presentation;
- strong visual hierarchy and readable typography;
- high contrast and accessible text sizing;
- living depth rather than flat/default AI-card styling;
- coherent NayaNET / Naya Power / MAXIS visual language;
- full-width, polished video presentation;
- jewel-inspired insight cards and intentional color use;
- clear user journey from discovery → experience → free trial;
- minimal, surgical changes rather than page rewrites.

## Frozen implementation principle
Do **not** rebuild or replace the approved page to make small changes. When a future request concerns navigation, CTA destinations, labels, tracking, or another isolated behavior, append a narrow patch or make the smallest possible targeted edit.

Do not reintroduce the earlier failure mode of repeatedly regenerating substantially identical code while claiming visual changes were made.

## Current CTA rule
The canonical Naya Power free-trial destination supplied on 2026-08-31 is:
`https://humanmaximuscodex.groovesell.com/checkout/08fba2cbd6488ef4d2cc82b52d361dab`

Selected entry buttons should route to that destination when explicitly requested, while preserving their approved visual treatment.

## Academy rule
The Five-Day Naya Power Academy experience is part of the approved page experience. Preserve the five lesson videos, cinematic 16:9 treatment, lesson structure, jewel/insight presentation, and final “Which Day Did You Feel Naya Power?” feedback experience. Do not redesign this layer unless explicitly requested.

## Source-of-truth context
The NayaPOWER repository contains the canonical Naya Power framework and Five-Day Academy structure. Recent commits document the Academy framework and curriculum, including the five-day experience and compounding-intelligence model.

## Future change protocol
1. Read this note before modifying the public page.
2. Treat the approved page as frozen.
3. Identify the exact requested delta.
4. Make the smallest change that solves it.
5. Verify the affected behavior without disturbing the visual baseline.
6. Record any material new decision as a follow-up Naya Note.

**AAA principle:** Preserve what is excellent. Change only what is necessary. Verify before claiming success.
