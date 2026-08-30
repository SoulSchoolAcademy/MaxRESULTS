# Naya Power — Universal Agent + Control Substrate Contract

**STATUS:** CANONICAL ARCHITECTURE CONTRACT
**VERSION:** 1.0
**PURPOSE:** Define the vendor-neutral boundary between Naya Power, AI models/agents, persistent control state, and external storage systems without creating competing authorities.

## 1. Product Definition

Naya Power is a **storage-agnostic Superbrain operating system for humans and AI agents**.

A Naya is an individual intelligence node operating under Naya Power. A model or agent is a replaceable execution capability. Storage systems are substrates or sources for particular information classes. NayaNET is the permissioned network of independent Naya Power Superbrains.

**MODEL ≠ AGENT ≠ NAYA POWER ≠ STORAGE ≠ AUTHORITY ≠ NETWORK ≠ INTELLIGENCE.**

## 2. Cardinal Law

> **STORAGE ≠ AUTHORITY.**

A physical system may store information without becoming authoritative over the meaning, state, provenance, or promotion of that information.

Authority is assigned by **information class and contract**, not by storage vendor.

## 3. Authority-by-Information-Class

| Information class | Canonical authority | Examples of substrate |
|---|---|---|
| Source code | source-control authority | Git repository |
| Laws / protocols | versioned canonical Naya Power repository | Git repository |
| Execution state | Naya Power control plane / mission state authority | control substrate |
| Note Events / durable learning | canonical event authority | event store |
| Human documents | originating authorized document authority | Google Drive / document system |
| Structured application data | application data authority | database |
| Media / assets | originating asset authority | object storage |
| External knowledge | originating authoritative source | external source |
| Human mission | Naya Power mission authority | control substrate |
| Network intelligence | permissioned CCT/CIS authority | NayaNET-compatible network |

Adapters MUST preserve the originating authority and MUST NOT silently promote imported data into Naya Power canonical intelligence.

## 4. Control Substrate Contract

Every Naya Power installation MUST have a trustworthy persistent control substrate capable of preserving, at minimum:

- identity;
- canonical configuration;
- operating laws and versions;
- authority registry;
- current mission state;
- execution continuity;
- provenance references;
- verification receipts;
- recovery state;
- version history or equivalent immutable change trace;
- authorization state;
- successor handoff state.

The required guarantees are:

**PERSISTENT → VERSIONED → TRACEABLE → AUTHORIZABLE → RECOVERABLE → AUDITABLE**

GitHub is one valid implementation for software-oriented deployments. It is not a product requirement.

## 5. Universal Agent Interface

The Universal Agent Interface is the vendor-neutral contract through which a compatible model or agent uses Naya Power.

The interface MUST expose the semantic operations needed to:

1. identify the active Naya/control context;
2. restore authorized context;
3. submit or refine human intent;
4. obtain current mission and priority state;
5. request or receive an executable Torch;
6. execute through the canonical execution boundary;
7. submit observed execution results;
8. obtain verification state;
9. capture durable learning through the canonical event path;
10. prepare a successor handoff.

The interface MUST NOT make any particular model, framework, vector database, repository, or cloud provider authoritative.

## 6. Storage Adapter Contract

A storage adapter connects an external system to Naya Power without replacing Naya Power authorities.

Adapter responsibilities:

- authenticate to the external source;
- identify the originating source and authority;
- retrieve authorized content;
- preserve source identity/version/timestamp metadata where available;
- classify the information;
- provide provenance;
- expose changes/supersession where the source supports them;
- hand content to the appropriate canonical Naya Power authority.

Adapter prohibitions:

- writing directly to derived indexes as canonical truth;
- silently changing source authority;
- bypassing canonical Note Events for durable Naya intelligence;
- bypassing mission qualification;
- bypassing verification;
- treating retrieved content as current truth without authority/evidence evaluation.

## 7. Activation of External Knowledge

The canonical path is:

**EXTERNAL SOURCE → AUTHENTICATE → CLASSIFY → PRESERVE SOURCE PROVENANCE → CANONICAL ACTIVATION → NOTE EVENT → VERIFY → INDEX/RELATE → INTELLIGENCE**

For example:

**Google Drive → authorized adapter → source document identity/version → canonical activation → Note Event**

The customer does not need to understand this internal pipeline. The product experience can simply be:

> **CONNECT YOUR KNOWLEDGE.**

## 8. Agent Independence

Any capable AI model or agent may operate as the model/execution layer if it can satisfy the Universal Agent Interface and honor Naya Power authority contracts.

Examples include hosted models, coding agents, local models, custom agents, and future model families.

Changing the model MUST NOT require rebuilding canonical memory, provenance, mission state, or network intelligence.

## 9. CCT / CIS / NayaNET Boundary

NayaNET connects independent Naya Power Superbrains through permissioned exchange.

**CCT** preserves provenance, lineage, authorization, and traceability across intelligence flows.

**CIS** compounds validated learning into progressively more useful intelligence.

Federation operates on authorized **knowledge/intelligence**, not unrestricted raw private memory.

A network adapter MUST NOT make a remote node authoritative over another node's private mission, control state, or canonical memory.

## 10. Conformance Requirements

A compatible implementation is conformant only if it can demonstrate:

1. storage can change without changing authority semantics;
2. model/agent can change without losing continuity;
3. external source provenance survives ingestion;
4. durable intelligence follows the canonical event path;
5. mission authority remains distinct from source storage;
6. Priority remains distinct from Torch construction;
7. Torch remains distinct from execution;
8. execution evidence remains tied to observed execution;
9. verification remains distinct from storage;
10. Smart Note promotion remains distinct from candidate generation;
11. CSI compounds only validated learning;
12. successor state can be restored without reconstructing conversation history;
13. permissions are explicit and revocable at federation boundaries;
14. derived indexes remain rebuildable from canonical authority.

## 11. Non-Goals

This contract does NOT define:

- a new memory store;
- a new event store;
- a new mission store;
- a new execution engine;
- a new verification engine;
- a new Smart Note authority;
- a new promotion engine;
- a new CSI engine;
- a mandatory cloud provider;
- a mandatory database;
- a mandatory model provider.

It composes the authorities already defined by Naya Power.

## 12. North Star

The purpose is not to make every system look like GitHub.

The purpose is to make the **Naya Power intelligence contract portable across models, agents, storage systems, and organizations while preserving authority, provenance, verification, continuity, and compounding intelligence.**
