"""Authentication request and response schemas."""

import re
import uuid
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, Field

from app.models.user import UserRole

_LOGIN_EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def _normalize_login_email(value: str) -> str:
    """Validate login email format; allow @demo.local seed addresses."""
    normalized = value.strip().lower()
    if not _LOGIN_EMAIL_RE.fullmatch(normalized):
        raise ValueError("value is not a valid email address")
    return normalized


LoginEmail = Annotated[str, BeforeValidator(_normalize_login_email)]


class LoginRequest(BaseModel):
    """POST /api/v1/auth/login body."""

    email: LoginEmail
    password: str = Field(min_length=1)


class TokenResponse(BaseModel):
    """Successful login response."""

    access_token: str
    token_type: str = "bearer"
    expires_in: int


class UserProfileResponse(BaseModel):
    """GET /api/v1/auth/me response."""

    id: uuid.UUID
    email: str
    role: UserRole
    display_name: str
