"""Student Routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.student_service import StudentService
from app.schemas import StudentCreate

router = APIRouter()

@router.post("/")
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.create_student(data)

@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    service = StudentService(db)
    student = service.get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/")
def get_all_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.get_all_students(skip, limit)

@router.put("/{student_id}")
def update_student(student_id: int, data, db: Session = Depends(get_db)):
    service = StudentService(db)
    student = service.update_student(student_id, data)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    service = StudentService(db)
    student = service.delete_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted"}

@router.get("/matric/{matric}")
def get_student_by_matric(matric: str, db: Session = Depends(get_db)):
    service = StudentService(db)
    student = service.get_student_by_matric(matric)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
