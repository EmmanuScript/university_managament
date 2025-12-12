"""Funding Repository"""
from sqlalchemy.orm import Session
from app.core.database import Funding

class FundingRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, data):
        funding = Funding(**data.dict())
        self.db.add(funding)
        self.db.commit()
        self.db.refresh(funding)
        return funding
    
    def get_by_id(self, funding_id: int):
        return self.db.query(Funding).filter(Funding.id == funding_id).first()
    
    def get_by_student(self, student_id: int):
        return self.db.query(Funding).filter(Funding.student_id == student_id).all()
    
    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Funding).offset(skip).limit(limit).all()
    
    def get_by_funding_type(self, funding_type):
        return self.db.query(Funding).filter(Funding.funding_type == funding_type).all()
    
    def update(self, funding_id: int, data):
        funding = self.get_by_id(funding_id)
        if funding:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(funding, key, value)
            self.db.commit()
            self.db.refresh(funding)
        return funding
    
    def delete(self, funding_id: int):
        funding = self.get_by_id(funding_id)
        if funding:
            self.db.delete(funding)
            self.db.commit()
        return funding
