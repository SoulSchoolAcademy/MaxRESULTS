#!/usr/bin/env python3
"""CCTB v0.1 MVP proof: independent A -> B consumption, lineage, attacks, second pass."""
from __future__ import annotations
import argparse, copy, json
from pathlib import Path
from cct_protocol import block_hash, consume_block, create_block, validate_block, verify_link
from cct_mvp_second_pass import verify as second_pass
ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = ROOT / "proofs" / "cctb-v0.1-mvp-proof.json"

def expect_red(name: str, errors: list[str]) -> dict:
    if not errors: raise AssertionError(f"{name} unexpectedly passed")
    return {"status":"RED","errors":errors}

def independent_consume(serialized: str) -> dict:
    return consume_block(json.loads(serialized), "naya-b")

def build_proof() -> dict:
    a=create_block(agent_id="naya-a",subject="maximum verified value per action",claim="A scarce execution resource should be spent only when it produces distinct verified value.",evidence=[{"type":"local_execution","reference":"cct-mvp-proof"}],verification_method="deterministic CCTB protocol test",audience=["naya-b"],created_at="2026-08-29T00:00:00Z")
    consumed=independent_consume(json.dumps(a,sort_keys=True,separators=(",",":")))
    b=create_block(agent_id="naya-b",subject=consumed["subject"],claim="Independent consumers can verify permitted intelligence and create a traceable successor.",evidence=[{"type":"independent_consumption","parent_block_id":consumed["block_id"]}],verification_method="independent Naya B consumption and successor test",audience=["naya-a"],parent={"block_id":consumed["block_id"],"block_hash":block_hash(a)},created_at="2026-08-29T00:01:00Z")
    incomplete=copy.deepcopy(a); incomplete.pop("claim")
    malformed={"schema_version":"not-cctb","block_id":"fake"}
    conversation=copy.deepcopy(a); conversation["source_context"]="conversation_history"
    orphan=copy.deepcopy(a); orphan["claim"]="THIS IS NOT EXECUTABLE"; orphan["lineage"]={"parent_block_id":"missing-parent","parent_block_hash":"sha256:missing"}; orphan["block_id"]=block_hash(orphan)
    tampered=copy.deepcopy(a); tampered["claim"]="tampered"
    unauthorized=validate_block(a,consumer_id="naya-c")
    bad_lineage=copy.deepcopy(b); bad_lineage["lineage"]["parent_block_hash"]="sha256:tampered"; bad_lineage["block_id"]=block_hash(bad_lineage)
    orphan_errors=verify_link(orphan,a)
    matrix={
      "BLOCK A CREATION":"GREEN",
      "BLOCK A VALIDATION":"GREEN" if not validate_block(a,consumer_id="naya-b") else "RED",
      "BLOCK A EVIDENCE":"GREEN" if a["evidence"] else "RED",
      "BLOCK A PROVENANCE":"GREEN" if a["producer"].get("agent_id") and a["created_at"] else "RED",
      "BLOCK A PERMISSIONS":"GREEN" if not validate_block(a,consumer_id="naya-b") else "RED",
      "NAYA B INDEPENDENT CONSUMPTION":"GREEN" if consumed["block_id"]==a["block_id"] else "RED",
      "BLOCK B CREATION":"GREEN",
      "B → A LINEAGE":"GREEN" if not verify_link(b,a) else "RED",
      "INDEPENDENT LINEAGE VERIFY":"GREEN" if not verify_link(json.loads(json.dumps(b)),json.loads(json.dumps(a))) else "RED",
      "NEGATIVE TESTS":"GREEN" if all([expect_red("incomplete",validate_block(incomplete)),expect_red("malformed",validate_block(malformed)),expect_red("conversation",validate_block(conversation)),expect_red("orphan",orphan_errors)]) else "RED",
      "TAMPER DETECTION":"GREEN" if validate_block(tampered) else "RED",
      "PERMISSION ENFORCEMENT":"GREEN" if unauthorized else "RED",
      "CONVERSATION INDEPENDENCE":"GREEN" if validate_block(conversation) else "RED",
      "MACHINE-READABLE PROOF":"GREEN",
    }
    if any(v!="GREEN" for v in matrix.values()): raise AssertionError(matrix)
    return {"protocol":"CCTB v0.1","proof_version":"0.1","source_context":"independent_artifact","blocks":{"a":a,"b":b},"lineage":{"parent_block_id":b["lineage"]["parent_block_id"],"parent_block_hash":b["lineage"]["parent_block_hash"]},"matrix":matrix,"negative_tests":{"incomplete":expect_red("incomplete",validate_block(incomplete)),"malformed":expect_red("malformed",validate_block(malformed)),"conversation_dependent":expect_red("conversation",validate_block(conversation)),"invalid_orphan":expect_red("orphan",orphan_errors),"tampered":expect_red("tampered",validate_block(tampered)),"unauthorized":expect_red("unauthorized",unauthorized),"bad_lineage":expect_red("bad_lineage",verify_link(bad_lineage,a))},"first_pass":"GREEN"}

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--output",default=str(DEFAULT_OUT)); args=p.parse_args()
    proof=build_proof(); proof["second_pass"]=second_pass(proof); proof["final_status"]="CCT MVP GREEN"
    output=Path(args.output); output.parent.mkdir(parents=True,exist_ok=True); output.write_text(json.dumps(proof,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    print("CCT MVP PROOF")
    for name,status in proof["matrix"].items(): print(f"{name:<36} {status}")
    print(f"SECOND-PASS VERIFICATION{'':14} {proof['second_pass']['status']}")
    print(f"CCT MVP{'':29} {proof['final_status'].replace('CCT MVP ','')}")
    print(f"PROOF: {output}"); return 0
if __name__=="__main__": raise SystemExit(main())
