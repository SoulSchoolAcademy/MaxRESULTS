# MAXESS Section Lock + Append-Only Law

**Timestamp:** 2026-08-19
**Category:** SOLUTION / DECISION

## Keywords

MAXESS section lock, append-only, immutable section, Section 01, Section 02, section-by-section, frozen baseline, preservation, regression, section contract, exact text, forbidden text, execution prompt, human review, Groove, Naya Nitro

## Aliases / synonyms

section freeze, section lock, immutable prior section, current-section-only, append-only build, protect previous work, no rewrite, no refactor, no cleanup, progressive page construction, locked artifact regions

## Related paths / concepts

- `NAYA-OS.md`
- `docs/REPOSITORY-MAP.md`
- `docs/smart-notes/INDEX.md`
- `E01-SECTION-01-WORKING.html`
- MAXESS Results section-by-section build model
- Groove human review

## Context

MAXESS is intentionally built as a sequential, cumulative experience. A major failure mode occurred when later work was treated like ordinary page refactoring: a request for Section 02 caused the previously refined Section 01 experience to be regenerated or disturbed. This violates the product methodology and creates avoidable regressions in a large artifact.

The durable solution is an explicit append-only construction law. Once a section is approved and frozen, its source, behavior, visual presentation, assets, CSS, JavaScript, copy, responsive behavior, and accessibility behavior are immutable unless the human explicitly reopens that section.

## LAW

### 1. SECTION-BY-SECTION CONSTRUCTION

MAXESS is built in this progression:

**SECTION 01 → FREEZE → SECTION 02 → FREEZE → SECTION 03 → FREEZE → …**

Each new section is an addition to the existing experience, not a reason to regenerate the complete document.

### 2. IMMUTABILITY

After a section is locked, later sections MUST NOT:

- rewrite it;
- regenerate it;
- refactor it;
- clean it up;
- reorder it;
- restyle it;
- alter its CSS;
- alter its JavaScript;
- alter its assets;
- alter its copy;
- alter its behavior;
- alter its responsive behavior;
- alter its accessibility behavior;
- alter its identifiers or data contracts;
- replace it with a new implementation.

### 3. APPEND-ONLY RULE

When Section N is active, implementation may add Section N code after the locked Section N-1 boundary. The intended model is:

**LOCKED 01 + NEW 02**

then:

**LOCKED 01 + LOCKED 02 + NEW 03**

and so on.

Earlier locked source regions must remain byte-for-byte unchanged unless explicitly reopened by the human.

### 4. NO GLOBAL DRIFT

A later section must not use global CSS, shared JavaScript, document-wide cleanup, or architectural regeneration as an excuse to alter the visual or behavioral result of an earlier locked section. New behavior should be scoped to the active section whenever technically possible.

If a genuine shared dependency requires changing a frozen section, stop ordinary section work, document the dependency, obtain explicit human authorization to reopen the affected section, and rerun that section's full regression and quality gate before continuing.

### 5. SECTION CONTRACT BEFORE CODE

Before implementing every new section, Naya MUST write a section contract containing:

- purpose;
- human/emotional objective;
- visual objective;
- exact required text;
- explicitly forbidden text/content;
- objects/components;
- dimensional/visual behavior;
- interaction behavior;
- responsive behavior;
- accessibility requirements;
- transition from the previous section;
- transition to the next section where known;
- acceptance criteria;
- failure conditions.

No invented copy, UI, explanation, marketing language, decorative content, or unrelated component may be introduced merely because it seems useful.

### 6. EXACT-TEXT LAW

Every section must distinguish:

**TEXT REQUIRED**

**TEXT OPTIONAL**

**TEXT FORBIDDEN**

Text not authorized by the section contract is a defect when it materially changes the intended experience.

### 7. VISUAL-OBJECT LAW

Before building visually significant objects such as Orbs, cards, nodes, or capability indicators, define what each object represents, what information it displays, its visual hierarchy, dimensional behavior, color role, movement, and responsive behavior. Effects are not added merely because another effect is possible. Mutate only when rendered evidence identifies a material weakness.

### 8. LOCK MANIFEST

Every active MAXESS build must maintain explicit section state:

- section number/name;
- status: ACTIVE / FROZEN / REOPENED;
- baseline commit/blob where applicable;
- protected scope;
- authorized mutation scope;
- verification status.

### 9. REGRESSION GATE

Before a new section can be frozen:

1. re-fetch the committed artifact;
2. diff the prior locked section(s) against their baseline;
3. prove no unauthorized mutation occurred;
4. run static QA;
5. run JavaScript/behavior QA;
6. run responsive QA;
7. run accessibility QA;
8. render the real assembled experience where available;
9. perform human review for the active section;
10. record the result and freeze only when the applicable quality gate passes.

### 10. HUMAN APPROVAL

A section becomes FROZEN only after the required human quality gate. Source existence or a successful commit does not equal approval.

### 11. RECOVERY RULE

If a later mutation damages a locked section, STOP. Do not patch the damaged result forward. Restore the locked section from its authoritative baseline, prove the restoration, then resume the active section using append-only construction.

### 12. NO WHOLE-DOCUMENT REGENERATION

For a large MAXESS artifact, the default response to a section change is NOT to regenerate the complete document. The default is to preserve the locked artifact and perform a surgical current-section mutation or append. Whole-document regeneration is prohibited when it risks altering locked sections.

## REQUIRED EXECUTION PROMPT STRUCTURE

Before consequential section implementation, Naya must generate a copy/paste-ready execution prompt containing:

**CURRENT LOCKED STATE → ACTIVE SECTION → MISSION → EXACT CONTENT → REQUIRED TEXT → FORBIDDEN TEXT → VISUAL SPECIFICATION → OBJECT/ORB SPECIFICATION → INTERACTION → RESPONSIVE → ACCESSIBILITY → APPEND-ONLY LAW → VERIFICATION → FAIL CONDITIONS → REQUIRED FINAL REPORT.**

This prompt is the execution contract for the next context/AI and must not rely on conversational memory.

## LEADERSHIP LAW

The user should not have to discover or specify the obvious next engineering action. After every consequential execution Naya must proactively provide:

**CURRENT STATE → WHAT WAS FOUND → RECOMMENDATION → WHY → EXACT NEXT ACTION → EXECUTION PROMPT → VERIFICATION STATUS.**

Naya must lead the path to success while preserving the user's authority over material product decisions.

## WHY THIS MATTERS

This is not merely a MAXESS coding preference. It is a reusable method for building large, beautiful, reliable web experiences with AI:

**DEFINE → BUILD ONE SECTION → VERIFY → LOCK → APPEND THE NEXT → VERIFY → LOCK → REPEAT.**

The method protects finished work, reduces regression, makes AI behavior predictable, preserves human intent, and creates a teachable process for extraordinary website creation.

## Evidence

- User explicitly established this law during MAXESS E02 recovery on 2026-08-19.
- Canonical `main:NAYA-OS.md` already contains Section Isolation + Freeze Law and must remain authoritative.
- `maxess-results-v21-working:E01-SECTION-01-WORKING.html` is the active E01 working artifact.
- `docs/smart-notes/2026/08/2026-08-19-section-isolation-and-nitro-execution-learning.md` records the earlier section-freeze learning.
