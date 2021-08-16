from typing import Any

from app.controllers import dependencies
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from fastapi_pagination import LimitOffsetPage
from tortoise.contrib.fastapi import HTTPNotFoundError

from app import models, schemas, services

router = APIRouter()


@router.get("/", response_model=LimitOffsetPage[schemas.Opinion])
async def get_opinions() -> Any:
    return await services.opinion_service.get_all()


@router.post("/", response_model=schemas.Opinion)
async def create_opinion(
    opinion: schemas.OpinionCreate,
    current_user: models.User = Depends(dependencies.get_current_active_user),
) -> Any:
    return await services.opinion_service.create_with_owner(opinion, current_user.id)


@router.post("/{id}/like", status_code=status.HTTP_200_OK)
async def like_opinion(
    id: int,
    background_tasks: BackgroundTasks,
    current_user: models.User = Depends(dependencies.get_current_active_user),
) -> Any:
    like_in = schemas.LikeCreate(opinion_id=id, user_id=current_user.id)
    background_tasks.add_task(services.like_service.give_a_like, like_in)


@router.delete("/{id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_opinion(
    id: int, current_user: models.User = Depends(dependencies.get_current_active_user)
) -> Any:
    opinion = await services.opinion_service.get(id=id)
    if not opinion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Opinion {id} not found"
        )
    if not current_user.is_superuser and (opinion.owner != current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough permissions"
        )
    await services.opinion_service.delete(id)
    return schemas.Message(detail=f"Deleted opinion {id}")
