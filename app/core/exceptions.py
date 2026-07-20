class AppException(Exception):
    """Base exception for all application specific errors"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class NotFoundError(AppException):
    """Raised when a requested resource does not exist."""
    pass

class AlreadyExistsError(AppException):
    """Raised when the requested resource already exists"""
    pass

class BusinessRuleViolationError(AppException):
    """Raise when a Business Rule is violated"""
    pass