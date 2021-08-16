from typing import Type

from app.models import Opinion
from app.repositories import OpinionRepository, opinion_repository
from app.schemas import OpinionCreate, OpinionUpdate
from app.services import BaseService
from fastapi_pagination.bases import AbstractPage


class OpinionService(
    BaseService[Opinion, OpinionCreate, OpinionUpdate, Type[OpinionRepository]]
):
    async def create_with_owner(self, obj: OpinionCreate, owner_id: int) -> Opinion:
        return await self.repository.create_with_owner(obj, owner_id=owner_id)

    async def get_all_by_owner_id(self, owner_id: int) -> AbstractPage[Opinion]:
        return await self.repository.get_all_by_owner_id(owner_id=owner_id)

    async def get_all_by_owner_username(
        self, owner_username: str
    ) -> AbstractPage[Opinion]:
        return await self.repository.get_all_by_owner_username(owner_username)


opinion_service = OpinionService(repository=opinion_repository)
