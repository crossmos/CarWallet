from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from config import settings
from db_helper import db_helper
from .model import SupplieLoss
from .schema import SupplieLossRead, SupplieLossCreate, SupplieLossUpdatePartial
from ..dao.base import BaseDAO

router = APIRouter(
    prefix=settings.api.v1.supplie_losses,
    tags=['Расходы на расходные материалы']
)


class SupplieLossDAO(BaseDAO):
    model = SupplieLoss


@router.get('/', response_model=list[SupplieLossRead])
async def get_repair_losses(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await SupplieLossDAO.get_all(session=session)


@router.post('/', response_model=SupplieLossCreate)
async def create_repair_loss(
        create_schema: SupplieLossCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await SupplieLossDAO.create(session=session, schema=create_schema)


@router.get('/{id}/', response_model=SupplieLossRead)
async def get_repair_loss(
        supplie_loss: SupplieLoss = Depends(SupplieLossDAO.get_by_id),
):
    return supplie_loss


@router.put('/{id}/')
async def update_repair_loss(
        update_schema: SupplieLossUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        supplie_loss: SupplieLoss = Depends(SupplieLossDAO.get_by_id),

):
    return await SupplieLossDAO.update(
        obj=supplie_loss,
        schema=update_schema,
        session=session,
    )


@router.patch('/{id}/')
async def update_repair_loss_partial(
        update_schema: SupplieLossUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        supplie_loss: SupplieLoss = Depends(SupplieLossDAO.get_by_id),

):
    return await SupplieLossDAO.update(
        obj=supplie_loss,
        schema=update_schema,
        session=session,
        partial=True,
    )


@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_repair_loss(
        session: AsyncSession = Depends(db_helper.session_getter),
        supplie_loss: SupplieLoss = Depends(SupplieLossDAO.get_by_id),
) -> None:
    await SupplieLossDAO.delete(obj=supplie_loss, session=session)

