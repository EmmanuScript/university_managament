"""Response Handler Utility"""

class ResponseHandler:
    @staticmethod
    def success(data, message: str = "Success"):
        return {
            "status": "success",
            "message": message,
            "data": data
        }
    
    @staticmethod
    def error(message: str, code: int = 400):
        return {
            "status": "error",
            "message": message,
            "code": code
        }
    
    @staticmethod
    def paginated(data, page: int, total: int, page_size: int = 10):
        return {
            "status": "success",
            "data": data,
            "pagination": {
                "page": page,
                "page_size": page_size,
                "total": total,
                "total_pages": (total + page_size - 1) // page_size
            }
        }
