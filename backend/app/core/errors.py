"""Canonical API error helpers."""

from typing import Any

from fastapi import HTTPException


def raise_app_error(
    status_code: int,
    code: str,
    message: str,
    details: Any = None,
) -> None:
    """Raise an HTTPException with the CONSTITUTION §12.2 error envelope."""
    raise HTTPException(
        status_code=status_code,
        detail={
            "error": {
                "code": code,
                "message": message,
                "details": details,
            }
        },
    )
