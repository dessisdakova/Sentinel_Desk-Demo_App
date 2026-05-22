"""Health check response models."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """GET /health response body."""

    status: str
