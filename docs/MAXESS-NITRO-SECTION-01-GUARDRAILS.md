# MAXESS NITRO — SECTION 01 GUARDRAILS

**Status:** ACTIVE + HARD LOCK  
**Scope:** Section-by-section execution  
**Active working source:** `E01-SECTION-01-WORKING.html`

## 00 — EXECUTION SUCCESS LOCK

**The objective is observable completed work, not a report.**

For every Section 01 execution:

1. Read canonical governance and the active Section 01 map first.
2. Fetch the current `E01-SECTION-01-WORKING.html` before planning or editing.
3. Establish the exact baseline blob SHA and current version marker.
4. Build the complete material-change checklist from the user's directive + current source + applicable Section 01 requirements.
5. Edit the **same active file** in place. Never create a substitute renderer for convenience.
6. The file written to GitHub must be the exact file intended for the human Groove handoff.
7. After writing, immediately re-fetch the **same path on the same branch**.
8. Verify the re-fetched content contains the actual requested changes. Do not treat a changed commit SHA, changed version string, or successful write response as implementation proof.
9. Compare baseline → new commit and confirm the intended artifact changed.
10. Run static QA and available behavior/regression QA.
11. Only then provide the raw GitHub link.
12. State IMPLEMENTED / VERIFIED / LIVE VERIFIED / HUMAN REVIEW REQUIRED / UNKNOWN separately.

### Hard completion rule

**NO REPORT-ONLY COMPLETION.**

A plan, critique, checklist, version bump, commit, or explanation is not completion. If the requested edits are not visibly present in the re-fetched active artifact, the work is **NOT DONE**.

### Self-instruction after every execution

Before returning the response, Naya must internally ask:

> **Did I actually mutate the active delivery file? Can I point to the requested changes inside the re-fetched file? Did I verify the exact raw link points to that same file? If any answer is NO or UNKNOWN, do not claim completion; continue execution or report the exact blocker.**

## 01 — Section scope is absolute

A Section 01 task produces Section 01 only. The complete Results implementation is reference material, not permission to redesign or replace the page.

## 02 — Reference is not authority

`NITRO/SECTION-01-NAYA-WELCOME-ORBSCORE.html` is preserved as a prior implementation/reference artifact. It is not a second active renderer and must not silently become the production source.

## 03 — One obvious artifact / one delivery payload

`E01-SECTION-01-WORKING.html` is the single active Section 01 engineering source **and the Groove handoff payload** unless the user explicitly changes that decision.

The human workflow is:

**Naya edits E01 → GitHub stores E01 → Naya verifies E01 → Naya returns E01 raw → human pastes E01 into Groove.**

Do not introduce a second delivery file, reconstructed embed, alternate renderer, or stale copy.

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

**However, lack of Groove access is not a blocker to engineering execution.** The human owns Groove deployment. Naya owns the GitHub engineering artifact and handoff.

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
