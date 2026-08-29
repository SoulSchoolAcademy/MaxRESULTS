#!/usr/bin/env python3
"""Minimal repository-local durable CCTB block serialization boundary."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from cct_protocol import block_hash, validate_block

SERIALIZATION_VERSION = "cctb-json-v0.1"


def canonical_bytes(block: dict[str, Any]) -> bytes:
    """Return the canonical durable representation of a CCTB block."""
    return (json.dumps(block, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def artifact_hash(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def write_block(path: Path, block: dict[str, Any]) -> dict[str, str]:
    """Validate and durably write one canonical CCTB block."""
    errors = validate_block(block)
    if errors:
        raise ValueError("cannot persist invalid block: " + "; ".join(errors))
    data = canonical_bytes(block)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return {"path": str(path), "artifact_hash": artifact_hash(data), "block_id": block["block_id"]}


def read_block(path: Path) -> dict[str, Any]:
    """Load one canonical CCTB block and reject corruption or invalid schema."""
    data = path.read_bytes()
    block = json.loads(data.decode("utf-8"))
    if not isinstance(block, dict):
        raise ValueError("durable artifact must contain a JSON object")
    errors = validate_block(block)
    if errors:
        raise ValueError("invalid durable CCTB block: " + "; ".join(errors))
    if canonical_bytes(block) != data:
        raise ValueError("durable artifact is not canonical JSON")
    if block_hash(block) != block["block_id"]:
        raise ValueError("durable artifact block_id does not match canonical content")
    return block


def reload_identity(path: Path) -> dict[str, str]:
    """Reload a block and return the identity that survived persistence."""
    block = read_block(path)
    data = path.read_bytes()
    return {"block_id": block["block_id"], "block_hash": block_hash(block), "artifact_hash": artifact_hash(data)}
