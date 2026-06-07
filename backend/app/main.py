"""SentinelDesk FastAPI application entry point."""

import logging
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

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


@app.exception_handler(HTTPException)
async def http_exception_handler(
    _request: Request,
    exc: HTTPException,
) -> JSONResponse:
    """Return CONSTITUTION §12.2 error envelope at the top level."""
    if isinstance(exc.detail, dict) and "error" in exc.detail:
        content: dict[str, Any] = exc.detail
    else:
        content = {
            "error": {
                "code": "HTTP_ERROR",
                "message": str(exc.detail),
                "details": None,
            }
        }
    return JSONResponse(status_code=exc.status_code, content=content)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestIdMiddleware)
app.include_router(api_router)
