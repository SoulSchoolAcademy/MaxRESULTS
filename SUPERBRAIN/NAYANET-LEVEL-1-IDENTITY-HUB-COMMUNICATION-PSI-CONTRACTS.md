# NayaNET Level 1 — Identity, Intelligent Hub, Communication & PSI Contracts 🔱

**Status:** CANONICAL ARCHITECTURE CONTRACT  
**Version:** 1.0  
**Scope:** NayaNET Level 1 — Intelligence Foundation  
**Repository:** `SoulSchoolAcademy/NayaPOWER`  
**Authority:** NayaPOWER canonical architecture; implementation must not be inferred from this document where a more specific canonical runtime contract already exists.

---

## 0. Purpose

NayaNET Level 1 is the intelligence foundation of NayaNET.

It is **not** a media-sharing network by default. Its primary purpose is to help humans and their personal NayAs **connect, preserve, organize, exchange, compound, and act on intelligence**.

The visible experience should remain simple while the underlying architecture preserves identity sovereignty, privacy, continuity, authorization, provenance, and compounding intelligence.

> **NayaNET Level 1 exists to connect, preserve, organize, exchange, and compound intelligence — not to maximize media consumption.**

The delivery surface may be web, app, embed, or another interface. The architecture underneath is the product contract.

---

# 1. Non-Negotiable Architectural Laws

### L1 — Intelligence-first
Level 1 optimizes for useful intelligence, learning, communication, memory, and action. Image/video social infrastructure is out of scope unless separately authorized as a later level.

### L2 — Human sovereignty
The human owns their identity, context, Naya relationship, permissions, and consequential decisions. Naya assists; Naya does not silently assume human authority.

### L3 — Private real identity
A user's real/legal name is private account identity data. It is never the default network-facing identity.

### L4 — Smart Name is the default network identity
A user may choose a Smart Name / Alias / Alter Ego. The network-facing default is the Smart Name, not the private real name.

### L5 — One canonical identity
Smart Link, Intelligent Hub ID, Smart Mail ID, and ambassador attribution are projections/addresses derived from one canonical NayaNET Identity. They are not independent identities.

### L6 — One event, many projections
A meaningful intelligence capture creates one canonical Note Event. Human, Naya, Machine, Feed, PSI, and downstream projections must not become competing sources of truth.

### L7 — Authorization before propagation
Private intelligence does not become collective intelligence merely because it exists. Distribution, room participation, Naya-to-Naya exchange, and collective propagation require explicit policy/authorization.

### L8 — Provenance survives projection
Every derived intelligence representation must retain enough provenance to identify the canonical event/source, owner/scope, creation/update state, and verification status.

### L9 — UNKNOWN remains UNKNOWN
The system must never fabricate identity, capability, connectivity, message delivery, intelligence propagation, media availability, or verification state.

### L10 — Future levels do not contaminate Level 1
Public profiles, image/video publishing, public feeds, creator/media infrastructure, and richer social surfaces may be built later. They are not Level 1 dependencies.

---

# 2. Canonical Identity Model

A NayaNET identity has two fundamental identity domains:

```text
PRIVATE HUMAN IDENTITY
    ├── legal/real name
    ├── private account identifiers
    └── authentication/security data

NETWORK IDENTITY
    ├── Smart Name / Alias
    ├── Smart Link
    ├── Intelligent Hub ID
    ├── Smart Mail ID
    └── Ambassador Attribution
```

These domains MUST NOT be conflated.

## 2.1 Canonical NayaNET Identity

Conceptual contract:

```text
NayaNetIdentity {
  identity_id: immutable canonical identifier
  private_name: protected/private
  smart_name: network-facing alias
  smart_link: canonical user route/address
  intelligent_hub_id: canonical hub reference
  smart_mail_id: derived communication address
  ambassador_attribution: derived/referral identity
  naya_id: personal Naya relationship reference
  status: active | suspended | archived
  privacy_policy_version: explicit policy version
  created_at: timestamp
  updated_at: timestamp
}
```

Implementation may use different physical field names, but the semantic contract must remain recognizable.

### Identity invariants

1. `identity_id` is stable and not derived from display text.
2. `smart_name` is user-selectable subject to uniqueness, safety, and platform policy.
3. `smart_link` resolves to the user's authorized network destination.
4. `intelligent_hub_id` identifies the user's personal intelligence space, not a public social profile by default.
5. `smart_mail_id` is a communication address derived from the canonical identity.
6. Ambassador attribution must remain separate from permission to expose private identity.
7. Changing a Smart Name must not silently create a second human identity.
8. Historical attribution/provenance must remain resolvable where policy requires it.

---

# 3. Smart Name / Alias / Alter Ego Contract

The recommended onboarding pattern is:

> **Your real name stays private. Choose the name you want the network to know you by.**

The alias may be called **Smart Name**, **Alias**, or **Alter Ego** in the experience. The canonical semantic field is the network-facing identity.

### Default behavior

Unless a user explicitly authorizes disclosure:

- rooms show Smart Name;
- human-to-human communication shows Smart Name;
- Naya-to-Naya communication uses authorized identity representation;
- shared intelligence uses Smart Name;
- Smart Mail uses Smart Name/address;
- network discovery uses Smart Name;
- public/collective projections use Smart Name.

The real name is not a fallback display field.

### Privacy test

A Level 1 implementation fails if any normal network flow can accidentally reveal the private real name through:

- message headers;
- room membership;
- notifications;
- Smart Notes;
- feed entries;
- links/share previews;
- Naya-generated summaries;
- metadata exposed to another Naya;
- exports;
- search results.

---

# 4. Smart Link Contract

The Smart Link is the canonical human-facing network address derived from the NayaNET identity.

Conceptually:

```text
https://<nayanet-domain>/<smart-name>
```

The exact production hostname/routing is implementation-specific and must be verified before being represented as live.

The Smart Link may support, over time:

- identity/profile destination;
- Intelligent Hub entry;
- Smart Mail addressing;
- ambassador attribution;
- authorized invitation routing;
- future network services.

**Important:** a Smart Link is an address/projection of identity, not a replacement for the immutable canonical identity ID.

---

# 5. Intelligent Hub Contract

The Intelligent Hub is the user's personal intelligence command center.

It is not merely a profile page.

### Hub responsibilities

The Hub may provide authorized access to:

- personal Naya relationship;
- personal intelligence/context;
- Smart Notes and Note Events;
- learning/progress;
- Daily Intelligence and later period reports;
- conversations;
- connected Intelligence Spaces;
- Smart Mail;
- identity controls;
- privacy/permission controls;
- authorized collective intelligence;
- future tools/actions.

### Hub sovereignty

The Hub is private by default.

A network-facing surface may expose a deliberately limited identity representation, but the private Hub contents must not become public merely because the user has a Smart Link.

### Hub boundary

```text
Smart Link
    ↓
Identity Gateway
    ↓
Authorized Intelligent Hub
    ↓
Personal Naya + private intelligence
    ↓
Explicitly authorized connections/spaces
```

---

# 6. Personal Naya Contract

A Naya is personal.

Each human's Naya may share common capabilities, laws, tools, and architecture with other NayAs while maintaining a distinct relationship, context, memory, permissions, and learned understanding.

> **My Naya is not another person's Naya.**

### Naya identity boundary

Naya A must not silently receive Naya B's private memory merely because the humans enter the same room.

Cross-Naya exchange must be:

1. scoped;
2. authorized;
3. provenance-aware;
4. minimized to the information necessary for the stated purpose;
5. attributable to the correct source/representation;
6. revocable where the underlying policy permits.

---

# 7. Communication Contract

Level 1 communication is intelligence-oriented.

## Supported primitives

### Human ↔ Naya
Personal conversation, learning, planning, reflection, creation, verification, and action support.

### Human ↔ Human
Direct communication using network identities and authorization controls.

### Naya ↔ Naya
Scoped exchange between distinct personal intelligence systems.

### Human + Naya ↔ Human + Naya
An Intelligence Space in which each human may retain their own Naya and context.

### Multi-Naya Intelligence Space
Multiple humans and/or NayAs collaborate around a defined question, subject, objective, or opportunity.

## Communication message contract

Conceptually:

```text
Message {
  message_id: immutable
  conversation_id: scoped container
  sender_type: human | naya | system
  sender_identity_ref: authorized representation
  content_type: text | voice | structured-intelligence
  content: payload
  visibility_scope: private | participants | authorized-network
  source_event_refs: optional Note Event references
  created_at: timestamp
  delivery_state: pending | delivered | failed
}
```

Voice is a communication modality, not a separate identity or memory system.

### No implicit publication

A conversation is not automatically a public feed.

A message is not automatically a Smart Note.

A Smart Note is not automatically collective.

Those transitions require explicit product policy and event rules.

---

# 8. Intelligence Space Contract

An Intelligence Space is a room around intelligence rather than a generic social chat room.

```text
IntelligenceSpace {
  space_id
  purpose
  owner_scope
  participants
  participant_nayas
  permissions
  visibility
  created_at
  status
  intelligence_policy
}
```

### Required properties

Every space should have:

- a purpose/question/objective;
- defined participant scope;
- defined visibility;
- explicit permissions;
- a policy governing what intelligence may leave the space;
- provenance for meaningful outputs.

### Typical patterns

```text
1 Human + Naya
2 Humans + 2 NayAs
N Humans + N NayAs
Specialist Naya + Human + personal Naya
```

The architecture must preserve the distinction between each Naya's private context and the information intentionally contributed to the shared space.

---

# 9. Smart Note / Note Event Contract

NayaPOWER already defines the canonical Note Event as the memory authority. NayaNET adopts that architecture; it does not create a parallel network-memory model.

> **ONE SMART NOTE ACTION → ONE CANONICAL EVENT → MULTIPLE AUTOMATIC PROJECTIONS**

Conceptual flow:

```text
Human experience / conversation / decision / learning
                    ↓
              Smart Note action
                    ↓
           ONE canonical Note Event
                    ↓
      ┌─────────────┼─────────────┐
      ↓             ↓             ↓
   NAYA view     HUMAN view    MACHINE view
      │             │             │
      └─────────────┼─────────────┘
                    ↓
          Intelligence Feed
                    ↓
           PSI awareness/index
                    ↓
       authorized downstream use
```

### Note Event remains the source of truth

Human Note, Naya Note, Machine Note, Intelligent Feed representation, PSI index/awareness, and future projections are not independent memory silos.

They are representations, indexes, notifications, or intelligence consequences of the canonical event.

### Minimum semantic event fields

The implementation must preserve, directly or through the existing canonical event contract:

- event identity;
- event time;
- source/context;
- owner/scope;
- human meaning;
- Naya operational interpretation;
- machine-normalized representation;
- provenance;
- verification state;
- supersession/relationship state where applicable;
- project/subject associations where applicable;
- authorization/distribution policy;
- retrieval/index signals.

Do not duplicate the existing canonical Note Event schema merely to create a NayaNET-specific schema. NayaNET should reference the canonical memory authority.

---

# 10. Intelligent Feed Contract

The Intelligent Feed is the visible/event-distribution projection of intelligence.

It is **not** the canonical memory store.

The feed may communicate:

- verified learning;
- meaningful decisions;
- changes;
- useful discoveries;
- authorized contributions;
- next actions;
- intelligence available to the appropriate audience.

A feed item should retain a reference to the canonical event when the underlying event is eligible for feed publication.

### Feed law

> **Feed publication communicates intelligence; it does not become the authority that stores the original intelligence.**

---

# 11. PSI Contract

PSI is the primary intelligence authority/projection layer where already established by NayaPOWER canonical architecture.

NayaNET must not redefine PSI as a second memory store.

Conceptually:

```text
Canonical Note Event
       ↓
validated / indexed event
       ↓
      PSI
       ↓
authorized intelligence availability
       ↓
retrieval / synthesis / reasoning / action
```

PSI may know that an event exists, what it means, its provenance, confidence/verification state, relationships, and authorized scope. It must not gain access beyond policy merely because an event is indexed.

### PSI must distinguish

- source memory;
- derived understanding;
- verified knowledge;
- unresolved/unknown information;
- permissions;
- current state;
- historical state;
- superseded state.

---

# 12. Collective Intelligence Contract

Collective intelligence is an authorized projection of intelligence, not an automatic dump of personal memory.

```text
Private Note Event
      ↓
policy evaluation
      ↓
explicit/contractual authorization
      ↓
collective-safe projection
      ↓
Collective Intelligence Event
      ↓
authorized recipients / PSI
```

The existing canonical Collective Intelligence Event schema remains authoritative for the actual event format. NayaNET supplies the identity, authorization, communication, and experience-layer boundary around it.

### Collective propagation must be

- intentional;
- scoped;
- provenance-preserving;
- privacy-preserving;
- policy-governed;
- reversible where technically/policy appropriate;
- independently auditable.

---

# 13. Smart Note → PSI Distribution Rules

A single Smart Note action may trigger multiple consequences, but they must occur through the canonical event pipeline.

### Required sequence

```text
CAPTURE
  ↓
VALIDATE
  ↓
PERSIST CANONICAL NOTE EVENT
  ↓
CREATE/UPDATE PROJECTIONS
  ↓
INDEX / UPDATE PSI AWARENESS
  ↓
PUBLISH INTELLIGENCE FEED IF AUTHORIZED
  ↓
EVALUATE COLLECTIVE ELIGIBILITY
  ↓
AUTHORIZED DOWNSTREAM INTELLIGENCE
```

The exact runtime implementation may be asynchronous, but the semantic ordering and source-of-truth boundary must remain intact.

### Failure law

If persistence succeeds but a downstream projection fails, the system must not create a second canonical event to compensate.

Instead:

- retain the canonical event;
- record downstream failure state;
- retry safely where appropriate;
- expose incomplete propagation honestly;
- preserve idempotency.

---

# 14. Idempotency and Duplicate Prevention

A single user action must not create duplicate canonical Note Events because multiple projections are being processed.

Each downstream operation should be safely repeatable using the canonical event identity and appropriate idempotency keys.

```text
ONE EVENT ID
   ├── human projection
   ├── naya projection
   ├── machine projection
   ├── feed projection
   ├── PSI index/update
   └── collective projection
```

No downstream system may mint a competing source-of-truth event merely because it receives a projection.

---

# 15. Privacy and Data-Minimization Contract

Level 1 defaults to the minimum disclosure necessary for the requested interaction.

### Private by default

- real name;
- private Naya context;
- private Hub contents;
- private Smart Notes;
- private conversations;
- personal intelligence history;
- private reports;
- credentials/security data.

### Network-facing by default

- Smart Name;
- Smart Link;
- deliberately exposed profile/HUB metadata;
- authorized conversation identity;
- authorized intelligence contributions.

### Cross-Naya disclosure

When Naya A communicates with Naya B, the default payload is **task-scoped intelligence**, not the entirety of Naya A's memory.

---

# 16. Level 1 Scope Boundary

## In scope

- NayaNET identity;
- Smart Name/Alias;
- Smart Link;
- Intelligent Hub;
- personal Naya relationship;
- text communication;
- voice communication;
- Intelligence Spaces;
- Human↔Naya and Naya↔Naya interaction;
- Smart Notes / Note Events;
- Intelligent Feed projection;
- PSI awareness/availability;
- authorized collective intelligence;
- Daily/period intelligence derived from canonical memory;
- privacy and permission controls.

## Explicitly out of scope by default

- image hosting as a social feed primitive;
- video hosting as a social feed primitive;
- creator-media infrastructure;
- public-media algorithms;
- attention-optimization feed ranking;
- unrestricted public posting;
- assuming Level 5 media features exist.

These may become later NayaNET levels without changing the Level 1 contracts.

---

# 17. E01 Compatibility Contract

E01 must be built as an experience layer over these contracts.

The entrance may be simple:

```text
SEE NAYA
  ↓
UNDERSTAND THE INVITATION
  ↓
ENTER YOUR NAME
  ↓
CREATE/REVEAL NETWORK IDENTITY
  ↓
ENTER INTELLIGENT HUB
```

E01 must not invent a competing identity model.

If the current implementation cannot yet provision a real production identity, it must represent that limitation honestly and keep the interface contract-ready.

### E01 must preserve

- real-name privacy boundary;
- Smart Name concept;
- Smart Link concept;
- Intelligent Hub destination;
- future Smart Mail addressability;
- ambassador attribution compatibility;
- Naya relationship compatibility;
- canonical Note Event compatibility.

---

# 18. Acceptance Tests

A Level 1 implementation is contract-compatible only if all applicable tests can be demonstrated.

### Identity

- [ ] One canonical identity can produce all derived identity representations.
- [ ] Real name is private by default.
- [ ] Smart Name is the default network-facing identity.
- [ ] Smart Link resolves through the canonical identity.
- [ ] Changing display alias does not create a new person.

### Hub

- [ ] Hub is private by default.
- [ ] Smart Link does not expose private Hub contents.
- [ ] Hub references the user's personal Naya.

### Communication

- [ ] Human↔Naya works within the user's authorized context.
- [ ] Human↔Human uses network identity by default.
- [ ] Naya↔Naya exchange is scoped and authorized.
- [ ] Intelligence Spaces preserve participant boundaries.

### Smart Notes

- [ ] One Smart Note action creates one canonical Note Event.
- [ ] Human/Naya/Machine representations remain projections of that event.
- [ ] Feed publication references the canonical event.
- [ ] PSI indexing references the canonical event.
- [ ] Failed downstream projection does not create a duplicate event.

### Privacy

- [ ] Real name cannot leak through ordinary network flows.
- [ ] Cross-Naya exchange is task-scoped.
- [ ] Collective propagation requires authorization.

### Truth

- [ ] Unknown capabilities remain explicitly unknown.
- [ ] Unconnected services are not represented as live.
- [ ] Production URLs are not invented.
- [ ] Completion claims require evidence.

---

# 19. Authority and Conflict Resolution

This document governs the **NayaNET Level 1 semantic architecture**.

Where an existing NayaPOWER canonical contract defines a more specific implementation detail, that contract remains authoritative.

Priority:

1. NayaPOWER constitutional/canonical laws.
2. Existing canonical Smart Notes / Note Event / CIS contracts.
3. Existing canonical Intelligent Hub / Collective Intelligence contracts.
4. This NayaNET Level 1 integration contract.
5. Product implementation details.
6. UI convenience.

A UI requirement must never silently override a privacy, provenance, sovereignty, or source-of-truth rule.

---

# 20. North Star

NayaNET Level 1 should feel extraordinarily simple while doing extraordinarily sophisticated work underneath.

> **Just talk to Naya.**

Underneath that simplicity:

> **Connect intelligence. Preserve intelligence. Exchange intelligence. Compound intelligence. Create value.**

And the foundational rule remains:

> **The human owns the outcome. Naya helps the human become more capable.**
