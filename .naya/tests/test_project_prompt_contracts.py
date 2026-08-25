#!/usr/bin/env python3
"""Positive and deliberate-failure tests for project/continuation/prompt contracts."""
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[2]
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path); mod=importlib.util.module_from_spec(spec); assert spec and spec.loader; spec.loader.exec_module(mod); return mod
project=load('project_contract','.naya/runtime/project_execution_contract.py')
prompt=load('prompt_contract','.naya/runtime/prompt_architect_contract.py')

def test_project_contract(): assert project.self_test()==0

def test_prompt_contract(): assert prompt.self_test()==0

def test_current_project_state():
    errors=project.validate_project(project.load(project.PROJECT)); assert errors==errors[:0], errors

def main():
    test_project_contract(); test_prompt_contract(); test_current_project_state(); print('PASS — project, Next Execution, paired representation, learning, and Prompt Architect contracts GREEN')
if __name__=='__main__': main()
