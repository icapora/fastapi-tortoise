from typing import Tuple, Type

from app.models import Like
from app.repositories import LikeRepository, like_repository
from app.schemas import LikeCreate, LikeUpdate
from app.services import BaseService
from fastapi_pagination.bases import AbstractPage


class LikeService(BaseService[Like, LikeCreate, LikeUpdate, Type[LikeRepository]]):
    async def get_or_create(self, like_in: LikeCreate) -> Tuple[Like, bool]:
        return await self.repository.get_or_create(like_in)

    async def update_or_create(self, like_in: LikeCreate) -> Tuple[Like, bool]:
        return await self.repository.update_or_create(like_in)

    async def give_a_like(self, like_in: LikeCreate) -> None:
        like, created = await self.repository.get_or_create(like_in)
        if not created:
            await self.repository.update_like(like.id)

    async def get_all_by_user_username(self, username: str) -> AbstractPage[Like]:
        return await self.repository.get_all_by_user_username(username)

    async def get_all_by_opinion_id(self, opinion_id: int) -> AbstractPage[Like]:
        return await self.repository.get_all_by_opinion(opinion_id)


like_service = LikeService(repository=like_repository)
