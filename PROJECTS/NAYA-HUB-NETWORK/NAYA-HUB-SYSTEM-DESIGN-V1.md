# 🔱 Naya Hub — System Design V1

**Status:** ACTIVE — AUTHORITATIVE PROJECT DESIGN
**Date:** 2026-08-26
**Parent project:** `PROJECTS/NAYA-HUB-NETWORK/`
**Related:** GitHub Issue #61 — Naya Hub / Naya Network — Front-End Core Integration

---

## 1. Executive Decision

Build **one Naya ecosystem experience**, not a collection of disconnected products.

The front-end core is the **Naya Hub**. The existing Naya Power back-end intelligence, MAXIS/MAXESS assessment system, identity, memory, communication, Ambassador/referral, learning, and future network capabilities become connected capabilities inside that Hub.

### Locked principle

> **ONE NAYA. ONE ECOSYSTEM. MANY CAPABILITIES. ONE STANDARD.**

Modes, roles, pages, products, and labels are implementation and human-understanding constructs. They must not artificially reduce Naya's underlying capability or service quality.

### Product model

**Free Naya Toolbox** = useful persistent Hub/account, assessment history, reports, stats, Naya access, identity, communication/network foundations, and available sharing/referral capabilities.

**Naya Power** = the premium empowerment layer: deeper intelligence, learning, courses/resources, player/Codex, and other approved premium capabilities.

The free Hub is therefore not the paid product. It is the **value-rich entry point and persistent relationship layer** that makes the premium value obvious.

---

## 2. North Star User Journey

```text
DISCOVER
   ↓
MAXESS / AI SCORE
   ↓
IDENTITY
   ↓
PERSIST RESULT
   ↓
NAYA HUB
   ↓
REPORTS + STATS
   ↓
NAYA
   ↓
TOOLBOX
   ↓
NAYA IDENTITY / LINK / MAIL
   ↓
CONNECTIONS + SHARING
   ↓
NETWORK
   ↓
NAYA POWER
```

The first successful experience should feel like:

> **"I took a free assessment, received something valuable, and suddenly I have a personal Naya space where my results, growth, Naya, tools, and future connections live."**

The system should minimize friction while preserving informed choice, consent, privacy, and trustworthy identity.

---

# 3. Architecture — Who Does What?

## 3.1 GitHub — Source of Truth for Software

GitHub stores and governs:

- application source code
- API/server code
- database migrations/schema definitions
- tests
- configuration templates
- deployment configuration
- system specifications and project documentation
- version history
- CI/CD definitions

**GitHub is not the runtime database and must not be treated as live transactional state.**

---

## 3.2 Vercel — Application Runtime / Deployment Target

Vercel is the initial preferred runtime for the Hub web application and its server/API layer where the framework and workload fit.

Conceptually:

```text
GitHub
  │
  │ commit / CI / deploy
  ▼
Vercel
  │
  ├── web application
  └── secure server/API functions
```

The runtime executes application logic. It does not become the authoritative owner of member, assessment, referral, or financial data.

**Cost rule:** begin on the applicable free tier where permitted and sufficient; monitor usage and plan terms; upgrade only when commercial requirements, reliability, scale, or usage justify it. Do not architect around a hypothetical million-user bill today.

---

## 3.3 Supabase — Persistent Application State

Supabase is the initial preferred durable data layer for:

- authentication/identity state
- member profiles
- assessment records
- report metadata
- permissions
- Naya conversations where approved
- contacts
- messages
- referral attribution
- Ambassador/referral records
- commission ledger records
- network relationships/permissions
- application events

Supabase may also provide approved server-side capabilities such as Edge Functions where useful. This does not change the authority model: each data domain must have one canonical owner.

---

## 3.4 Groove — Human-Facing Cockpit / Embed Surface

Groove is the initial presentation/cockpit environment where existing pages/embeds are appropriate.

Groove should display and collect user actions but must not be the authority for:

- identity
- assessment truth
- referral attribution
- commission balances
- security secrets
- permission state
- transactional history

Target:

```text
USER
  ↓
GROOVE / HUB UI
  ↓
SECURE APPLICATION/API
  ↓
SUPABASE
```

The Hub may ultimately become a standalone application surface while continuing to reuse proven Groove/MAXESS assets where that is the smallest safe path.

---

## 3.5 External Providers

Email delivery, inbound mail, payment, AI inference, TTS, and other providers remain replaceable infrastructure behind server-side interfaces.

No provider-specific implementation should unnecessarily become the product's canonical business logic.

---

# 4. The Critical Data Rule

For every important object we ask:

1. **Who owns the truth?**
2. **Where is it stored?**
3. **Where is it created?**
4. **Where can it be updated?**
5. **Who is allowed to read it?**
6. **Who is allowed to change it?**
7. **What event proves the change occurred?**
8. **How is it recovered?**

### Initial authority map

| Domain | Canonical authority | Created by | Consumed by |
|---|---|---|---|
| Source code | GitHub | Engineering | CI/CD/runtime |
| Member identity | Supabase/application auth | Auth flow | Hub, API, Naya |
| Smart Name/handle | Application + Supabase | Identity provisioning | Hub, referral layer |
| Assessment definition | MAXESS canonical config | MAXESS engineering | Assessment runtime |
| Assessment result | MAXESS result contract + persisted record | Verified assessment execution | Hub/reporting |
| Historical score | Persisted result record | Completed assessment | Hub/stats |
| Report | Persisted report/result artifact | Result pipeline | Hub/member |
| Referral attribution | Secure backend/Supabase | Referral-aware funnel | Conversion/ledger |
| Commission | Immutable commission ledger | Verified conversion processing | Ambassador dashboard |
| Contacts | Supabase | Member/import process | Communication layer |
| Messages | Supabase + provider event state | Communication service | Hub/inbox |
| Permissions | Application/Supabase | Member/admin action | All protected features |
| Network relationship | Application/Supabase | Explicit authorized action | Network |
| Naya knowledge/runtime configuration | Approved Naya source-of-truth system | Naya engineering | Naya runtime |

**Important:** historical MAXESS results must never be silently rescored because a later scoring implementation changed.

---

# 5. Authentication Strategy

## Recommended product behavior

Do not make authentication a confusing wall before value is demonstrated.

The preferred flow is:

```text
Visitor
  ↓
Start MAXESS
  ↓
Complete assessment
  ↓
Correct result
  ↓
"Save your result + unlock your Naya Hub"
  ↓
Fast identity creation
  ↓
Hub
```

### Identity options

The system should support, subject to implementation/provider availability:

- name
- email
- Google sign-in
- other approved identity providers

### Important refinement

**Do not silently create a durable account from a name alone if that creates ambiguity about identity, consent, or recoverability.**

Instead, use a progressive identity model:

```text
assessment session
      ↓
known visitor
      ↓
verified identity
      ↓
member account
      ↓
full Naya identity
```

If product testing proves that an immediate account after assessment materially improves conversion without creating trust problems, the flow can be tightened later.

---

# 6. The Hub's First Screen

## Screen 01 — My Naya / Reports

This is the recommended landing surface immediately after successful assessment/account entry.

### Visual hierarchy

```text
┌──────────────────────────────────────────┐
│ MY NAYA                         Profile  │
│                                          │
│              NAYA ORB                    │
│        "I'm here. What do you need?"     │
│                                          │
│        YOUR LATEST AI SCORE              │
│              78                          │
│        ADVANCING                         │
│                                          │
│  [ VIEW FULL REPORT ] [ TALK TO NAYA ]   │
│                                          │
│  Your Growth                             │
│  3 Assessments   ↑12 pts   5 Dimensions  │
│                                          │
│  [ Assessment History ]                  │
│                                          │
│  YOUR NAYA TOOLBOX                       │
│  Report • Naya • Link • Mail • Network  │
│                                          │
│  [ EXPLORE NAYA POWER ]                  │
└──────────────────────────────────────────┘
```

This is intentionally a **report-first Hub**, because the user's first reason for being there is the value they just earned.

### UX laws

- No unnecessary dashboard clutter.
- The latest meaningful result is immediately visible.
- Naya is visually present but does not obstruct the report.
- Every major action has a clear purpose.
- Buttons must be premium, responsive, accessible, and unmistakably interactive.
- Information hierarchy must be obvious at a glance.
- Mobile is first-class.
- The interface should feel like Naya, not like a generic SaaS admin panel.

---

# 7. Assessment History

## Screen 02 — My Assessments

Members can see every completed assessment.

Each card contains only the highest-value summary:

- assessment name
- date
- score
- mastery/capability band
- key dimension snapshot
- View Report

Example:

```text
AI CRAFTSMANSHIP
Aug 26, 2026
78 · ADVANCING
[ VIEW REPORT ]

AI CRAFTSMANSHIP
Aug 14, 2026
66 · DEVELOPING
[ VIEW REPORT ]
```

### Growth view

Where multiple comparable assessments exist:

```text
66 ──────────────── 78
        +12

DEVELOPING → ADVANCING
```

Never compare incompatible assessment versions as if they were equivalent. Version identity belongs to the stored result.

---

# 8. Report Screen

## Screen 03 — Assessment Report

Reuse the strongest existing MAXESS results experience rather than recreating it unnecessarily.

Primary sequence:

1. score reveal
2. personalized analysis
3. capability spectrum
4. five-dimension profile
5. how the user works with AI
6. natural advantage + opportunity
7. save/share report
8. Naya response
9. path back to Hub

The report should contain a persistent **Back to My Naya** action.

---

# 9. Naya Screen

## Screen 04 — Talk to Naya

Naya is the primary human interface.

### Core interaction

```text
              ◉
          NAYA ORB

     "What would you like to do?"

        [ 🎙 SPEAK ]

      or type a message

      [ SEND ]
```

When Naya is speaking, the orb should use the established visual language/animation from the MAXESS experience where technically appropriate.

### Voice path

```text
User microphone
      ↓
Speech-to-text
      ↓
Secure application/API
      ↓
Authorized Naya knowledge/context
      ↓
Naya response
      ↓
TTS
      ↓
Browser audio + orb state
```

Voice providers are implementation details. The authoritative Naya knowledge/runtime boundary must remain explicit.

---

# 10. Toolbox Screen

## Screen 05 — My Naya Toolbox

The member receives practical capabilities before being asked to purchase anything.

### Toolbox blocks

**MY IDENTITY**
- Smart Name
- personal Naya link
- profile

**MY REPORTS**
- latest report
- assessment history
- growth

**MY NAYA**
- conversation
- voice where available

**MY COMMUNICATION**
- NayaMail identity/interface
- contacts
- messages

**MY SHARING**
- personal link
- approved share messages
- referral/ambassador activity where applicable

**MY NETWORK**
- connections
- communities
- privacy controls

**NAYA POWER**
- trial/offer
- courses
- player
- Codex
- premium intelligence

---

# 11. Referral / Ambassador Integration

The member should never have to understand the machinery.

Behind the scenes:

```text
MEMBER ACCOUNT
     ↓
SMART NAME
     ↓
PERSONAL NAYA URL
     ↓
REFERRAL PROFILE
     ↓
MAXESS ATTRIBUTION
     ↓
VERIFIED CONVERSION
     ↓
COMMISSION LEDGER
     ↓
AMBASSADOR STATS
```

The personal URL is an alias. The immutable user ID is the canonical attribution key.

A URL parameter or client-side value is never sufficient proof of a commission.

---

# 12. NayaMail Integration

V1 should be a communication hub, not a full mailbox-infrastructure project.

### V1

```text
Contacts
  ↓
Select
  ↓
Compose
  ↓
Preview
  ↓
Send
  ↓
Delivery state
  ↓
Inbox / Reply
```

The outbound provider must be abstracted behind a server-side interface.

### Later

Real hosted personal addresses such as `smartname@...` require additional mailbox, DNS, inbound delivery, storage, abuse, authentication, and operational infrastructure. This must not block the first working Hub.

---

# 13. Network Model

The network is **permission-based, not engagement-maximized**.

Members can choose:

- private
- connection-only
- community
- public

Naya may suggest useful connections but does not silently create relationships or grant communication permission.

A future network interaction may look like:

> "Naya, are there people in the network interested in AI entrepreneurship?"

Naya can identify eligible matches based on authorized data and present a connection option.

The recipient chooses whether to accept, decline, ignore, or block.

---

# 14. Output Intelligence Standard

The Hub must apply the same **10-Star Service** standard to every user-facing response.

The system should first classify the interaction by intent:

### WORK MODE
The user is creating, building, repairing, executing, or managing a project.

Output priority:

**state → decision → action → implementation → verification → next move**

### LEARNING MODE
The user is trying to understand something.

Output priority:

**simple explanation → analogy → key facts → example → check understanding → next step**

### REFLECTION / CONVERSATION MODE
The user is exploring, thinking aloud, deciding, or sharing.

Output priority:

**understand meaning → reflect clearly → identify insight → suggest useful next move**

### Universal output rule

**MINIMUM SUFFICIENT + MAXIMUM USEFUL.**

Do not produce a giant wall of text merely because more information exists.

The response should be:

- skimmable
- structured
- concise when conversation is rapid
- detailed when the user requests a full artifact
- direct
- warm
- honest
- evidence-aware
- action-oriented

---

# 15. Smart Notes / Intelligence Blocks

A meaningful project event may generate:

### Smart Note
A human-readable intelligence record containing both:

- Naya perspective
- Shawn/human perspective

### Machine Note
A structured technical representation where machine-to-machine retrieval or processing benefits from it.

### Intelligence Block
A subject-centered block that combines multiple perspectives, facts, decisions, lessons, artifacts, receipts, and context.

The system should associate meaningful events with the active project and mode.

The lifecycle is:

```text
EVENT
 ↓
SMART NOTE
 ↓
INTELLIGENCE BLOCK
 ↓
DAILY / WEEKLY / MONTHLY SYNTHESIS
 ↓
KNOWLEDGE + EXPERIENCE
 ↓
WISDOM
```

The Hub should not expose this complexity unless it is useful to the member.

---

# 16. Development Phases

## Phase 0 — Architecture + Inventory

**Goal:** eliminate guessing.

Inventory existing assets before building replacements:

- MAXESS canonical assessment/result path
- authentication/identity code
- existing Hub/app shells
- existing Groove embeds
- Supabase projects/schema/functions
- Vercel projects/deployments
- Naya voice/TTS implementation
- Naya knowledge/runtime
- NayaMail assets
- Ambassador/referral assets
- existing personal-link implementation

**Exit gate:** each reusable asset has a known location, owner, authority, and integration status.

---

## Phase 1 — Working Vertical Slice

**Build this first.**

```text
MAXESS
  ↓
IDENTITY
  ↓
PERSIST RESULT
  ↓
HUB
  ↓
DISPLAY SCORE + REPORT
```

### Required proof

A test user can:

1. start MAXESS;
2. complete it;
3. receive the correct score;
4. establish/continue identity;
5. persist the result;
6. enter the Hub;
7. see the same authoritative result;
8. return to the report;
9. refresh without losing the result.

**This is the first real product milestone.**

---

## Phase 2 — Assessment Intelligence

Add:

- assessment history
- multiple results
- report retrieval
- dimension statistics
- growth/trend presentation
- version-aware comparisons

Exit gate: historical results remain stable and correctly associated with the member.

---

## Phase 3 — Naya Interface

Add:

- orb
- conversation
- approved voice path
- knowledge/runtime integration
- member context
- output-intelligence behavior

Exit gate: Naya can converse with the member through the Hub using authorized data and produces verified, intelligible responses.

---

## Phase 4 — Identity + Toolbox

Add:

- Smart Name
- personal Naya URL
- profile
- toolbox
- NayaMail identity/interface
- basic share actions

Exit gate: a new member receives a coherent personal Naya identity without manual synchronization.

---

## Phase 5 — Communication + Ambassador

Add:

- contacts
- CSV import
- compose/preview/send
- inbox/reply
- referral attribution
- Ambassador dashboard
- conversion events
- commission ledger

Exit gate: a complete referral → MAXESS → qualifying conversion → ledger path is proven with test evidence.

---

## Phase 6 — Network

Add:

- connections
- groups/communities
- aliases/lists
- privacy controls
- permissioned messaging
- AI participation rules

Exit gate: every relationship/message action has explicit authorization and auditable state.

---

## Phase 7 — Naya Power + Network Intelligence

Add:

- premium entitlements
- five-day trial if still commercially approved
- courses/resources
- Max Player
- Human Maximus Codex
- Daily Naya Intelligent Network
- higher-order intelligence synthesis

Exit gate: the free toolbox and premium Naya Power experience are visibly one ecosystem rather than separate products.

---

# 17. Recommended Execution Order Across Platforms

The order is **not** “finish GitHub, then Vercel, then Supabase, then Groove.” They are connected layers, so we build the smallest vertical slice across all required layers.

### Step 1 — GitHub
Establish source truth, contracts, project structure, tests, and deployment configuration.

### Step 2 — Supabase
Create only the minimum durable schema required for Phase 1:

- users / identity mapping
- assessment definitions reference/version
- assessment results
- report metadata

### Step 3 — Vercel
Deploy the application/API that connects the Hub UI to Supabase.

### Step 4 — Groove/MAXESS
Connect the existing assessment/result experience to the new identity/result handoff.

### Step 5 — End-to-end verification
Run:

```text
Browser → Groove/MAXESS → API → Supabase → API → Hub
```

Do not advance because individual components look correct. Advance when the **whole path works**.

### Step 6 — Expand one block at a time
Only after Phase 1 is green do we add history, Naya, toolbox, communication, Ambassador, network, and premium layers.

---

# 18. Why This Is Better Than Building the Hub All at Once

The Hub is large, but the first functioning product is small.

A giant simultaneous build creates too many unknowns:

- authentication failure
- stale/incorrect result mapping
- database schema drift
- UI/runtime mismatch
- voice integration failure
- referral attribution failure
- provider configuration failure

A vertical slice makes every boundary observable.

### Engineering principle

> **Build breadth in the design. Build depth in one verified vertical slice. Then expand.**

This preserves the ability to zoom out without forcing us to build everything before anything works.

---

# 19. Cost-Control Architecture

Initial target:

**$0 incremental infrastructure where free tiers and applicable terms permit.**

The system must track usage before upgrading.

### Upgrade triggers are based on:

- actual requests
- compute/runtime usage
- database/storage usage
- bandwidth/egress
- email volume
- voice/TTS usage
- AI inference cost
- commercial plan requirements
- reliability requirements

Not arbitrary user-count thresholds.

### Scaling law

```text
BUILD CHEAP
   ↓
MEASURE
   ↓
OPTIMIZE
   ↓
GROW
   ↓
CALCULATE UNIT ECONOMICS
   ↓
UPGRADE ONLY WHEN JUSTIFIED
```

Cloudflare remains a future option where edge routing, caching, security, queues, or economics justify adding it. It is not required for Phase 1.

---

# 20. Failure and Recovery Model

Every phase must explicitly handle:

### Missing identity
→ preserve assessment session where possible → request identity → do not fabricate ownership.

### Missing result
→ show truthful recovery state → retrieve from authoritative source → never invent score.

### Duplicate result
→ use stable event/result IDs → idempotent persistence → preserve history.

### Conflicting result
→ surface conflict → identify authority/version → do not silently overwrite.

### API unavailable
→ graceful UI state → retry/recover → preserve user-entered state where safe.

### Supabase unavailable
→ do not claim persistence → clearly distinguish saved vs unsaved.

### Voice unavailable
→ fall back to text interaction → explain briefly → do not pretend audio succeeded.

### Provider failure
→ record provider state → retry according to policy → preserve auditable event state.

### Unauthorized network action
→ do not execute → explain permission requirement → offer authorized alternative.

---

# 21. Definition of Done for the First Block

Phase 1 is **DONE** only when all are true:

- [ ] MAXESS assessment is browser-proven through the current canonical path.
- [ ] Identity boundary works.
- [ ] Result is generated by the canonical MAXESS engine.
- [ ] Result is persisted durably.
- [ ] Hub retrieves the persisted result.
- [ ] Hub displays the correct score/report.
- [ ] Refresh/re-entry preserves the result.
- [ ] No client-side fabricated score/state.
- [ ] Authentication/authorization boundary is verified.
- [ ] Mobile and desktop critical paths work.
- [ ] Failure states are truthful.
- [ ] Evidence is captured.
- [ ] Source documentation is updated.

Only then do we promote to Phase 2.

---

# 22. Immediate Execution Directive

## DO NOT START BY BUILDING THE WHOLE HUB.

Start by proving this:

```text
                    ┌──────────────┐
                    │   MAXESS     │
                    └──────┬───────┘
                           │
                      result + identity
                           │
                           ▼
                    ┌──────────────┐
                    │   SUPABASE   │
                    │ durable data │
                    └──────┬───────┘
                           │
                        secure API
                           │
                           ▼
                    ┌──────────────┐
                    │    VERCEL    │
                    │ app + API    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   NAYA HUB   │
                    │ report first │
                    └──────────────┘
```

Groove/MAXESS remains the current entry/presentation asset while the Hub becomes the persistent destination.

### First implementation target

**One user → one identity → one completed MAXESS result → one persisted result → one Hub → one visible report.**

Once that works, the rest of the ecosystem has a stable spine to attach to.

---

# 23. Master Engineering Questions

Before adding any capability, the implementation must answer:

**Where is it created?**

**Where is it stored?**

**Who owns the truth?**

**Who can modify it?**

**Who can read it?**

**How is authorization checked?**

**How is it versioned?**

**How is it recovered?**

**How do we know it worked?**

**What does the user see if it fails?**

**What happens on duplicate execution?**

**What happens when two truths conflict?**

**What is the smallest useful implementation?**

**Can an existing working asset be reused instead of rebuilt?**

**What evidence promotes this block to the next phase?**

If the team cannot answer the why, the design is not ready.

---

# 24. Locked Product Philosophy

Naya should feel like a brilliant friend, teacher, apprentice, strategist, and operating partner — not because separate modes create separate personalities, but because one integrated Naya adapts to the user's objective.

She should understand:

**what the user says → what they mean → what they are trying to accomplish → what would actually help.**

She should not blindly execute literal wording when doing so would clearly undermine the user's intended objective. She should clarify only when ambiguity materially affects the result.

### Service formula

```text
INTENT
  ↓
UNDERSTAND
  ↓
INFER MEANING
  ↓
MINIMUM QUESTIONS
  ↓
BEST SAFE PLAN
  ↓
EXECUTE
  ↓
VERIFY
  ↓
SHOW RECEIPT
  ↓
NEXT BEST MOVE
  ↓
LEARN
  ↓
IMPROVE
```

The user remains in control of consequential decisions.

---

# 25. Final Lock

### The Hub is the front-end core.
### Supabase is the initial durable state layer.
### Vercel is the initial application/API runtime.
### GitHub is the engineering/source/deployment authority.
### Groove is the initial cockpit/presentation layer.
### MAXESS is the first intelligence-generating doorway.
### Naya is the primary human interface.
### Naya Power is the empowerment layer.
### NayaMail is the communication layer.
### Ambassador is the growth/referral layer.
### The Network is the connection layer.

They are not separate destinations in the user's mind.

They are **one ecosystem, connected block by block.**

> **FUNCTION FIRST. BEAUTY SECOND. BOTH REQUIRED.**
>
> **DESIGN THE WHOLE. BUILD THE SLICE. VERIFY THE BOUNDARIES. EXPAND THE SYSTEM.**
>
> **ONE NAYA. ONE ECOSYSTEM. ONE STANDARD.**
