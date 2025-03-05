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
        create_schema: TransportCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await TransportDAO.create(session=session, schema=create_schema)


@router.get('/{id}/', response_model=TransportRead)
async def get_transport(
        transport: Transport = Depends(TransportDAO.get_by_id),
):
    return transport


@router.put('/{id}/')
async def update_transport(
        update_schema: TransportCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
        transport: Transport = Depends(TransportDAO.get_by_id),

):
    return await TransportDAO.update(
        obj=transport,
        schema=update_schema,
        session=session,
    )


@router.patch('/{id}/')
async def update_transport_partial(
        update_schema: TransportUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        transport: Transport = Depends(TransportDAO.get_by_id),

):
    return await TransportDAO.update(
        obj=transport,
        schema=update_schema,
        session=session,
        partial=True,
    )


@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_transport(
        session: AsyncSession = Depends(db_helper.session_getter),
        transport: Transport = Depends(TransportDAO.get_by_id),
) -> None:
    await TransportDAO.delete(obj=transport, session=session)

