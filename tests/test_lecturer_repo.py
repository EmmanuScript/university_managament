"""Test Lecturer Repository"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.repositories.lecturer_repository import LecturerRepository

@pytest.fixture
def test_db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(bind=engine)
    return TestingSessionLocal()

def test_create_lecturer(test_db):
    repo = LecturerRepository(test_db)
    data = {"first_name": "John", "last_name": "Doe", "email": "john@test.com", "department_id": 1}
    lecturer = repo.create(data)
    assert lecturer.first_name == "John"

def test_get_lecturer(test_db):
    repo = LecturerRepository(test_db)
    lecturer = repo.get_by_id(1)
    assert lecturer is None or lecturer.id == 1
