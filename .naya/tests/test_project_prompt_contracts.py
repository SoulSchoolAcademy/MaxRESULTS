#!/usr/bin/env python3
"""Positive and deliberate-failure tests for project/continuation/prompt contracts."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parents[2]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path); mod=importlib.util.module_from_spec(spec); assert spec and spec.loader; spec.loader.exec_module(mod); return mod
project=load('project_contract','.naya/runtime/project_execution_contract.py')
prompt=load('prompt_contract','.naya/runtime/prompt_architect_contract.py')

def test_project_contract(): assert project.self_test()==0

def test_prompt_contract(): assert prompt.self_test()==0

def test_current_project_state():
    errors=project.validate_project(project.load(project.PROJECT)); assert errors==errors[:0], errors

def test_canonical_torch_schema():
    contract=project.load(project.TORCH_CONTRACT)
    assert contract['schema_version']==1
    assert contract['required_fields']==['mission','desired_outcome','current_state','verified','unknown','protected','blocked','decision_recommendation','next_actor','next_action','ready_to_run_execution','expected_output','success_criteria','verification','constraints']
    assert contract['human_continuation']['human_prompt_authoring_required'] is True
    assert 'human_action' in contract['human_continuation']['required_additional_fields']
    assert 'human_return_payload' in contract['human_continuation']['required_additional_fields']

def test_successor_survival_and_negative_contract():
    policy=project.load(project.POLICY)
    good={'mission':'test mission','desired_outcome':'test outcome','current_state':'test state','verified':'test evidence','unknown':'none','protected':'test baseline','blocked':'none','decision_recommendation':'test recommendation','next_action':'Inspect the authoritative continuity contract and run the narrow regression suite now.','next_actor':'successor_naya','ready_to_run_execution':'WHERE: NayaPOWER. WHY: verify the contract. CURRENT STATE: test state. WHAT WAS VERIFIED: test evidence. WHAT IS UNKNOWN: none. WHAT IS PROTECTED: test baseline. WHAT IS BLOCKED: none. WHAT TO READ: contract and tests. WHAT TO DO: run narrow tests. WHAT NOT TO DO: bypass validators. WHAT TO PRESERVE: evidence. WHAT TO VERIFY: exact results. EXPECTED RESULT: tests pass. FAILURE HANDLING: stop at first failure. NEXT DECISION POINT: authoritative gate.','expected_output':'Observed test results and exact first failure if any.','success_criteria':'All positive fixtures pass and all deliberate-negative fixtures fail.','verification':'Run the authoritative project/prompt contract regression suite.','constraints':'test constraints','current_objective':'test objective'}
    assert project.validate_next_action_delivery(good,policy)==[]
    for field in ('next_action','next_actor','ready_to_run_execution','expected_output','success_criteria','verification'):
        bad=json.loads(json.dumps(good)); bad.pop(field,None); assert any(field in e for e in project.validate_next_action_delivery(bad,policy)), field
    vague=json.loads(json.dumps(good)); vague['next_action']='inspect it'; assert any('vague/non-executable' in e for e in project.validate_next_action_delivery(vague,policy))
    human=json.loads(json.dumps(good)); human['next_actor']='human'; assert any('human_prompt_authoring_required' in e for e in project.validate_next_action_delivery(human,policy))
    human['human_prompt_authoring_required']=True; assert any('human continuation missing human_action' in e for e in project.validate_next_action_delivery(human,policy))
    human['human_action']='Paste the requested evidence back to Naya.'; human['human_return_payload']='Paste the exact GitHub screen text.'; assert project.validate_next_action_delivery(human,policy)==[]
    context=json.loads(json.dumps(good)); context['current_state']=''; assert any('reconstructing context' in e for e in project.validate_next_action_delivery(context,policy))

def main():
    test_project_contract(); test_prompt_contract(); test_current_project_state(); test_canonical_torch_schema(); test_successor_survival_and_negative_contract(); print('PASS — project, successor torch, paired representation, learning, and Prompt Architect contracts GREEN')
if __name__=='__main__': main()
