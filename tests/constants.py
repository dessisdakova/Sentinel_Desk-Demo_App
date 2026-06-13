# Seconds to wait for a TCP port check before treating a service as down.
PORT_CHECK_TIMEOUT = 0.5
# Default timeout (seconds) for Postgres, Redis, and MailHog probe clients.
CLIENT_TIMEOUT_SEC = 2
# Default timeout (seconds) for HTTP calls to the FastAPI application.
API_TIMEOUT_SEC = 5

SEED_PASSWORD = "DemoPass123!"
SEED_ANALYST_USER = {
    "email": "analyst@demo.local",
    "password": SEED_PASSWORD,
    "role": "ANALYST",
    "display_name": "Alex Analyst",
    "status": "active"
}
SEED_LEAD_USER = {
    "email": "lead@demo.local",
    "password": SEED_PASSWORD,
    "role": "LEAD",
    "display_name": "Jordan Lead",
    "status": "active"
}
SEED_ADMIN_USER = {
    "email": "admin@demo.local",
    "password": SEED_PASSWORD,
    "role": "ADMIN",
    "display_name": "Sam Admin",
    "status": "active"
}
SEED_INACTIVE_USER = {
    "email": "inactive@demo.local",
    "password": SEED_PASSWORD,
    "role": "ANALYST",
    "display_name": "Dana Inactive",
    "status": "inactive",
}
SEED_USERS = [
    SEED_ANALYST_USER,
    SEED_LEAD_USER,
    SEED_ADMIN_USER,
    SEED_INACTIVE_USER,
]

SPA_ORIGIN = "http://localhost:5173"
