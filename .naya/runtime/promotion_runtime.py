#!/usr/bin/env python3
"""Deterministic promotion boundary for Claim -> Evidence -> Verification -> Oscar."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from typing import Any

LEVELS = ["UNVERIFIED", "BUILDER_VERIFIED", "OSCAR_ACCEPTED", "CANONICAL_VERIFIED", "PRODUCTION_SAFE"]
FORBIDDEN_METHODS = {"model_assertion", "memory_assertion", "user_assertion", "retrieved_content"}


def fail(reasons: list[str]) -> dict[str, Any]:
    return {"eligible": False, "level": "UNVERIFIED", "reasons": reasons}


def evaluate(package: dict[str, Any], current_commit: str) -> dict[str, Any]:
    reasons: list[str] = []
    claim = package.get("claim") or {}
    evidence = package.get("evidence") or []
    oscar = package.get("oscar") or {}
    target = package.get("target", "CANONICAL_VERIFIED")
    if target not in LEVELS:
        return fail([f"unknown target level: {target}"])
    if claim.get("status") != "VERIFIED":
        reasons.append("builder verification is not VERIFIED")
    criteria = claim.get("success_criteria")
    if not isinstance(criteria, list) or not criteria:
        reasons.append("claim has no success criteria")
    if not claim.get("claim_id") or not claim.get("source"):
        reasons.append("claim provenance is missing")
    if not evidence:
        reasons.append("qualifying evidence is missing")
    passing, failing = [], []
    for item in evidence:
        if item.get("commit_sha") == current_commit and item.get("result") == "FAIL":
            failing.append(item)
        if item.get("result") != "PASS":
            continue
        if item.get("method") in FORBIDDEN_METHODS:
            continue
        if item.get("commit_sha") != current_commit:
            continue
        if not item.get("source") or not item.get("environment") or not item.get("command") or not item.get("observed_at"):
            continue
        if item.get("superseded_at") is not None or item.get("status") == "SUPERSEDED":
            continue
        passing.append(item)
    if passing and failing:
        reasons.append("conflicting current evidence contains both PASS and FAIL")
    if not passing:
        reasons.append("no current, qualifying, non-superseded PASS evidence with provenance")
    evidence_criteria = set().union(*(set(e.get("criteria_covered") or []) for e in passing)) if passing else set()
    if set(criteria or []) - evidence_criteria:
        reasons.append("qualifying evidence does not cover every success criterion")
    if target in {"OSCAR_ACCEPTED", "CANONICAL_VERIFIED", "PRODUCTION_SAFE"}:
        if oscar.get("verdict") != "ACCEPT":
            reasons.append("Oscar verdict is not ACCEPT")
        if oscar.get("independent") is not True:
            reasons.append("Oscar is not marked independent")
        if oscar.get("promotion_allowed") is not True:
            reasons.append("Oscar did not allow promotion")
        if oscar.get("expected_commit") != current_commit:
            reasons.append("Oscar evidence is bound to a different commit")
        covered = set(oscar.get("criteria_covered") or [])
        if set(criteria or []) - covered:
            reasons.append("Oscar does not cover every success criterion")
        if oscar.get("claim_id") != claim.get("claim_id"):
            reasons.append("Oscar claim_id does not match claim")
    if target == "CANONICAL_VERIFIED" and package.get("promotion_decision") != "PROMOTE":
        reasons.append("canonical promotion requires an explicit PROMOTE decision")
    if target == "PRODUCTION_SAFE":
        production = [e for e in passing if e.get("method") == "production_test" and e.get("environment") == "production"]
        if not production:
            reasons.append("PRODUCTION_SAFE requires qualifying production evidence")
        if package.get("promotion_decision") != "PROMOTE":
            reasons.append("production promotion requires an explicit PROMOTE decision")
    if reasons:
        return fail(reasons)
    level = "BUILDER_VERIFIED"
    if target in {"OSCAR_ACCEPTED", "CANONICAL_VERIFIED", "PRODUCTION_SAFE"}:
        level = "OSCAR_ACCEPTED"
    if target == "CANONICAL_VERIFIED":
        level = "CANONICAL_VERIFIED"
    if target == "PRODUCTION_SAFE":
        level = "PRODUCTION_SAFE"
    return {"eligible": True, "level": level, "claim_id": claim["claim_id"], "current_commit": current_commit, "target": target, "passing_evidence": [e["evidence_id"] for e in passing], "promotion_decision": package.get("promotion_decision"), "reasons": []}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("package")
    ap.add_argument("--commit", required=True)
    args = ap.parse_args()
    package = json.loads(Path(args.package).read_text(encoding="utf-8"))
    result = evaluate(package, args.commit)
    print(json.dumps(result, indent=2))
    return 0 if result.get("eligible") else 1

if __name__ == "__main__":
    sys.exit(main())
