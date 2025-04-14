import enum

from sqlalchemy.orm import Mapped

from core.models.base import BaseLoss


class RepairType(str, enum.Enum):
    Unplanned_repairs = 'Внеплановый ремонт'
    Technical_maintenance = 'Техническое обслуживание'


class RepairLoss(BaseLoss):
    repair_type: Mapped[RepairType]