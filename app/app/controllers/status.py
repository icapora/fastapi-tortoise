from typing import Any

from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("/", response_model=schemas.Status)
async def get_status() -> Any:
    return schemas.Status(status="Alive!")
