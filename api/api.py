from fastapi import APIRouter
from api.endpoints import embed, admin

api_router = APIRouter()

api_router.include_router(embed.router)
api_router.include_router(admin.router)
