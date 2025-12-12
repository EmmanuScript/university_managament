"""Grade Service"""
from app.repositories.grade_repository import GradeRepository
from sqlalchemy.orm import Session

class GradeService:
    def __init__(self, db: Session):
        self.repository = GradeRepository(db)
    
    def create_grade(self, data):
        return self.repository.create(data)
    
    def get_grade(self, grade_id: int):
        return self.repository.get_by_id(grade_id)
    
    def get_all_grades(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
    
    def get_student_grades(self, student_id: int):
        return self.repository.get_by_student(student_id)
    
    def get_course_grades(self, course_id: int):
        return self.repository.get_by_course(course_id)
    
    def update_grade(self, grade_id: int, data):
        return self.repository.update(grade_id, data)
    
    def calculate_gpa(self, student_id: int):
        grades = self.get_student_grades(student_id)
        if not grades:
            return 0.0
        total = sum(g.score for g in grades)
        return total / len(grades)
