from datetime import date
from typing import Optional

from pydantic import BaseModel

from .model import RepairType


class RepairLossCreate(BaseModel):
    repair_type: RepairType
    date: date
    description: str
    price: float
    amount: float
    transport_id: int


class RepairLossUpdatePartial(BaseModel):
    fuel_type: Optional[RepairType] = None
    date: Optional[date] = None
    description:Optional [str] = None
    price: Optional[int] = None
    amount: Optional[float] = None
    transport_id: Optional[int] = None


class RepairLossRead(RepairLossCreate):
    id: int

