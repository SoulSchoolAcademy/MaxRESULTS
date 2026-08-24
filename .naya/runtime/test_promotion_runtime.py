#!/usr/bin/env python3
import copy
import unittest
from promotion_runtime import evaluate

COMMIT = "a" * 40
CLAIM = {
    "claim_id": "CL-1",
    "status": "VERIFIED",
    "source": "github-actions:1",
    "success_criteria": ["tests pass", "process exits successfully"],
}
EVIDENCE = {
    "evidence_id": "EV-1",
    "result": "PASS",
    "method": "ci_test",
    "commit_sha": COMMIT,
    "source": "workflow-run:1",
    "environment": "github-actions",
    "command": "python tests.py",
    "observed_at": "2026-08-24T02:00:00Z",
}
OSCAR = {
    "claim_id": "CL-1",
    "verdict": "ACCEPT",
    "independent": True,
    "promotion_allowed": True,
    "expected_commit": COMMIT,
    "criteria_covered": ["tests pass", "process exits successfully"],
}


def package(target="CANONICAL_VERIFIED", decision="PROMOTE"):
    return {
        "claim": copy.deepcopy(CLAIM),
        "evidence": [copy.deepcopy(EVIDENCE)],
        "oscar": copy.deepcopy(OSCAR),
        "target": target,
        "promotion_decision": decision,
    }


class PromotionTests(unittest.TestCase):
    def test_builder_verified_oscar_rejected(self):
        p = package("OSCAR_ACCEPTED"); p["oscar"]["verdict"] = "REJECT"
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_builder_verified_stale_evidence(self):
        p = package("BUILDER_VERIFIED"); p["evidence"][0]["commit_sha"] = "b" * 40
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_oscar_accepted_wrong_commit(self):
        p = package("OSCAR_ACCEPTED"); p["oscar"]["expected_commit"] = "b" * 40
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_oscar_accepted_superseded_evidence(self):
        p = package("OSCAR_ACCEPTED"); p["evidence"][0]["superseded_at"] = "2026-08-24T03:00:00Z"
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_oscar_accepted_missing_provenance(self):
        p = package("OSCAR_ACCEPTED"); del p["evidence"][0]["source"]
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_conflicting_evidence(self):
        p = package("BUILDER_VERIFIED")
        conflict = copy.deepcopy(EVIDENCE); conflict["evidence_id"] = "EV-2"; conflict["result"] = "FAIL"
        p["evidence"].append(conflict)
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_production_claim_without_production_evidence(self):
        p = package("PRODUCTION_SAFE")
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_historical_verification_is_not_current(self):
        p = package("OSCAR_ACCEPTED"); p["evidence"][0]["commit_sha"] = "c" * 40
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_verified_state_followed_by_repository_change(self):
        p = package("OSCAR_ACCEPTED")
        r = evaluate(p, "d" * 40); self.assertFalse(r["eligible"])

    def test_retrieved_content_cannot_influence_promotion(self):
        p = package("BUILDER_VERIFIED"); p["evidence"][0]["method"] = "retrieved_content"
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_eligible_is_not_automatically_canonical(self):
        p = package("CANONICAL_VERIFIED", decision=None)
        r = evaluate(p, COMMIT); self.assertFalse(r["eligible"])

    def test_oscar_acceptance_can_reach_eligible(self):
        p = package("OSCAR_ACCEPTED")
        r = evaluate(p, COMMIT); self.assertTrue(r["eligible"]); self.assertEqual(r["level"], "OSCAR_ACCEPTED")

    def test_canonical_requires_explicit_promotion(self):
        p = package("CANONICAL_VERIFIED", decision="PROMOTE")
        r = evaluate(p, COMMIT); self.assertTrue(r["eligible"]); self.assertEqual(r["level"], "CANONICAL_VERIFIED")


if __name__ == "__main__": unittest.main()
