"""Course Repository"""
from sqlalchemy.orm import Session
from app.core.database import Course

class CourseRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data):
        course = Course(**data.dict())
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course
    
    def get_by_id(self, course_id: int):
        return self.db.query(Course).filter(Course.id == course_id).first()
    
    def get_by_code(self, code: str):
        return self.db.query(Course).filter(Course.code == code).first()
    
    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Course).offset(skip).limit(limit).all()
    
    def get_by_department(self, dept_id: int):
        return self.db.query(Course).filter(Course.department_id == dept_id).all()
    
    def get_by_level(self, level: int):
        return self.db.query(Course).filter(Course.level == level).all()
    
    def update(self, course_id: int, data):
        course = self.get_by_id(course_id)
        if course:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(course, key, value)
            self.db.commit()
            self.db.refresh(course)
        return course
    
    def delete(self, course_id: int):
        course = self.get_by_id(course_id)
        if course:
            self.db.delete(course)
            self.db.commit()
        return course
