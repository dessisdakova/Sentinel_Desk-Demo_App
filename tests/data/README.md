# Test data files

Static files used by pytest. **Do not** put secrets or production credentials here.

| File | Used by | Purpose |
|------|---------|---------|
| `invalid_postgres.json` | `test_postgres_rejects_invalid_credentials` | Wrong DB user/password for QA-101-2 |
| `auth_seed.py` | `test_auth_seed` | Seed users for QA-104 (superseded by `tests/constants.py` + SENT-108 seed script) |

Application seed data and stable UUIDs are documented in [docs/TEST_DATA.md](../../docs/TEST_DATA.md). User seed DB assertions: SENT-108-QA (`test_seed_users.py`); alert UUID assertions from **E02** onward.
