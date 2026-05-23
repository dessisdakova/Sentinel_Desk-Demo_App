# Epic Index — SentinelDesk

**Implementation agent:** implement epics in order using `SENT-###` tickets only — see [IMPLEMENTATION_AGENT.md](../IMPLEMENTATION_AGENT.md).

Implement in order. Each epic has acceptance criteria at epic level; break down using sample tickets as templates.

| Epic | File | Depends on | Est. stories |
|------|------|------------|--------------|
| E01 | [E01-platform-foundation.md](./E01-platform-foundation.md) | — | 6–8 |
| E02 | [E02-alert-ingestion.md](./E02-alert-ingestion.md) | E01 | 5–7 |
| E03 | [E03-triage-queue-ui.md](./E03-triage-queue-ui.md) | E02 | 6–8 |
| E04 | [E04-alert-detail.md](./E04-alert-detail.md) | E03 | 5–6 |
| E05 | [E05-case-management.md](./E05-case-management.md) | E04 | 6–7 |
| E06 | [E06-playbooks-async.md](./E06-playbooks-async.md) | E02, E04 | 5–6 |
| E07 | [E07-webhooks.md](./E07-webhooks.md) | E02 | 4–5 |
| E08 | [E08-dashboard-audit.md](./E08-dashboard-audit.md) | E03, E05 | 4–5 |
| E09 | [E09-admin-notifications.md](./E09-admin-notifications.md) | E01, E06 | 5–6 |
| E10 | [E10-test-harness-bug-garden.md](./E10-test-harness-bug-garden.md) | E08 | 4–6 |
| E11 | [E11-portfolio-scale.md](./E11-portfolio-scale.md) | E10 | 3–5 |

**Tickets:** [docs/tickets/README.md](../tickets/README.md) — per-epic folders `E01`–`E11` with implementation + `-QA` pairs.
