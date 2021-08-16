from app.models import User
from app.repositories import user_repository
from app.schemas import UserCreate
from app.test.utils.utils import random_email, random_lower_string


async def create_random_user() -> User:
    user_in = UserCreate(
        username=random_lower_string(),
        email=random_email(),
        name=random_lower_string(),
        last_name=random_lower_string(),
        password=random_lower_string(),
        is_active=True,
    )
    user = await user_repository.create(user_in)
    return user


async def create_superuser() -> User:
    user_in = UserCreate(
        username=random_lower_string(),
        email=random_email(),
        name=random_lower_string(),
        last_name=random_lower_string(),
        password=random_lower_string(),
        is_active=True,
        is_superuser=True,
    )
    user = await User.create(**user_in.dict())
    return user
