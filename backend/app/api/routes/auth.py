"""Authentication endpoints."""

from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, get_settings
from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.user import User
from app.schemas.auth import LoginRequest, TokenResponse, UserProfileResponse
from app.services.auth_service import login, user_to_profile

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=TokenResponse)
async def auth_login(
    body: LoginRequest,
    db: Annotated[AsyncSession, Depends(get_db)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> TokenResponse:
    """Issue a JWT access token for valid email/password credentials."""
    return await login(
        db,
        email=body.email,
        password=body.password,
        settings=settings,
    )


@router.get("/me", response_model=UserProfileResponse)
async def auth_me(
    current_user: Annotated[User, Depends(get_current_user)],
) -> UserProfileResponse:
    """Return the authenticated user's profile."""
    return user_to_profile(current_user)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def auth_logout(
    _current_user: Annotated[User, Depends(get_current_user)],
) -> Response:
    """Acknowledge logout; client discards the stored token."""
    return Response(status_code=status.HTTP_204_NO_CONTENT)
