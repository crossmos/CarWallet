from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth import security as auth_utils
from core.config import settings
from core.models.db_helper import db_helper
from core.models.user import User
from ..dao.base import BaseDAO
from .schema import UserRead, UserCreate, UserUpdatePartial, UserWrite

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
        create_schema: UserWrite,
        session: AsyncSession = Depends(db_helper.session_getter),
):
    obj = UserCreate(
        username=create_schema.username,
        email=create_schema.email,
        password=auth_utils.hash_password(create_schema.password),
    )

    obj = User(**obj.model_dump())
    session.add(obj)
    await session.commit()
    return obj



@router.get('/{id}/', response_model=UserRead)
async def get_user(
        user: User = Depends(UserDAO.get_by_id),
):
    return user


# @router.put('/{id}/')
# async def update_user(
#         update_schema: UserCreate,
#         session: AsyncSession = Depends(db_helper.session_getter),
#         user: User = Depends(UserDAO.get_by_id),
#
# ):
#     return await UserDAO.update(
#         obj=user,
#         schema=update_schema,
#         session=session,
#     )


@router.patch('/{id}/', response_model=UserRead)
async def update_user_partial(
        update_schema: UserUpdatePartial,
        session: AsyncSession = Depends(db_helper.session_getter),
        user: User = Depends(UserDAO.get_by_id),
):
    if update_schema.password:
        update_schema.password = auth_utils.hash_password(update_schema.password)
    for key, value in update_schema.model_dump(exclude_unset=True).items():
        setattr(user, key, value)
    await session.commit()
    return user


@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        session: AsyncSession = Depends(db_helper.session_getter),
        user: User = Depends(UserDAO.get_by_id),
) -> None:
    await UserDAO.delete(obj=user, session=session)
