from fastapi import APIRouter, Depends
from pydantic import BaseModel

from api.api_v1.users.schema import UserCreate
from api.auth.security import (
    encode_jwt,
    get_current_active_auth_user,
    validate_auth_user)
from core.config import settings

router = APIRouter(
    prefix=settings.auth_jwt.prefix,
    tags=["Авторизация и аутентификация"]
)


class TokenInfo(BaseModel):
    access_token: str
    token_type: str


@router.post("/login/", response_model=TokenInfo)
def auth_user_issue_jwt(
        user: UserCreate = Depends(validate_auth_user),
):
    jwt_payload = {
        # subject
        "sub": user.username,
        "id": user.id,
    }
    token = encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )


@router.get('/test/')
def test(
        user: UserCreate = Depends(get_current_active_auth_user),
):
    return {
        'username': user.username,
    }
