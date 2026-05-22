"""Root API router — versioned routes added in later tickets."""

from fastapi import APIRouter

from app.api.routes import health

api_router = APIRouter()

# SENT-104+: include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(health.router)
