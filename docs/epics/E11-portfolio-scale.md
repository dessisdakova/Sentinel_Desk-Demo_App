# Epic E11 — Portfolio Scale & NFR Hooks

**Epic key:** `SENT-E11`  
**Summary:** Bulk seed, performance test hooks, optional accessibility IDs.  
**Business value:** Stretch goals for non-functional and complex data scenarios.

---

## Acceptance criteria

- [ ] `POST /api/v1/dev/seed-bulk?count=N` (admin, max 50000)
- [ ] Documented p95 targets in README for locust/k6 scripts (scripts optional)
- [ ] Index verification for slow query log locally
- [ ] Optional: `aria-label` mirrors `data-testid` on primary actions (a11y practice)
- [ ] Optional: screenshot baseline folder for visual regression experiments

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-1101 | Bulk seed endpoint |
| SENT-1102 | Locustfile sample for ingest + list |
| SENT-1103 | aria-label pass on P1–P3 pages |

---

## QA notes

- Performance: run only when learning — not blocking MVP
- Compare queue API latency before/after bulk seed
