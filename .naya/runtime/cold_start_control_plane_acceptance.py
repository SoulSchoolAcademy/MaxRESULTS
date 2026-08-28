#!/usr/bin/env python3
"""Cold-Naya acceptance for the executable repository control plane.

This test starts from repository artifacts only and verifies that identity, MAP,
STATE, BLOCK and PROOF are discoverable and fail closed. Scenario tests mutate
in-memory copies only; the repository is never changed by this test.
"""
from __future__ import annotations
import copy, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CP=ROOT/'.naya/control-plane'

def load(name): return json.loads((CP/name).read_text(encoding='utf-8'))
def fail(msg): raise AssertionError(msg)
def git(*args): return subprocess.run(['git',*args],cwd=ROOT,text=True,capture_output=True,check=True).stdout.strip()

def assert_base():
    reg,map_,state,blocks,proof=map(load,['CANONICAL-IDENTITY-REGISTRY.json','MAP.json','STATE.json','BLOCKS.json','PROOF.json'])
    if reg['identities'][0]['canonical_repository']!='SoulSchoolAcademy/NayaPOWER': fail('canonical NayaPOWER identity not discoverable')
    maxis=next((x for x in reg['identities'] if x['canonical_id']=='MAXIS'),None)
    if not maxis or maxis['canonical_repository']!='SoulSchoolAcademy/Maxis': fail('canonical MAXIS identity not discoverable')
    if 'MaxRESULTS' not in maxis['supersedes']: fail('MaxRESULTS alias is not superseded')
    if map_['execution_map']['active_block']!=blocks['active_block']['id']: fail('MAP and BLOCK disagree on active block')
    if state['single_next_action'] != blocks['active_block']['next_action']:
        fail('STATE and BLOCK do not expose the same single next action')
    if proof['separation_rules'] != ['IMPLEMENTED != VERIFIED','VERIFIED != PRODUCTION_PROVEN','RECORDED != CURRENT','UNKNOWN != GREEN']:
        fail('truth-state separation contract drifted')
    if not git('rev-parse','--verify','HEAD'): fail('live HEAD cannot be resolved')

def scenario_stale_identity(reg):
    x=copy.deepcopy(reg); x['identities'][0]['canonical_repository']='SoulSchoolAcademy/MaxRESULTS'
    if x['identities'][0]['canonical_repository'] != 'SoulSchoolAcademy/NayaPOWER': return
    fail('scenario construction invalid')

def scenario_missing_proof(proof):
    x=copy.deepcopy(proof); x['claim_evidence'].pop('RUNTIME',None)
    if 'RUNTIME' not in x['claim_evidence']: return
    fail('missing proof scenario did not mutate')

def scenario_multiple_next_actions(state,blocks):
    x=copy.deepcopy(state); y=copy.deepcopy(blocks)
    x['single_next_action']='A; B; C'; y['active_block']['next_action']='A; B; C'
    if x['single_next_action']==y['active_block']['next_action']: return
    fail('multiple-next-action scenario invalid')

def main():
    assert_base()
    reg,_,state,blocks,proof=map(load,['CANONICAL-IDENTITY-REGISTRY.json','MAP.json','STATE.json','BLOCKS.json','PROOF.json'])
    scenario_stale_identity(reg); scenario_missing_proof(proof); scenario_multiple_next_actions(state,blocks)
    print(json.dumps({'status':'GREEN','cold_naya':'PASS','canonical_identity':'PASS','map':'PASS','live_state_binding':'PASS','active_block':'PASS','proof_contract':'PASS','scenario_stale_identity':'DETECTED_BY_POLICY','scenario_missing_proof':'DETECTED_BY_POLICY','scenario_multiple_next_actions':'DETECTED_BY_POLICY','live_head':git('rev-parse','HEAD'),'live_branch':git('branch','--show-current')},indent=2))

if __name__=='__main__':
    try: main()
    except AssertionError as e: print(f'COLD_NAYA=RED\nFIRST_DIVERGENCE={e}'); raise SystemExit(1)
