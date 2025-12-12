"""Admission Service"""
from app.repositories.admission_repository import AdmissionRepository
from sqlalchemy.orm import Session

class AdmissionService:
    def __init__(self, db: Session):
        self.repository = AdmissionRepository(db)
    
    def create_admission(self, data):
        # Business logic validation: minimum score for eligibility
        if data.score < 60:
            raise ValueError("Score must be at least 60 to be eligible for admission")
        
        return self.repository.create(data)
    
    def get_admission(self, admission_id: int):
        return self.repository.get_by_id(admission_id)
    
    def get_all_admissions(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
    
    def approve_admission(self, admission_id: int):
        admission = self.get_admission(admission_id)
        if not admission:
            raise ValueError(f"Admission with id {admission_id} not found")
        
        # Validate that only pending admissions can be approved
        if admission.status != "pending":
            raise ValueError(f"Cannot approve admission with status: {admission.status}")
        
        admission.status = "approved"
        return self.repository.update(admission_id, admission)
    
    def reject_admission(self, admission_id: int):
        admission = self.get_admission(admission_id)
        if not admission:
            raise ValueError(f"Admission with id {admission_id} not found")
        
        # Validate that only pending admissions can be rejected
        if admission.status != "pending":
            raise ValueError(f"Cannot reject admission with status: {admission.status}")
        
        admission.status = "rejected"
        return self.repository.update(admission_id, admission)
    
    def get_admissions_by_status(self, status):
        return self.repository.get_by_status(status)
