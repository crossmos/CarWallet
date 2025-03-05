import enum

from sqlalchemy.orm import Mapped

from api.api_v1.base_models import BaseLoss


class FuelType(enum.Enum):
    Petrol_80 = 'Бензин 80'
    Petrol_92 = 'Бензин 92'
    Petrol_95 = 'Бензин 95'
    Petrol_100 = 'Бензин 100'
    Diesel = 'Дизельное топливо'


class FuelLoss(BaseLoss):
    fuel_type: Mapped[FuelType]
