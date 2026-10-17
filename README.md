# Quality Event Register API

A demonstration API that returns fictional manufacturing quality events.
This project combines quality assurance knowledge with API testing and
technical documentation.

The current implementation provides two read-only endpoints. It does not
create, update or store quality events.

## Available endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/` | Check that the API responds and retrieve its version |
| GET | `/quality-events` | Retrieve two simulated quality events |

## Try the API in Swagger UI

With the API server running:

1. Open your application's base URL and add `/docs`.
2. Expand `GET /quality-events`.
3. Select **Try it out**, then **Execute**.
4. Check the **Server response**.

Expected result: HTTP `200` with a JSON array containing two quality events.

When using GitHub Codespaces, use the forwarded URL for port 8000.
The Codespace and API server must remain running.

## Retrieve quality events

### Request

`GET /quality-events`

This endpoint requires no path parameters, query parameters or request body.

From a terminal in the same environment as the running API:

```bash
curl -i http://127.0.0.1:8000/quality-events
```

The `-i` option includes the response headers so you can inspect the
HTTP status and content type.

### Successful response

HTTP status: `200 OK`

Content-Type: `application/json`

```json
[
  {
    "event_id": "QE-2026-0001",
    "event_type": "Deviation",
    "title": "Packaging seal integrity failure",
    "severity": "Major",
    "status": "Open"
  },
  {
    "event_id": "QE-2026-0002",
    "event_type": "Nonconformance",
    "title": "Finished product outside weight specification",
    "severity": "Minor",
    "status": "Under Investigation"
  }
]
```

### Response fields

Each object in the response represents one fictional quality event.

| Field | Type | Description |
| --- | --- | --- |
| `event_id` | string | Identifier of the simulated event |
| `event_type` | string | Event classification, such as Deviation or Nonconformance |
| `title` | string | Brief description of the quality issue |
| `severity` | string | Severity assigned to the simulated event |
| `status` | string | Current investigation status of the simulated event |

These values are fixed demonstration data. Repeating the request returns
the same two records.

## Check API availability

### Request

`GET /`

### Successful response

HTTP status: `200 OK`

```json
{
  "message": "Quality Event Register API is running",
  "status": "success",
  "version": "0.1.0"
}
```

## Manual testing

Both requests were executed in Swagger UI on October 16, 2026.

| Test ID | Request | Expected result | Observed result |
| --- | --- | --- | --- |
| API-TC-001 | `GET /` | HTTP 200 and the API status message | Passed |
| API-TC-002 | `GET /quality-events` | HTTP 200 and both expected quality events | Passed |

Saved evidence for API-TC-001:

- [Functional test report](evidence/API-TC-001-Functional-Test-Report.pdf)
- [Swagger screenshots](evidence/API-TC-001-Swagger-Evidence.pdf)

## Troubleshooting

If the Codespaces URL returns HTTP 502, check that the API server is
running. From the project directory, start it with:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

This command requires FastAPI and Uvicorn to be installed in the active
Python environment.

Leave the server terminal running, then refresh `/docs`.
If startup fails, inspect the terminal error before retrying.

## Project scope

This is a learning and portfolio project using fictional data.
The current version does not implement event creation, editing, deletion,
database persistence or CAPA workflows.