"""Lecturer Service"""
from app.repositories.lecturer_repository import LecturerRepository
from app.schemas import LecturerCreate, LecturerUpdate
from sqlalchemy.orm import Session

class LecturerService:
    def __init__(self, db: Session):
        self.repository = LecturerRepository(db)
    
    def create_lecturer(self, data: LecturerCreate):
        return self.repository.create(data)
    
    def get_lecturer(self, lecturer_id: int):
        return self.repository.get_by_id(lecturer_id)
    
    def get_all_lecturers(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
    
    def get_lecturers_by_department(self, dept_id: int):
        return self.repository.get_by_department(dept_id)
    
    def update_lecturer(self, lecturer_id: int, data: LecturerUpdate):
        return self.repository.update(lecturer_id, data)
    
    def delete_lecturer(self, lecturer_id: int):
        return self.repository.delete(lecturer_id)
    
    def get_lecturer_by_email(self, email: str):
        return self.repository.get_by_email(email)
