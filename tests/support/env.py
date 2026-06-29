import os

import pytest


def _env(name: str, default: str | None = None) -> str:
    """Read an environment variable or fail the test run with a clear message.

    :param name: Variable name as it appears in '.env' (e.g. 'POSTGRES_HOST').
    :param default: Value to use when the variable is unset.
    :return: Non-empty string value.
    :raises: pytest.Failed: When the variable is missing and no usable default exists.
    """
    value = os.getenv(name, default)
    if value is None or value == "":
        pytest.fail(f"Missing environment variable {name}. Copy .env.example to .env")
    return value
