"""Library Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/books")
def get_books():
    return {"books": []}

@router.post("/borrow")
def borrow_book(data):
    return {"borrowed": data}

@router.post("/return")
def return_book(data):
    return {"returned": data}

@router.get("/student/{student_id}")
def get_student_borrowing(student_id: int):
    return {"borrowing": []}
