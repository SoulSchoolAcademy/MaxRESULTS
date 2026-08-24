import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("oscar", Path(__file__).with_name("oscar.py"))
oscar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oscar)


class OscarTests(unittest.TestCase):
    def setUp(self):
        self.claim = {
            "schema": "naya-power-claim/v1",
            "claim_id": "CL-OSCAR-1",
            "statement": "Runtime satisfies its acceptance criteria",
            "success_criteria": ["tests pass", "current commit is verified"],
            "status": "VERIFIED",
        }
        self.evidence = {
            "schema": "naya-power-evidence/v1",
            "evidence_id": "EV-OSCAR-1",
            "claim_id": "CL-OSCAR-1",
            "observed_at": "2026-08-24T02:30:00Z",
            "method": "ci_test",
            "command": "python tests.py",
            "observed_output": "all tests passed",
            "result": "PASS",
            "commit_sha": "abc123",
            "environment": "github-actions",
            "source": "workflow-run-1",
            "criteria_covered": ["tests pass", "current commit is verified"],
        }

    def test_accepts_independently_sufficient_package(self):
        result = oscar.challenge(self.claim, [self.evidence], "abc123")
        self.assertEqual(result["verdict"], "ACCEPT")
        self.assertTrue(result["independent"])
        self.assertTrue(result["promotion_allowed"])

    def test_rejects_model_assertion(self):
        result = oscar.challenge(self.claim, [dict(self.evidence, method="model_assertion")], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_memory_assertion(self):
        result = oscar.challenge(self.claim, [dict(self.evidence, method="memory_assertion")], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_user_assertion(self):
        result = oscar.challenge(self.claim, [dict(self.evidence, method="user_assertion")], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_retrieved_content(self):
        result = oscar.challenge(self.claim, [dict(self.evidence, method="retrieved_content")], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_wrong_commit(self):
        result = oscar.challenge(self.claim, [self.evidence], "different")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_stale_or_missing_criteria_coverage(self):
        result = oscar.challenge(self.claim, [dict(self.evidence, criteria_covered=["tests pass"])], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_contradictory_result(self):
        result = oscar.challenge(self.claim, [dict(self.evidence, result="FAIL")], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_empty_output(self):
        result = oscar.challenge(self.claim, [dict(self.evidence, observed_output="")], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_missing_command(self):
        result = oscar.challenge(self.claim, [dict(self.evidence, command="")], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_cross_claim_evidence(self):
        result = oscar.challenge(self.claim, [dict(self.evidence, claim_id="OTHER")], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_unverified_claim(self):
        result = oscar.challenge(dict(self.claim, status="UNVERIFIED"), [self.evidence], "abc123")
        self.assertEqual(result["verdict"], "REJECT")

    def test_rejects_no_evidence(self):
        result = oscar.challenge(self.claim, [], "abc123")
        self.assertEqual(result["verdict"], "REJECT")


if __name__ == "__main__":
    unittest.main()
