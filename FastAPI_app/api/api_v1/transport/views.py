from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.dao.base import BaseDAO
from api.api_v1.transport.schema import TransportRead, TransportCreate, TransportUpdatePartial, TransportWrite
from api.auth.security import get_current_token_payload
from core.config import settings
from core.models.db_helper import db_helper
from core.models.transport import Transport

router = APIRouter(
    prefix=settings.api.v1.transports,
    tags=['Транспортные средства']
)


class TransportDAO(BaseDAO):
    model = Transport


@router.get('/', response_model=list[TransportRead])
async def get_transports(
        session: AsyncSession = Depends(db_helper.session_getter),
        payload: dict = Depends(get_current_token_payload)
):
    return await TransportDAO.get_all(session=session)


@router.post('/', response_model=TransportRead)
async def create_transport(
        create_schema: TransportWrite,
        session: AsyncSession = Depends(db_helper.session_getter),
        payload: dict = Depends(get_current_token_payload)
):
    obj = TransportCreate(
        brand=create_schema.brand,
        model=create_schema.model,
        user_id=payload['id']
    )
    obj = Transport(**obj.model_dump())
    session.add(obj)
    await session.commit()
    return obj


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
