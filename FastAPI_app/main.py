from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
# from fastapi.responses import ORJSONResponse

from api import router as api_router
from api.auth.views import router as auth_router
from core.config import settings
from core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    # default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
main_app.include_router(
    auth_router,
)
main_app.include_router(
    api_router,
)

if __name__ == '__main__':
    uvicorn.run(
        'main:main_app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )

# alembic revision --autogenerate -m 'create user table'
# alembic upgrade head
#
# alembic downgrade base
