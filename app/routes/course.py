"""Course Routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.course_service import CourseService

router = APIRouter()

@router.post("/")
def create_course(data, db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.create_course(data)

@router.get("/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    service = CourseService(db)
    course = service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.get("/")
def get_all_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.get_all_courses(skip, limit)

@router.put("/{course_id}")
def update_course(course_id: int, data, db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.update_course(course_id, data)

@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    service = CourseService(db)
    service.delete_course(course_id)
    return {"message": "Course deleted"}

@router.get("/department/{dept_id}")
def get_courses_by_department(dept_id: int, db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.get_courses_by_department(dept_id)

@router.get("/level/{level}")
def get_courses_by_level(level: int, db: Session = Depends(get_db)):
    service = CourseService(db)
    return service.get_courses_by_level(level)
