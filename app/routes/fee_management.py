"""Fee Management Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_fees():
    return {"fees": []}

@router.post("/pay")
def pay_fee(data):
    return {"payment": "processed"}

@router.get("/student/{student_id}")
def get_student_fees(student_id: int):
    return {"fees": []}
