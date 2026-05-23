# SentinelDesk — Ticket index

Jira-style tickets for **implementation** (app code only) and **QA** (human QA engineer + separate QA workflow).

**Implementation agents:** start with [IMPLEMENTATION_AGENT.md](../IMPLEMENTATION_AGENT.md). Implement `SENT-###` only — never `-QA` tickets.

## Workflow

```text
Implementation agent (per epic):
  1. Implement SENT-###     ← app code only; never tests/
  2. Stop — QA is a separate human workflow

QA engineer (separate AI assistant):
  1. After app story is runnable, complete SENT-###-QA under tests/
  2. Next QA ticket
```

**QA-only tickets (no implementation story):** [SENT-1002-QA](./E10/SENT-1002-QA.md) (supersedes SENT-1002), [SENT-1003-QA](./E10/SENT-1003-QA.md) (Selenium POM polish — bootstrap is SENT-107-QA).

**E2E prerequisite:** UI tickets with e2e scope require [SENT-107-QA](./E01/SENT-107-QA.md) bootstrap first (TESTING_STRATEGY §4.3).

**Seed baseline (all QA tickets):** Before **SENT-1001** app (E10), use manual re-seed ([TEST_DATA.md §5 Option B/C](../TEST_DATA.md#5-how-to-reset-by-phase)). After **SENT-1002-QA**, prefer `clean_db` fixture / reset API.

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
| SENT-E10 Test Harness & Bug Garden | [E10](./E10/README.md) | 2 (1001, 1004) | 4 (incl. 1002-QA, 1003-QA QA-only) |
| SENT-E11 Portfolio Scale | [E11](./E11/README.md) | 3 | 3 |

**Total:** 52 implementation tickets + 54 QA tickets.

## Ticket format

Each file includes: Summary, Description (user story), Acceptance criteria, Technical notes, Out of scope, Definition of Done.
