# SENT-302 — PATCH alert and bulk endpoint

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Epic** | SENT-E03 Triage Queue UI |
| **Priority** | High |
| **Story Points** | 8 |
| **Labels** | `backend`, `alerts`, `implementation` |
| **Paired QA ticket** | [SENT-302-QA](./SENT-302-QA.md) |

---

## Summary

Single-alert PATCH and bulk assign / change-status API with audit logging.

---

## Description

**As a** SOC lead  
**I want to** update one or many alerts via API  
**So that** triage actions are fast and recorded for compliance  

---

## Acceptance criteria

### AC1 — PATCH single alert

- **When** `PATCH /api/v1/alerts/{id}` with `assigned_to`, `status`, or `severity`
- **Then** `200` with updated alert
- **And** `audit_logs` row with appropriate action

### AC2 — Bulk assign

- **Given** alert IDs in `NEW` or `TRIAGING`
- **When** `POST /api/v1/alerts/bulk` with `{ "alert_ids", "action": "ASSIGN", "assigned_to" }`
- **Then** `200` with `{ "updated", "failed" }`
- **And** DB `assigned_to_id` set for each success
- **And** audit per alert

### AC3 — Partial failure

- **Given** one alert `CLOSED` in bulk request
- **Then** `200` with one success and `failed` entry `INVALID_STATE`

### AC4 — Bulk change status

- **When** `action: "CHANGE_STATUS"` with valid target status
- **Then** same partial-failure semantics

### AC5 — Limits

- Max 100 `alert_ids`; empty list → `422`

---

## Technical notes

- Document transaction strategy in code comment
- Error shape per CONSTITUTION §12.2

---

## Out of scope

- Queue UI (SENT-303–305)
- Tests in `tests/` (SENT-302-QA)

---

## Definition of Done

- [ ] OpenAPI updated
- [ ] No test files outside `tests/`
