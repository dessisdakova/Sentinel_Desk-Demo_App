from typing import Any

import httpx

from tests.support.clients.base import BaseApiClient

_LOGIN_PATH = "/api/v1/auth/login"
_ME_PATH = "/api/v1/auth/me"
_LOGOUT_PATH = "/api/v1/auth/logout"


class AuthClient(BaseApiClient):
    """Service object for ``/api/v1/auth`` endpoints."""

    def login(self, email: str, password: str) -> httpx.Response:
        """POST ``/api/v1/auth/login`` with email and password credentials.

        :param email: User email address.
        :param password: User password.
        :return: Raw HTTP response (caller asserts status and body).
        """
        return self.post(_LOGIN_PATH, json={"email": email, "password": password})

    def login_with_payload(self, payload: dict[str, Any]) -> httpx.Response:
        """POST ``/api/v1/auth/login`` with an arbitrary JSON body.

        Useful for negative tests (missing fields, wrong types).

        :param payload: JSON-serializable login body.
        :return: Raw HTTP response.
        """
        return self.post(_LOGIN_PATH, json=payload)

    def login_with_malformed_body(self) -> httpx.Response:
        """POST ``/api/v1/auth/login`` with an invalid JSON body.

        :return: Raw HTTP response (expect 422 JSON decode error).
        """
        return self.post(
            _LOGIN_PATH,
            content=b"{not valid json}",
            headers={"Content-Type": "application/json"},
        )

    def me(self, *, token: str | None = None) -> httpx.Response:
        """GET ``/api/v1/auth/me`` for the current or supplied bearer token.

        :param token: Optional JWT override; uses constructor token when omitted.
        :return: Raw HTTP response.
        """
        return self.get(_ME_PATH, token=token)

    def logout(self, *, token: str | None = None) -> httpx.Response:
        """POST ``/api/v1/auth/logout`` for the current or supplied bearer token.

        :param token: Optional JWT override; uses constructor token when omitted.
        :return: Raw HTTP response.
        """
        return self.post(_LOGOUT_PATH, token=token)

    def me_preflight(self, *, origin: str) -> httpx.Response:
        """OPTIONS preflight for ``GET /api/v1/auth/me`` from a browser origin.

        :param origin: Value for the ``Origin`` request header.
        :return: Raw HTTP response.
        """
        return self.options(
            _ME_PATH,
            headers={
                "Origin": origin,
                "Access-Control-Request-Method": "GET",
                "Access-Control-Request-Headers": "authorization",
            },
        )
