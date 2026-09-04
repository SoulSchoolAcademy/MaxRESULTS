# 🔱 Naya Note — 2026-09-04 Daily Intelligence Lessons

**Status:** CANONICAL OPERATIONAL LEARNING
**Project:** NayaPOWER × MAXIS × NayaNET
**Source:** live NayaPOWER/MAXIS repository state, recent commit history, prior daily report, and current Primary Intelligence Hub.

## Core lesson

Smart Note integrity requires more than matching an event identifier. The claimed operation must match the persisted canonical Note Event across `event_id`, `effective_at`, and aligned `representations`.

## Why it matters

A Smart Note is one underlying intelligence event with multiple aligned views. If the claim can diverge from persisted time or representation payload, downstream receipts, Smart Links, PIS/CIS propagation, and successor retrieval can become untrustworthy even when the event ID looks correct.

## Durable operating rule

Treat canonical-operation validation as an integrity gate before delivery. Add adversarial tests whenever the contract changes. Prove the real caller path invokes the gate. Never treat source-level tests as runtime or production proof.

## Compounding delta

Previous learning established the need for Smart Links and separate propagation evidence. Today adds the missing binding rule: the delivered claim must be payload-consistent with the persisted event, not merely refer to it.

## Required follow-through

`CLAIM → ENFORCE → PERSISTED MATCH → RETURN PAYLOAD → DEREFERENCE SMART LINKS → PROPAGATE → RECEIPTS`

## Status

Implemented in source; adversarial suite added; runtime and production proof remain UNKNOWN until an exact-SHA execution environment produces evidence.
