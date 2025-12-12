"""Department Routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.department_service import DepartmentService

router = APIRouter()

@router.post("/")
def create_department(data, db: Session = Depends(get_db)):
    return DepartmentService(db).create_department(data)

@router.get("/{dept_id}")
def get_department(dept_id: int, db: Session = Depends(get_db)):
    dept = DepartmentService(db).get_department(dept_id)
    if not dept:
        raise HTTPException(status_code=404)
    return dept

@router.get("/")
def get_all_departments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return DepartmentService(db).get_all_departments(skip, limit)

@router.put("/{dept_id}")
def update_department(dept_id: int, data, db: Session = Depends(get_db)):
    return DepartmentService(db).update_department(dept_id, data)

@router.delete("/{dept_id}")
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    DepartmentService(db).delete_department(dept_id)
    return {"message": "Deleted"}
