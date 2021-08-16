import logging

from app.api.routes import api_route
from app.core.config import settings
from app.core.initializer import init
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.API_TITLE,
        description=settings.API_DESCRIPTION,
        version=settings.API_VERSION,
        openapi_url=f"{settings.API_V1}/openapi.json",
        debug=settings.DEBUG,
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(api_route, prefix=settings.API_V1)
    return application


app = create_application()


@app.on_event("startup")
async def startup_event() -> None:
    log.info("starting up...")
    init(app)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    log.info("shutting down...")
