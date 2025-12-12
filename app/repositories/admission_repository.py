"""Admission Repository"""
from sqlalchemy.orm import Session
from app.core.database import Admission

class AdmissionRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data):
        admission = Admission(**data.dict())
        self.db.add(admission)
        self.db.commit()
        self.db.refresh(admission)
        return admission
    
    def get_by_id(self, admission_id: int):
        return self.db.query(Admission).filter(Admission.id == admission_id).first()
    
    def get_by_application_id(self, app_id: str):
        return self.db.query(Admission).filter(Admission.application_id == app_id).first()
    
    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Admission).offset(skip).limit(limit).all()
    
    def get_by_status(self, status):
        return self.db.query(Admission).filter(Admission.status == status).all()
    
    def get_by_department(self, dept_id: int):
        return self.db.query(Admission).filter(Admission.department_id == dept_id).all()
    
    def update(self, admission_id: int, data):
        admission = self.get_by_id(admission_id)
        if admission:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(admission, key, value)
            self.db.commit()
            self.db.refresh(admission)
        return admission
