import enum

from sqlalchemy.orm import Mapped

from core.models.base import BaseLoss


class FuelType(str, enum.Enum):
    Petrol_80 = 'Бензин 80'
    Petrol_92 = 'Бензин 92'
    Petrol_95 = 'Бензин 95'
    Petrol_100 = 'Бензин 100'
    Diesel = 'Дизельное топливо'


class FuelLoss(BaseLoss):
    fuel_type: Mapped[FuelType]
