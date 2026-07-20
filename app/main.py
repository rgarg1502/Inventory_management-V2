from fastapi import FastAPI
from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers


def create_app() -> FastAPI:
    
    app = FastAPI(
        title = settings.APP_NAME,
        version = settings.APP_VERSION
    )

    register_exception_handlers(app)

    @app.get("/health", tags=["Health"])
    async def health_check():
        return {
            "status": "healthy"
        }

    return app

app = create_app()