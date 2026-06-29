from typing import Any

import httpx

from tests.support.api_session import ApiSession


class BaseApiClient:
    """Thin wrapper around ``httpx.Client`` with shared auth header handling."""

    def __init__(self, session: ApiSession, token: str | None = None) -> None:
        """Store the API session and an optional default JWT.

        :param session: Session-scoped ``ApiSession`` (``base_url`` + ``client``).
        :param token: Optional bearer token applied when a call omits ``token``.
        """
        self._session = session
        self._token = token

    @property
    def base_url(self) -> str:
        """FastAPI root URL for this session."""
        return self._session.base_url

    @property
    def _client(self) -> httpx.Client:
        """Underlying HTTP client (single instance per pytest session)."""
        return self._session.client

    def _merge_headers(
        self,
        headers: dict[str, str] | None,
        token: str | None,
    ) -> dict[str, str]:
        """Build request headers, injecting ``Authorization`` when a token exists.

        :param headers: Caller-supplied headers; may be ``None``.
        :param token: Per-call token override; falls back to ``self._token``.
        :return: Merged header dict (never ``None``).
        """
        merged = dict(headers or {})
        effective_token = self._token if token is None else token
        if effective_token and "Authorization" not in merged:
            merged["Authorization"] = f"Bearer {effective_token}"
        return merged

    def get(
        self,
        path: str,
        *,
        token: str | None = None,
        **kwargs: Any,
    ) -> httpx.Response:
        """Send ``GET`` and return the raw response."""
        headers = self._merge_headers(kwargs.pop("headers", None), token)
        return self._client.get(path, headers=headers, **kwargs)

    def post(
        self,
        path: str,
        *,
        token: str | None = None,
        **kwargs: Any,
    ) -> httpx.Response:
        """Send ``POST`` and return the raw response."""
        headers = self._merge_headers(kwargs.pop("headers", None), token)
        return self._client.post(path, headers=headers, **kwargs)

    def put(
        self,
        path: str,
        *,
        token: str | None = None,
        **kwargs: Any,
    ) -> httpx.Response:
        """Send ``PUT`` and return the raw response."""
        headers = self._merge_headers(kwargs.pop("headers", None), token)
        return self._client.put(path, headers=headers, **kwargs)

    def patch(
        self,
        path: str,
        *,
        token: str | None = None,
        **kwargs: Any,
    ) -> httpx.Response:
        """Send ``PATCH`` and return the raw response."""
        headers = self._merge_headers(kwargs.pop("headers", None), token)
        return self._client.patch(path, headers=headers, **kwargs)

    def delete(
        self,
        path: str,
        *,
        token: str | None = None,
        **kwargs: Any,
    ) -> httpx.Response:
        """Send ``DELETE`` and return the raw response."""
        headers = self._merge_headers(kwargs.pop("headers", None), token)
        return self._client.delete(path, headers=headers, **kwargs)

    def options(
        self,
        path: str,
        *,
        token: str | None = None,
        **kwargs: Any,
    ) -> httpx.Response:
        """Send ``OPTIONS`` and return the raw response."""
        headers = self._merge_headers(kwargs.pop("headers", None), token)
        return self._client.options(path, headers=headers, **kwargs)
