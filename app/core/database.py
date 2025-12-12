"""
Database configuration and models
"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float, ForeignKey, Text, Date, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import enum

from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Enums
class LecturerType(str, enum.Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"

class AdmissionStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class EnrollmentStatus(str, enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    DROPPED = "dropped"

class FundingType(str, enum.Enum):
    SCHOLARSHIP = "scholarship"
    LOAN = "loan"
    GRANT = "grant"

class GradeType(str, enum.Enum):
    SEMESTER = "semester"
    CONTINUOUS = "continuous"
    FINAL = "final"

# Models
class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    code = Column(String, unique=True)
    description = Column(Text)
    head_id = Column(Integer, ForeignKey("lecturers.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    lecturers = relationship("Lecturer", back_populates="department")
    courses = relationship("Course", back_populates="department")

class Lecturer(Base):
    __tablename__ = "lecturers"
    
    id = Column(Integer, primary_key=True)
    employee_id = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    lecturer_type = Column(SQLEnum(LecturerType))
    qualification = Column(String)
    specialization = Column(String)
    office_location = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    department = relationship("Department", back_populates="lecturers")
    courses = relationship("Course", back_populates="lecturer")

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    title = Column(String)
    description = Column(Text)
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))
    lecturer_id = Column(Integer, ForeignKey("lecturers.id"))
    level = Column(Integer)  # 100, 200, 300, 400
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    department = relationship("Department", back_populates="courses")
    lecturer = relationship("Lecturer", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    matric_number = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    date_of_birth = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.id"))
    level = Column(Integer)  # 100, 200, 300, 400
    admission_year = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    department = relationship("Department")
    enrollments = relationship("Enrollment", back_populates="student")

class Admission(Base):
    __tablename__ = "admissions"
    
    id = Column(Integer, primary_key=True)
    application_id = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    qualification = Column(String)
    score = Column(Float)
    status = Column(SQLEnum(AdmissionStatus), default=AdmissionStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)

class Enrollment(Base):
    __tablename__ = "enrollments"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    enrollment_date = Column(DateTime, default=datetime.utcnow)
    status = Column(SQLEnum(EnrollmentStatus), default=EnrollmentStatus.ACTIVE)
    
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

class Funding(Base):
    __tablename__ = "funding"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    funding_type = Column(SQLEnum(FundingType))
    amount = Column(Float)
    academic_year = Column(String)
    status = Column(String, default="active")
    created_at = Column(DateTime, default=datetime.utcnow)

class Grade(Base):
    __tablename__ = "grades"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    grade_type = Column(SQLEnum(GradeType))
    score = Column(Float)
    letter_grade = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
