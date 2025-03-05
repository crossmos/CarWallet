from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from config import settings
from db_helper import db_helper
from .model import FuelLoss
from .schema import FuelLossRead, FuelLossCreate, FuelLossUpdatePartial
from ..dao.base import BaseDAO

router = APIRouter(
    prefix=settings.api.v1.fuel_losses,
    tags=['Расходы на топливо']
)


class FuelLossDAO(BaseDAO):
    model = FuelLoss


@router.get('/', response_model=list[FuelLossRead])
async def get_fuel_losses(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await FuelLossDAO.get_all(session=session)


@router.post('/', response_model=FuelLossCreate)
async def create_fuel_loss(
        user_create: FuelLossCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await FuelLossDAO.create(session=session, schema=user_create)


@router.get('/{id}/', response_model=FuelLossRead)
async def get_fuel_loss(
        fuel_loss: FuelLoss = Depends(FuelLossDAO.get_by_id),
):
    return fuel_loss


@router.put('/{id}/')
async def update_fuel_loss(
        update_schema: FuelLossCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
        fuel_loss: FuelLoss = Depends(FuelLossDAO.get_by_id),

):
    return await FuelLossDAO.update(
        obj=fuel_loss,
        schema=update_schema,
        session=session,
    )


@router.patch('/{id}/')
async def update_fuel_loss_partial(
        update_schema: FuelLossUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        fuel_loss: FuelLoss = Depends(FuelLossDAO.get_by_id),

):
    return await FuelLossDAO.update(
        obj=fuel_loss,
        schema=update_schema,
        session=session,
        partial=True,
    )


@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_fuel_loss(
        session: AsyncSession = Depends(db_helper.session_getter),
        fuel_loss: FuelLoss = Depends(FuelLossDAO.get_by_id),
) -> None:
    await FuelLossDAO.delete(obj=fuel_loss, session=session)

