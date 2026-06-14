# Epic E01 — Platform Foundation

**Epic key:** `SENT-E01`  
**Summary:** Bootstrapping SentinelDesk: Docker, PostgreSQL, FastAPI skeleton, React SPA, auth, RBAC.  
**Business value:** Analysts can securely sign in; all later modules share one platform.

---

## Goals

- One command starts the full local stack **once E01 is complete** (services are added incrementally per story — see story breakdown below)
- Users authenticate with JWT Bearer (`Authorization` header) and see role-appropriate navigation
- Database migrations run cleanly on empty DB

---

## Acceptance criteria (epic level — cumulative)

These criteria describe **epic completion after SENT-108**, not what any single story must deliver on its own. When implementing one ticket, follow **only that ticket’s acceptance criteria** ([sentinel-impl skill](../../.cursor/skills/sentinel-impl/SKILL.md): ticket beats epic summary).

| Epic criterion (done when epic is complete) | Delivered by |
|---------------------------------------------|--------------|
| `docker compose up` starts postgres, redis, mailhog | SENT-101 |
| `docker compose up` starts `api` on port 8000 | SENT-102 |
| `docker compose up` starts `frontend` (dev, port 5173) | SENT-106 |
| `alembic upgrade head` creates schema | SENT-103 |
| `backend/scripts/seed.py` creates **3 users only** per TEST_DATA.md | SENT-108 |
| Login works for all roles; invalid password returns 401 | SENT-104 |
| Protected route returns 403 for wrong role | SENT-105 |
| README documents prerequisites (Docker Desktop, Python 3.12) | SENT-101 (+ updated in later stories as needed) |

**Epic checklist** (verify after SENT-108, not mid-epic):

- [ ] Full stack from table above runs with one `docker compose up`
- [ ] Schema migrated; seed users loaded
- [ ] Auth + RBAC behave as specified
- [ ] README prerequisites documented

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
