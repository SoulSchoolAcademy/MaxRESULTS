#!/usr/bin/env python3
"""Deterministic zero-setup document activation.

This layer accepts extracted document text (from PDF upload, copy/paste, or a
future hosted uploader), establishes immutable document identity, chunks content
deterministically, detects duplicates/conflicts, and can promote a verified
activation into the existing canonical event writer.

No vector database is required. Canonical memory is authoritative; all search
indexes are derived and reproducible.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable

from activation_contract import validate_manifest

ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / ".naya" / "memory"
ACTIVATION_ROOT = MEMORY / "activations"
STATE_FILE = ACTIVATION_ROOT / "ACTIVATION-STATE.json"
RECEIPT_FILE = ACTIVATION_ROOT / "ACTIVATION-RECEIPT.json"
NEXT_EXECUTION = ".naya/handoffs/NEXT-EXECUTION-20260825-SUPERBRAIN-CONTRACT-ENFORCEMENT.md"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def stable_document_identity(package_id: str, document_id: str, version: str, content: str) -> str:
    payload = f"{package_id}\n{document_id}\n{version}\n{sha256_text(content)}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def chunk_text(text: str, max_chars: int = 2400, overlap: int = 240) -> list[str]:
    """Create deterministic paragraph-aware chunks with bounded overlap."""
    if max_chars <= 0 or overlap < 0 or overlap >= max_chars:
        raise ValueError("chunk bounds are invalid")
    normalized = re.sub(r"\r\n?", "\n", text).strip()
    if not normalized:
        return []
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", normalized) if p.strip()]
    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        candidate = paragraph if not current else current + "\n\n" + paragraph
        if len(candidate) <= max_chars:
            current = candidate
            continue
        if current:
            chunks.append(current)
        if len(paragraph) <= max_chars:
            current = paragraph
            continue
        start = 0
        while start < len(paragraph):
            end = min(start + max_chars, len(paragraph))
            piece = paragraph[start:end].strip()
            if piece:
                chunks.append(piece)
            if end >= len(paragraph):
                break
            start = max(0, end - overlap)
        current = ""
    if current:
        chunks.append(current)
    return chunks


@dataclass(frozen=True)
class ActivatedDocument:
    document_id: str
    version: str
    package_id: str
    order: int
    purpose: str
    content_sha256: str
    identity: str
    chunk_count: int
    status: str = "READY"


def prepare_document(document: dict[str, Any], chunk_size: int = 2400) -> tuple[ActivatedDocument, list[str]]:
    required = ("document_id", "version", "package_id", "order", "purpose", "content")
    missing = [key for key in required if document.get(key) in (None, "")]
    if missing:
        raise ValueError("document missing: " + ", ".join(missing))
    content = str(document["content"])
    chunks = chunk_text(content, max_chars=chunk_size)
    if not chunks:
        raise ValueError(f"document {document['document_id']} has no usable content")
    identity = stable_document_identity(
        str(document["package_id"]), str(document["document_id"]), str(document["version"]), content
    )
    result = ActivatedDocument(
        document_id=str(document["document_id"]),
        version=str(document["version"]),
        package_id=str(document["package_id"]),
        order=int(document["order"]),
        purpose=str(document["purpose"]),
        content_sha256=sha256_text(content),
        identity=identity,
        chunk_count=len(chunks),
    )
    return result, chunks


def inspect_package(manifest: dict[str, Any], chunk_size: int = 2400) -> dict[str, Any]:
    errors = validate_manifest(manifest)
    if errors:
        return {"status": "FAILED", "errors": errors, "documents": []}
    prepared: list[ActivatedDocument] = []
    identities: set[str] = set()
    for document in sorted(manifest["documents"], key=lambda x: x["order"]):
        item, _ = prepare_document(document, chunk_size=chunk_size)
        if item.identity in identities:
            return {"status": "CONFLICT", "errors": [f"duplicate content identity: {item.document_id}"], "documents": []}
        identities.add(item.identity)
        prepared.append(item)
    expected = list(range(1, len(prepared) + 1))
    actual = [item.order for item in prepared]
    if actual != expected:
        return {"status": "PARTIAL", "errors": [f"missing or out-of-order documents: expected {expected}, got {actual}"], "documents": [asdict(x) for x in prepared]}
    return {
        "status": "READY",
        "errors": [],
        "package_id": manifest["package_id"],
        "package_version": manifest["package_version"],
        "document_count": len(prepared),
        "chunk_count": sum(x.chunk_count for x in prepared),
        "documents": [asdict(x) for x in prepared],
    }


def persist_activation_state(result: dict[str, Any], manifest: dict[str, Any]) -> None:
    ACTIVATION_ROOT.mkdir(parents=True, exist_ok=True)
    state = {
        "schema_version": 1,
        "package_id": manifest.get("package_id"),
        "package_version": manifest.get("package_version"),
        "status": result.get("status"),
        "document_count": result.get("document_count", 0),
        "chunk_count": result.get("chunk_count", 0),
        "documents": result.get("documents", []),
        "authoritative_source": "canonical Note Events",
        "derived_indexes": ["events/INDEX.json", "retrieval baseline"],
        "vectors": "OPTIONAL_DERIVED",
        "errors": result.get("errors", []),
    }
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def make_receipt(result: dict[str, Any]) -> dict[str, Any]:
    status = result.get("status")
    return {
        "schema_version": 1,
        "receipt_type": "NAYAPOWER_ACTIVATION",
        "status": "VERIFIED" if status == "READY" else status,
        "verified": status == "READY",
        "package_id": result.get("package_id"),
        "package_version": result.get("package_version"),
        "document_count": result.get("document_count", 0),
        "chunk_count": result.get("chunk_count", 0),
        "canonical_source": "Note Events",
        "derived_representations": ["chunks", "lexical index", "retrieval"],
        "vector_requirement": "NONE",
        "next_execution": NEXT_EXECUTION,
        "errors": result.get("errors", []),
    }


def persist_receipt(result: dict[str, Any]) -> dict[str, Any]:
    ACTIVATION_ROOT.mkdir(parents=True, exist_ok=True)
    receipt = make_receipt(result)
    RECEIPT_FILE.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return receipt


def activate(manifest: dict[str, Any], chunk_size: int = 2400) -> dict[str, Any]:
    """Prepare and persist an activation state/receipt without mutating canonical memory.

    Canonical promotion is deliberately a separate, explicit phase so a malformed
    package can never partially write memory. This is the zero-setup safety boundary.
    """
    result = inspect_package(manifest, chunk_size=chunk_size)
    persist_activation_state(result, manifest)
    persist_receipt(result)
    return result
