"""Notification Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_notifications(skip: int = 0, limit: int = 10):
    return {"notifications": []}

@router.post("/send")
def send_notification(data):
    return {"message": "Notification sent"}
