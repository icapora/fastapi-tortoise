from unittest.mock import AsyncMock, patch

import pytest
from app.models import User
from app.repositories import UserRepository
from app.schemas import UserCreate
from app.test.utils.utils import random_email, random_lower_string


@pytest.mark.asyncio
@patch("app.models.User", new_callable=AsyncMock)
async def test_create_user(mock_user) -> None:
    user_repository = UserRepository(model=mock_user)
    username = random_lower_string()
    email = random_email()
    name = random_lower_string()
    last_name = random_lower_string()
    password = random_lower_string()
    is_active = True
    user_in = UserCreate(
        username=username,
        email=email,
        name=name,
        last_name=last_name,
        password=password,
        is_active=is_active,
    )
    user_to_create = User(**user_in.dict())
    mock_user.create.return_value = user_to_create
    user_created = await user_repository.create(user_in)
    assert user_created == user_to_create
    assert mock_user.create.called
    assert mock_user.create.await_count == 1
    mock_user.create.assert_awaited_with(
        **user_in.dict(exclude_unset=True), hashed_password=user_in.password
    )
