"""Health Center Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_health_records():
    return {"records": []}

@router.post("/checkup")
def create_checkup(data):
    return {"checkup": data}

@router.get("/student/{student_id}")
def get_student_health(student_id: int):
    return {"health": []}
