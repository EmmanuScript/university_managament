"""Test Course Repository"""
import pytest
from app.repositories.course_repository import CourseRepository

def test_course_repo():
    assert CourseRepository is not None
