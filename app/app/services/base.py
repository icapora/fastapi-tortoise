from typing import Any, Generic, Optional, Type, TypeVar

from app.repositories.base import BaseRepository
from fastapi_pagination.bases import AbstractPage
from pydantic import BaseModel
from tortoise import Model

ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
RepositoryType = TypeVar("RepositoryType", bound=BaseRepository)


class BaseService(
    Generic[ModelType, CreateSchemaType, UpdateSchemaType, RepositoryType]
):
    def __init__(self, repository: Type[RepositoryType]):
        self.repository = repository

    async def get(self, id: Any) -> Optional[ModelType]:
        return await self.repository.get(id)

    async def get_all(self) -> AbstractPage[ModelType]:
        return await self.repository.get_all()

    async def create(self, obj: CreateSchemaType) -> ModelType:
        return await self.repository.create(obj)

    async def update(self, id: Any, obj: UpdateSchemaType) -> ModelType:
        return await self.repository.update(id, obj)

    async def delete(self, id: Any) -> int:
        return await self.repository.delete(id)
