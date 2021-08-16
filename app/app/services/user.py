from typing import Optional, Type

from app.models import User
from app.repositories import UserRepository, user_repository
from app.schemas import UserCreate, UserUpdate
from app.services import BaseService


class UserService(BaseService[User, UserCreate, UserUpdate, Type[UserRepository]]):
    async def authenticate(self, email: str, password: str) -> Optional[User]:
        return await self.repository.authenticate(email, password)


user_service = UserService(repository=user_repository)
