from app.controllers import login, opinions, status, users
from fastapi import APIRouter

api_route = APIRouter()
api_route.include_router(status.router, prefix="/status", tags=["status"])
api_route.include_router(login.router, prefix="/login", tags=["login"])
api_route.include_router(users.router, prefix="/users", tags=["users"])
api_route.include_router(opinions.router, prefix="/opinions", tags=["opinions"])
