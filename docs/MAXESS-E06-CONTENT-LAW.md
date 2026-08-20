# MAXESS E06 — Content Law

**Status:** ACTIVE
**Scope:** E06 — Naya Supercharger
**Branch:** `maxess-results-v21-working`

## Purpose

This document preserves the content decisions that must govern the E06 redesign so they are not lost between iterations.

## Core Content Law — WHAT'S IN IT FOR ME?

The visitor does not primarily care about the internal architecture of Naya. They care about the benefit to themselves.

Every E06 capability board must answer:

> **What does this do for me?**

Each of the seven systems must present **five strong, understandable user benefits**. Benefits should explain how the capability helps the user, what problem it removes, what becomes easier, what becomes possible, or what improves.

Do not lead with technical implementation language when a human benefit can be stated instead.

## The Seven Systems — LOCKED NAMES

1. **Naya Personality**
2. **Naya Brain**
3. **Naya Notes**
4. **Naya Lead Mode**
5. **Naya Law**
6. **Naya Scorecarding**
7. **Naya Language**

### Naming distinction

Do **not** use `Laws + Procedures` as the E06 system name.

**Naya Law** is the correct name.

Law, policy, and procedure are distinct concepts and must not be casually collapsed into one product label.

## Naya Language — Required Meaning

Naya Language is not merely a glossary feature.

It provides a defined language/reference system so AI can understand the intended meaning of important terms instead of guessing among multiple possible interpretations.

The system can include a directory/glossary that defines what specific words, phrases, concepts, commands, standards, or internal terminology mean in the user's world.

### User benefit

The user can communicate more precisely with Naya and reduce ambiguity because important terms have explicitly defined meanings.

The language definitions can also be made available as a reference for other AI systems, allowing the user's terminology to remain understandable beyond a single AI conversation or model.

The benefit language should communicate ideas such as:

- Less explaining what you mean.
- Less ambiguity and fewer incorrect interpretations.
- Important words can carry the user's intended meaning.
- Complex concepts can be activated through shared terminology.
- The user's defined language can be portable across AI systems.

## Customization Law

The seven systems are delivered as a highly tuned, optimized starting system designed to produce maximum useful results to the best of the system's ability.

**They are not immutable.**

The user can custom-tune the system for themselves.

Where supported, the experience should explicitly communicate that the user can ask Naya to update or refine relevant system elements, for example:

- `Naya, update my policy to...`
- `Naya, update my law to...`
- `Naya, update my language definition for...`
- `Naya, change this rule so that...`
- `Naya, refine how you handle...`

The exact command syntax is illustrative, not a hard-coded UX requirement. The important product promise is that the user can **tell Naya what should change and have the system evolve to fit them better**.

## Positioning

The system should be presented as:

**Pre-tuned for maximum results. Customizable for maximum personal fit.**

The user receives a strong default operating system and can progressively tune it to their own preferences, terminology, standards, workflows, and needs.

## Board Content Pattern

Each Maxis board should generally follow this hierarchy:

1. **Naya system name**
2. **One-line human benefit**
3. **Five user-benefit points**
4. Optional supporting explanation: what the system actually means/how it works

The technical mechanism comes after the benefit, not before it.

## Example — Naya Language

**Naya Language**

*Give your AI a shared vocabulary for how you think and work.*

Potential benefit framing:

- **No more guessing what you mean.** Define important terms so Naya understands them the way you intend.
- **Your words become more powerful.** A defined phrase can represent a larger concept, process, or way of working.
- **Different interpretations get reduced.** Important terminology has an explicit meaning instead of relying on AI assumptions.
- **Your language can travel with you.** Definitions can provide a reference that other AI systems can understand too.
- **You spend less time explaining yourself.** Once the language is defined, complex intent can be communicated faster.

## Maxis Visual Law

E06 must use the **actual supplied Maxis visual components/code** where applicable.

Do not invent substitute icons, bullet systems, board structures, or a generic approximation of the Maxis design language when the real components are available in the repository.

The E06 content should be adapted to the Maxis visual system rather than creating a separate visual system and merely making it look premium.

## E06 Conversion Sequence

The page should create this progression:

1. **Whoa. That's Naya.** — Naya is the unmistakable visual hero.
2. **Oh... that's what the Supercharger activates.** — The seven manifestations become immediately understandable.
3. **Oh damn. I want those things.** — The Maxis boards translate each system into tangible personal benefits.

## QA Content Test

Before E06 is considered complete, ask of every bullet:

> **Does this clearly tell the visitor what's in it for them?**

If not, rewrite it.

Also verify:

- Names are exact and consistent.
- `Naya Law` is used, never `Laws + Procedures`.
- `Naya Language` is explained as a shared, defined language/reference system, not merely documentation.
- Customization is communicated as a genuine benefit.
- The user understands that the system is optimized by default but can be tuned further for their individual needs.
- Technical explanations support the benefit rather than replacing it.
