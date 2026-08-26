#!/usr/bin/env python3
"""Regression and deliberate-failure tests for dependency-free smart retrieval."""
from __future__ import annotations
import sys
from pathlib import Path

MEMORY = Path(__file__).resolve().parents[1] / 'memory'
sys.path.insert(0, str(MEMORY))
import smart_notes_v3 as brain

exact = brain.retrieve('SE-20260825-220300-superbrain-p0-verification', limit=1)
assert exact, 'exact event-id query returned nothing'
assert exact[0][1]['event_id'] == 'SE-20260825-220300-superbrain-p0-verification'

expanded = brain.expanded_tokens('decision about the Superbrain')
assert 'architecture' in expanded
assert 'continuity' in expanded

filtered = brain.retrieve('Superbrain', limit=20, tag='brain-gate')
assert filtered, 'metadata-filtered retrieval returned nothing'
assert all('brain-gate' in {str(x).lower() for x in (e.get('tags') or [])} for _, e in filtered)

results = brain.retrieve('What was our decision about the Superbrain?', limit=5)
assert results, 'expanded retrieval returned nothing'
assert any('superbrain' in brain.all_text(e).lower() for _, e in results)

# Deliberate failure: unrelated queries must not manufacture zero-score top-N hits.
unknown = brain.retrieve('zxqv-unrecoverable-token-9917', limit=5)
assert unknown == [], 'unmatched query must fail cleanly instead of returning arbitrary events'

# Deliberate failure: impossible metadata constraints must fail closed.
impossible = brain.retrieve('Superbrain', limit=5, project='PROJECT-THAT-DOES-NOT-EXIST')
assert impossible == [], 'impossible metadata filter must fail closed'

print('PASS — retrieval quality regression + deliberate-failure suite GREEN')
print(f'exact_top={exact[0][1]["event_id"]}')
print(f'filtered_results={len(filtered)}')
print(f'expanded_results={len(results)}')
print('unknown_query=EMPTY')
print('impossible_filter=EMPTY')
