"""Pydantic schemas for admin endpoints."""

from pydantic import BaseModel


class AdminPingResponse(BaseModel):
    """Response body for GET /api/v1/admin/ping."""

    message: str
    user_id: str
