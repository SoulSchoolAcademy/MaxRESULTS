# NayaNET Intelligent Hub — V5 Living Intelligence Cockpit

## Status
PROTOTYPE / EXPERIENCE LAYER — Cloudflare static package

## Purpose
The Hub is the living front door for Naya Power intelligence. It presents the current intelligence state, saved Daily/Weekly/Monthly/Yearly reports, Smart Notes, the Intelligent Feed, evidence, source links, Naya listening/conversation surfaces, and the next right action.

## Core loop

`SMART BRAIN → INTELLIGENT FEED → INTELLIGENT HUB → INTELLIGENCE REPORT → NAYA`

## V5 experience changes

- Replaced the dashboard-like hero with a report-first “Here is what matters right now” experience.
- Increased text contrast so labels and secondary information remain easy to read.
- Made saved Intelligence Reports a first-class Hub concept.
- Added Daily / Weekly / Monthly / Yearly report archive views.
- Added explicit Listen-to-Naya surfaces for saved reports.
- Added Human / Naya / Machine Smart Notes.
- Added source-link presentation back to the canonical Smart Brain repository.
- Added a visible Live Intelligence Feed and event-flow model.
- Added a clear Next Right Action above the fold.
- Preserved the privacy and evidence truth boundaries; the static artifact never claims a live backend, persistence layer, or cloned-voice connector without runtime observation.

## Truth boundary

This artifact is the experience layer. Real personal-intelligence sync, persistence, and cloned Naya voice playback require authorized live connectors and independent runtime observation.

Runtime proof follows:

`SOURCE → BUILD ARTIFACT → DEPLOYMENT → EXACT PUBLIC RUNTIME → INDEPENDENT OBSERVATION`

## Cloudflare Pages

Use this directory as the Pages project root. The site is static and requires no build command.

- Build command: none
- Output directory: `.`
- Entry point: `index.html`
