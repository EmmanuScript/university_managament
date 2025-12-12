"""Student Repository"""
from sqlalchemy.orm import Session
from app.core.database import Student
from app.schemas import StudentCreate

class StudentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data: StudentCreate):
        student = Student(**data.dict())
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student
    
    def get_by_id(self, student_id: int):
        return self.db.query(Student).filter(Student.id == student_id).first()
    
    def get_by_matric(self, matric_number: str):
        return self.db.query(Student).filter(Student.matric_number == matric_number).first()
    
    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Student).offset(skip).limit(limit).all()
    
    def get_by_department(self, department_id: int):
        return self.db.query(Student).filter(Student.department_id == department_id).all()
    
    def update(self, student_id: int, data):
        student = self.get_by_id(student_id)
        if student:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(student, key, value)
            self.db.commit()
            self.db.refresh(student)
        return student
    
    def delete(self, student_id: int):
        student = self.get_by_id(student_id)
        if student:
            self.db.delete(student)
            self.db.commit()
        return student
