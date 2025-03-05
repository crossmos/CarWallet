from datetime import date
from typing import Optional

from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import declared_attr, DeclarativeBase, Mapped, mapped_column

from config import settings
from utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return camel_case_to_snake_case(cls.__name__)

    id: Mapped[int] = mapped_column(primary_key=True)

class BaseLoss(Base):
    __abstract__ = True

    date: Mapped[date]
    description: Mapped[Optional[str]]
    price: Mapped[float]
    amount: Mapped[float]
    transport_id: Mapped[int] = mapped_column(ForeignKey(
        'transport.id',
        ondelete='CASCADE',
    ))