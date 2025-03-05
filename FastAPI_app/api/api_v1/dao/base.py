from typing import Annotated
from fastapi import Depends, Path, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.users.model import User
from db_helper import db_helper


class BaseDAO:
    model = None

    @classmethod
    async def get_by_id(
            cls,
            session: Annotated[
                AsyncSession,
                Depends(db_helper.session_getter),
            ],
            id: Annotated[int, Path],
    ):
        user = await session.get(cls.model, id)
        if user:
            return user
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{id} not found!'
        )

    @classmethod
    async def get_all(
            cls,
            session: AsyncSession
    ):
        stmt = select(cls.model).order_by(cls.model.id.desc())
        result = await session.scalars(stmt)
        return result.all()

    @classmethod
    async def create(
            cls,
            session: AsyncSession,
            schema,
    ):
        obj = cls.model(**schema.model_dump())
        session.add(obj)
        await session.commit()
        return obj

    @classmethod
    async def update(
            cls,
            obj,
            schema,
            session: AsyncSession,
            partial: bool = False,
    ):
        for key, value in schema.model_dump(exclude_unset=partial).items():
            setattr(obj, key, value)
        await session.commit()
        return obj

    @classmethod
    async def delete(
            cls,
            obj,
            session: AsyncSession,
    ) -> None:
        await session.delete(obj)
        await session.commit()
