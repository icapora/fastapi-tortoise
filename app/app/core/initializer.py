from app.core.config import settings
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from tortoise.contrib.fastapi import register_tortoise


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": ["app.models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


def init(app: FastAPI) -> None:
    init_db(app)
    add_pagination(app)
