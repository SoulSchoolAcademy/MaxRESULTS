# 🔱 Naya Note — NayaNET E-Series Architecture + Design Language Lock

**Date:** 2026-08-31  
**Status:** CANONICAL / LOCKED  
**Related work:** E01 Ultimate Entrance → E02 → E03 → E04 continuation architecture

## Decision

NayaNET Intelligent Hub experiences are now treated as an **E-Series**: E01, E02, E03, E04 and future chapters of one coherent Naya world.

Each E is independently deployable and independently verifiable. The default connection between E experiences is URL navigation plus a lightweight shared session/identity contract. Direct DOM/JavaScript coupling and iframe-internal dependencies are prohibited by default.

Groove is the outer composition/orchestration layer. Cloudflare-hosted E artifacts are the independently deployable experience layer.

## Why this decision was made

A single giant embedded page would make later work risky: changing E02 could regress E01, deployment would become monolithic, and human-approved scenes would be difficult to protect.

Independent E artifacts allow:

- E01 to be locked after human approval;
- E02 to evolve without rewriting E01;
- failures to remain isolated;
- each experience to receive its own QA and deployment evidence;
- the entire network to retain one shared design language.

Embedding remains available for exceptional modules that genuinely need to coexist on one screen, but it is not the default architecture.

## Design-system decision

The **NayaNET Experience System v1.0** is now canonical at:

`.naya/design/NAYA-EXPERIENCE-SYSTEM.md`

It governs:

- visual world;
- typography;
- color;
- spatial geometry;
- Naya presence/state language;
- surfaces;
- motion;
- responsive behavior;
- interaction language;
- navigation/continuity;
- accessibility;
- non-regression;
- the canonical button system.

## Button lock

Buttons are no longer to be redesigned independently inside each E.

The system defines Primary, Secondary, Ghost/Text, Continue/Next, Back, and Disabled/Processing families. New button variants require an explicit design-system extension rather than local invention.

The user's requested standard is: **buttons must look premium, dimensional, intentional and at least as strong as the approved NayaNET reference—not flat, generic, or SaaS-template-like.**

## E01 role

E01 is not merely a webpage. It is the first chapter and visual foundation of the NayaNET Intelligent Hub / Naya Power entrance to the internet.

E01 establishes the shared visual, interaction, motion, Naya-presence, and navigation language that E02+ inherit.

## Non-regression rule

Once a scene or component is human-approved, it becomes a protected baseline. Later feedback must modify only the rejected design unit unless a deliberate system-level change is explicitly approved.

## Evidence

Canonical design-system commit:

`5261c1926dbd93ec4c9b362374c7cde728f1399f`

This note is the institutional memory for the architectural/design decision so future Naya instances do not re-litigate or accidentally undo it.
