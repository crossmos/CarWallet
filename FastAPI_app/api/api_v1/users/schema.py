from typing import Any, Optional, Union

from pydantic import BaseModel, EmailStr, ConfigDict


class UserWrite(BaseModel):
    username: str
    email: Optional[EmailStr]
    password: Union[str, bytes]


class UserCreate(UserWrite):
    is_active: bool = True


class UserUpdatePartial(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Any = None
    is_active: Optional[bool] = True


class UserRead(UserWrite):
    id: int

