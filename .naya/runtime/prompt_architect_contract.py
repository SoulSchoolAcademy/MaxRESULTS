#!/usr/bin/env python3
"""Machine validation for Prompt Architect execution specifications."""
from __future__ import annotations
import argparse, json
from pathlib import Path

REQUIRED=("goal","vision","mission","north_star","current_project","current_state","known_context","unknowns","protected_baseline","constraints","inputs","required_actions","quality_standard","output_requirements","verification_requirements","evidence_requirements","authorization_boundary","failure_handling","learning_capture","receipt_requirements","next_execution")
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'.naya'/'memory'/'PROMPT-ARCHITECT-CONTRACT-REPORT.json'

def validate(spec):
    errors=[]
    for key in REQUIRED:
        if key not in spec or spec[key] in (None,'',[],{}): errors.append(f'missing prompt contract field: {key}')
    if spec.get('quality_standard') not in ('AAA','10-STAR','AAA/10-STAR'):
        errors.append('quality_standard must declare AAA/10-Star service')
    if spec.get('next_execution') and not isinstance(spec['next_execution'],(dict,str)):
        errors.append('next_execution must be a structured handoff or canonical path')
    return errors

def self_test():
    good={k:'test' for k in REQUIRED}; good['quality_standard']='AAA/10-STAR'; assert validate(good)==[]
    bad=dict(good); del bad['north_star']; bad['quality_standard']='MINIMUM'; errors=validate(bad); assert any('north_star' in x for x in errors) and any('quality_standard' in x for x in errors)
    print('PASS — Prompt Architect positive and deliberate-failure tests GREEN'); return 0

def validate_fixture(path):
    spec=json.loads(Path(path).read_text(encoding='utf-8')); errors=validate(spec); report={'schema_version':1,'status':'GREEN' if not errors else 'RED','error_count':len(errors),'errors':errors}; REPORT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8'); print(json.dumps(report,indent=2)); return 0 if not errors else 1

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='command',required=True); sub.add_parser('self-test'); v=sub.add_parser('validate'); v.add_argument('path'); args=ap.parse_args(); return self_test() if args.command=='self-test' else validate_fixture(args.path)
if __name__=='__main__': raise SystemExit(main())
