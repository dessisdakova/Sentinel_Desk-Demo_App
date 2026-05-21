# Epic E01 — Platform Foundation

**Epic key:** `SENT-E01`  
**Summary:** Bootstrapping SentinelDesk: Docker, PostgreSQL, FastAPI skeleton, React SPA, auth, RBAC.  
**Business value:** Analysts can securely sign in; all later modules share one platform.

---

## Goals

- One command starts the full local stack
- Users authenticate with JWT and see role-appropriate navigation
- Database migrations run cleanly on empty DB

---

## Acceptance criteria (epic level)

- [ ] `docker compose up` starts postgres, redis, api, frontend (dev), mailhog
- [ ] `alembic upgrade head` creates schema
- [ ] `scripts/seed.py` creates 3 users per TEST_DATA.md
- [ ] Login works for all roles; invalid password returns 401
- [ ] Protected route returns 403 for wrong role
- [ ] README documents prerequisites (Docker Desktop, Python 3.12)

---

## Technical scope

| In scope | Out of scope |
|----------|--------------|
| User model, bcrypt passwords | Alerts, cases |
| JWT login/logout/me | Celery worker (E02) |
| React login page + app shell | Playbooks |
| CORS, health check `GET /health` | Bug garden |

---

## Stories (suggested breakdown)

| Story key | Title |
|-----------|-------|
| SENT-101 | Docker Compose for Postgres, Redis, MailHog |
| SENT-102 | FastAPI project structure + health endpoint |
| SENT-103 | User model + Alembic initial migration |
| SENT-104 | Auth API login/logout/me |
| SENT-105 | RBAC dependency `require_roles` |
| SENT-106 | React app shell, router, auth context |
| SENT-107 | Login page with data-testid |
| SENT-108 | Seed script for users |

---

## QA notes (for later tests)

- API: login positive/negative, me with expired token
- E2E: login as each role, assert nav items visible/hidden
- Integration: user row exists after seed

---

## Tickets

See [docs/tickets/E01/](../tickets/E01/README.md) — implement `SENT-101` … `SENT-108`, then each `-QA` ticket.
