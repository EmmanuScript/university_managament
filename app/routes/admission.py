"""Admission Routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.admission_service import AdmissionService

router = APIRouter()

@router.post("/apply")
def apply_admission(data, db: Session = Depends(get_db)):
    return AdmissionService(db).create_admission(data)

@router.get("/{admission_id}")
def get_admission(admission_id: int, db: Session = Depends(get_db)):
    admission = AdmissionService(db).get_admission(admission_id)
    if not admission:
        raise HTTPException(status_code=404)
    return admission

@router.get("/")
def get_all_admissions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return AdmissionService(db).get_all_admissions(skip, limit)

@router.post("/{admission_id}/approve")
def approve_admission(admission_id: int, db: Session = Depends(get_db)):
    return AdmissionService(db).approve_admission(admission_id)

@router.post("/{admission_id}/reject")
def reject_admission(admission_id: int, db: Session = Depends(get_db)):
    return AdmissionService(db).reject_admission(admission_id)

@router.get("/status/{status}")
def get_admissions_by_status(status: str, db: Session = Depends(get_db)):
    return AdmissionService(db).get_admissions_by_status(status)
