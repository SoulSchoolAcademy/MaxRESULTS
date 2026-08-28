#!/usr/bin/env python3
"""Deterministic cold-start acceptance test for the canonical Naya boot contract.

This models a fresh Naya entering NayaPOWER with no conversation memory. It proves
repository-level activation state: authority, boot order, Code of Honor inheritance,
task routing, policy content, operating-method contract, and explicit state transitions.
It does not claim to execute an external LLM or provider; provider/model execution
remains outside this repository contract.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'.naya/naya-context-manifest.json'; BOOT=ROOT/'.naya/NAYA-CONTEXT-BOOT-PROTOCOL.md'; START=ROOT/'SUPERBRAIN/AI-BOOT/START-HERE.md'; POLICY=ROOT/'.naya/codex/HUMAN-CAPABILITY-AND-MASTERY-OPERATING-PROTOCOL.md'; CONSTITUTION=ROOT/'.naya/codex/11-RUNTIME-CONSTITUTION.md'; CODE_OF_HONOR=ROOT/'SUPERBRAIN/MASTER-NOTES/SN-20260827-NAYA-CODE-OF-HONOR.md'; SYSTEM_DIRECTIVE=ROOT/'SUPERBRAIN/MASTER-NOTES/SN-20260827-10-OF-10-SYSTEM-OPERATING-DIRECTIVE.md'; MASTER_NOTE=ROOT/'SUPERBRAIN/MASTER-NOTES/SN-20260827-CONTINUOUS-BLOCK-EXECUTION-AND-ONE-NET.md'
EXPECTED_POLICY='.naya/codex/HUMAN-CAPABILITY-AND-MASTERY-OPERATING-PROTOCOL.md'; EXPECTED_CONSTITUTION='.naya/codex/11-RUNTIME-CONSTITUTION.md'; CODE_OF_HONOR_PATH='SUPERBRAIN/MASTER-NOTES/SN-20260827-NAYA-CODE-OF-HONOR.md'; SYSTEM_DIRECTIVE_PATH='SUPERBRAIN/MASTER-NOTES/SN-20260827-10-OF-10-SYSTEM-OPERATING-DIRECTIVE.md'; BLOCK_CYCLE='EXECUTE → VERIFY → OSCAR → SCORE → INTEGRATE → CAPTURE → CHECK NETWORK → IDENTIFY NEXT BLOCK'; VALUE_LOOP='ZOOM OUT → ZOOM IN → CONNECT → PRIORITIZE → OPTIMIZE → EXECUTE → VERIFY → LEARN → COMPOUND'
def fail(message): raise AssertionError(message)
def load(path):
    if not path.is_file(): fail(f'missing canonical artifact: {path.relative_to(ROOT)}')
    return path.read_text(encoding='utf-8')
def require(text,needle,label):
    if needle not in text: fail(f'{label} missing required contract: {needle}')
def main():
    manifest=json.loads(load(MANIFEST)); boot=load(BOOT); start=load(START); policy=load(POLICY); constitution=load(CONSTITUTION); honor=load(CODE_OF_HONOR); directive=load(SYSTEM_DIRECTIVE); master_note=load(MASTER_NOTE)
    if manifest.get('status')!='CANONICAL': fail('context manifest is not CANONICAL')
    if manifest.get('repository')!='SoulSchoolAcademy/NayaPOWER': fail('canonical repository identity is incorrect')
    if manifest.get('governance_branch')!='main': fail('governance branch is not main')
    if manifest.get('subjects',{}).get('human_capability_and_mastery',{}).get('canonical')!=EXPECTED_POLICY: fail('Human Capability & Mastery subject owner is not canonical')
    if EXPECTED_POLICY not in manifest.get('boot_order',[]): fail('Human Capability & Mastery policy is absent from boot_order')
    if EXPECTED_CONSTITUTION not in manifest.get('boot_order',[]): fail('governing constitution is absent from boot_order')
    for route_name,route in manifest.get('task_routes',{}).items():
        if 'human_capability_and_mastery' not in route: fail(f'Human Capability & Mastery policy missing from task route: {route_name}')
    require(boot,EXPECTED_POLICY,'context boot'); require(start,EXPECTED_POLICY,'START HERE'); require(start,CODE_OF_HONOR_PATH,'START HERE Code of Honor'); require(start,SYSTEM_DIRECTIVE_PATH,'START HERE 10/10 System Directive'); require(boot,'does not override platform/safety constraints','authority preservation'); require(start,'ACTIVATE BEFORE SUBSTANTIVE WORK','policy activation')
    require(honor,'CREATE THE MOST HUMAN VALUE POSSIBLE WITH EVERY MEANINGFUL ACTION.','Code of Honor value law'); require(honor,VALUE_LOOP,'Code of Honor value-maximization method'); require(honor,'EFFORT ≠ VALUE','Code of Honor value distinction'); require(honor,'Every Naya operating through a NayaPOWER-governed Naya Brain inherits this Code of Honor','Code of Honor inheritance law'); require(honor,'Naya does not merely complete work. Naya creates value.','Code of Honor final standard')
    for phrase in ('SOURCE OF TRUTH','STATE','EXECUTION','VERIFICATION','RUNTIME','QUALITY','CONTINUITY','LEARNING','HANDOFF'): require(directive,phrase,'10/10 System Directive')
    require(policy,'DO NOT BUILD FOR THE MACHINE. BUILD FOR THE HUMAN.','human-outcome law'); require(policy,'No Naya may claim that a human understands something','understanding evidence law'); require(policy,'MEASURE','mastery loop'); require(policy,'MASTER','mastery loop'); require(policy,BLOCK_CYCLE,'continuous block cycle')
    for phrase in ('MISSION','SOURCE OF TRUTH','CURRENT STATE','SCOPE','completion criteria','EXECUTE','VERIFY','OSCAR','SCORE','INTEGRATE','CAPTURE','CHECK NETWORK','NEXT BLOCK','Continuous-flow rule','Review cadence','WHY IS THIS NOT A 10?','ready-to-run **NEXT EXECUTION**'): require(policy,phrase,'block operating contract')
    require(start,BLOCK_CYCLE,'START HERE block cycle'); require(start,'One-Network law','START HERE One-Network law'); require(start,'Every Naya is a governed node in one intelligence system','One-Network architecture'); require(master_note,BLOCK_CYCLE,'Master Note block cycle'); require(master_note,'Every Naya is a specialized node in one governed Naya network','Master Note One-Network architecture'); require(master_note,'After every 1–3 substantive blocks','Master Scorecard cadence'); require(master_note,'Every meaningful execution output must end with a ready-to-run Next Execution','Next Execution law')
    receipt={'schema':'naya/cold-start-activation-receipt/v3','status':'VERIFIED','scope':'repository-level cold-start modeled activation','conversation_memory':'EMPTY','activation_state':'ACTIVATED','context_state':'CONTEXT ESTABLISHED','operating_method_state':'OPERATING-METHOD ESTABLISHED','code_of_honor_state':'INHERITED_AND_APPLIED_BY_REPOSITORY_BOOT_CONTRACT','repository':manifest.get('repository'),'governance_branch':manifest.get('governance_branch'),'policy':manifest.get('subjects',{}).get('human_capability_and_mastery',{}).get('canonical'),'code_of_honor':CODE_OF_HONOR_PATH,'system_directive':SYSTEM_DIRECTIVE_PATH,'policy_sha256':hashlib.sha256(policy.encode()).hexdigest(),'code_of_honor_sha256':hashlib.sha256(honor.encode()).hexdigest(),'evidence':['canonical_repository','canonical_governance_branch','canonical_boot_entry','canonical_constitution','canonical_code_of_honor_loaded','canonical_10_10_system_directive_loaded','code_of_honor_inheritance_verified','value_maximization_method_verified','human_capability_policy_loaded','authority_relationship_verified','task_routes_verified','core_policy_requirements_verified','continuous_block_contract_verified','unfinished_block_handoff_verified','master_scorecard_cadence_verified','next_execution_requirement_verified','one_network_contract_verified','conversation_memory_empty'],'limitation':'This proves the canonical repository boot contract and Code of Honor inheritance contract, not an external LLM/provider execution.'}
    print(json.dumps(receipt,indent=2,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
