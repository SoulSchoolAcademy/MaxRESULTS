# 🔱 NayaNET E01 — Identity Doorway

**Status:** IMPLEMENTED / STATIC-FIRST REVIEW BUILD
**Architecture:** NayaNET Level 1 Identity + Intelligent Hub + Communication + Smart Note/PSI compatible

## Purpose

E01 is the first real doorway into NayaNET. It intentionally does not attempt to build the whole network. It establishes the human journey:

`SEE NAYA → ENTER NAME → CREATE/REVEAL NETWORK IDENTITY → ENTER INTELLIGENT HUB → DISCOVER FIRST EXPERIENCES`

The experience is built against the canonical NayaNET Level 1 contract: one canonical identity with private and network-facing representations, a private-by-default Intelligent Hub, personal Naya, scoped future communication, and compatibility with the existing Note Event / PSI architecture.

## Included experience

1. **Door** — Welcome to NayaNET, name-first entry, dimensional controls.
2. **Identity** — private real name + editable Smart Name, Smart Link preview.
3. **Reveal** — Smart Name + Smart Link preview and Hub handoff.
4. **Intelligent Hub** — minimal personal Naya space and truthful first-experience choices.
5. **MAXESS handoff** — honest destination boundary; no fabricated score.
6. **Naya Power** — supplied introduction video embedded from YouTube privacy-enhanced mode.
7. **Five-Day Challenge** — canonical Day 1–5 lesson structure and outcomes, with an in-session “what day did you feel Naya Power?” interaction.

## Truth boundaries

This is a static-first review artifact. The following are deliberately **not** claimed as live:

- persistent production account/authentication;
- production identity database record;
- provisioned Smart Link route;
- Smart Mail address;
- live communication;
- live Naya memory backend;
- PSI ingestion;
- MAXESS scoring/runtime;
- server-side Five-Day Challenge progress.

The browser creates a temporary review identity state and explicitly labels the Smart Link as **Preview · not provisioned**.

## Privacy invariant

The entered real name is treated as private identity data. After the identity step, network-facing views use the Smart Name. E01 does not expose the real name in the reveal, Hub, MAXESS handoff, Naya Power, or challenge views.

## Smart Note / PSI compatibility

E01 does not create a competing note store or memory object. It is only an experience layer over the canonical Note Event architecture. No Smart Note, Feed publication, PSI update, or collective propagation is claimed by this static build.

## Media

The Naya Power introduction is the user-supplied reference video:

`https://www.youtube.com/watch?v=wnjvDqEhBCY`

The five-day lesson titles and outcomes are derived from the canonical `5 Day Challenge` repository material. No unverified individual lesson-video URLs are invented.

## Embedding

The artifact is static HTML/CSS/JS and does not require a framework or Wrangler. It is suitable for a static host and can be embedded in a parent experience. No postMessage contract is introduced because E01 has no demonstrated parent/child messaging requirement yet.

## Accessibility

- semantic headings, sections, forms, buttons and tablist semantics;
- labelled name fields;
- keyboard-operable controls;
- visible focus states;
- live status messages for validation and the in-session Day selection;
- no state conveyed by color alone;
- reduced-motion support via `prefers-reduced-motion`;
- responsive touch-friendly controls.

## Review entry point

Open `index.html` directly. No build step is required.

## Evidence classification

- **DESIGNED:** E01 architecture and visual system alignment.
- **IMPLEMENTED:** complete static interaction flow in `index.html`.
- **TESTED:** static/syntax checks in `tests/smoke-test.sh`.
- **VERIFIED:** repository content and code inspection performed during this execution.
- **DEPLOYED:** not claimed.
- **GROOVE-VERIFIED:** not claimed.
- **PRODUCTION-PROVEN:** not claimed.
