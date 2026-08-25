# Naya Power — AI Operating Feed

This is the shared operational handoff stream for every AI/session entering the Superbrain. It is not the canonical memory database; it is the fast human/AI-readable change stream that tells a fresh AI what changed, why, what was verified, and what to read next.

## Feed rules

1. Append; do not rewrite history.
2. One entry per meaningful operating change.
3. Include date/time, actor/session if known, event/commit, what changed, verification state, affected canonical paths, and next action.
4. Link to readable notes and receipts whenever available.
5. Never put secrets or private credentials here.
6. Never treat the feed as stronger evidence than canonical events/evidence.
7. If an operating rule changes, create/update the appropriate Master Note and canonical protocol; the feed announces the change.
8. A new AI reads the newest entries first, then follows links into canonical sources.

## 2026-08-25 — Superbrain federation/boot architecture

**Status:** IMPLEMENTED IN REPOSITORY

**What changed:** Established a mandatory AI boot entry point and an append-only AI Operating Feed. The boot file defines the source-of-truth hierarchy, object routing, human-service receipt requirement, privacy boundary, and perpetual operating loop.

**Why:** A new chat/model/session must be able to enter the repository without prior conversational context and become operationally current quickly. The system must behave like a continuously maintained AI handoff layer, not a collection of disconnected documents.

**Canonical entry:** `SUPERBRAIN/AI-BOOT/START-HERE.md`

**Build protocol:** `SUPERBRAIN/SUPERBRAIN-BUILD-PROTOCOL.md`

**Current design decision:** Each personal Naya Power remains private. Future NayaNET connectivity is federation, not automatic pooling of raw personal memory.

**Next:** Build automated feed/index refresh and then implement controlled federation contracts for explicit knowledge exchange.

---

## Entry template

### YYYY-MM-DD HH:MM — <change title>

**Status:** VERIFIED / PENDING / FAILED

**Event:** `<event_id>`

**What changed:**

**Why it changed:**

**Verified by:**

**Canonical paths:**

**Readable note:**

**Receipt:**

**Next action:**
