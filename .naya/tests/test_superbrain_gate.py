#!/usr/bin/env python3
"""Deterministic regression checks for the canonical Superbrain runtime."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / '.naya' / 'memory'
RUNTIME = MEMORY / 'smart_notes_v3.py'
INDEX = MEMORY / 'events' / 'INDEX.json'
GRAPH = MEMORY / 'RELATIONSHIP-GRAPH.json'


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


mod = load_module('smart_notes_v3', RUNTIME)
graph_mod = load_module('relationship_graph', MEMORY / 'relationship_graph.py')
audit_mod = load_module('duplicate_entity_audit', MEMORY / 'duplicate_entity_audit.py')

errors = mod.validate()
assert not errors, 'canonical validation failed: ' + '; '.join(errors)

loaded = [(p, e) for p, e in mod.load_events() if '__parse_error__' not in e]
assert loaded, 'no canonical events found'
assert INDEX.exists(), 'canonical index missing'

idx = json.loads(INDEX.read_text(encoding='utf-8'))
ids = {e['event_id'] for _, e in loaded}
indexed = {e['event_id'] for e in idx['events']}
assert ids == indexed, f'index mismatch: canonical={len(ids)} indexed={len(indexed)}'

# Every meaningful canonical event must have a readable note representation.
for path, event in loaded:
    reps = mod.reps(event)
    assert reps, f'{event.get("event_id")}: missing representations'
    rep_ids = {r.get('id') for r in reps}
    assert any(str(x).startswith('SN-') for x in rep_ids), f'{event.get("event_id")}: no readable note representation'

# Exact duplicates are a hard failure; ambiguous candidates are surfaced, never merged.
audit = audit_mod.audit()
assert audit['exact_duplicate_count'] == 0, f'exact duplicate events detected: {audit["exact_duplicate_event_ids"]}'

# Relationship graph must be reproducible from canonical events.
graph = graph_mod.build()
assert GRAPH.exists(), 'relationship graph was not generated'
assert graph['event_count'] == len(loaded), 'relationship graph node count mismatch'
assert set(graph['nodes']) == ids, 'relationship graph node set mismatch'

# Retrieval must return deterministic results for a canonical query.
results = mod.retrieve('Superbrain CIS Naya Power', limit=5)
assert results, 'retrieval returned no results'
assert any('superbrain' in mod.all_text(e).lower() for _, e in results), 'retrieval failed to surface Superbrain context'

# Daily CIS must be source-event based and explicitly require verification.
report = mod.daily_report('2026-08-25', 'America/Vancouver')
assert report['report_type'] == 'DAILY_INTELLIGENCE_REPORT'
assert report['verification_required'] is True
assert isinstance(report['source_event_ids'], list)

print('PASS — Superbrain regression suite GREEN')
print(f'canonical_events={len(loaded)}')
print(f'retrieval_results={len(results)}')
print(f'graph_edges={graph["edge_count"]}')
print(f'daily_source_events={len(report["source_event_ids"])}')
