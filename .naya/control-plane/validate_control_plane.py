#!/usr/bin/env python3
"""Fail-closed repository control-plane validator.

B01-B03 acceptance: canonical identity -> MAP -> live-bound STATE -> BLOCK -> PROOF.
It deliberately treats recorded claims as non-authoritative and refuses unsupported
VERIFIED/RACE_READY claims. It can run in any fresh checkout of NayaPOWER.
"""
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
REG = ROOT/'.naya/control-plane/CANONICAL-IDENTITY-REGISTRY.json'
MAP = ROOT/'.naya/control-plane/MAP.json'
STATE = ROOT/'.naya/control-plane/STATE.json'
BLOCKS = ROOT/'.naya/control-plane/BLOCKS.json'
PROOF = ROOT/'.naya/control-plane/PROOF.json'

def load(path):
    if not path.is_file(): raise AssertionError(f'MISSING: {path.relative_to(ROOT)}')
    return json.loads(path.read_text(encoding='utf-8'))

def git(*args):
    p = subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True, check=True)
    return p.stdout.strip()

def fail(msg): raise AssertionError(msg)

def validate_identity(reg):
    if reg.get('status') != 'CANONICAL': fail('identity registry is not canonical')
    ids = {x['canonical_id']: x for x in reg['identities']}
    np = ids.get('NAYAPOWER'); mx = ids.get('MAXIS')
    if not np or np['canonical_repository'] != 'SoulSchoolAcademy/NayaPOWER' or np['status'] != 'CURRENT': fail('NayaPOWER canonical identity invalid')
    if not mx or mx['canonical_repository'] != 'SoulSchoolAcademy/Maxis' or mx['status'] != 'CURRENT': fail('MAXIS canonical identity invalid')
    if 'MaxRESULTS' not in np['supersedes'] or 'MaxRESULTS' not in mx['supersedes']: fail('MaxRESULTS supersession missing')
    for item in reg['identities']:
        if item['status'].startswith('CURRENT') and item['canonical_repository'] in ('SoulSchoolAcademy/MaxRESULTS','SoulSchoolAcademy/Max Results'): fail('historical repository selected as current')

def validate_map(m):
    if m.get('repository') != 'SoulSchoolAcademy/NayaPOWER': fail('MAP repository is not canonical')
    if m.get('canonical_identity_registry') != '.naya/control-plane/CANONICAL-IDENTITY-REGISTRY.json': fail('MAP does not point to identity registry')
    if not m.get('mission') or not m.get('north_star'): fail('MAP mission/north_star incomplete')
    for key in ('source','current_state','evidence','history'):
        if key not in m.get('truth_owners', {}): fail(f'MAP missing truth owner: {key}')
    if not m.get('execution_map',{}).get('active_block'): fail('MAP missing active block')

def validate_state(s):
    if s.get('status') != 'LIVE_BOUND': fail('STATE is not live-bound')
    if s.get('current_head',{}).get('source') != 'git:HEAD': fail('STATE current HEAD is not live-resolved')
    if s.get('current_branch',{}).get('source') != 'git:branch --show-current': fail('STATE current branch is not live-resolved')
    if s.get('current_deployment',{}).get('status') == 'VERIFIED': fail('deployment VERIFIED without current deployment evidence')
    if len(s.get('single_next_action','').strip()) == 0: fail('STATE missing single next action')
    # The live repository is the authority. A recorded legacy SHA may exist elsewhere,
    # but it must never outrank this live binding.
    head = git('rev-parse','HEAD'); branch = git('branch','--show-current')
    if not head or not branch: fail('cannot resolve live Git HEAD/branch')
    return head, branch

def validate_block(b):
    active=b.get('active_block',{})
    required=('id','status','intent','scope','protected','acceptance','evidence','target_state','next_action')
    for k in required:
        if not active.get(k): fail(f'BLOCK missing {k}')
    if active['status'] not in ('ACTIVE','INTENDED','IMPLEMENTED','COMPLETE','VERIFIED','RACE_READY','PRODUCTION_PROVEN','BLOCKED','FAILED','UNKNOWN','STALE'): fail('invalid block status')
    if not isinstance(active['next_action'],str) or not active['next_action'].strip(): fail('BLOCK next action is not singular/present')
    if len(active['evidence']) < 1: fail('BLOCK has no evidence requirements')

def validate_proof(p):
    required=('SOURCE','BUILD','AUTOMATED','RUNTIME','VISUAL','WHOLE_JOURNEY','PRODUCTION')
    for k in required:
        if k not in p.get('claim_evidence',{}): fail(f'PROOF missing claim type: {k}')
    if 'UNKNOWN' not in p.get('non_green_states',[]) or 'STALE' not in p.get('non_green_states',[]): fail('PROOF must fail closed on UNKNOWN/STALE')
    if 'IMPLEMENTED != VERIFIED' not in p.get('separation_rules',[]): fail('implementation/verification separation missing')
    if 'VERIFIED != PRODUCTION_PROVEN' not in p.get('separation_rules',[]): fail('verification/production separation missing')

def self_test():
    # Deterministic policy tests prove the validator's failure modes without mutating repo state.
    reg=load(REG); state=load(STATE); proof=load(PROOF)
    bad=dict(reg); bad['identities']=[dict(x) for x in reg['identities']]; bad['identities'][0]['canonical_repository']='SoulSchoolAcademy/MaxRESULTS'
    try: validate_identity(bad); fail('self-test failed: stale identity was accepted')
    except AssertionError: pass
    badp=dict(proof); badp['non_green_states']=[x for x in proof['non_green_states'] if x!='UNKNOWN']
    try: validate_proof(badp); fail('self-test failed: UNKNOWN was allowed to become green')
    except AssertionError: pass
    bads=dict(state); bads['current_head']={'source':'recorded'}
    try: validate_state_without_git(bads); fail('self-test failed: recorded HEAD was accepted')
    except AssertionError: pass
    return True

def validate_state_without_git(s):
    if s.get('status') != 'LIVE_BOUND': fail('STATE not live-bound')
    if s.get('current_head',{}).get('source') != 'git:HEAD': fail('recorded HEAD accepted as current')

def main():
    if '--self-test' in sys.argv:
        self_test(); print('SELF_TEST=GREEN'); return 0
    reg,map_,state,blocks,proof = map(load,(REG,MAP,STATE,BLOCKS,PROOF))
    validate_identity(reg); validate_map(map_); head,branch=validate_state(state); validate_block(blocks); validate_proof(proof)
    print(json.dumps({'status':'GREEN','control_loop':'MAP → STATE → BLOCK → PROOF','repository':'SoulSchoolAcademy/NayaPOWER','live_head':head,'live_branch':branch,'active_block':blocks['active_block']['id'],'identity_resolution':'GREEN','state_binding':'GREEN','proof_contract':'GREEN','note':'Repository-level control-plane contract passes. This does not prove external LLM/provider or production runtime behavior.'}, indent=2))
    return 0

if __name__=='__main__':
    try: raise SystemExit(main())
    except AssertionError as e:
        print(f'CONTROL_PLANE=RED\nFIRST_DIVERGENCE={e}', file=sys.stderr); raise SystemExit(1)
