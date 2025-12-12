"""Academic Calendar Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_academic_calendar():
    return {"calendar": []}

@router.post("/")
def create_event(data):
    return {"event": data}
