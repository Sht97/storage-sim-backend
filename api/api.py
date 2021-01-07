from fastapi import APIRouter

from api.endpoints import compare

api_router = APIRouter()
api_router.include_router(compare.router, prefix="/disk", tags=["compare"])
