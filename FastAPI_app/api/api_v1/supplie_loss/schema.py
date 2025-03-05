from datetime import date
from typing import Optional

from pydantic import BaseModel




class SpareLossCreate(BaseModel):
    date: date
    description: str
    price: float
    amount: float
    transport_id: int


class SpareLossUpdatePartial(BaseModel):
    date: Optional[date] = None
    description:Optional [str] = None
    price: Optional[int] = None
    amount: Optional[float] = None
    transport_id: Optional[int] = None


class SpareLossRead(SpareLossCreate):
    id: int

