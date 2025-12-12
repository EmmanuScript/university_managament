"""
Main application entry point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import Settings
from app.core.database import Base, engine
from app.routes import (
    lecturer, student, admission, funding, course, 
    department, enrollment, notification, report,
    academic_calendar, examination, grading,
    fee_management, student_discipline, library,
    hostel_management, transport, health_center
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="University Management System",
    description="Comprehensive system for managing university operations",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(lecturer.router, prefix="/api/lecturers", tags=["Lecturers"])
app.include_router(student.router, prefix="/api/students", tags=["Students"])
app.include_router(admission.router, prefix="/api/admission", tags=["Admission"])
app.include_router(funding.router, prefix="/api/funding", tags=["Funding"])
app.include_router(course.router, prefix="/api/courses", tags=["Courses"])
app.include_router(department.router, prefix="/api/departments", tags=["Departments"])
app.include_router(enrollment.router, prefix="/api/enrollment", tags=["Enrollment"])
app.include_router(notification.router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(report.router, prefix="/api/reports", tags=["Reports"])
app.include_router(academic_calendar.router, prefix="/api/academic-calendar", tags=["Academic Calendar"])
app.include_router(examination.router, prefix="/api/examination", tags=["Examination"])
app.include_router(grading.router, prefix="/api/grading", tags=["Grading"])
app.include_router(fee_management.router, prefix="/api/fees", tags=["Fee Management"])
app.include_router(student_discipline.router, prefix="/api/discipline", tags=["Student Discipline"])
app.include_router(library.router, prefix="/api/library", tags=["Library"])
app.include_router(hostel_management.router, prefix="/api/hostel", tags=["Hostel"])
app.include_router(transport.router, prefix="/api/transport", tags=["Transport"])
app.include_router(health_center.router, prefix="/api/health", tags=["Health Center"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to University Management System",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
