from typing import Tuple

from app.models import Like
from app.repositories import BaseRepository
from app.schemas import LikeCreate, LikeUpdate
from fastapi_pagination.bases import AbstractPage
from fastapi_pagination.ext.tortoise import paginate
from tortoise.expressions import F


class LikeRepository(BaseRepository[Like, LikeCreate, LikeUpdate]):
    async def get_or_create(self, like_in: LikeCreate) -> Tuple[Like, bool]:
        return await self.model.get_or_create(**like_in.dict())

    async def update_or_create(self, like_in: LikeCreate) -> Tuple[Like, bool]:
        return await self.model.update_or_create(**like_in.dict())

    async def update_like(self, like_id: int) -> None:
        await self.model.filter(id=like_id).update(like=~F("like"))

    async def get_all_by_user_username(self, username: str) -> AbstractPage[Like]:
        likes = self.model.filter(user__username=username)
        return await paginate(likes)

    async def get_all_by_opinion(self, opinion_id: int) -> AbstractPage[Like]:
        likes = self.model.filter(opinion_id=opinion_id)
        return await paginate(likes)


like_repository = LikeRepository(model=Like)
