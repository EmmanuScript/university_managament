"""Validators Utility"""
import re

class Validators:
    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = r'^\+?1?\d{9,15}$'
        return re.match(pattern, phone) is not None
    
    @staticmethod
    def validate_student_id(student_id: str) -> bool:
        return len(student_id) > 0
    
    @staticmethod
    def validate_gpa(gpa: float) -> bool:
        return 0 <= gpa <= 4.0
    
    @staticmethod
    def validate_score(score: float) -> bool:
        return 0 <= score <= 100
