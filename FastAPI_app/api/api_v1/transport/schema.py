from typing import Optional

from pydantic import BaseModel

from core.models.transport import Brand


class TransportWrite(BaseModel):
    brand: Brand
    model: str


class TransportCreate(TransportWrite):
    user_id: int


class TransportUpdatePartial(BaseModel):
    brand: Optional[Brand] = None
    model: Optional[str] = None
    user_id: Optional[int] = None


class TransportRead(TransportCreate):
    id: int
