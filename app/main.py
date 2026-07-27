from fastapi import FastAPI
from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.health import router as health_router
from app.category import router as category_router
from app.users import router as User_router


def create_app() -> FastAPI:

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION
    )

    register_exception_handlers(app)

    app.include_router(health_router)
    app.include_router(category_router)
    app.include_router(User_router)

    return app


app = create_app()
