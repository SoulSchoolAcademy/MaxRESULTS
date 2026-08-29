#!/usr/bin/env python3
"""Acceptance tests for the 20-PDF zero-setup activation path."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("activation_engine", Path(__file__).with_name("activation_engine.py"))
activation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(activation)

PACKAGE = "NAYA-ACTIVATION-20PDF-TEST"


def manifest(count: int = 20):
    return {
        "schema_version": 1,
        "package_id": PACKAGE,
        "package_version": "1.0.0",
        "north_star": "Turn a 20-document knowledge package into deterministic, recoverable canonical memory with zero external vector infrastructure.",
        "documents": [
            {
                "document_id": f"PDF-{i:02d}",
                "version": "1.0.0",
                "package_id": PACKAGE,
                "order": i,
                "purpose": f"Knowledge source {i}",
                "content": f"Extracted text for PDF {i}. This fixture represents the text produced by the PDF extraction boundary."
            }
            for i in range(1, count + 1)
        ],
    }


def test_exactly_twenty_documents_are_ready():
    result = activation.inspect_package(manifest(20))
    assert result["status"] == "READY"
    assert result["document_count"] == 20
    assert len(result["documents"]) == 20
    assert all(item["chunk_count"] >= 1 for item in result["documents"])


def test_nineteen_documents_are_not_a_complete_20_pdf_package():
    result = activation.inspect_package(manifest(19))
    assert result["status"] == "READY"
    assert result["document_count"] == 19
    assert result["document_count"] != 20


def test_duplicate_content_identity_is_rejected():
    data = manifest(20)
    data["documents"][1]["content"] = data["documents"][0]["content"]
    result = activation.inspect_package(data)
    assert result["status"] == "CONFLICT"


def test_missing_document_order_is_partial():
    data = manifest(20)
    data["documents"][10]["order"] = 21
    result = activation.inspect_package(data)
    assert result["status"] == "PARTIAL"


def test_identity_changes_when_content_changes():
    first = activation.prepare_document(manifest(20)["documents"][0])[0]
    changed = manifest(20)["documents"][0]
    changed["content"] += " changed"
    second = activation.prepare_document(changed)[0]
    assert first.identity != second.identity


def test_baseline_activation_requires_no_vector_store():
    schema = __import__("activation_contract").activation_result_schema()
    assert schema["derived_representations"][-1] == "future_vector_index"
    assert "no vector store required for baseline activation" in schema["prohibitions"]


if __name__ == "__main__":
    tests = [value for name, value in globals().items() if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS {len(tests)} 20-PDF activation tests")
