# 🔱 NayaPOWER Intelligent Hub — Official Master Plan

**STATUS:** CANONICAL DESIGN / CONTRACTS ESTABLISHED / KERNEL IMPLEMENTED / UI NOT YET BUILT
**DATE:** 2026-08-30

## North Star

Create a beautiful, privacy-first Intelligent Hub through which a human can connect their sovereign Superbrain, choose what wisdom to contribute, and receive relevant collective intelligence — without surrendering their private Superbrain.

> **Connect the Superbrain. Preserve sovereignty. Contribute wisdom. Compound intelligence.**

## NayaNET Level 1 integration contract

**CANONICAL:** `SUPERBRAIN/NAYANET-LEVEL-1-IDENTITY-HUB-COMMUNICATION-PSI-CONTRACTS.md`

NayaNET Level 1 is the intelligence-first product/network layer around the Intelligent Hub. It defines the semantic contracts for:

- canonical NayaNET Identity;
- private real identity vs network-facing Smart Name/Alias;
- Smart Link, Intelligent Hub ID, Smart Mail ID, and ambassador attribution as derived identity projections;
- personal Naya sovereignty and cross-Naya boundaries;
- Human↔Naya, Human↔Human, Naya↔Naya, and multi-Naya Intelligence Spaces;
- canonical Note Event usage;
- Intelligent Feed as a distribution/projection surface rather than memory authority;
- PSI as the intelligence authority/projection layer where established by NayaPOWER;
- authorized collective propagation;
- privacy, provenance, authorization, idempotency, and truth boundaries;
- the Level 1 scope boundary excluding media/social publishing infrastructure by default.

This contract is intentionally an integration layer. Existing NayaPOWER canonical Note Event, Smart Notes/CIS, Intelligent Hub, and Collective Intelligence contracts remain authoritative for their specific implementation schemas.

### Identity law

> **One canonical identity → multiple authorized representations.**

A user's private real name is never the default network identity. The Smart Name/Alias is the default network-facing identity. Smart Link, Intelligent Hub ID, Smart Mail ID, and ambassador attribution derive from the same canonical identity and must not become competing identities.

### Intelligence law

> **ONE SMART NOTE ACTION → ONE CANONICAL EVENT → MULTIPLE AUTOMATIC PROJECTIONS.**

Human, Naya, Machine, Intelligent Feed, PSI, and collective representations are projections/consequences of the canonical event, not independent memory silos. Downstream failure must not create a duplicate canonical event.

### Level 1 product law

> **NayaNET Level 1 connects, preserves, organizes, exchanges, and compounds intelligence. It does not require a media-sharing network.**

Public image/video publishing may be introduced as a later NayaNET level without becoming a Level 1 dependency.

## Architecture decision

The Intelligent Hub is a first-class NayaPOWER system. Its stable interfaces are defined before the Hub UI so Naya Power Player, MAXIS, future Superbrains, and the Collective can integrate without rebuilding the foundation.

### The three first-class contracts

1. `SUPERBRAIN/INTELLIGENT-HUB-SUPERBRAIN-CONNECTION-CONTRACT.md`
2. `SUPERBRAIN/WISDOM-CONTRIBUTION-PROTOCOL.md`
3. `SUPERBRAIN/COLLECTIVE-INTELLIGENCE-EVENT-SCHEMA.md`

Machine-readable contract projections now live under `.naya/runtime/intelligent_hub_contracts/`.

## Connection architecture

```text
HUMAN
  ↓ authentication + explicit consent
INTELLIGENT HUB
  ↓ least-privilege connection
SUPERBRAIN ADAPTER
  ↓
SOVEREIGN SUPERBRAIN
  │
  └── optional authorized wisdom scope
          ↓
   WISDOM CONTRIBUTION PROTOCOL
          ↓
   VALUE EXTRACTION / GENERALIZATION
          ↓
   HUMAN REVIEW + PRIVACY / QUALITY GATE
          ↓
   COLLECTIVE INTELLIGENCE EVENT
          ↓
   COLLECTIVE CHAIN / INTELLIGENCE FEED
          ↓
   RELEVANT COLLECTIVE WISDOM
          ↓
   PARTICIPATING SUPERBRAINS
```

## GitHub role

GitHub remains a canonical engineering/source substrate. A GitHub-backed Superbrain should connect through a Naya Intelligent Hub GitHub App with least-privilege repository selection. A fork remains an optional installation/ownership mechanism, not a collective synchronization mechanism.

## Privacy law

The collective does not synchronize repositories or personal memories. Collective Intelligence Events contain generalized reusable wisdom and explicitly exclude contributor identity and raw private source material. Internal consent/audit records may exist for legitimate operational needs, but identity is not part of the collective intelligence object.

## Human agency

Participation is opt-in. The contributor chooses scope and sees the proposed extracted wisdom before publication. They can edit, reject, or keep it private. Collective knowledge can be reviewed, applied, or ignored.

## Intelligence Feed

The running intelligence update surface is called the **Intelligence Feed**. It communicates meaningful collective/system learning, decisions, verification state, and next actions while canonical Note Events remain the underlying memory authority.

The existing `SUPERBRAIN/AI-BOOT/AI-OPERATING-FEED.md` remains the AI/session operational handoff stream. It must not be confused with a new competing memory store. The Intelligence Feed concept is a product/network projection of verified intelligence, backed by canonical events.

## Personal → Collective → Personal flywheel

`LEARN → CONTRIBUTE → COLLECTIVE LEARNS → RECEIVE RELEVANT WISDOM → LEARN MORE`

This is the intended collective-intelligence flywheel.

## Kernel checkpoint

The first provider-neutral kernel is implemented at `.naya/runtime/intelligent_hub_kernel.py`.

It currently proves:

- authenticated connection binding
- explicit, separately revocable wisdom-contribution consent
- least-privilege capability declaration
- human approval before publication
- minimum-necessary contribution intake
- rejection of raw/private-source fields
- deterministic privacy screening for common identifiers, repository URLs, and credential patterns
- duplicate detection
- canonical Collective Intelligence Event construction and validation
- anonymous collective projection with contributor identity excluded
- Intelligence Feed publication/retrieval
- event acknowledgement
- connection revocation

The reference authentication implementation is deliberately a test fixture. Production provider authentication must be supplied by a provider adapter (for example, a GitHub App installation) and must never require unrestricted repository access.

## Product sequence

1. Establish and verify the three contracts. **DONE**
2. Build the Hub connection layer. **KERNEL IMPLEMENTED**
3. Implement GitHub App authorization and selected-Superbrain connection.
4. Implement contribution scope and consent UX.
5. Implement wisdom extraction and privacy/quality gate.
6. Emit Collective Intelligence Events and Intelligence Feed updates.
7. Implement collective retrieval/feedback into participating Superbrains.
8. Build the polished Hub UI around the proven contracts.
9. Connect Naya Power Player and MAXIS as first application consumers.
10. Prove end-to-end privacy, consent, contribution, retrieval, revocation, and correction/supersession behavior.

## Non-negotiables

- No repository-to-repository synchronization as the collective model.
- No default unrestricted Superbrain access.
- No pasted GitHub credentials/tokens as the normal UX.
- No identity in collective intelligence objects.
- No publication without explicit contribution authorization.
- No unverified knowledge presented as established truth.
- No competing personal-memory store outside the canonical Note Event architecture.

## Success condition

A person can connect a Superbrain, keep private intelligence private, deliberately contribute a useful piece of wisdom, see exactly what will be shared, publish it with consent, and later receive useful collective intelligence — while the Collective gains reusable wisdom without gaining ownership of the person's life or Superbrain.
