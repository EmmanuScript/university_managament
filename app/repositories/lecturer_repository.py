"""Lecturer Repository"""
from sqlalchemy.orm import Session
from app.core.database import Lecturer
from app.schemas import LecturerCreate, LecturerUpdate

class LecturerRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data: LecturerCreate):
        lecturer = Lecturer(**data.dict())
        self.db.add(lecturer)
        self.db.commit()
        self.db.refresh(lecturer)
        return lecturer
    
    def get_by_id(self, lecturer_id: int):
        return self.db.query(Lecturer).filter(Lecturer.id == lecturer_id).first()
    
    def get_by_email(self, email: str):
        return self.db.query(Lecturer).filter(Lecturer.email == email).first()
    
    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Lecturer).offset(skip).limit(limit).all()
    
    def update(self, lecturer_id: int, data: LecturerUpdate):
        lecturer = self.get_by_id(lecturer_id)
        if lecturer:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(lecturer, key, value)
            self.db.commit()
            self.db.refresh(lecturer)
        return lecturer
    
    def delete(self, lecturer_id: int):
        lecturer = self.get_by_id(lecturer_id)
        if lecturer:
            self.db.delete(lecturer)
            self.db.commit()
        return lecturer
    
    def get_by_department(self, department_id: int):
        return self.db.query(Lecturer).filter(Lecturer.department_id == department_id).all()
