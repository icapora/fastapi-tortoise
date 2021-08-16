from pydantic import AnyUrl, BaseSettings
from starlette.config import Config


class Settings(BaseSettings):
    config = Config(".env")

    API_TITLE: str = "FastAPI & Tortoise template"
    API_DESCRIPTION: str = "Made with ♥ and FastAPI"
    API_VERSION: str = "0.1.0"
    API_V1: str = "/api/v1"

    DEBUG: bool = config("DEBUG", cast=bool, default=False)
    DATABASE_URL: AnyUrl = config("DATABASE_URL", cast=str)
    DATABASE_TEST_URL: str = config("DATABASE_TEST_URL", cast=str)

    ALGORITHM: str = "HS256"
    SECRET_KEY: str = config("SECRET_KEY", cast=str)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7


settings = Settings()
