"""Enrollment Routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.enrollment_service import EnrollmentService

router = APIRouter()

@router.post("/")
def create_enrollment(data, db: Session = Depends(get_db)):
    return EnrollmentService(db).create_enrollment(data)

@router.get("/{enroll_id}")
def get_enrollment(enroll_id: int, db: Session = Depends(get_db)):
    enroll = EnrollmentService(db).get_enrollment(enroll_id)
    if not enroll:
        raise HTTPException(status_code=404)
    return enroll

@router.get("/")
def get_all_enrollments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return EnrollmentService(db).get_all_enrollments(skip, limit)

@router.get("/student/{student_id}")
def get_student_enrollments(student_id: int, db: Session = Depends(get_db)):
    return EnrollmentService(db).get_student_enrollments(student_id)

@router.get("/course/{course_id}")
def get_course_enrollments(course_id: int, db: Session = Depends(get_db)):
    return EnrollmentService(db).get_course_enrollments(course_id)

@router.put("/{enroll_id}")
def update_enrollment(enroll_id: int, data, db: Session = Depends(get_db)):
    return EnrollmentService(db).update_enrollment(enroll_id, data)

@router.delete("/{enroll_id}")
def delete_enrollment(enroll_id: int, db: Session = Depends(get_db)):
    EnrollmentService(db).delete_enrollment(enroll_id)
    return {"message": "Deleted"}
