#!/usr/bin/env python3
"""Machine-readable Superbrain health metrics derived from canonical state."""
from __future__ import annotations
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / ".naya" / "memory"
EVENTS = MEMORY / "events"
sys.path.insert(0, str(MEMORY))
import smart_notes_v3 as brain

def report() -> dict:
    loaded = [(p,e) for p,e in brain.load_events() if not e.get("__parse_error__")]
    ids = {e.get("event_id") for _,e in loaded}
    parse_errors = sum(1 for p,e in brain.load_events() if e.get("__parse_error__"))
    relationships = 0
    orphan_relationships = 0
    for _,e in loaded:
        rel = e.get("relationships", {}) or {}
        for key in ("related","depends_on","supersedes","superseded_by","source_events"):
            vals = rel.get(key, [])
            vals = [vals] if isinstance(vals, str) else (vals or [])
            relationships += len(vals)
            orphan_relationships += sum(1 for target in vals if target not in ids and not str(target).startswith("EXT:"))
    verified = sum(1 for _,e in loaded if (e.get("verification") or {}).get("status") == "VERIFIED")
    receipts = sum(1 for _,e in loaded if (e.get("receipt") or {}).get("receipt_id") or (e.get("verification") or {}).get("receipt") or (e.get("verification") or {}).get("receipt_url"))
    delivery = sum(1 for _,e in loaded if (e.get("delivery") or {}).get("state") or (e.get("verification") or {}).get("feed_status"))
    statuses = {}
    for _,e in loaded: statuses[e.get("status", "UNKNOWN")] = statuses.get(e.get("status", "UNKNOWN"), 0) + 1
    return {"schema_version":1,"status":"GREEN" if parse_errors == 0 and orphan_relationships == 0 else "RED","canonical_event_count":len(ids),"parse_error_count":parse_errors,"relationship_reference_count":relationships,"orphan_relationship_count":orphan_relationships,"verified_event_count":verified,"receipt_completeness":round(receipts/len(ids),4) if ids else 1.0,"delivery_state_completeness":round(delivery/len(ids),4) if ids else 1.0,"status_counts":statuses,"derived_indexes":{"index_exists":(EVENTS/"INDEX.json").exists(),"validation_report_exists":(MEMORY/"VALIDATION-REPORT.json").exists(),"relationship_graph_exists":(MEMORY/"RELATIONSHIP-GRAPH.json").exists()},"note":"Metrics are derived; they do not replace canonical events or authoritative CI."}

if __name__ == "__main__":
    print(json.dumps(report(), indent=2, ensure_ascii=False))
