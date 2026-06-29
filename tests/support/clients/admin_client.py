import httpx

from tests.support.clients.base import BaseApiClient

_PING_PATH = "/api/v1/admin/ping"


class AdminClient(BaseApiClient):
    """Service object for ``/api/v1/admin`` endpoints."""

    def ping(self, *, token: str | None = None) -> httpx.Response:
        """GET ``/api/v1/admin/ping`` for the current or supplied bearer token.

        :param token: Optional JWT override; uses constructor token when omitted.
        :return: Raw HTTP response.
        """
        return self.get(_PING_PATH, token=token)

    def ping_preflight(self, *, origin: str) -> httpx.Response:
        """OPTIONS preflight for ``GET /api/v1/admin/ping`` from a browser origin.

        :param origin: Value for the ``Origin`` request header.
        :return: Raw HTTP response.
        """
        return self.options(
            _PING_PATH,
            headers={
                "Origin": origin,
                "Access-Control-Request-Method": "GET",
                "Access-Control-Request-Headers": "authorization",
            },
        )
