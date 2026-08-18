# MAXESS FAST EDIT SYSTEM

## North Star

A natural-language request must become:

`LOCATE → PATCH → VALIDATE → LOCAL QA → COMMIT → REPORT`

for a small change without rebuilding the entire project mentally.

## Edit modes

### MICRO

Examples: color, copy, spacing, size, position, button label.

Target: 1–5 minutes.

Run only owner resolution, targeted patch, syntax validation, local QA, and checkpoint.

### SECTION

Examples: redesign Naya Arrival or reorganize Score Meaning.

Target: 5–20 minutes.

Run section contract, coherent patch, local regression, checkpoint.

### RELEASE

Examples: data contract, architecture, major visual system, new runtime behavior.

Run full build, full QA, regression, PDF, and release validation.

## Micro-edit transaction

1. Read `docs/MAXESS-COMPONENT-OWNERSHIP-REGISTRY.md`.
2. Resolve one active owner.
3. Refuse ambiguous ownership.
4. Snapshot the target file hash.
5. Apply the smallest safe patch.
6. Validate the target language.
7. Run the smallest applicable section check.
8. Require a source hash delta.
9. Require a non-empty diff.
10. Commit immediately to the authoritative branch.
11. Write one fast-edit ledger record.

## Never

- rebuild the whole page for a CSS/text-only micro-edit;
- modify a legacy hidden owner when an active owner exists;
- stash a verified micro-edit as normal workflow;
- declare success when the source hash is unchanged;
- run release QA just because a button color changed;
- allow generated tooling to overwrite a human-approved checkpoint.

## Escalation

Escalate MICRO → SECTION when:

- more than one active owner is found;
- the edit changes DOM structure;
- the edit affects multiple sections;
- the edit changes behavior rather than styling/copy;
- local QA cannot isolate the risk.

Escalate SECTION → RELEASE when:

- data contract changes;
- renderer ownership changes;
- global design tokens change;
- runtime initialization changes;
- preservation boundaries change.

## Success definition

Five consecutive real micro-edits with:

- source delta;
- valid syntax;
- targeted local QA pass;
- committed checkpoint;
- no unrelated source rewrite.

Only then do we claim the Fast Edit System is proven.
