from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import users as users_crud
from core.config import settings
from core.models import db_helper, User
from core.schemas.user import UserRead, UserCreate

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=['Пользователи']
)


@router.get('/', response_model=list[UserRead])
async def get_users(
        # session: AsyncSession = Depends(db_helper.session_getter)
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
):
    return await users_crud.get_all_users(session=session)


@router.post('/', response_model=UserRead)
async def create_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        user_create: UserCreate,
):
    return await users_crud.create_user(
        session=session,
        user_create=user_create,
    )


@router.get('/{user_id}/', response_model=UserRead)
async def get_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        user_id: int
):
    user = await users_crud.get_user(session=session, user_id=user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User {user_id} not found!'
    )


@router.put('/{user_id}/')
async def update_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        user_id: int,
        user_update: UserCreate
):
    pass

@router.delete('/{user_id}/')
async def delete_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        user_id: int
):
    user = await session.delete(User, user_id)
    return user
