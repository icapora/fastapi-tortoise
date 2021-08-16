from app.models import Opinion
from app.repositories import BaseRepository
from app.schemas import OpinionCreate, OpinionUpdate
from fastapi_pagination.bases import AbstractPage
from fastapi_pagination.ext.tortoise import paginate


class OpinionRepository(BaseRepository[Opinion, OpinionCreate, OpinionUpdate]):
    async def create_with_owner(self, obj: OpinionCreate, owner_id: int) -> Opinion:
        return await self.model.create(
            **obj.dict(exclude_unset=True), owner_id=owner_id
        )

    async def get_all_by_owner_id(self, owner_id: int) -> AbstractPage[Opinion]:
        opinions = self.model.filter(owner_id=owner_id)
        return await paginate(opinions)

    async def get_all_by_owner_username(
        self, owner_username: str
    ) -> AbstractPage[Opinion]:
        opinions = self.model.filter(owner__username=owner_username)
        return await paginate(opinions)


opinion_repository = OpinionRepository(model=Opinion)
