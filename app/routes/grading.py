"""Grading Routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.grade_service import GradeService

router = APIRouter()

@router.post("/")
def create_grade(data, db: Session = Depends(get_db)):
    return GradeService(db).create_grade(data)

@router.get("/{grade_id}")
def get_grade(grade_id: int, db: Session = Depends(get_db)):
    return GradeService(db).get_grade(grade_id)

@router.get("/student/{student_id}")
def get_student_grades(student_id: int, db: Session = Depends(get_db)):
    return GradeService(db).get_student_grades(student_id)

@router.get("/gpa/{student_id}")
def get_student_gpa(student_id: int, db: Session = Depends(get_db)):
    gpa = GradeService(db).calculate_gpa(student_id)
    return {"gpa": gpa}

@router.put("/{grade_id}")
def update_grade(grade_id: int, data, db: Session = Depends(get_db)):
    return GradeService(db).update_grade(grade_id, data)
