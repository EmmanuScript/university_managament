"""Helper Functions Utility"""
from datetime import datetime, timedelta

class Helpers:
    @staticmethod
    def get_current_semester():
        month = datetime.now().month
        if month < 7:
            return "First"
        else:
            return "Second"
    
    @staticmethod
    def get_academic_year():
        year = datetime.now().year
        if datetime.now().month < 7:
            return f"{year-1}/{year}"
        return f"{year}/{year+1}"
    
    @staticmethod
    def calculate_age(birth_date):
        today = datetime.now()
        return today.year - birth_date.year
    
    @staticmethod
    def format_date(date_obj):
        return date_obj.strftime("%d/%m/%Y")
    
    @staticmethod
    def is_weekend(date_obj):
        return date_obj.weekday() >= 5
