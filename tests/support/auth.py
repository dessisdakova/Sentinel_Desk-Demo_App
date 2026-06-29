from tests.support.api_session import ApiSession
from tests.support.clients.auth_client import AuthClient


def _login_as(role: str, session: ApiSession, credentials: dict[str, str]) -> str:
    """Log in with the given user's credentials and return the token.

    :param role: Role name (for the error message only).
    :param session: Session-scoped API session.
    :param credentials: Dict with "email" and "password" from the secrets provider.
    :return: JWT access token string.
    """
    response = AuthClient(session).login(
        credentials["email"],
        credentials["password"],
    )
    if response.status_code != 200:
        raise ValueError(f"Failed to login as {role}: {response.json()}")
    return response.json()["access_token"]
