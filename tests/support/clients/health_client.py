import httpx

from tests.support.clients.base import BaseApiClient


class HealthClient(BaseApiClient):
    """Service object for health and routing probes."""

    def health(self, *, request_id: str | None = None) -> httpx.Response:
        """GET ``/health``, optionally sending ``X-Request-ID``.

        :param request_id: When set, sent as ``X-Request-ID`` header.
        :return: Raw HTTP response.
        """
        headers = {"X-Request-ID": request_id} if request_id else None
        return self.get("/health", headers=headers)

    def unknown_path(self) -> httpx.Response:
        """GET a route that does not exist (negative routing probe).

        :return: Raw HTTP response (expect 404).
        """
        return self.get("/unknown-path")
