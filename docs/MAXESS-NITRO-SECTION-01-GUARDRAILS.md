# MAXESS NITRO — SECTION 01 GUARDRAILS

**Status:** ACTIVE  
**Scope:** Section-by-section execution  
**Active working source:** `E01-SECTION-01-WORKING.html`

## 01 — Section scope is absolute

A Section 01 task produces Section 01 only. The complete Results implementation is reference material, not permission to redesign or replace the page.

## 02 — Reference is not authority

`NITRO/SECTION-01-NAYA-WELCOME-ORBSCORE.html` is preserved as a prior implementation/reference artifact. It is not a second active renderer and must not silently become the production source.

The current active E01 source is:

`E01-SECTION-01-WORKING.html`

## 03 — One obvious artifact

Future Section 01 work should start from `E01-SECTION-01-WORKING.html` and `docs/MAXESS-NITRO-SECTION-01-INDEX.md`, after canonical `main` governance and the active-branch map have been read.

## 04 — Preserve validated Orb behavior

Unless a verified defect is demonstrated, preserve score-dependent color, 6s Orb breathing, the existing Orb composition, and the 14px/220px/10s desktop plus 11px/140px mobile Orbital Bead behavior.

## 05 — Naya is a human arrival

Opening hierarchy:

**Naya presence → Naya message → Listen → YOUR AI SCORE → score reveal → Orb/Bead → score context.**

Use direct human language. Avoid generic AI journey/potential marketing language.

## 06 — One Listen action

Never create a second audio system. Delegate to an existing listener when present; otherwise emit the established `maxess:naya-listen` event for the containing system.

## 07 — Honest verification

Static implementation success does not equal rendered visual QA, Groove publication, or live verification. Unknown evidence remains UNKNOWN.

## 08 — Discoverable memory

Section-specific execution documents use explicit `MAXESS-NITRO-SECTION-01-*` names and are linked from the Section 01 index.

## 09 — No silent overwrite

No automation lane may replace verified Section 01 work from an obsolete baseline. Product ownership and write ownership must remain explicit.

## 10 — Automation must validate the active source

Any Section 01 automation must inspect/validate `E01-SECTION-01-WORKING.html` unless a current human directive explicitly changes the active source.

Automation must never write to retired monolithic artifacts as a side effect of a Section 01 task.

## 11 — Source ambiguity is a stop condition

If the active source, product owner, or deployment payload is ambiguous, STOP and resolve the authority before editing. Never choose a source merely because it is larger, newer-looking, or historically successful.

## 12 — Responsive containment law

Section 01 responsive elements must size themselves to their actual containing block rather than assuming viewport width equals available content width.

Do not use viewport-relative widths such as `92vw` or `94vw` for a child whose parent has horizontal padding unless the resulting geometry has been explicitly proven not to overflow at every required viewport.

Prefer `width:100%` with an appropriate `max-width` inside the padded content container.

For the protected Orb/Bead system, preserve the approved desktop/mobile bead geometry while ensuring the containing Orb wrapper itself cannot exceed its parent.

This rule exists because the previous Section 01 implementation could make the Orb wrapper wider than the padded content area at mid-width viewports such as 600px and 768px, creating a potential horizontal clipping/overflow condition.
