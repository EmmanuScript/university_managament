"""Report Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/students")
def student_report():
    return {"report": "student_report"}

@router.get("/lecturers")
def lecturer_report():
    return {"report": "lecturer_report"}

@router.get("/funding")
def funding_report():
    return {"report": "funding_report"}

@router.get("/enrollment")
def enrollment_report():
    return {"report": "enrollment_report"}
