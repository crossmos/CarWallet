from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from config import settings
from db_helper import db_helper
from .model import Transport
from .schema import TransportRead, TransportCreate, TransportUpdatePartial
from ..dao.base import BaseDAO

router = APIRouter(
    prefix=settings.api.v1.transports,
    tags=['Транспортные средства']
)


class TransportDAO(BaseDAO):
    model = Transport


@router.get('/', response_model=list[TransportRead])
async def get_transports(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await TransportDAO.get_all(session=session)


@router.post('/', response_model=TransportRead)
async def create_transport(
        user_create: TransportCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await TransportDAO.create(session=session, schema=user_create)


@router.get('/{id}/', response_model=TransportRead)
async def get_transport(
        user: Transport = Depends(TransportDAO.get_by_id),
):
    return user


@router.put('/{id}/')
async def update_transport(
        user_update: TransportCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
        user: Transport = Depends(TransportDAO.get_by_id),

):
    return await TransportDAO.update(
        obj=user,
        schema=user_update,
        session=session,
    )


@router.patch('/{id}/')
async def update_transport_partial(
        user_update: TransportUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        user: Transport = Depends(TransportDAO.get_by_id),

):
    return await TransportDAO.update(
        obj=user,
        schema=user_update,
        session=session,
        partial=True,
    )


@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_transport(
        session: AsyncSession = Depends(db_helper.session_getter),
        user: Transport = Depends(TransportDAO.get_by_id),
) -> None:
    await TransportDAO.delete(obj=user, session=session)

