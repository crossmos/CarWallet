from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from config import settings
from db_helper import db_helper
from .model import SpareLoss
from .schema import SpareLossRead, SpareLossCreate, SpareLossUpdatePartial
from ..dao.base import BaseDAO

router = APIRouter(
    prefix=settings.api.v1.spare_losses,
    tags=['Расходы на запчасти']
)


class SpareLossDAO(BaseDAO):
    model = SpareLoss


@router.get('/', response_model=list[SpareLossRead])
async def get_repair_losses(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await SpareLossDAO.get_all(session=session)


@router.post('/', response_model=SpareLossCreate)
async def create_repair_loss(
        create_schema: SpareLossCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await SpareLossDAO.create(session=session, schema=create_schema)


@router.get('/{id}/', response_model=SpareLossRead)
async def get_repair_loss(
        spare_loss: SpareLoss = Depends(SpareLossDAO.get_by_id),
):
    return spare_loss


@router.put('/{id}/')
async def update_repair_loss(
        update_schema: SpareLossUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        spare_loss: SpareLoss = Depends(SpareLossDAO.get_by_id),

):
    return await SpareLossDAO.update(
        obj=spare_loss,
        schema=update_schema,
        session=session,
    )


@router.patch('/{id}/')
async def update_repair_loss_partial(
        update_schema: SpareLossUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        spare_loss: SpareLoss = Depends(SpareLossDAO.get_by_id),

):
    return await SpareLossDAO.update(
        obj=spare_loss,
        schema=update_schema,
        session=session,
        partial=True,
    )


@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_repair_loss(
        session: AsyncSession = Depends(db_helper.session_getter),
        spare_loss: SpareLoss = Depends(SpareLossDAO.get_by_id),
) -> None:
    await SpareLossDAO.delete(obj=spare_loss, session=session)

