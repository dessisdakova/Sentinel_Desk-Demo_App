"""HTTP middleware."""

import logging
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.core.context import request_id_ctx

logger = logging.getLogger("sentineldesk.api")


class RequestIdMiddleware(BaseHTTPMiddleware):
    """
    Assign a unique request_id per HTTP request for structured logs.

    Uses incoming X-Request-ID when present; otherwise generates a UUID.
    Echoes the id on the response as X-Request-ID.
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        incoming = request.headers.get("X-Request-ID")
        request_id = incoming or str(uuid.uuid4())
        token = request_id_ctx.set(request_id)

        logger.info(
            "request_started method=%s path=%s",
            request.method,
            request.url.path,
        )
        try:
            response = await call_next(request)
        finally:
            request_id_ctx.reset(token)

        response.headers["X-Request-ID"] = request_id
        logger.info(
            "request_finished method=%s path=%s status=%s",
            request.method,
            request.url.path,
            response.status_code,
        )
        return response
