"""Authentication business logic."""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings
from app.core.errors import raise_app_error
from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.schemas.auth import TokenResponse, UserProfileResponse
from app.services.user_service import get_user_by_email


async def login(
    session: AsyncSession,
    *,
    email: str,
    password: str,
    settings: Settings,
) -> TokenResponse:
    """Authenticate credentials and issue a JWT access token."""
    user = await get_user_by_email(session, email)
    if user is None or not verify_password(password, user.password_hash):
        raise_app_error(
            401,
            "INVALID_CREDENTIALS",
            "Invalid email or password",
        )

    if not user.active:
        raise_app_error(
            403,
            "ACCOUNT_DISABLED",
            "This account has been disabled",
        )

    access_token, expires_in = create_access_token(
        user_id=str(user.id),
        role=user.role.value,
        settings=settings,
    )
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        expires_in=expires_in,
    )


def user_to_profile(user: User) -> UserProfileResponse:
    """Map a User ORM row to the /auth/me response schema."""
    return UserProfileResponse(
        id=user.id,
        email=user.email,
        role=user.role,
        display_name=user.display_name,
    )
