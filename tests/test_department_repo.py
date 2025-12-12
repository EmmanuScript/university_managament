"""Test Department Repository"""
import pytest
from app.repositories.department_repository import DepartmentRepository

def test_dept_repo():
    assert DepartmentRepository is not None
