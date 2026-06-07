import httpx
import pytest

from tests.conftest import API_TIMEOUT_SEC


@pytest.fixture(scope="session")
def api_client(api_base_url: str, require_api: None) -> httpx.Client:
    """Synchronous HTTP client pointed at the SentinelDesk API.

    :param api_base_url: Root URL of the FastAPI service (from root conftest).
    :param require_api: Gate fixture — skips if the API is down or unhealthy.
    :yield: Configured ``httpx.Client`` with ``base_url`` and timeout set.
    """
    client = httpx.Client(base_url=api_base_url, timeout=API_TIMEOUT_SEC)
    yield client
    client.close()
