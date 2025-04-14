from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=True)
    password: Mapped[bytes]
    is_active: Mapped[bool] = mapped_column(server_default='True', default=True)