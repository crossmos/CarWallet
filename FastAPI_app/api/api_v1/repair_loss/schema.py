from datetime import date
from typing import Optional

from pydantic import BaseModel

from .model import FuelType


class FuelLossCreate(BaseModel):
    fuel_type: FuelType
    date: date
    description: str
    price: float
    amount: float
    transport_id: int


class FuelLossUpdatePartial(BaseModel):
    fuel_type: Optional[FuelType] = None
    date: Optional[date] = None
    description:Optional [str] = None
    price: Optional[int] = None
    amount: Optional[float] = None
    transport_id: Optional[int] = None


class FuelLossRead(FuelLossCreate):
    id: int

