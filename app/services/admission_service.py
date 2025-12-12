"""Admission Service"""
from app.repositories.admission_repository import AdmissionRepository
from sqlalchemy.orm import Session

class AdmissionService:
    def __init__(self, db: Session):
        self.repository = AdmissionRepository(db)
    
    def create_admission(self, data):
        return self.repository.create(data)
    
    def get_admission(self, admission_id: int):
        return self.repository.get_by_id(admission_id)
    
    def get_all_admissions(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
    
    def approve_admission(self, admission_id: int):
        admission = self.get_admission(admission_id)
        if admission:
            admission.status = "approved"
        return self.repository.update(admission_id, admission)
    
    def reject_admission(self, admission_id: int):
        admission = self.get_admission(admission_id)
        if admission:
            admission.status = "rejected"
        return self.repository.update(admission_id, admission)
    
    def get_admissions_by_status(self, status):
        return self.repository.get_by_status(status)
