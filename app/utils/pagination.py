"""Pagination Utility"""

class Pagination:
    @staticmethod
    def paginate(items: list, skip: int = 0, limit: int = 10):
        return items[skip:skip + limit]
    
    @staticmethod
    def get_total_pages(total_items: int, page_size: int = 10):
        return (total_items + page_size - 1) // page_size
    
    @staticmethod
    def get_offset(page: int, page_size: int = 10):
        return (page - 1) * page_size
