"""Enrollment Repository"""
from sqlalchemy.orm import Session
from app.core.database import Enrollment

class EnrollmentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data):
        enrollment = Enrollment(**data.dict())
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)
        return enrollment
    
    def get_by_id(self, enroll_id: int):
        return self.db.query(Enrollment).filter(Enrollment.id == enroll_id).first()
    
    def get_by_student(self, student_id: int):
        return self.db.query(Enrollment).filter(Enrollment.student_id == student_id).all()
    
    def get_by_course(self, course_id: int):
        return self.db.query(Enrollment).filter(Enrollment.course_id == course_id).all()
    
    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Enrollment).offset(skip).limit(limit).all()
    
    def update(self, enroll_id: int, data):
        enrollment = self.get_by_id(enroll_id)
        if enrollment:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(enrollment, key, value)
            self.db.commit()
            self.db.refresh(enrollment)
        return enrollment
    
    def delete(self, enroll_id: int):
        enrollment = self.get_by_id(enroll_id)
        if enrollment:
            self.db.delete(enrollment)
            self.db.commit()
        return enrollment
