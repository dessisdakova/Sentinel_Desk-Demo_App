# Epic E02 — Alert Ingestion & Async Enrichment

**Epic key:** `SENT-E02`  
**Summary:** External systems submit alerts; worker enriches and sets SLA.  
**Business value:** SOC receives normalized events without manual data entry.

---

## Goals

- Mock SIEM can POST alerts on a schedule
- Ingest API validates payload and returns 202
- Celery worker enriches alert (tags, `sla_due_at`, `enrichment_status`)

---

## Acceptance criteria

- [ ] `POST /api/v1/alerts/ingest` with API key creates alert in `NEW`
- [ ] Duplicate `external_id` returns 409
- [ ] Worker sets `enrichment_status` from PENDING → COMPLETE within 30s
- [ ] `GET /api/v1/alerts/{id}` shows enrichment fields
- [ ] Audit log entry `ALERT_INGESTED` created
- [ ] mock-siem container posts at least 1 alert/minute (configurable)

---

## Data model additions

- `alerts` table per CONSTITUTION
- `alert_events` for timeline
- Enum types: severity, source, status

---

## Stories

| Story key | Title |
|-----------|-------|
| SENT-201 | Alert + AlertEvent models and migration |
| SENT-202 | Ingest API with API key auth |
| SENT-203 | Celery worker + enrich_alert task |
| SENT-204 | Alert GET by id + list (basic, no UI filters yet) |
| SENT-205 | mock-siem Python script |
| SENT-206 | Seed alerts per TEST_DATA.md |

---

## QA notes

- API: ingest valid/invalid payload, duplicate external_id
- Integration: after ingest, poll DB until enrichment COMPLETE
- Contract: OpenAPI documents ingest schema
