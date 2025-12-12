"""
Configuration settings
"""
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "University Management System"
    PROJECT_VERSION: str = "1.0.0"
    DESCRIPTION: str = "Comprehensive management system for university operations"

    # Database - PostgreSQL Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:newpassword@localhost:5432/university_management")

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # CORS
    CORS_ORIGINS: list = ["*"]

    # Email
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))

    class Config:
        env_file = ".env"

settings = Settings()
