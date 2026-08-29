#!/usr/bin/env python3
"""Independent second-pass verifier for a generated CCTB MVP proof."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from cct_protocol import block_hash, validate_block, verify_link

def verify(proof: dict) -> dict:
    a, b = proof["blocks"]["a"], proof["blocks"]["b"]
    checks = {
        "a_hash": block_hash(a) == a["block_id"],
        "b_hash": block_hash(b) == b["block_id"],
        "a_valid_for_b": not validate_block(a, consumer_id="naya-b"),
        "b_valid_for_a": not validate_block(b, consumer_id="naya-a"),
        "lineage_id": b["lineage"]["parent_block_id"] == a["block_id"],
        "lineage_hash": b["lineage"]["parent_block_hash"] == block_hash(a),
        "recorded_lineage_id": proof["lineage"]["parent_block_id"] == a["block_id"],
        "recorded_lineage_hash": proof["lineage"]["parent_block_hash"] == block_hash(a),
        "first_pass_green": proof["first_pass"] == "GREEN",
        "matrix_all_green": all(v == "GREEN" for v in proof["matrix"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    if verify_link(b, a):
        raise AssertionError("independent lineage verification failed")
    return {"status": "GREEN", "verifier": "cct_mvp_second_pass.py", "checks": checks}

def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("proof", type=Path); args = p.parse_args()
    proof = json.loads(args.proof.read_text(encoding="utf-8"))
    proof["second_pass"] = verify(proof)
    proof["final_status"] = "CCT MVP GREEN"
    args.proof.write_text(json.dumps(proof, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("SECOND-PASS VERIFICATION → GREEN")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
