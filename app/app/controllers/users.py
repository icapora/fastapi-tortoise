from typing import Any

from app.controllers import dependencies
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import LimitOffsetPage
from tortoise.contrib.fastapi import HTTPNotFoundError

from app import models, schemas, services

router = APIRouter()


@router.get("/", response_model=LimitOffsetPage[schemas.User])
async def get_users(
    current_user: models.User = Depends(dependencies.get_current_superuser),
) -> Any:
    return await services.user_service.get_all()


@router.post("/", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate,
    current_user: models.User = Depends(dependencies.get_current_superuser),
) -> Any:
    return await services.user_service.create(user)


@router.get("/me", response_model=schemas.User)
async def get_me(
    current_user: models.User = Depends(dependencies.get_current_active_user),
) -> Any:
    return current_user


@router.put(
    "/me", response_model=schemas.User, responses={404: {"model": HTTPNotFoundError}}
)
async def update_user(
    user: schemas.UserUpdate,
    current_user: models.User = Depends(dependencies.get_current_active_user),
) -> Any:
    return await services.user_service.update(current_user.id, user)


@router.get("/{username}/opinions", response_model=LimitOffsetPage[schemas.Opinion])
async def get_opinions_by_user(
    username: str,
) -> Any:
    return await services.opinion_service.get_all_by_owner_username(username)


@router.get("/{username}/likes", response_model=LimitOffsetPage[schemas.Like])
async def get_likes_by_user(username: str) -> Any:
    return await services.like_service.get_all_by_user_username(username)


@router.get(
    "/{id}", response_model=schemas.User, responses={404: {"model": HTTPNotFoundError}}
)
async def get_user(
    id: int, current_user: models.User = Depends(dependencies.get_current_active_user)
) -> Any:
    user = services.user_service.get(id=id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found"
        )
    if user == current_user:
        return user
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User doesn't have enough privileges",
        )
    return user
