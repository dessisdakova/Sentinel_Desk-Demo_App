"""SentinelDesk FastAPI application entry point."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging_config import RequestIdFilter, configure_logging
from app.core.middleware import RequestIdMiddleware

configure_logging()
logging.getLogger().addFilter(RequestIdFilter())

settings = get_settings()

app = FastAPI(
    title="SentinelDesk API",
    description="SecOps Alert Triage Portal — local development",
    version="0.1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestIdMiddleware)
app.include_router(api_router)
