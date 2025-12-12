"""Enrollment Service"""
from app.repositories.enrollment_repository import EnrollmentRepository
from sqlalchemy.orm import Session

class EnrollmentService:
    def __init__(self, db: Session):
        self.repository = EnrollmentRepository(db)
    
    def create_enrollment(self, data):
        return self.repository.create(data)
    
    def get_enrollment(self, enroll_id: int):
        return self.repository.get_by_id(enroll_id)
    
    def get_all_enrollments(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
    
    def get_student_enrollments(self, student_id: int):
        return self.repository.get_by_student(student_id)
    
    def get_course_enrollments(self, course_id: int):
        return self.repository.get_by_course(course_id)
    
    def update_enrollment(self, enroll_id: int, data):
        return self.repository.update(enroll_id, data)
    
    def delete_enrollment(self, enroll_id: int):
        return self.repository.delete(enroll_id)
