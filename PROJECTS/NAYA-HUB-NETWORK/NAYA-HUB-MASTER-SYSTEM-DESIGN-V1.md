# 🔱 NAYA HUB / NAYA NETWORK — MASTER SYSTEM DESIGN V1

**Status:** ACTIVE — SYSTEM DESIGN BASELINE  
**Date:** 2026-08-26  
**Project:** Naya Hub / Naya Network  
**North Star:** One Naya. One coherent experience. One intelligent ecosystem. Block by block.

## 0. PURPOSE

This document is the architectural source of truth for designing the Naya Hub before implementation. It intentionally zooms out before building any individual block so that earlier decisions do not accidentally constrain later capabilities.

The system is designed around one principle:

> **The human should experience one coherent Naya ecosystem, while the engineering underneath may contain many specialized services and capabilities.**

MAXESS is the first intelligence-generating doorway. The Hub is the persistent human-facing home. Naya is the primary human interface. NayaMail, identity, assessments, conversations, connections, communities, Ambassador, Naya Power, and network intelligence are capabilities of the same ecosystem—not disconnected products.

---

# 1. SYSTEM NORTH STAR

### User experience

A person should be able to:

`DISCOVER → IDENTIFY → ASSESS → UNDERSTAND → SAVE → RETURN → TALK → GROW → CONNECT → COMMUNICATE → LEARN → EMPOWER`

without repeatedly feeling that they are entering unrelated applications.

### Engineering objective

Create one authoritative identity and one durable member boundary through which all authorized capabilities can safely connect.

### Primary success condition

A new user can enter through MAXESS, establish identity, complete an assessment, receive a correct durable result, enter their Hub, retrieve that result later, interact with Naya, and progressively activate communication/network/Naya Power capabilities without broken handoffs or invented state.

---

# 2. ARCHITECTURAL LAW

## One Naya. Many Perspectives. One Standard.

Modes, roles, and perspectives emphasize behavior; they do not create separate Nayas or reduce capability.

## Result over label

Subsystem names are for human understanding. The experienced outcome is authoritative.

## Working first

A UI is not complete until its underlying action/data path works and is verified.

## Back-end authority

The front end renders and requests authoritative state. It never invents authoritative scores, identities, entitlements, permissions, commissions, or network relationships.

## Minimum sufficient + maximum useful

Every screen, output, button, notification, and data element must earn its place by improving the user's ability to understand or act.

## Anticipate without overstepping

Naya should infer intent and recommend the best next action, but consequential actions remain governed by authority, consent, permissions, and explicit system rules.

---

# 3. SYSTEM MAP

```text
                         ┌──────────────────────┐
                         │       PERSON         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      MAXESS          │
                         │ Assessment / Score   │
                         └──────────┬───────────┘
                                    │
                         identity + result
                                    │
                                    ▼
                     ┌────────────────────────────┐
                     │       NAYA HUB             │
                     │ persistent human boundary  │
                     └─────────────┬──────────────┘
                                   │
             ┌─────────────┬───────┼────────┬─────────────┐
             ▼             ▼       ▼        ▼             ▼
         MY NAYA       RESULTS   GROWTH  NAYAMAIL     CONNECTIONS
             │             │       │        │             │
             └─────────────┴───────┼────────┴─────────────┘
                                   ▼
                           NETWORK / COMMUNITIES
                                   │
                                   ▼
                              AMBASSADOR
                                   │
                                   ▼
                             NAYA POWER
                                   │
                                   ▼
                         NETWORK INTELLIGENCE
```

The Hub is the integration boundary. Individual services may evolve independently, but the member experience and canonical identity must remain coherent.

---

# 4. CANONICAL ENTITIES

## 4.1 Member Identity

**Question:** Who is this person?  
**Answer:** The canonical member identity service/account boundary.

**Owns:** stable member ID, authentication linkage, identity-provider links, account lifecycle.

**Stored:** authoritative identity store.

**Created:** first successful identity/account establishment.

**Updated:** authorized profile/account operations.

**Read by:** Hub, MAXESS handoff, Naya, NayaMail, Ambassador, permissions, analytics, entitlements.

**Rule:** one member ID; many providers may map to it.

**Failure rule:** never create a second member merely because a second authentication provider is used; require safe account-linking/recovery behavior.

---

## 4.2 Profile

**Question:** What user-facing information has the member chosen to provide?

**Owns:** display name, preferences, visibility choices, profile metadata.

**Stored:** profile store associated with canonical member ID.

**Created:** during onboarding or first profile save.

**Updated:** explicit member action or authorized profile workflow.

**Read by:** Hub, Naya, network/profile surfaces, communication UI.

**Rule:** profile data is not identity authority. A display-name change must not change the stable member ID.

---

## 4.3 Assessment

**Question:** What assessment was taken, under which version/configuration?

**Owns:** assessment instance metadata, question/config version, timestamps, completion state.

**Stored:** assessment/result data store.

**Created:** assessment start and/or authoritative completion event.

**Updated:** permitted lifecycle transitions only.

**Read by:** results, Hub, growth, Naya context, analytics.

**Rule:** every completed assessment gets a durable unique assessment ID.

---

## 4.4 Assessment Result

**Question:** What was the authoritative result for that assessment instance?

**Owns:** canonical score, mastery band, dimension results, fingerprint, report payload/version, provenance.

**Created:** canonical scoring/result-generation path.

**Stored:** authoritative result record keyed by assessment ID + member ID.

**Updated:** only through explicitly authorized versioned repair/migration.

**Read by:** results UI, Hub history, growth, Naya, analytics.

**Rule:** **NO HISTORICAL RESCORING.** Historical results remain authoritative.

---

## 4.5 Conversation

**Question:** What did the member and Naya/authorized participant discuss?

**Owns:** conversation ID, participants, timestamps, messages, context references, visibility state.

**Stored:** conversation/message store.

**Created:** first message/session.

**Updated:** append-only message/event behavior plus explicit metadata updates.

**Read by:** member, authorized Naya runtime, permitted participants.

**Rule:** conversation access follows permissions and privacy boundaries.

---

## 4.6 Naya Memory / Knowledge Context

**Question:** What authorized information may Naya use to help this person?

**Owns:** approved knowledge references, member-authorized context, durable notes where applicable, provenance.

**Stored:** authoritative knowledge/memory systems already established by the Naya architecture.

**Created:** governed ingestion/learning/note/event pathways.

**Updated:** governed learning, corrections, migrations, or user-authorized changes.

**Read by:** Naya runtime and authorized intelligence services.

**Rule:** memory is not automatically permission to expose information to another person.

---

## 4.7 NayaMail

**Question:** How can this member communicate within the Naya ecosystem?

**Owns:** Naya identity/address, inbox/outbox state, message metadata, notification preferences, opt-out state.

**Stored:** communication system.

**Created:** member onboarding/provisioning.

**Updated:** message operations, settings, delivery state, authorized identity changes.

**Read by:** member, communication UI, authorized delivery services.

**Rule:** recipient preferences and anti-spam/consent controls are authoritative.

---

## 4.8 Contact / Alias / List / Group

**Question:** How has the member chosen to organize relationships?

**Owns:** member-owned organization structures and references to canonical identities.

**Stored:** relationship/organization store.

**Created:** explicit member action or approved import.

**Updated:** explicit member action/import synchronization.

**Read by:** contacts, messaging, communities, Naya suggestions.

**Rule:** deleting an organization reference must not silently delete the underlying person/account.

---

## 4.9 Connection

**Question:** What relationship exists between members?

**Owns:** relationship state, initiator, recipient, status, permissions, timestamps.

**Stored:** relationship store.

**Created:** explicit acceptance/authorized relationship workflow.

**Updated:** acceptance, decline, block, removal, or policy-governed changes.

**Read by:** profiles, messaging, communities, Naya, network views.

**Rule:** Naya may recommend; she must not silently establish a consequential relationship.

---

## 4.10 Community

**Question:** What shared space do people participate in?

**Owns:** membership, rules, visibility, moderation state, messages/content, AI participation policy.

**Stored:** community store.

**Created:** authorized community creation.

**Updated:** owner/moderator/member actions according to rules.

**Read by:** authorized members and approved Naya/AI agents.

**Rule:** private means private; visibility is explicit.

---

## 4.11 Ambassador

**Question:** What referral identity/activity belongs to this member?

**Owns:** referral identity, attribution, verified events, commission ledger, member stats.

**Stored:** authoritative referral/commission system.

**Created:** eligible member provisioning.

**Updated:** verified referral/conversion events and ledger operations.

**Read by:** member dashboard, admin/finance-authorized systems, Naya.

**Rule:** commissions are based on verified authoritative events, not client-side claims.

---

## 4.12 Entitlement

**Question:** What capabilities is the member authorized to use?

**Owns:** Naya Power status, trial state, purchased entitlements, expiration/cancellation state.

**Stored:** authoritative entitlement/billing system.

**Created:** grant/trial/purchase event.

**Updated:** authorized billing/entitlement transitions.

**Read by:** Hub, Naya Power surfaces, course/player/Codex access gates.

**Rule:** free Hub access and premium Naya Power are separate concepts.

---

# 5. AUTHORITATIVE OWNERSHIP MATRIX

| Truth | Authority | UI may write? | UI may invent? |
|---|---|---:|---:|
| Member ID | Identity service | No | No |
| Display name | Profile service | Via authorized API | No |
| Assessment config | Assessment authority | No | No |
| Score | Canonical scoring/result engine | No | No |
| Historical result | Result store | No | No |
| Conversation messages | Conversation service | Via API | No |
| Naya knowledge | Governed knowledge layer | No | No |
| Permissions | Permission/identity authority | Via authorized action | No |
| NayaMail delivery | Communication service | Via API | No |
| Connection state | Relationship service | Via authorized action | No |
| Community membership | Community service | Via authorized action | No |
| Referral attribution | Ambassador authority | No | No |
| Commission | Commission ledger | No | No |
| Premium access | Entitlement authority | No | No |

---

# 6. EVENT / HANDOFF CONTRACT

The system should communicate meaningful state transitions through explicit, traceable events.

Core examples:

```text
MEMBER_CREATED
IDENTITY_LINKED
ASSESSMENT_STARTED
ASSESSMENT_COMPLETED
RESULT_GENERATED
RESULT_PERSISTED
RESULT_VIEWED
HUB_SESSION_STARTED
NAYA_SESSION_STARTED
MESSAGE_CREATED
MESSAGE_DELIVERED
MESSAGE_OPTED_OUT
CONNECTION_REQUESTED
CONNECTION_ACCEPTED
COMMUNITY_JOINED
REFERRAL_ATTRIBUTED
CONVERSION_VERIFIED
COMMISSION_POSTED
ENTITLEMENT_GRANTED
ENTITLEMENT_EXPIRED
```

Each meaningful event should have:

- stable event ID
- event type/version
- actor/member ID where applicable
- subject/entity ID
- timestamp
- source/provenance
- correlation/trace ID
- idempotency strategy
- authorization context where required
- result/status

A retry must not create duplicate authoritative outcomes.

---

# 7. SCREEN-BY-SCREEN EXPERIENCE

## Screen 00 — Entry

**Goal:** immediate comprehension and low friction.

Primary action: **START MY AI SCORE**.

Avoid premature complexity. No dashboard, navigation maze, or large registration wall.

**Why:** the user came for a reason; respect momentum.

---

## Screen 01 — Identity

**Goal:** create/recover the member boundary with minimum friction.

Primary actions:

- Google sign-in
- Facebook sign-in where supported/approved
- minimal manual identity path

Collect only what is necessary at this point.

**Why:** identity should feel like personalization, not bureaucracy.

Failure cases:

- provider cancellation → remain recoverable
- existing account → sign in/link safely
- duplicate email/provider identity → account-linking flow
- network interruption → no false success

---

## Screen 02 — MAXESS

Preserve the proven MAXESS visual language and interaction quality.

Required behavior:

- question state
- answer selection
- progress
- Naya guidance where configured
- Continue validation
- recovery from refresh/session interruption where supported

No Hub navigation should distract from assessment completion.

---

## Screen 03 — Results

Cinematic result experience remains the authoritative interpretation surface.

Required sequence:

`SCORE → ANALYSIS → CAPABILITY → HOW YOU WORK → ADVANTAGE/OPPORTUNITY → SAVE → NAYA`

The result must be persisted before being presented as durable.

Primary transition:

### **CONTINUE TO MY NAYA HUB**

The user should understand that their result is now theirs—not merely a temporary web page.

---

## Screen 04 — Hub Home

Purpose: persistent home, not analytics overload.

Top:

`HELLO, [NAME]`

Central Naya/orb experience.

Primary destinations:

- **MY NAYA** — conversation
- **MY RESULTS** — assessments/reports
- **MY GROWTH** — trends/comparison
- **NAYAMAIL** — communication
- **MY CONNECTIONS** — people/communities
- **NAYA POWER** — deeper capabilities

The home screen should prioritize the user's next useful action and current context rather than displaying every capability simultaneously.

---

## Screen 05 — My Results

Show:

- latest assessment
- previous assessments
- score
- mastery band
- dimensions
- report access
- date/version metadata

Primary action:

**VIEW REPORT**

Secondary:

**TAKE ANOTHER ASSESSMENT**

Never silently replace a previous result.

---

## Screen 06 — My Growth

Show change over time.

Potential views:

- score trajectory
- dimension movement
- assessment timeline
- comparison
- Naya interpretation

Important wording:

> “Your score changed from X to Y.”

not:

> “Your old score was recalculated.”

Historical records remain immutable.

---

## Screen 07 — Naya

Naya is the primary interface.

Visual centerpiece: the established Naya orb language.

Interaction:

`TAP / SPEAK → LISTENING → THINKING → RESPONDING`

Voice/TTS is used only through the approved runtime path.

Naya can use authorized member context, but the interface must never imply access she does not have.

Outputs follow the Output Intelligence Standard:

- identify intent
- lead appropriately
- answer directly
- explain why when useful
- surface risks/unknowns
- provide the best next action
- avoid unnecessary walls of text

---

## Screen 08 — NayaMail

Primary hierarchy:

`Inbox → Compose → Contacts → Lists/Groups → Settings`

The interface should make sending simple while preserving recipient controls.

No “blast everyone” action should bypass consent, recipient preferences, rate limits, or policy.

---

## Screen 09 — Connections

Show:

- current connections
- requests
- suggested connections
- communities
- privacy controls

Suggestions are recommendations, not relationships.

---

## Screen 10 — Community

A community may be:

- private
- connection-only
- public

Human and authorized AI participation can coexist where community rules permit it.

Visibility and identity disclosure are explicit choices.

---

## Screen 11 — Ambassador

Show:

- personal Naya link
- referral activity
- verified conversions
- commission status
- share actions

The member should not need to understand attribution machinery.

---

## Screen 12 — Naya Power

Show the value of the premium empowerment layer.

Potential destinations:

- courses
- Human Maximus Codex
- Max Player
- advanced Naya capabilities
- deeper learning/intelligence

The free Hub remains useful without Naya Power.

Naya Power should feel like **empowerment of the toolbox**, not a punishment for using the free product.

---

# 8. NEW USER JOURNEY

```text
DISCOVER MAXESS
      ↓
START
      ↓
ESTABLISH IDENTITY
      ↓
TAKE ASSESSMENT
      ↓
CANONICAL SCORE
      ↓
RESULT PERSISTED
      ↓
RESULT EXPERIENCE
      ↓
ENTER MY NAYA HUB
      ↓
SEE MY RESULT
      ↓
MEET NAYA
      ↓
RETURN ANY TIME
      ↓
TAKE MORE ASSESSMENTS
      ↓
SEE GROWTH
      ↓
COMMUNICATE / CONNECT
      ↓
OPTIONALLY ACTIVATE NAYA POWER
```

The journey should feel like one continuous experience, even when backend services are separate.

---

# 9. FAILURE AND RECOVERY MATRIX

| Failure | Required behavior |
|---|---|
| User closes browser mid-assessment | Preserve valid progress if supported; never fabricate completion |
| Network failure during submit | Show retry state; idempotent retry; no duplicate result |
| Double-click Continue | Single logical submission |
| Refresh on results | Retrieve authoritative result; do not recompute casually |
| Result service unavailable | Explain temporary state; never show fake score |
| Authentication provider fails | Preserve user state; offer retry/alternate path |
| Existing account detected | Safe sign-in/link path; avoid duplicate member |
| Two tabs open | Server authority wins; client reconciles state |
| User takes assessment twice | Create separate assessment IDs/results |
| Historical result requested | Retrieve stored result; never silently rescore |
| User changes profile name | Update profile only; stable member ID unchanged |
| User opts out of messages | Delivery respects opt-out |
| User blocks another member | Future interaction respects block |
| User leaves community | Membership ends; history/records follow retention rules |
| Ambassador event delayed | Pending state until verified; never claim commission early |
| Premium entitlement expires | Premium surfaces gate correctly; free Hub remains |
| Naya lacks required context | Say what is unknown and ask/offer the smallest useful next step |

---

# 10. PRIVACY / PERMISSION MODEL

Every cross-user action answers:

1. **Who is acting?**
2. **On whose data?**
3. **What authority permits it?**
4. **What is the minimum information required?**
5. **What visibility does the recipient have?**
6. **Can the action be reversed?**
7. **What audit/event evidence exists?**

Default posture: private unless explicitly shared.

Network growth must never require surrendering privacy.

---

# 11. OUTPUT INTELLIGENCE STANDARD

Every Naya response should first classify the interaction at a practical level:

### WORK
Project/build/execution.

### LEARN
Teaching/research/explanation.

### REFLECT / CONVERSE
Thinking, discussion, emotional/contextual processing, exploration.

The response format then adapts.

### Rapid mode
Direct answer → key reasoning → next action.

### Guided mode
Context → explanation → options → recommended action → next step.

### Deep mode
Full structured analysis when the user explicitly needs comprehensive work.

Never equate “shorter” with “better.” Optimize for **minimum human friction + maximum useful intelligence**.

---

# 12. INTELLIGENCE / NOTE MODEL

A **Smart Note** means both:

- **Naya Note** — machine/intelligence-facing understanding.
- **Shawn/Human Note** — human-facing understanding, decision, context, and why.

A separate **Machine Note** may be created when technical agents require a native machine-readable representation.

An **Intelligence Block** can combine multiple perspectives about one subject:

```text
SUBJECT
 ├── FACTS
 ├── DECISIONS
 ├── HUMAN MEANING
 ├── NAYA INTERPRETATION
 ├── TECHNICAL STATE
 ├── EXPERIENCE INSIGHT
 ├── RISKS
 ├── OPPORTUNITIES
 └── NEXT ACTION
```

Knowledge + experience → wisdom.

Daily/periodic intelligence should summarize the highest-value learning, not dump everything.

---

# 13. DESIGN SYSTEM REQUIREMENTS

The Hub should inherit the strongest proven visual language from MAXESS rather than reverting to generic SaaS UI.

Required:

- premium dark foundation
- strong white typography
- controlled purple/magenta energy
- clear contrast
- cinematic orb/Naya centerpiece
- tactile primary actions
- meaningful hover/focus/active/loading/success states
- responsive behavior
- keyboard accessibility
- semantic labels/ARIA where needed
- reduced-motion consideration
- no decorative element that competes with the primary action

Buttons must be designed as interactive objects, not flat rectangles with text.

Every primary button answers:

> What happens when I press this?

Every screen answers:

> Why am I here?

Every secondary action answers:

> Why is this here instead of somewhere else?

---

# 14. ENGINEERING BOUNDARIES

The front end should consume explicit contracts.

Minimum contract boundaries:

```text
AUTH CONTRACT
PROFILE CONTRACT
ASSESSMENT CONTRACT
RESULT CONTRACT
NAYA SESSION CONTRACT
MEMORY/CONTEXT CONTRACT
MESSAGE CONTRACT
CONTACT CONTRACT
CONNECTION CONTRACT
COMMUNITY CONTRACT
AMBASSADOR CONTRACT
ENTITLEMENT CONTRACT
EVENT/RECEIPT CONTRACT
```

Each contract must define:

- request shape
- response shape
- authority
- validation
- error states
- idempotency
- authentication/authorization
- versioning
- observability

---

# 15. BLOCK STRATEGY

## Block 1 — Working Foundation

`IDENTITY → MAXESS → RESULT → HUB`

Definition of done:

A real user can establish identity, complete MAXESS, receive the authoritative result, persist it, enter the Hub, retrieve it, and return later.

## Block 2 — Assessment Intelligence

`HISTORY → MULTIPLE RESULTS → GROWTH`

## Block 3 — Naya Interface

`ORB → VOICE → AUTHORIZED CONTEXT → OUTPUT INTELLIGENCE`

## Block 4 — Identity + Communication

`NAYA IDENTITY → NAYAMAIL → CONTACTS → LISTS → GROUPS`

## Block 5 — Network + Ambassador

`CONNECTIONS → COMMUNITIES → SHARING → AMBASSADOR`

## Block 6 — Naya Power + Network Intelligence

`ENTITLEMENT → COURSES/CODEX/PLAYER → NETWORK LEARNING → INTELLIGENCE`

A block may contain multiple coherent engineering tasks. We do not artificially stop useful work merely because a phase label has been reached.

---

# 16. GATE MODEL

Every block passes:

### G0 — DESIGN COMPLETE
Architecture, UX, contracts, failure cases, dependencies understood.

### G1 — IMPLEMENTED
Code exists.

### G2 — FUNCTIONAL
Real end-to-end action path works.

### G3 — VERIFIED
Executable evidence proves expected behavior.

### G4 — HUMAN EXPERIENCE
Human testing confirms clarity, usability, beauty, and flow.

### G5 — FREEZE
Known-good state preserved before the next major boundary.

No “green” based solely on static files or visual existence.

---

# 17. PRE-BUILD HOLE CHECK

Before implementation of a block, ask:

- What creates this state?
- Who owns it?
- Where is it stored?
- What reads it?
- What writes it?
- What is the unique ID?
- What is the lifecycle?
- What happens on retry?
- What happens on duplicate action?
- What happens on refresh?
- What happens on two tabs?
- What happens when the user leaves?
- What happens when a service fails?
- What happens when data is missing?
- What happens when permissions change?
- What happens when the user changes identity/profile data?
- What is the audit/receipt?
- What does the human see?
- What does the human feel?
- What is the next obvious action?
- Can the user recover without support?
- Can the system prove what happened?

If a material “why” cannot be answered, the design is not ready.

---

# 18. OPEN ENGINEERING DISCOVERIES — NOT ASSUMPTIONS

The following must be verified against the live implementation before coding rather than guessed:

- exact production authentication provider/runtime
- exact Hub hosting/runtime boundary
- exact database/storage authority
- exact Naya voice/TTS implementation currently available
- exact MAXESS result persistence/handoff implementation
- exact NayaMail backend/provider boundary
- exact Ambassador attribution implementation
- exact entitlement/billing authority
- exact event/receipt implementation and canonical paths

The design defines the required behavior; implementation work must reconcile it against repository reality.

---

# 19. FIRST IMPLEMENTATION TARGET

Do not begin by building every Hub screen.

First produce the **Block 1 technical design and live inventory**:

1. locate canonical MAXESS identity creation/handoff
2. locate canonical result generation
3. locate canonical result persistence/receipt
4. locate existing Hub/runtime entry point
5. locate authentication boundary
6. define member/result IDs and relationship
7. define the minimal Block 1 contracts
8. define the exact screen flow
9. implement the smallest complete vertical slice
10. execute browser verification
11. human-test it
12. preserve the proven state

This is the fastest safe route to a genuinely functioning ecosystem.

---

# 20. FINAL DESIGN PRINCIPLE

> **Do not build a collection of features. Build one living system.**
>
> **Design the whole system before locking the part.**
>
> **Build the smallest complete vertical slice.**
>
> **Verify the real behavior.**
>
> **Learn from execution.**
>
> **Update the system design.**
>
> **Then build the next block.**

**One Naya. Many perspectives. One standard. One ecosystem. Block by block.** 🔱
