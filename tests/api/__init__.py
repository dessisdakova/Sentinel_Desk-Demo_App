"""API-layer tests for SentinelDesk (HTTP contract tests).

Tests in this package call the running FastAPI application over HTTP. They do
**not** open database connections directly unless a future story requires it.

Typical flow:
    1. A test requests a fixture such as ``api_client``.
    2. ``require_api`` (in ``tests/conftest.py``) verifies the API is up.
    3. The test calls ``api_client.get("/some/path")`` and asserts status/body/headers.

Marker:
    Every test file should use ``@pytest.mark.api`` or ``pytestmark = pytest.mark.api``.

Run:
    pytest -m api -v
"""
