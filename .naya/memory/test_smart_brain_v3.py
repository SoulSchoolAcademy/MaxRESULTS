#!/usr/bin/env python3
import sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.naya/memory'))
import smart_notes_v3 as brain


class SmartBrainV3Tests(unittest.TestCase):
    def test_canonical_events_are_valid(self):
        self.assertEqual(brain.validate(), [], 'canonical Smart Brain validation failed')

    def test_index_is_rebuildable(self):
        data = brain.build_index()
        ids = {e['event_id'] for _, e in brain.load_events() if not e.get('__parse_error__')}
        indexed_ids = {e['event_id'] for e in data['events']}
        self.assertEqual(indexed_ids, ids)
        self.assertEqual(data['version'], '3.0.0')

    def test_hybrid_retrieval_returns_verified_context(self):
        results = brain.retrieve('MAXESS scoring Continue terminal', limit=5)
        self.assertTrue(results)
        self.assertTrue(any(e.get('verification', {}).get('status') == 'VERIFIED' for _, e in results))

    def test_alias_or_concept_retrieval(self):
        results = brain.retrieve('super brain memory architecture CIS', limit=10)
        self.assertTrue(results)
        joined = ' '.join((e.get('title') or e.get('subject') or '').lower() for _, e in results)
        self.assertTrue('smart' in joined or 'cis' in joined or 'memory' in joined)

    def test_daily_report_is_source_linked(self):
        report = brain.daily_report('2026-08-25')
        self.assertEqual(report['report_type'], 'DAILY_INTELLIGENCE_REPORT')
        self.assertIn('source_event_ids', report)
        self.assertTrue(report['verification_required'])


if __name__ == '__main__':
    unittest.main()
