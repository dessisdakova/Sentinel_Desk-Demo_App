from dataclasses import dataclass

import httpx


@dataclass
class ApiSession:
    """Bundled API config and transport for one pytest session.

    Holds the resolved ``base_url`` and a single shared ``httpx.Client`` so
    service wrappers and teardown helpers can access both without re-reading
    environment variables or opening duplicate connection pools.

    :param base_url: FastAPI root URL with no trailing slash.
    :param client: Session-scoped HTTP client with ``base_url`` already set.
    """

    base_url: str
    client: httpx.Client

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self.client.close()
