"""Pydantic Schemas"""
from pydantic import BaseModel, EmailStr, validator, field_validator
from typing import Optional
from datetime import date, datetime
from app.utils.validators import Validators

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
    email: str
    phone: str
    department_id: int
    qualification: str
    score: float
    
    @field_validator('email')
    def validate_email_format(cls, v):
        if not Validators.validate_email(v):
            raise ValueError('Invalid email format')
        return v
    
    @field_validator('phone')
    def validate_phone_format(cls, v):
        if not Validators.validate_phone(v):
            raise ValueError('Invalid phone format')
        return v
    
    @field_validator('score')
    def validate_score_range(cls, v):
        if not Validators.validate_score(v):
            raise ValueError('Score must be between 0 and 100')
        return v
    
    @field_validator('first_name', 'last_name')
    def validate_names(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Name cannot be empty')
        return v.strip()
    
    @field_validator('qualification')
    def validate_qualification(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Qualification cannot be empty')
        return v.strip()

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
