from sqlalchemy.orm import Mapped, mapped_column

from api.api_v1.base_models import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
