# SentinelDesk — Ticket index

Jira-style tickets for **implementation** (app code only) and **QA** (your tests in root `tests/`).

## Workflow

```text
For each epic (E01 → E11):
  1. Implement SENT-###     ← AI builds app; no test files
  2. Complete SENT-###-QA   ← You write pytest/Selenium under tests/
  3. Next ticket
```

**Exception:** `SENT-1003-QA` has no implementation ticket (Selenium scaffolding only).

## Epics

| Epic | Folder | Implement stories | QA tickets |
|------|--------|-------------------|------------|
| SENT-E01 Platform Foundation | [E01](./E01/README.md) | 8 | 8 |
| SENT-E02 Alert Ingestion | [E02](./E02/README.md) | 6 | 6 |
| SENT-E03 Triage Queue UI | [E03](./E03/README.md) | 6 | 6 |
| SENT-E04 Alert Detail | [E04](./E04/README.md) | 6 | 6 |
| SENT-E05 Case Management | [E05](./E05/README.md) | 5 | 5 |
| SENT-E06 Playbooks | [E06](./E06/README.md) | 4 | 4 |
| SENT-E07 Webhooks | [E07](./E07/README.md) | 4 | 4 |
| SENT-E08 Dashboard & Audit | [E08](./E08/README.md) | 4 | 4 |
| SENT-E09 Admin & Notifications | [E09](./E09/README.md) | 4 | 4 |
| SENT-E10 Test Harness & Bug Garden | [E10](./E10/README.md) | 3 + harness | 4 (incl. 1003-QA only) |
| SENT-E11 Portfolio Scale | [E11](./E11/README.md) | 3 | 3 |

**Total:** 53 implementation tickets + 54 QA tickets.

## Ticket format

Each file includes: Summary, Description (user story), Acceptance criteria, Technical notes, Out of scope, Definition of Done.
