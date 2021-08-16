from typing import Any, Generic, Optional, Type, TypeVar

from fastapi_pagination.bases import AbstractPage
from fastapi_pagination.ext.tortoise import paginate
from pydantic import BaseModel
from tortoise import Model

ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, id: Any) -> Optional[ModelType]:
        return await self.model.get_or_none(id=id)

    async def get_all(self) -> AbstractPage[ModelType]:
        return await paginate(self.model.all())

    async def create(self, obj: CreateSchemaType) -> ModelType:
        return await self.model.create(**obj.dict(exclude_unset=True))

    async def update(self, id: Any, obj: UpdateSchemaType) -> ModelType:
        await self.model.filter(id=id).update(**obj.dict(exclude_unset=True))
        return await self.model.get(id=id)

    async def delete(self, id: Any) -> int:
        return await self.model.filter(id=id).delete()
