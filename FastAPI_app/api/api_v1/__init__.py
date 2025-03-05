from fastapi import APIRouter

from config import settings

from api.api_v1.fuel_loss.views import router as fuel_losses_router
from api.api_v1.users.views import router as users_router
from api.api_v1.transport.views import router as transports_router
from api.api_v1.repair_loss.views import router as repair_losses_router
from api.api_v1.spare_loss.views import router as spare_losses_router
from api.api_v1.supplie_loss.views import router as supplie_losses_router


router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    users_router,
)
router.include_router(
    transports_router,
)
router.include_router(
    fuel_losses_router,
)
router.include_router(
    repair_losses_router,
)
router.include_router(
    spare_losses_router,
)
router.include_router(
    supplie_losses_router,
)


