from fastapi import APIRouter

from config import settings
from .api_v1 import router as api_router_v1

router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(
    api_router_v1,
)