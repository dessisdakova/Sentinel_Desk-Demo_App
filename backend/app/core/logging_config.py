"""Structured logging configuration for the API service."""

import logging
import sys

from app.core.context import request_id_ctx


def configure_logging() -> None:
    """Configure root logger with a consistent format for local and Docker runs."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] request_id=%(request_id)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
        stream=sys.stdout,
    )


class RequestIdFilter(logging.Filter):
    """Inject request_id from context into every log record."""

    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_ctx.get()
        return True
