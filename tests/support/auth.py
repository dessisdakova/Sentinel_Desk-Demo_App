

def _login_as(role: str, api_client, credentials: dict[str, str]) -> str:
    """Log in with the given user's credentials and return the token.

    :param role: Role name (for the error message only).
    :param api_client: Configured httpx client.
    :param credentials: Dict with "email" and "password" from the secrets provider.
    :return: JWT access token string.
    """
    response = api_client.post(
        "/api/v1/auth/login",
        json={"email": credentials["email"], "password": credentials["password"]},
    )
    if response.status_code != 200:
        raise ValueError(f"Failed to login as {role}: {response.json()}")
    return response.json()["access_token"]
