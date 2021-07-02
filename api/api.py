from fastapi import APIRouter
from api.endpoints import embed

api_router = APIRouter()

api_router.include_router(embed.router)
