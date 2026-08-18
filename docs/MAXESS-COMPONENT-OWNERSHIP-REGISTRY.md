# MAXESS COMPONENT OWNERSHIP REGISTRY

## Purpose

This registry answers one question before every edit:

> Where is the single active owner of the thing the user wants changed?

Fast editing depends on one visible owner per component.

## Authoritative branch

`maxess-results-v21-working`

## Global rules

- `window.MAXESS_RESULT` is the only authoritative production result source.
- The V21 canonical renderer owns the visible V21 Results presentation unless explicitly marked runtime-owned.
- Legacy V11/V12/V13/V18/V20 code may remain for preservation/recovery, but it is not an active visible owner when hidden or superseded.
- Micro-edits must patch the smallest safe owned source region.
- Do not rewrite the whole page for a local change.

## Active component map

| Component | Section | Active owner | Primary selector / anchor | Typical fast edits |
|---|---|---|---|---|
| Naya Arrival | 01 | V21 canonical renderer | `.v21-naya`, `#v21-naya-introduction` | copy, avatar, spacing, button, typography |
| Signature Score Orb | 02 | V21 canonical renderer | `.v21-score-orb`, `.v21-score-core` | size, glow, colors, typography, motion |
| Score Meaning | 03 | V21 canonical/runtime | `#what-it-means`, `.v21-meaning-section` | copy, stage, spacing, visual emphasis |
| Personalized Report | 04 | V21 canonical renderer | `.v21-report` | copy, layout, emphasis, spacing |
| AI Fingerprint | 05 | V21 runtime | `.v21-fingerprint-panel`, fingerprint renderer | radar geometry, labels, colors |
| Five Dimensions | 06 | V21 runtime | `.v21-dims`, `.v21-dim` | orb size, score style, labels, detail surface |
| Pattern | 07 | V21 canonical renderer | `.v21-story` / pattern section | layout, visual relationships, copy |
| Strength | 08 | V21 canonical renderer | strength section / `.v21-card` | emphasis, copy, visual treatment |
| Lever | 09 | V21 canonical renderer | lever section / `.v21-purple` | emphasis, copy, CTA |
| Next Move | 10 | V21 canonical renderer | `.v21-next-grid`, `.v21-next-card` | action cards, spacing, copy |
| 18 Naya Masters | 11 | V21 canonical renderer | `.v21-masters`, `.v21-master` | ordering, relevance, CTA, card treatment |
| Naya in Practice / Media | 12 | Runtime/preserved media owner | `#v21-video-host`, Naya media region | video, Naya walkthrough |
| Playground | 13 | Runtime/preserved Playground owner | `#naya-playground`, `#v21-playground-host` | placement, spacing, presentation |
| Closing Naya | 14 | Runtime/Naya owner | `.naya-final-signature`, final Naya region | copy, image, spacing |
| Final Continuation CTA | 15 | V21 canonical renderer | `.v21-cta-final`, `.v21-cta-link` | copy, color, size, destination |

## Ownership resolution law

Resolve in this order:

1. Exact component selector.
2. Section owner.
3. Canonical renderer source anchor.
4. Runtime owner.
5. Legacy code only for preservation/recovery.

Never edit the first matching string in the entire repository.

## Fast-edit safety

A micro-edit is safe when:

- the target owner is unique;
- the requested property is in `editable fields` for that owner;
- the patch is local;
- syntax validation is available;
- the resulting diff is smaller than a full-renderer rewrite.
