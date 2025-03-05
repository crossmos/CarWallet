import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from api.api_v1.base_models import Base


class Brand(enum.Enum):
    Audi = 'Audi'
    BMW = 'BMW'


class Transport(Base):
    brand: Mapped[Brand]
    model: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey(
        'user.id',
        ondelete='CASCADE',
    ))