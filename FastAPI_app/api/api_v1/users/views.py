from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from config import settings
from db_helper import db_helper
from .model import User
from .schema import UserRead, UserCreate, UserUpdatePartial
from ..dao.base import BaseDAO

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=['Пользователи']
)


class UserDAO(BaseDAO):
    model = User


@router.get('/', response_model=list[UserRead])
async def get_users(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await UserDAO.get_all(session=session)


@router.post('/', response_model=UserRead)
async def create_user(
        create_schema: UserCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    return await UserDAO.create(session=session, schema=create_schema)


@router.get('/{id}/', response_model=UserRead)
async def get_user(
        user: User = Depends(UserDAO.get_by_id),
):
    return user


@router.put('/{id}/')
async def update_user(
        update_schema: UserCreate,
        session: AsyncSession = Depends(db_helper.session_getter),
        user: User = Depends(UserDAO.get_by_id),

):
    return await UserDAO.update(
        obj=user,
        schema=update_schema,
        session=session,
    )


@router.patch('/{id}/')
async def update_user_partial(
        update_schema: UserUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        user: User = Depends(UserDAO.get_by_id),

):
    return await UserDAO.update(
        obj=user,
        schema=update_schema,
        session=session,
        partial=True,
    )


@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        session: AsyncSession = Depends(db_helper.session_getter),
        user: User = Depends(UserDAO.get_by_id),
) -> None:
    await UserDAO.delete(obj=user, session=session)

