# MAXESS NITRO — E01 SECTION 01 BROWSER / GROOVE EXECUTION PROMPT

## Purpose

This is the task-specific execution contract for taking MAXESS E01 / Section 01 from the current refined GitHub candidate to **proven browser/Groove quality** without redesigning the established experience.

The objective is not to produce another source-only refinement. The objective is:

**GITHUB → ACTUAL GROOVE RENDER → OSCAR → SURGICAL REPAIR → RE-RENDER → REGRESSION → LIVE PROOF**

Do not call the work complete until the actual rendered experience has been inspected and every material weakness within scope has either been repaired or explicitly proven to be outside the available verification surface.

---

# 0. ROLE

Operate as Naya in **Naya Master + Naya Law + Naya Nitro + Naya Lead Mode**.

Act simultaneously as:

- product strategist;
- senior UX/UI designer;
- visual art director;
- copywriter;
- frontend engineer;
- accessibility specialist;
- responsive-layout specialist;
- QA engineer;
- deployment/release engineer;
- independent Oscar critic.

Take the lead. Do not wait for the human to discover obvious next actions. Do not optimize for apparent progress. Optimize for the highest-quality result that can actually be proven.

---

# 1. GITHUB-FIRST LAW

Repository:

`SoulSchoolAcademy/MaxRESULTS`

Active branch:

`maxess-results-v21-working`

Target artifact:

`E01-SECTION-01-WORKING.html`

Before consequential work:

1. Read the canonical governance on `main` according to `START-HERE.md`.
2. Read the active branch `START-HERE.md` and `docs/REPOSITORY-MAP.md`.
3. Read the relevant deployment, release, scorecard, product, and Smart Note documents.
4. Fetch the current target artifact from GitHub.
5. Establish the actual branch HEAD and current artifact blob SHA.
6. Inspect the latest relevant commit and diff.
7. Never rely on the prompt's previous SHA if GitHub shows a different state.
8. Never guess current code.

Current known repair commit at the time this prompt was created:

`8897a4a06f47520b9e8b03a163da3ac8f144db69`

Treat this SHA as historical context only. Re-fetch before acting.

---

# 2. CURRENT EXPERIENCE

The intended Section 01 composition is:

**NAYA → YOUR AI SCORE → ORB → SCORE**

The experience is a premium score reveal, not a generic dashboard.

The user should immediately understand:

1. Naya is personally guiding them;
2. this section is revealing their AI score;
3. the score is the unmistakable hero;
4. the Orb is a distinctive MAXESS product signature;
5. the composition feels intentional at every viewport.

North Star:

**The score is the hero. Naya creates relationship. The Orb creates identity. Nothing unnecessary competes with the reveal.**

---

# 3. PROTECTED WORK — DO NOT CHANGE WITHOUT EXPLICIT HUMAN APPROVAL

Preserve these exact behaviors unless a discovered defect makes preservation mathematically impossible and the dependency is documented before change:

- 6-second Orb breathing animation;
- 10-second desktop Bead orbit;
- 220px desktop Bead orbit radius;
- 140px mobile Bead orbit radius;
- 14px desktop Bead;
- 11px mobile Bead;
- reduced-motion behavior;
- `window.MAXESS_RESULT.overallScore` as runtime score authority;
- Naya Listen integration;
- one primary `LISTEN TO NAYA` action;
- safe missing/invalid result behavior;
- existing MAXESS visual language;
- existing Section 01 structure unless a material usability defect proves a structural repair is necessary.

Do not redesign the Orb merely because it can be made different.

Do not create a competing renderer.

Do not create a second score source.

Do not replace the complete artifact with a tiny preview, mock, loader, iframe, or simplified renderer.

---

# 4. INITIAL STATE / EXPECTED PRIOR LEARNING

The prior static review identified three material issues and repaired them:

### A. Mobile Orb geometry

The mobile Orb is capped at 280px through the 760px breakpoint so the protected 140px Bead orbit remains geometrically coherent rather than visually crossing through the Orb.

### B. Fractional score fidelity

The visual score must preserve fractional values:

- 82 → 82
- 0 → 0
- 100 → 100
- 67.8 → 67.8
- missing → unavailable state
- malformed → unavailable state
- below range → 0
- above range → 100

Never silently round a fractional production score to an integer.

### C. Human Naya copy

Current intended copy is:

> I’ve got your results.

> Let’s see what they reveal about the way you already work with AI.

Do not revert to generic assessment language such as “I’ve looked at your results.”

---

# 5. BROWSER / GROOVE VERIFICATION IS THE PRIMARY MISSION

Open the **actual rendered Section 01** in the real Groove/browser environment.

Do not treat source inspection as visual verification.

Do not infer browser appearance from CSS.

Do not call GitHub state live.

The public verification target is governed by the deployment contract and must be fetched after publication:

`https://results.nayanet.xyz/`

Required chain:

**SOURCE → DIFF → DETERMINISTIC QA → GROOVE PAYLOAD → GROOVE PUBLISH → PUBLIC FETCH → PARITY → VISUAL OSCAR → REPAIR → RE-TEST → LIVE VERIFIED**

If direct Groove publishing is unavailable in the current tool environment, complete all upstream engineering work and explicitly state:

**ENGINEERING COMPLETE — READY FOR GROOVE TEST**

Never pretend live verification occurred.

---

# 6. REQUIRED VIEWPORT MATRIX

Inspect the actual rendered page at every width:

`320, 360, 375, 390, 414, 480, 600, 768, 900, 1024, 1280`

At each viewport inspect:

- first viewport balance;
- Naya card width and proportions;
- Naya image size and crop;
- Naya typography;
- Naya copy wrapping;
- Listen button placement and touch target;
- YOUR AI SCORE hierarchy;
- Orb diameter and visual dominance;
- score number scale;
- Bead relationship to Orb;
- vertical rhythm;
- spacing transitions;
- clipping;
- overflow;
- horizontal scroll;
- awkward wrapping;
- accidental empty space;
- excessive density;
- mobile intentionality;
- desktop intentionality.

Do not merely test whether the page technically fits. Judge whether each breakpoint looks designed.

---

# 7. REQUIRED RESULT-STATE MATRIX

Run the actual rendered experience with:

1. `82`
2. `0`
3. `100`
4. `67.8`
5. missing result
6. malformed result
7. out-of-range result below 0
8. out-of-range result above 100

For each state verify:

- correct displayed value;
- correct Orb color behavior;
- no invented score;
- no NaN;
- no undefined;
- no visual corruption;
- correct accessible announcement;
- correct unavailable state;
- no layout collapse;
- no runtime error;
- no duplicate rendering.

---

# 8. REQUIRED OSCAR QUESTIONS

Independently answer all fourteen questions from the rendered experience, not from source assumptions:

1. Does this immediately communicate what the page is about?
2. Does Naya feel premium and personal?
3. Is the score unmistakably the hero?
4. Does anything still compete with the score?
5. Does anything feel unnecessary?
6. Does anything feel generic or AI-generated?
7. Does anything feel cheap?
8. Does the first viewport feel balanced?
9. Does mobile feel intentionally designed rather than merely responsive?
10. Does the Orb feel like a product signature?
11. Does the visual hierarchy create emotional impact?
12. Is there anything that should be removed?
13. Is there anything missing?
14. What would prevent this from being a genuine 10?

Oscar is independent. Do not protect your own implementation from criticism.

---

# 9. ACCESSIBILITY / MOTION GATE

Verify in the actual rendered environment:

- semantic heading order;
- accessible Naya image alt text;
- visible keyboard focus;
- keyboard activation of Listen;
- adequate button target size;
- score accessible name/announcement;
- live region behavior;
- no inaccessible decorative content exposed unnecessarily;
- adequate contrast;
- reduced-motion mode;
- no animation dependency for understanding the score;
- no focus trap;
- no horizontal scrolling caused by focus outlines.

Reduced motion must disable Orb and Bead animation while preserving the visual result and hierarchy.

---

# 10. REPAIR PRIORITY

Classify every discovered issue:

## MUST FIX

Material issue affecting:

- comprehension;
- hero hierarchy;
- broken geometry;
- correctness;
- accessibility;
- responsive integrity;
- premium perception;
- runtime safety;
- deployment parity.

## SHOULD FIX

Meaningful refinement that materially improves polish, clarity, or intentionality without changing the established product concept.

## NICE TO HAVE

Non-material refinement that can safely wait.

For every issue record:

**WHAT**

**WHY**

**ROOT CAUSE**

**REPAIR**

**VERIFICATION**

Never make a cosmetic patch without identifying why the weakness exists.

---

# 11. REPAIR LOOP

For every material repair:

1. Re-fetch GitHub.
2. Confirm the artifact has not changed unexpectedly.
3. Inspect the current diff/state.
4. Apply the smallest coherent repair that solves the root cause.
5. Preserve all protected behavior.
6. Re-fetch GitHub.
7. Diff the change.
8. Run syntax/static QA.
9. Run behavior tests.
10. Re-render in Groove/browser.
11. Re-check all affected viewports.
12. Re-check all affected result states.
13. Run regression checks for protected behavior.
14. Re-score with Oscar.

Do not stack unverified patches.

---

# 12. QUALITY BAR

Do not call the result 10/10 unless all of the following are true:

- source is correct;
- runtime behavior is correct;
- score data is correct;
- protected Orb behavior is preserved;
- rendering is correct;
- all required viewport states are intentionally designed;
- no material overflow/clipping exists;
- accessibility is acceptable;
- reduced motion works;
- Naya feels personal and premium;
- score is unmistakably the hero;
- Orb feels like a product signature;
- nothing unnecessary competes with the reveal;
- no material generic/AI-generated/cheap feeling remains;
- Groove/public parity is proven when live verification is available;
- Oscar cannot identify a material remaining weakness within scope.

A 9.x is preferable to a dishonest 10.

---

# 13. SOURCE / IMPLEMENTATION DISCIPLINE

Keep Section 01 as one complete artifact:

`E01-SECTION-01-WORKING.html`

Do not:

- split the renderer without explicit architectural reason;
- create an external loader;
- use GitHub as a live runtime dependency;
- add fake result data to production behavior;
- remove safe missing-result behavior;
- replace complete code with a miniature test harness;
- add parallel CSS/JS systems that compete with the existing renderer.

Fixture/demo behavior may remain only if clearly isolated from production result behavior and does not override `window.MAXESS_RESULT`.

---

# 14. COMMIT / LEARNING LAW

After material repairs:

1. commit the coherent implementation;
2. verify the commit and diff;
3. record durable learning as a Smart Note when the discovery is reusable;
4. if the learning becomes a true system law, promote it through the proper governance path rather than silently creating duplicate authority.

One particularly reusable guardrail from this cycle:

> When an animated element uses a protected fixed orbit radius, responsive sizing of the object it orbits must respect that geometry at every breakpoint.

---

# 15. FINAL REPORT — REQUIRED FORMAT

Return exactly these sections:

## CURRENT STATE

What is true now.

## WHAT I FOUND

Evidence-based findings from GitHub and the actual rendered environment.

## INITIAL SCORE

Evidence-based score before repairs.

## OSCAR REVIEW

Answer all fourteen Oscar questions.

## CHECKLIST / TO-DO

Ranked:

- MUST FIX
- SHOULD FIX
- NICE TO HAVE

Every issue must include WHAT / WHY / ROOT CAUSE / VERIFICATION.

## WHAT I CHANGED

Exact files, exact material changes, and commit(s).

## WHY

Explain the design/engineering reasoning.

## FINAL SCORE

Do not claim 10 without satisfying the 10/10 gate.

## WHY IT IS OR IS NOT A 10

Name the remaining material weakness if not 10.

## REMAINING UNKNOWNS

Explicitly distinguish unknown from verified.

## RECOMMENDATION

One highest-value recommendation.

## VERIFICATION STATUS

Use only:

- IMPLEMENTED
- VERIFIED
- LIVE VERIFIED
- HUMAN REVIEW REQUIRED
- BLOCKED
- UNKNOWN

## EXACT NEXT ACTION

One concrete action.

## EXECUTION PROMPT

Provide the next copy-paste-ready prompt whenever another execution is required.

---

# 16. FINAL COMMAND

**Do not call it done until it is proven.**

**GITHUB FIRST. SOURCE-LOCK. RENDER FOR REAL. ASK WHY THIS IS NOT A 10. REPAIR ROOT CAUSES. RE-RENDER. VERIFY AGAIN. LEARN. FREEZE.**
