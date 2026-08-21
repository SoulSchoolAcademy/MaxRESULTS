# MAXESS E02 — Surgical Edit Guardrail

## Purpose

Prevent any future E02 repair from replacing, compressing, regenerating, or structurally rewriting a known-good Groove artifact when the requested change is surgical.

## Mandatory Procedure

1. **GitHub first.** Read the current E02 source and its blob SHA before changing anything.
2. **Use the user's working Groove artifact as the visual source** when the user supplies a known-good Groove version.
3. **Preserve the embed contract.** E02 remains a self-contained `<section id="maxess-e02-v2">` Groove embed. Never convert it into a standalone `<!doctype html>`, `<html>`, `<head>`, or `<body>` document unless the source artifact itself is explicitly changed by contract.
4. **No compression or beautification.** Preserve source formatting, comments, section structure, CSS, HTML, and responsive rules unless the requested change requires them to change.
5. **Surgical diff only.** Before committing, compare the proposed file against the known-good source. Any large deletion, line-count collapse, major byte-count change, or unrelated structural rewrite is an automatic STOP condition.
6. **No demo data in production behavior.** E02 must consume `window.MAXESS_RESULT` / `MAXESS_RESULT_V1` and listen for `maxess:result-updated` and `MAXESS_RESULT_READY`. If a real result is unavailable, never invent a score.
7. **Preserve the five canonical dimensions:** Direction, Communication, Evaluation, Iteration, Systems Thinking.
8. **Animation contract:** Orb breathing is exactly `6s ease-in-out infinite`.
9. **Validate syntax before delivery.** JavaScript must pass a syntax check. HTML structure must retain the original section wrapper and five-dimension structure.
10. **Re-fetch after mutation.** Verify the committed blob, commit SHA, diff, and critical contract strings after every write.
11. **Runtime honesty.** Source verification is not browser/Groove verification. Report `VERIFIED` and `RUNTIME VERIFIED` separately.
12. **Never hand the user a replacement artifact after a failed verification loop.** Repair first, re-check, then deliver.

## Automatic STOP Conditions

- Source shrinks dramatically compared with the known-good artifact.
- A large percentage of lines are deleted without explicit authorization.
- `<section id="maxess-e02-v2">` disappears.
- The five-dimension DOM is replaced by generated/minified markup.
- E02 becomes a standalone HTML document.
- Static demo scores become the authoritative source.
- `window.MAXESS_RESULT` bridge disappears.
- The 6-second breathing contract changes.
- The resulting source has not been re-fetched after commit.

## Failure Lesson

A valid-looking replacement is not equivalent to the production artifact. For E02, preservation of the Groove embed, visual source, responsive behavior, and existing structure is part of correctness. A smaller file is not an improvement when it destroys the artifact's contract.
