from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from config import settings
from db_helper import db_helper
from .model import RepairLoss
from .schema import RepairLossRead, RepairLossCreate, RepairLossUpdatePartial
from ..dao.base import BaseDAO

router = APIRouter(
    prefix=settings.api.v1.repair_losses,
    tags=['Расходы на ремонт']
)


class RepairLossDAO(BaseDAO):
    model = RepairLoss


@router.get('/', response_model=list[RepairLossRead])
async def get_repair_losses(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await RepairLossDAO.get_all(session=session)


@router.post('/', response_model=RepairLossCreate)
async def create_repair_loss(
        create_schema: RepairLossCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await RepairLossDAO.create(session=session, schema=create_schema)


@router.get('/{id}/', response_model=RepairLossRead)
async def get_repair_loss(
        repair_loss: RepairLoss = Depends(RepairLossDAO.get_by_id),
):
    return repair_loss


@router.put('/{id}/')
async def update_repair_loss(
        update_schema: RepairLossUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        repair_loss: RepairLoss = Depends(RepairLossDAO.get_by_id),

):
    return await RepairLossDAO.update(
        obj=repair_loss,
        schema=update_schema,
        session=session,
    )


@router.patch('/{id}/')
async def update_repair_loss_partial(
        update_schema: RepairLossUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        repair_loss: RepairLoss = Depends(RepairLossDAO.get_by_id),

):
    return await RepairLossDAO.update(
        obj=repair_loss,
        schema=update_schema,
        session=session,
        partial=True,
    )


@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_repair_loss(
        session: AsyncSession = Depends(db_helper.session_getter),
        fuel_loss: RepairLoss = Depends(RepairLossDAO.get_by_id),
) -> None:
    await RepairLossDAO.delete(obj=fuel_loss, session=session)

