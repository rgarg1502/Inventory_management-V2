from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import    AlreadyExistsError, BusinessRuleViolationError,    NotFoundError


def register_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(NotFoundError)
    async def not_found_exception_handler(
        request: Request,
        exc: NotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "error": {
                        "code": "NOT_FOUND",
                        "message": exc.message,
    }
            },
        )

    @app.exception_handler(AlreadyExistsError)
    async def already_exists_exception_handler(
        request: Request,
        exc: AlreadyExistsError,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "error": {
                    "code": "ALREADY_EXISTS",
                    "message": exc.message,
    }
            },
        )

    @app.exception_handler(BusinessRuleViolationError)
    async def business_rule_exception_handler(
        request: Request,
        exc: BusinessRuleViolationError,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "error": {
                    "code": "BUSINESS_RULE_VIOLATION",
                    "message": exc.message,
    }
            },
        )