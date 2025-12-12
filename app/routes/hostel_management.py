"""Hostel Management Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_hostels():
    return {"hostels": []}

@router.get("/rooms")
def get_hostel_rooms():
    return {"rooms": []}

@router.post("/allocate")
def allocate_room(data):
    return {"allocation": data}

@router.get("/student/{student_id}")
def get_student_hostel(student_id: int):
    return {"hostel": None}
