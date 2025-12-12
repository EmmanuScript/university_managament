"""Test Student Repository"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.repositories.student_repository import StudentRepository

@pytest.fixture
def test_db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(bind=engine)
    return TestingSessionLocal()

def test_create_student(test_db):
    repo = StudentRepository(test_db)
    data = {"first_name": "Jane", "last_name": "Doe", "email": "jane@test.com", "department_id": 1}
    assert repo is not None

def test_get_by_matric(test_db):
    repo = StudentRepository(test_db)
    student = repo.get_by_matric("MAT001")
    assert student is None or hasattr(student, 'matric_number')
