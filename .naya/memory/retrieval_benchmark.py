#!/usr/bin/env python3
"""Baseline retrieval benchmark for the existing deterministic retrieval path.

This intentionally measures the current implementation before claiming semantic
retrieval improvement. It does not pretend lexical TF-IDF is a vector database.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import smart_notes_v3 as brain

CASES = [
    {"query":"Superbrain CIS Naya Power","expected_tokens":["superbrain","cis"]},
    {"query":"execution continuity learning","expected_tokens":["continuity","learning"]},
    {"query":"duplicate entity resolution","expected_tokens":["duplicate","entity"]},
    {"query":"Daily Intelligence","expected_tokens":["daily","intelligence"]},
]

def run() -> dict:
    results=[]
    for case in CASES:
        ranked=brain.retrieve(case["query"], limit=5)
        texts=[brain.all_text(e).lower() for _,e in ranked]
        hits=sum(1 for token in case["expected_tokens"] if any(token in text for text in texts))
        results.append({"query":case["query"],"returned_event_ids":[e["event_id"] for _,e in ranked],"top_scores":[round(score,3) for score,_ in ranked],"expected_token_coverage":round(hits/len(case["expected_tokens"]),3)})
    coverage=sum(x["expected_token_coverage"] for x in results)/len(results) if results else 1.0
    return {"schema_version":1,"status":"BASELINE","retrieval_engine":"lexical+TFIDF-cosine+metadata+graph boost","semantic_vector_engine":False,"case_count":len(results),"mean_expected_token_coverage":round(coverage,3),"cases":results,"next_measurement":"Re-run this exact corpus after a real semantic/vector adapter is integrated; compare precision/recall and ranking metrics."}

if __name__ == "__main__": print(json.dumps(run(), indent=2, ensure_ascii=False))
