"""Lecturer Routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.lecturer_service import LecturerService
from app.schemas import LecturerCreate, LecturerUpdate

router = APIRouter()

@router.post("/")
def create_lecturer(data: LecturerCreate, db: Session = Depends(get_db)):
    service = LecturerService(db)
    return service.create_lecturer(data)

@router.get("/{lecturer_id}")
def get_lecturer(lecturer_id: int, db: Session = Depends(get_db)):
    service = LecturerService(db)
    lecturer = service.get_lecturer(lecturer_id)
    if not lecturer:
        raise HTTPException(status_code=404, detail="Lecturer not found")
    return lecturer

@router.get("/")
def get_all_lecturers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = LecturerService(db)
    return service.get_all_lecturers(skip, limit)

@router.put("/{lecturer_id}")
def update_lecturer(lecturer_id: int, data: LecturerUpdate, db: Session = Depends(get_db)):
    service = LecturerService(db)
    lecturer = service.update_lecturer(lecturer_id, data)
    if not lecturer:
        raise HTTPException(status_code=404, detail="Lecturer not found")
    return lecturer

@router.delete("/{lecturer_id}")
def delete_lecturer(lecturer_id: int, db: Session = Depends(get_db)):
    service = LecturerService(db)
    lecturer = service.delete_lecturer(lecturer_id)
    if not lecturer:
        raise HTTPException(status_code=404, detail="Lecturer not found")
    return {"message": "Lecturer deleted successfully"}

@router.get("/department/{dept_id}")
def get_lecturers_by_department(dept_id: int, db: Session = Depends(get_db)):
    service = LecturerService(db)
    return service.get_lecturers_by_department(dept_id)
