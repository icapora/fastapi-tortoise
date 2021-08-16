import asyncio
from typing import Generator

import pytest
from app.core.config import settings
from app.main import create_application
from fastapi.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise


@pytest.fixture(scope="module")
def client() -> Generator:
    app = create_application()
    register_tortoise(
        app,
        db_url=settings.DATABASE_TEST_URL,
        modules={"models": ["app.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
