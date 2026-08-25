#!/usr/bin/env python3
"""Regression tests for the execution-continuity contract."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / ".naya" / "runtime" / "continuity_enforcement.py"
spec = importlib.util.spec_from_file_location("continuity_enforcement", RUNTIME)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def test_positive_and_deliberate_failures():
    assert module.self_test() == 0


def test_current_canonical_corpus():
    code, report = module.validate()
    assert code == 0, report
    assert report["status"] == "GREEN"


if __name__ == "__main__":
    raise SystemExit(0 if module.self_test() == 0 else 1)
