"""Examination Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_examinations():
    return {"exams": []}

@router.post("/")
def create_examination(data):
    return {"exam": data}

@router.get("/timetable")
def get_exam_timetable():
    return {"timetable": []}
