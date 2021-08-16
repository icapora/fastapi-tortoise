from typing import Optional

from app.core.security import verify_password
from app.models import User
from app.repositories import BaseRepository
from app.schemas import UserCreate, UserUpdate


class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    async def create(self, obj: UserCreate) -> User:
        return await self.model.create(
            **obj.dict(exclude_unset=True), hashed_password=obj.password
        )

    async def authenticate(self, email: str, password: str) -> Optional[User]:
        user = await self.model.get_or_none(email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


user_repository = UserRepository(model=User)
