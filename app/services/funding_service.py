"""Funding Service"""
from app.repositories.funding_repository import FundingRepository
from sqlalchemy.orm import Session

class FundingService:
    def __init__(self, db: Session):
        self.repository = FundingRepository(db)
    
    def create_funding(self, data):
        return self.repository.create(data)
    
    def get_funding(self, funding_id: int):
        return self.repository.get_by_id(funding_id)
    
    def get_all_funding(self, skip: int = 0, limit: int = 10):
        return self.repository.get_all(skip, limit)
    
    def get_student_funding(self, student_id: int):
        return self.repository.get_by_student(student_id)
    
    def get_funding_by_type(self, funding_type):
        return self.repository.get_by_funding_type(funding_type)
    
    def update_funding(self, funding_id: int, data):
        return self.repository.update(funding_id, data)
    
    def delete_funding(self, funding_id: int):
        return self.repository.delete(funding_id)
