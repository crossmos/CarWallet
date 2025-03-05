import enum

from sqlalchemy.orm import Mapped

from api.api_v1.base_models import BaseLoss


class RepairType(enum.Enum):
    Unplanned_repairs = 'Внеплановый ремонт'
    Technical_maintenance = 'Техническое обслуживание'


class RepairLoss(BaseLoss):
    repair_type: Mapped[RepairType]