"""Grade Repository"""
from sqlalchemy.orm import Session
from app.core.database import Grade

class GradeRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data):
        grade = Grade(**data.dict())
        self.db.add(grade)
        self.db.commit()
        self.db.refresh(grade)
        return grade
    
    def get_by_id(self, grade_id: int):
        return self.db.query(Grade).filter(Grade.id == grade_id).first()
    
    def get_by_student(self, student_id: int):
        return self.db.query(Grade).filter(Grade.student_id == student_id).all()
    
    def get_by_course(self, course_id: int):
        return self.db.query(Grade).filter(Grade.course_id == course_id).all()
    
    def get_by_student_course(self, student_id: int, course_id: int):
        return self.db.query(Grade).filter(
            Grade.student_id == student_id,
            Grade.course_id == course_id
        ).first()
    
    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Grade).offset(skip).limit(limit).all()
    
    def update(self, grade_id: int, data):
        grade = self.get_by_id(grade_id)
        if grade:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(grade, key, value)
            self.db.commit()
            self.db.refresh(grade)
        return grade
