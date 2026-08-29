#!/usr/bin/env python3
"""Positive and deliberate-failure tests for project/continuation/prompt contracts."""
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[2]
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path);mod=importlib.util.module_from_spec(spec);assert spec and spec.loader;spec.loader.exec_module(mod);return mod
project=load('project_contract','.naya/runtime/project_execution_contract.py')
prompt=load('prompt_contract','.naya/runtime/prompt_architect_contract.py')
ARTIFACT='.naya/handoffs/NEXT-EXECUTION-20260825-SUPERBRAIN-CONTRACT-ENFORCEMENT.md'

def valid_successor():
    return {field:('Run the validation and inspect the result' if field=='execution_instructions' else ['verified test'] if field in {'completed_work','verified_evidence','unresolved_issues','constraints','success_criteria','verification_requirements'} else 'test') for field in project.NEXT_FIELDS}

def test_project_contract(): assert project.self_test()==0

def test_prompt_contract(): assert prompt.self_test()==0

def test_current_project_state():
    errors=project.validate_project(project.load(project.PROJECT));assert errors==[],errors

def test_behavioral_matrix():
    valid=valid_successor();assert project.validate_next_execution(valid)==[]
    assert project.validate_next_execution_reference(None)
    assert project.validate_next_execution_reference('arbitrary continuation')
    assert project.validate_next_execution_reference('.naya/handoffs/NEXT-EXECUTION-20990101-MISSING.md')
    incomplete=dict(valid);incomplete.pop('success_criteria');assert any('missing success_criteria' in x for x in project.validate_next_execution(incomplete))
    dependent=dict(valid);dependent['execution_instructions']='Continue from this conversation';assert any('conversation-dependent' in x for x in project.validate_next_execution(dependent))
    orphan={'event_id':'SE-20260825-999999-orphan','continuity':{'execution_state':'COMPLETED'},'ready_to_run_execution':'THIS IS NOT EXECUTABLE'}
    assert any('canonical NEXT-EXECUTION' in x for x in project.validate_event(orphan,{'project_id':'x','project_name':'x'},{}) )

def test_independent_consumption():
    artifact,errors=project.resolve_next_execution(ARTIFACT);assert errors==[],errors
    consumed=project.consume_next_execution(ARTIFACT);assert tuple(consumed)==project.NEXT_FIELDS
    assert all(consumed[field] not in (None,'',[]) for field in project.NEXT_FIELDS)
    assert 'Naya Power Superbrain' in str(consumed['project'])
    assert project.validate_next_execution_reference(ARTIFACT)==[]

def main():
    test_project_contract();test_prompt_contract();test_current_project_state();test_behavioral_matrix();test_independent_consumption();print('INVALID ORPHAN → RED');print('CANONICAL SUCCESSOR → GREEN');print('PASS — project, continuation, Prompt Architect, behavioral matrix, and independent consumption GREEN')
if __name__=='__main__':main()
