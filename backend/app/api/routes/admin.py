"""Admin-only endpoints."""

import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.deps import require_roles
from app.models.user import User
from app.schemas.admin import AdminPingResponse

logger = logging.getLogger(__name__)

router = APIRouter(tags=["admin"])

_require_admin = require_roles(["ADMIN"])


@router.get("/ping", response_model=AdminPingResponse)
async def admin_ping(
    current_user: Annotated[User, Depends(_require_admin)],
) -> AdminPingResponse:
    """Health-check endpoint restricted to ADMIN role."""
    logger.info("admin ping user_id=%s", current_user.id)
    return AdminPingResponse(message="pong", user_id=str(current_user.id))
