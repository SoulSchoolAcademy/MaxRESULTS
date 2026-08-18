# MAXESS AAA PRIORITY MATRIX

Status: AUTHORITATIVE EXECUTION PRIORITY
Version: V21

## North Star

Get every meaningful MAXESS section to an evidenced AAA state with the least wasted work, while preserving working functionality and continuously increasing the probability of a 9+ first-pass result.

## Priority law

Priority is dynamic.

At any moment:

Priority = Human Impact × Product Leverage × User Visibility × Dependency Value × Risk Reduction × Reuse Value

Execution must attack the highest combined-value work first.

Passing QA does not make a product item high priority. A visually important or user-critical unfinished section outranks another diagnostic or documentation task unless the latter is a release blocker.

## Current priority weights

| Priority | Workstream | Weight | Why now |
|---|---|---:|---|
| P0 | Section completion: 01–15 | 100 | Main North Star. The product must visibly move. |
| P0 | Canonical product source ownership | 100 | Prevents mutation from disappearing during rebuilds. |
| P0 | MAXESS_RESULT/data integrity | 100 | Nothing else matters if the result is wrong. |
| P0 | Hero / Orb / Naya | 100 | Highest visibility and emotional first impression. |
| P0 | Score meaning / report | 95 | Converts a number into useful understanding. |
| P0 | Fingerprint / five dimensions | 95 | Core signature of the assessment product. |
| P0 | Next Move | 95 | Converts insight into action. |
| P1 | Pattern / Strength / Lever | 90 | Makes the report genuinely interpretive and useful. |
| P1 | 18 Masters | 85 | Major value/continuation layer. |
| P1 | Media / Playground | 85 | Lower-page reliability and practice bridge. |
| P1 | Closing Naya / CTA | 80 | Conversion/continuation after value has been delivered. |
| P1 | Responsive / accessibility | 90 | Applies to every section and is required for release quality. |
| P1 | Performance / initialization | 85 | Prevents the lower-page loading and race problems we have already seen. |
| P1 | PDF / print | 75 | First-class product, but after core interactive experience is excellent. |
| P2 | QA tooling refinement | 60 | Important only when it verifies or blocks real product correctness. |
| P2 | Repair tooling refinement | 55 | Needed for safe execution, but never allowed to substitute for product work. |
| P2 | Documentation expansion | 40 | Useful only when it prevents recurrence or improves execution. |

## Immediate execution order

### Batch 1 — Highest value

1. Naya Arrival
2. Score / Orb
3. What Your Score Means

### Batch 2

4. Personalized Report
5. AI Fingerprint
6. Five Dimensions

### Batch 3

7. Pattern
8. Strength
9. Biggest Lever

### Batch 4

10. Next Move
11. 18 Naya Masters
12. Naya in Practice / Media

### Batch 5

13. Playground
14. Closing Naya
15. Final Continuation CTA

### Cross-section finishing

Responsive
→ Accessibility
→ Performance
→ PDF/Print
→ Deployment
→ Human review
→ Release

## Dynamic reprioritization

After each batch, rescore every section 0–10.

Then calculate:

Gap = 10 - Current Score

Next Priority = Gap × Weight × Dependency Factor × User Visibility

Highest next priority wins.

If a section is blocked by a material dependency, document the blocker and move to the highest-value unblocked section instead of waiting unnecessarily.

## Hard anti-loop rules

- Never spend an entire execution cycle on documentation if a product section can safely be improved.
- Never run the same QA chain repeatedly without changing the underlying owner of the failing requirement.
- Never treat a build-pass as product progress if the candidate hash and relevant source content did not change.
- Never treat an existing AAA/Nitro marker as proof of completion.
- Never allow a QA failure to stop safe product mutation; it may block release, not improvement.
- Every batch must produce either a material product delta or a documented material blocker.

## Evidence required for a section to become FROZEN

- source delta proven;
- visual target implemented;
- real data verified;
- interactions verified;
- responsive verified;
- accessibility verified;
- regression verified;
- no competing owner;
- Change Ledger updated;
- Smart Note recorded when a reusable lesson was learned.
