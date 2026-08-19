# MAXESS Results — Deployment + Groove Boundary Contract

**Status:** CANONICAL GOVERNANCE
**Effective:** 2026-08-19
**Authority:** NAYA LAW / MAXESS EXECUTION SYSTEM

## 1. PURPOSE

This document defines the exact boundary between MAXESS engineering and Groove publishing.

The boundary exists to prevent a recurring execution error: treating Groove as an engineering renderer, QA environment, or part of Naya's implementation job.

## 2. SOURCE OF TRUTH

GitHub is the engineering source of truth.

- Repository: `SoulSchoolAcademy/MaxRESULTS`
- Governance/reference branch: `main`
- Active Results engineering branch: `maxess-results-v21-working`

The MAXESS artifact in GitHub is the source Naya must build, inspect, protect, diff, test, and deliver.

## 3. GROOVE IS NOT NAYA'S ENGINEERING ENVIRONMENT

**Groove is the user's publishing environment.**

Naya does **not** own Groove execution.

Naya must not:

- render MAXESS inside Groove;
- inspect a Groove-rendered page and represent that inspection as completed engineering QA;
- claim Groove runtime verification;
- claim Groove live verification;
- publish to Groove;
- replace GitHub source with a Groove-specific implementation;
- create a competing Groove renderer;
- invent or assume Groove-specific APIs, behavior, dimensions, or limitations;
- use Groove as a substitute for source, static, behavioral, responsive, accessibility, or artifact QA.

When Groove is mentioned in an execution request, interpret it as a **delivery target and human review boundary**, not as permission to operate Groove.

## 4. NAYA'S GROOVE RESPONSIBILITY

Naya's responsibility is to produce the **best possible self-contained Groove embed payload** from the authoritative MAXESS engineering source.

That means the delivered code must be:

- complete;
- self-contained;
- deterministic where practical;
- responsive;
- accessible;
- visually intentional;
- free of unnecessary dependencies;
- free of competing renderers;
- compatible with the intended embed context;
- resilient to normal container-width variation;
- free of assumptions that require Naya to control the host page;
- clearly scoped to the active MAXESS section;
- ready for the user to paste into Groove.

The engineering objective is:

**BUILD THE BEST EMBED → VERIFY THE SOURCE → DELIVER THE EMBED → HUMAN PASTES INTO GROOVE → HUMAN REVIEWS THE ACTUAL GROOVE EXPERIENCE.**

## 5. HUMAN GROOVE REVIEW

The user is the authority for final Groove presentation review.

After Naya delivers an embed payload, the user may paste it into Groove and inspect the actual result.

That human review can evaluate:

- visual composition;
- actual host-container behavior;
- spacing;
- cropping;
- responsive behavior in the real host;
- typography;
- motion;
- perceived quality;
- section transitions;
- any Groove-specific rendering behavior.

Naya must treat the user's Groove review as new evidence and may then repair the GitHub source within the authorized mutation zone.

## 6. VERIFICATION STATES

Never collapse these states:

### IMPLEMENTED
The code has been written in the authorized GitHub artifact.

### SOURCE VERIFIED
The GitHub artifact was re-fetched and its identity, scope, integrity, and required QA evidence were checked.

### RUNTIME VERIFIED
The artifact was actually executed in an available engineering/runtime environment and the stated behavior was observed there.

### LIVE VERIFIED
The artifact was actually verified at the public production target by an authorized verification path.

### HUMAN REVIEW REQUIRED
The remaining evidence requires the user's actual human-facing host environment, including Groove when Groove presentation is the subject.

### UNKNOWN
The evidence does not exist or cannot be established. Never substitute inference.

**A GitHub commit is not Groove verification.**

## 7. WHAT NAYA MUST DELIVER FOR GROOVE

When the user asks for the Groove embed, the response should prioritize:

1. the exact current GitHub artifact or embed-ready code;
2. the source/commit identity;
3. the mutation scope;
4. what was actually verified;
5. what remains for human Groove review;
6. the exact next action for the user.

Do not bury the deliverable under a speculative Groove discussion.

## 8. EMBED ENGINEERING RULES

Unless the active product contract explicitly requires otherwise, a MAXESS Groove payload should:

- avoid external page loaders;
- avoid iframe-based Results substitution;
- avoid GitHub fetches at runtime;
- avoid dependence on host-page CSS selectors;
- namespace section-specific selectors and IDs;
- avoid global CSS that can corrupt the host page;
- avoid assumptions about viewport height;
- tolerate narrow and wide containers;
- include reduced-motion handling;
- preserve keyboard and screen-reader behavior;
- fail safely when required result data is unavailable;
- use the authoritative `window.MAXESS_RESULT` contract when applicable;
- never invent production result data merely to make a visual appear complete.

## 9. DO NOT CONFUSE ENGINEERING QA WITH GROOVE QA

Engineering QA happens before delivery and includes the applicable:

**SOURCE → DIFF → STATIC → JS/BEHAVIOR → RESPONSIVE → ACCESSIBILITY → REGRESSION → OSCAR**

gates.

Groove QA is the user's subsequent host-environment review.

Naya must not claim the latter from completion of the former.

## 10. FAILURE / FEEDBACK LOOP

If the user reports a Groove-specific problem:

**STOP → IDENTIFY WHETHER THE FAILURE IS SOURCE OR HOST → PRESERVE FROZEN SECTIONS → MODIFY ONLY THE AUTHORIZED SOURCE ZONE → REFETCH → DIFF → QA → DELIVER NEW EMBED → HUMAN GROOVE REVIEW.**

Do not mutate a frozen section to solve an unproven host-environment problem.

Do not create a special Groove-only renderer unless the human explicitly changes the architecture.

## 11. RELEASE CHAIN

The engineering chain is:

**AUTHORITATIVE SOURCE
→ ACTIVE-SECTION CONTRACT
→ IMPLEMENT
→ REFETCH
→ DIFF
→ STATIC QA
→ BEHAVIOR QA
→ RESPONSIVE QA
→ ACCESSIBILITY QA
→ REGRESSION
→ OSCAR
→ COMMIT
→ REFETCH
→ DELIVER EMBED**

The human delivery chain is then:

**PASTE INTO GROOVE
→ HUMAN REVIEW
→ REPORT ACTUAL HOST RESULT
→ NAYA REPAIRS SOURCE IF REQUIRED
→ REPEAT**

## 12. HARD STOP CONDITIONS

Naya must stop and state `UNKNOWN` rather than guess when:

- the intended Groove embed context is unknown and the missing detail materially affects implementation;
- a claimed Groove behavior has not been observed;
- a live/public result has not actually been fetched;
- a host-specific rendering problem cannot be distinguished from a source problem;
- the requested change would require modifying a frozen section;
- the authoritative GitHub source cannot be established.

## 13. CORE LAW

**NAYA BUILDS. GITHUB PROVES THE ENGINEERING SOURCE. THE USER PUBLISHES AND REVIEWS GROOVE.**

The objective is not merely to make code exist.

The objective is to produce extraordinary MAXESS experiences while keeping the engineering boundary, source of truth, frozen sections, and human review boundary intact.
