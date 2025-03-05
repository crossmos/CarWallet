from typing import Optional

from pydantic import BaseModel

from .model import Brand

class TransportCreate(BaseModel):
    brand: Brand
    model: str
    user_id: int


class TransportUpdatePartial(BaseModel):
    brand: Optional[Brand] = None
    model: Optional[str] = None
    user_id: Optional[int] = None


class TransportRead(TransportCreate):
    id: int
