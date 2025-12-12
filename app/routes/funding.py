"""Funding Routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.funding_service import FundingService

router = APIRouter()

@router.post("/")
def create_funding(data, db: Session = Depends(get_db)):
    return FundingService(db).create_funding(data)

@router.get("/{funding_id}")
def get_funding(funding_id: int, db: Session = Depends(get_db)):
    return FundingService(db).get_funding(funding_id)

@router.get("/")
def get_all_funding(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return FundingService(db).get_all_funding(skip, limit)

@router.get("/student/{student_id}")
def get_student_funding(student_id: int, db: Session = Depends(get_db)):
    return FundingService(db).get_student_funding(student_id)

@router.put("/{funding_id}")
def update_funding(funding_id: int, data, db: Session = Depends(get_db)):
    return FundingService(db).update_funding(funding_id, data)

@router.delete("/{funding_id}")
def delete_funding(funding_id: int, db: Session = Depends(get_db)):
    FundingService(db).delete_funding(funding_id)
    return {"message": "Deleted"}
