# Test data files

Static files used by pytest. **Do not** put secrets or production credentials here.

| File | Used by | Purpose |
|------|---------|---------|
| `invalid_postgres.json` | `test_postgres_rejects_invalid_credentials` | Wrong DB user/password for QA-101-2 |
| `auth_seed.py` | `test_auth_seed` | Seed users for QA-104 |

Application seed data and stable UUIDs are documented in [docs/TEST_DATA.md](../../docs/TEST_DATA.md) and will be asserted from **E02** onward.
