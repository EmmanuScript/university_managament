"""Student Discipline Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_discipline_records():
    return {"records": []}

@router.post("/record")
def record_discipline(data):
    return {"record": data}

@router.get("/student/{student_id}")
def get_student_discipline(student_id: int):
    return {"records": []}
