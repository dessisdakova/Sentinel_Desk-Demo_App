"""Password hashing and JWT access tokens."""

from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from passlib.context import CryptContext

from app.core.config import Settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

JWT_ALGORITHM = "HS256"


def hash_password(plain_password: str) -> str:
    """Hash a plaintext password with bcrypt."""
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    """Return True when the plaintext password matches the stored hash."""
    return pwd_context.verify(plain_password, password_hash)


def create_access_token(
    *,
    user_id: str,
    role: str,
    settings: Settings,
) -> tuple[str, int]:
    """Build a signed JWT access token and its lifetime in seconds."""
    expires_in = settings.jwt_expire_hours * 3600
    now = datetime.now(UTC)
    expire = now + timedelta(seconds=expires_in)
    payload: dict[str, Any] = {
        "sub": user_id,
        "role": role,
        "iat": now,
        "exp": expire,
    }
    token = jwt.encode(payload, settings.jwt_secret, algorithm=JWT_ALGORITHM)
    return token, expires_in


def decode_access_token(token: str, settings: Settings) -> dict[str, Any]:
    """Decode and validate a JWT access token."""
    return jwt.decode(token, settings.jwt_secret, algorithms=[JWT_ALGORITHM])
