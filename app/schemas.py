"""Pydantic Schemas"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class LecturerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    department_id: int
    lecturer_type: str
    qualification: str
    specialization: str

class LecturerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    qualification: Optional[str] = None

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    date_of_birth: date
    department_id: int
    admission_year: int

class CourseCreate(BaseModel):
    code: str
    title: str
    description: str
    credits: int
    department_id: int
    lecturer_id: int
    level: int

class DepartmentCreate(BaseModel):
    name: str
    code: str
    description: str

class AdmissionCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    department_id: int
    qualification: str
    score: float

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class FundingCreate(BaseModel):
    student_id: int
    funding_type: str
    amount: float
    academic_year: str

class GradeCreate(BaseModel):
    student_id: int
    course_id: int
    grade_type: str
    score: float
    letter_grade: str
