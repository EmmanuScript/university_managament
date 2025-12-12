"""Student Service"""
from app.repositories.student_repository import StudentRepository
from app.schemas import StudentCreate
from sqlalchemy.orm import Session

class StudentService:
    def __init__(self, db: Session):
        self.repository = StudentRepository(db)
    
    def create_student(self, data: StudentCreate):
        return self.repository.create(data)
    
    def get_student(self, student_id: int):
        return self.repository.get_by_id(student_id)
    
    def get_all_students(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
    
    def get_students_by_department(self, dept_id: int):
        return self.repository.get_by_department(dept_id)
    
    def update_student(self, student_id: int, data):
        return self.repository.update(student_id, data)
    
    def delete_student(self, student_id: int):
        return self.repository.delete(student_id)
    
    def get_student_by_matric(self, matric: str):
        return self.repository.get_by_matric(matric)
