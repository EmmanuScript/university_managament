"""Transport Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_transport():
    return {"transport": []}

@router.post("/register")
def register_transport(data):
    return {"registration": data}

@router.get("/student/{student_id}")
def get_student_transport(student_id: int):
    return {"transport": None}
