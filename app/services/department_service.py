"""Department Service"""
from app.repositories.department_repository import DepartmentRepository
from sqlalchemy.orm import Session

class DepartmentService:
    def __init__(self, db: Session):
        self.repository = DepartmentRepository(db)
    
    def create_department(self, data):
        return self.repository.create(data)
    
    def get_department(self, dept_id: int):
        return self.repository.get_by_id(dept_id)
    
    def get_all_departments(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
    
    def update_department(self, dept_id: int, data):
        return self.repository.update(dept_id, data)
    
    def delete_department(self, dept_id: int):
        return self.repository.delete(dept_id)
    
    def get_department_by_code(self, code: str):
        return self.repository.get_by_code(code)
