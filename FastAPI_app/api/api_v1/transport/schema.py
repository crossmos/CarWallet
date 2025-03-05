from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr

class UserUpdatePartial(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None


class UserRead(UserCreate):
    id: int
