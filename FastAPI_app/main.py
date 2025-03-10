from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
# from fastapi.responses import ORJSONResponse

from api import router as api_router
from config import settings
from db_helper import db_helper


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
