# CCTB v0.1 — Collective Chain Technology Block Protocol

**Status:** Experimental protocol specification  
**Technology:** Collective Chain Technology (CCT)  
**Block protocol:** CCTB  
**Network:** NayaNet

## 1. What we are building

CCT is an intelligence-network architecture for moving **verified learning**, rather than raw data, between autonomous personal AI systems.

A **CCTB intelligent block** is a portable, permissioned unit of knowledge or learning that carries its meaning, evidence, verification state, provenance, permissions, and lineage. A receiving Naya can independently validate and consume the block without access to the originating conversation.

NayaNet is the network in which these blocks may be exchanged by permission. CCTB is the protocol that defines what a trustworthy exchanged intelligence block must contain and how its lineage is verified.

### Plain-language answer

> **Blockchain records and verifies transactions. CCTB records, verifies, transports, and compounds the lifecycle of verified intelligence.**

The comparison is useful, but CCT is **not a blockchain**. It does not require mining, a global consensus ledger, cryptocurrency, or one universal chain. It is closer to a permissioned, evidence-backed intelligence provenance graph in which many autonomous systems can create local chains of learning and link them when authorized.

## 2. Protocol layers

### Contract Layer
Defines the minimum semantic contract for an intelligent block:

- identity and schema;
- producer/agent identity;
- subject and claim/learning;
- evidence references;
- verification state;
- permissions;
- timestamps;
- lineage references.

### Trust Layer
Makes a block independently checkable:

- deterministic canonical representation;
- content hash / block ID;
- verification status;
- evidence references;
- producer provenance;
- parent block hash when linked;
- explicit permission scope.

### Network Layer
Defines exchange without prescribing a single transport:

- publish/export a block;
- discover an authorized block;
- import/consume a block;
- create a linked successor;
- preserve source and parent lineage.

Transport may later be implemented through NayaNet bridges, APIs, repositories, or other infrastructure. Transport is not part of the v0.1 proof.

### Proof Layer
Defines what must be demonstrated before a block is trusted:

1. block structure is valid;
2. block ID matches canonical content;
3. evidence and verification state are present;
4. permissions allow the consumer;
5. the consumer needs no originating conversation;
6. a successor preserves parent identity/hash;
7. lineage can be followed deterministically.

## 3. Canonical intelligent block

The v0.1 reference shape is:

```json
{
  "schema_version": "cctb-0.1",
  "block_id": "sha256:...",
  "block_type": "learning",
  "producer": {"agent_id": "naya-a"},
  "created_at": "2026-08-29T00:00:00Z",
  "subject": "...",
  "claim": "...",
  "evidence": [{"type": "repository_test", "ref": "..."}],
  "verification": {"status": "VERIFIED", "method": "..."},
  "permissions": {"scope": "network:approved", "audience": ["naya-b"]},
  "lineage": {"parent_block_id": null, "parent_block_hash": null}
}
```

`block_id` is derived from the canonical block content excluding `block_id` itself. This makes identity deterministic and makes tampering observable.

## 4. Lineage

A block with no parent is a root intelligence block. A successor block references its parent by both `parent_block_id` and `parent_block_hash`.

This creates a verifiable chain/DAG of intelligence:

`A₀ → B₁ → C₂ → ...`

Multiple roots and branches are valid. A global single chain is not required.

## 5. Permission model

CCTB is permissioned by design. A block is not globally shareable merely because it exists. The permission scope must explicitly allow the intended consumer or network scope.

Future versions may add capability tokens, revocation, encryption, selective disclosure, and organization policies. These are deliberately outside the v0.1 proof.

## 6. Smallest proof

The first protocol proof is intentionally small:

1. **Naya A** creates a verified intelligent block.
2. A computes its deterministic block identity.
3. **Naya B** receives only that durable block plus the permission necessary to consume it.
4. B independently verifies the block and consumes its learning.
5. B creates a new verified block that references A's block ID and hash.
6. The verifier proves that B's block has valid parent lineage.

If this succeeds repeatedly, the core protocol is demonstrated. Federation scale, routing, discovery, storage, conflict resolution, reputation, and optimization become subsequent engineering layers rather than prerequisites for proving the concept.

## 7. Human value

For humans, CCTB turns valuable learning into reusable, permission-controlled intelligence instead of disposable conversation history.

For personal AIs, it reduces isolated learning silos: an AI can consume verified learning produced elsewhere without pretending that unverified text is truth.

For organizations, it can preserve institutional knowledge with provenance and permission boundaries intact.

For NayaNet, the optimization target is **more verified useful learning reused successfully**, not more blocks.

## 8. Safety and quality boundaries

CCTB must not silently convert claims into facts. Verification status, evidence, provenance, permissions, and uncertainty remain explicit.

The protocol must preserve:

- human ownership and authority;
- privacy by default;
- permissioned sharing;
- provenance;
- evidence-backed claims;
- contradiction handling;
- revocation/correction paths in later versions.

## 9. MPA alignment

CCTB follows the Naya-wide **MPA — Maximum Value Per Action** doctrine. A block is valuable when it creates durable, verified learning that can be reused. The protocol therefore measures success by verified reuse and useful outcomes, not activity or block count.

## 10. v0.1 acceptance criteria

- deterministic block creation;
- deterministic verification;
- independent consumption with zero conversation context;
- permission enforcement;
- tamper detection;
- parent ID/hash lineage;
- two-Naya A→B→successor proof;
- machine-readable proof output.

**Next boundary:** do not build federation infrastructure until this smallest proof is GREEN.
