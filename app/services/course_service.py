"""Course Service"""
from app.repositories.course_repository import CourseRepository
from sqlalchemy.orm import Session

class CourseService:
    def __init__(self, db: Session):
        self.repository = CourseRepository(db)
    
    def create_course(self, data):
        return self.repository.create(data)
    
    def get_course(self, course_id: int):
        return self.repository.get_by_id(course_id)
    
    def get_all_courses(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
    
    def get_courses_by_department(self, dept_id: int):
        return self.repository.get_by_department(dept_id)
    
    def get_courses_by_level(self, level: int):
        return self.repository.get_by_level(level)
    
    def update_course(self, course_id: int, data):
        return self.repository.update(course_id, data)
    
    def delete_course(self, course_id: int):
        return self.repository.delete(course_id)
    
    def get_course_by_code(self, code: str):
        return self.repository.get_by_code(code)
