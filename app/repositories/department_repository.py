"""Department Repository"""
from sqlalchemy.orm import Session
from app.core.database import Department

class DepartmentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data):
        dept = Department(**data.dict())
        self.db.add(dept)
        self.db.commit()
        self.db.refresh(dept)
        return dept
    
    def get_by_id(self, dept_id: int):
        return self.db.query(Department).filter(Department.id == dept_id).first()
    
    def get_by_code(self, code: str):
        return self.db.query(Department).filter(Department.code == code).first()
    
    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Department).offset(skip).limit(limit).all()
    
    def update(self, dept_id: int, data):
        dept = self.get_by_id(dept_id)
        if dept:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(dept, key, value)
            self.db.commit()
            self.db.refresh(dept)
        return dept
    
    def delete(self, dept_id: int):
        dept = self.get_by_id(dept_id)
        if dept:
            self.db.delete(dept)
            self.db.commit()
        return dept
