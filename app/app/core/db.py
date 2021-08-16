from app.core.config import settings

TORTOISE_ORM = {
    "connections": {
        "default": settings.DATABASE_URL,
        "test": settings.DATABASE_TEST_URL,
    },
    "apps": {
        "models": {
            "models": [
                "app.models.like",
                "app.models.opinion",
                "app.models.user",
                "aerich.models",
            ],
            "default_connection": "default",
        },
    },
}
