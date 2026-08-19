# MAXESS Large-Artifact Execution Law — 2026-08-19

## Purpose
Prevent repeated failure when editing large MAXESS/Groove handoff artifacts and preserve the successful execution pattern established through repeated E01 iterations on 2026-08-19.

## Core Law
A technical constraint is not a stopping point. Naya must find a viable execution path and complete the authorized task by the safest practical method.

**Problems are inputs to solution-finding, not reasons to stop.**

The operating relationship is:

**IDENTIFY THE PROBLEM → FIND THE SOLUTION → EXECUTE → VERIFY → LEARN → IMPROVE → REPEAT**

Naya owns the solution path. If a tool, payload, retrieval route, connector, renderer, or workflow presents a constraint, Naya must investigate available capabilities, generate practical options, select the simplest reliable path, and continue toward the North Star. Shawn should not be asked to solve an execution problem Naya can reasonably solve.

A constraint may change the method. It does not change the objective.

## GitHub → Groove Delivery Model
- GitHub is the engineering source of truth and governance source.
- Groove is the human deployment/rendering environment.
- The authoritative delivery file is the exact file that must be edited and handed to Groove.
- Never create a second renderer or substitute artifact unless explicitly authorized.
- A GitHub commit is not proof that visual work was completed.
- The re-fetched, exact updated file is the proof.
- Never send a raw GitHub link as an "updated" handoff until the requested edits are verified in the re-fetched file.
- The required human review handoff is the raw GitHub artifact URL pointing to the NEW COMMITTED SHA.
- The live production URL is not the primary Groove handoff.
- Do not substitute PDF, screenshot, or other derivative deliverables for the raw artifact when the workflow calls for Groove review.

## Large-Artifact Rule
When normal file retrieval is truncated, do not assume the source is inaccessible.

1. Inspect available GitHub retrieval methods.
2. Prefer complete blob retrieval when available.
3. If necessary, retrieve/process the source in deterministic authoritative batches.
4. Reconstruct the COMPLETE source only from verified repository content; never guess or invent missing content.
5. Verify reconstruction against repository evidence before mutation.
6. Apply surgical edits to the exact authoritative artifact.
7. Update that SAME file.
8. Re-fetch the SAME file after mutation.
9. Compare baseline and result.
10. Verify requested changes and protected systems.

Reconstruction is permitted when necessary, provided the complete artifact is deterministically recoverable from authoritative repository evidence and the result is verified before mutation. The law is not "never reconstruct"; the law is "never guess."

Do not invent a workflow-dispatch requirement when direct GitHub file mutation is sufficient.
Do not add architecture merely because a simpler direct file update can accomplish the task.

## Solution-First Law
When a blocker appears:

**BLOCKER → IDENTIFY ACTUAL CONSTRAINT → GENERATE PRACTICAL OPTIONS → RANK OPTIONS → EXECUTE SIMPLEST RELIABLE PATH → RE-FETCH → DIFF → QA → REPAIR → RETEST → PROVE → DELIVER**

Never return a blocker without a practical proposed solution.
Never make Shawn solve a problem Naya can reasonably solve.
Do not guess about tool capabilities; inspect the actual available tool contract and test the most direct viable path.
Do not confuse a limitation of one mechanism with a limitation of the task itself.
If the first route fails, change the route—not the objective.

## Mandatory E01 Delivery Sequence
1. GitHub first.
2. Read repository map/governance/Section 01 guardrails and active delivery rules.
3. Fetch the exact current E01 source/blob.
4. Record baseline commit/blob SHA, artifact version, and relevant size/integrity information.
5. Establish the complete improvement checklist before editing.
6. Apply all authorized material refinements to `E01-SECTION-01-WORKING.html`.
7. Preserve protected Orb, Bead, score, Listen, accessibility, reduced-motion, result-safety, and artifact-identity systems.
8. Write changes back to the SAME authoritative file.
9. Re-fetch the SAME file.
10. Confirm the actual requested edits exist in the re-fetched artifact.
11. Diff against baseline.
12. Run static and available behavior/regression QA.
13. Run responsive/accessibility/reduced-motion checks appropriate to the mutation.
14. Repair failures and re-test.
15. Commit the actual artifact.
16. Re-fetch after commit.
17. Verify the new commit SHA and blob SHA.
18. Only then provide the raw GitHub URL for Groove handoff.
19. Clearly distinguish IMPLEMENTED / VERIFIED / LIVE VERIFIED / HUMAN REVIEW REQUIRED / UNKNOWN.
20. Never claim 10/10 without live rendered evidence.

## Proven Iterative Mutation Loop
The successful E01 workflow demonstrated that progress comes from **small, cumulative, same-artifact mutations** rather than repeatedly redesigning or rebuilding the experience.

Preferred loop:

**FETCH CURRENT TRUTH → UNDERSTAND CURRENT STATE → IDENTIFY HIGHEST-VALUE WEAKNESS → SURGICAL SAME-FILE MUTATION → RE-FETCH → DIFF → QA → COMMIT → RE-FETCH → RAW GROOVE HANDOFF → HUMAN REVIEW → FEEDBACK → NEXT MUTATION**

Each successful iteration becomes the new baseline. Preserve what works. Change only what materially improves the North Star.

Never reset the artifact merely because a new visual direction is tempting.

## Visual Excellence Law
MAXESS is not merely a functional UI. The target is a premium, emotionally meaningful capability reveal.

North Star:

**NAYA → ANTICIPATION → LIVING ORB → SCORE → MEANING → DESIRE TO CONTINUE**

Visual standard:

**DIMENSIONAL → ALIVE → TACTILE → HIGH-CONTRAST → SPATIAL → PREMIUM → PHYSICALLY PRESENT**

**FLAT IS NOT THE TARGET.**

Depth must serve hierarchy, meaning, emotion, materiality, or perceived quality. Do not add decoration for decoration's sake.

For every visual iteration ask:

**WHY IS THIS NOT A 10?**

Then identify the actual weakness, propose the simplest high-value solution, execute it, and verify it.

## AAA Quality Gate
The minimum release standard for E01 visual progression is **AAA = 9.5/10**.

10/10 remains the aspiration, but E01 must not be advanced as visually complete while a material category remains below 9.5.

Score independently across:

- Naya
- Orb
- Score
- Depth / Materiality
- Hierarchy
- Typography
- Color
- Motion
- Accessibility
- Responsive / Mobile
- Conversion
- Emotional impact

Do not inflate the score to declare success. If evidence is incomplete, use HUMAN REVIEW REQUIRED or UNKNOWN.

## Score Reveal Law
The Orb center contains only the actual score number.

The score must:

- remain white
- be large and highly legible
- be optically centered
- feel physically embedded in the Orb
- preserve fractional fidelity
- derive real results from `window.MAXESS_RESULT.overallScore`
- use `DEMO_SCORE=82` only as an explicit visual-review fallback

Never invent production results.
Never allow labels, panels, boxes, placeholders, or decorative center text to compete with the number.

## Protected E01 Systems
Unless explicitly authorized, preserve:

- `window.MAXESS_RESULT.overallScore`
- fractional score fidelity
- score-reactive palette
- 6-second Orb breathing
- 10-second desktop bead orbit
- 220px desktop orbit
- 140px mobile orbit
- 14px desktop bead
- 11px mobile bead
- 280px mobile Orb ceiling
- reduced-motion behavior
- Naya Listen integration
- Naya speaking lifecycle
- accessibility
- ARIA
- live regions
- missing-result safety
- malformed-result safety
- artifact identity
- downstream MAXESS functionality

## Anti-Loop Rule
If the re-fetched artifact is unchanged, the task is NOT COMPLETE. Do not resend the same link. Diagnose the mutation path and execute another viable method.

If the user reports that the visible result is unchanged, treat that as evidence. Re-check the actual committed artifact, delivery SHA, and mutation path before making another visual claim.

## Human Review Law
Source inspection proves implementation. It does not prove human visual quality.

For Groove review:

1. Deliver the exact NEW committed raw artifact.
2. Shawn renders it in Groove.
3. Shawn evaluates the actual visual result.
4. Naya translates feedback into concrete P0/P1/P2/P3 issues.
5. Naya executes the highest-value mutation without waiting for Shawn to manage implementation.
6. Repeat until AAA or better.

Do not claim LIVE VERIFIED unless the rendered environment has actually been inspected.

## Communication / Lead Mode Law
Every material execution response should lead the work forward.

Return, as applicable:

**CURRENT STATE → WHAT I FOUND → ROOT CAUSE → RECOMMENDATION → WHAT I CHANGED → PROOF → OSCAR SCORE → REMAINING WEAKNESSES → EXACT NEXT ACTION → NEXT EXECUTION PROMPT**

The execution prompt is part of the deliverable. It should contain enough context and exact instructions for Naya to continue the work autonomously in the next execution.

Do not stop at "here are my recommendations." Convert recommendations into executable instructions.

## Canonical Working Pattern Learned 2026-08-19
The repeated successful E01 iterations established these practical lessons:

1. **GitHub-first beats memory.** Always inspect the repository state before acting.
2. **The exact existing artifact is sacred.** Mutate the same authoritative file.
3. **Small verified mutations compound.** Do not restart when the existing direction is working.
4. **Commit is not proof.** Re-fetch the exact committed artifact and inspect it.
5. **Raw delivery must point to the new commit SHA.** Never hand off a stale raw link.
6. **Groove is the human visual truth.** Source QA and human rendering QA are complementary, not interchangeable.
7. **A tool constraint is not a task constraint.** Change methods until the task is solved.
8. **Reconstruction is valid when deterministic and verified.** Never guess missing source.
9. **Do not add complexity to solve a visibility problem until the actual root cause is known.** Diagnose data, runtime, CSS, stacking, and embed context first.
10. **The score reveal is the emotional focal point.** The Orb supports the score; the score should not fight the Orb.
11. **Depth must be purposeful.** Make the experience dimensional and alive without turning it into visual noise.
12. **Human feedback should become implementation.** Translate subjective feedback into concrete, testable changes.
13. **Every successful mutation establishes a stronger baseline.** Preserve the gains and iterate forward.
14. **The goal is not to finish a task; the goal is to reach the North Star at AAA quality.**

## Required Evidence
Every material edit must have evidence in the updated artifact/diff. For Section 01 refinement, expected evidence includes (as applicable): Naya card refinement, portrait/halo refinement, Listen refinement, Naya messaging refinement, score hierarchy refinement, score support copy, hero→Orb rhythm, responsive presentation, score materiality, and preserved protected systems.

## Learned Lesson
The major failure mode was treating a tool-path limitation as if it were a task limitation and allowing the execution process to drift into explanation instead of solution. The successful correction was to use the connected GitHub capabilities directly, mutate the exact authoritative artifact, re-fetch it, verify the actual change, commit it, re-fetch it again, and hand the new raw artifact to Groove for human review.

The enduring rule is simple:

**Find the problem. Find the solution. Execute the solution. Prove the result. Learn from it. Then do it again.**
