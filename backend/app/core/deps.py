"""FastAPI dependencies for authentication."""

import uuid
from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import PyJWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.core.database import get_db
from app.core.errors import raise_app_error
from app.core.security import decode_access_token
from app.models.user import User
from app.services.user_service import get_user_by_id

_bearer_scheme = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(_bearer_scheme),
    ],
    db: Annotated[AsyncSession, Depends(get_db)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> User:
    """Resolve the authenticated user from a Bearer JWT."""
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise_app_error(
            401,
            "UNAUTHORIZED",
            "Missing or invalid authorization header",
        )

    try:
        payload = decode_access_token(credentials.credentials, settings)
    except PyJWTError:
        raise_app_error(401, "UNAUTHORIZED", "Invalid or expired access token")

    subject = payload.get("sub")
    if not subject:
        raise_app_error(401, "UNAUTHORIZED", "Invalid or expired access token")

    try:
        user_id = uuid.UUID(str(subject))
    except ValueError:
        raise_app_error(401, "UNAUTHORIZED", "Invalid or expired access token")

    user = await get_user_by_id(db, user_id)
    if user is None or not user.active:
        raise_app_error(401, "UNAUTHORIZED", "Invalid or expired access token")

    return user
