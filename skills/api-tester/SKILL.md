---
name: api-tester
description: "Auto-generates a pytest test suite from an OpenAPI spec (YAML or JSON) and runs it against a live endpoint. Discovers all operations, generates parametric tests for success, error, and edge cases, runs them with httpx async client, and outputs API_TEST_REPORT.md. Use when you have an OpenAPI spec and want instant test coverage for an API. Requires a running API endpoint or mock server."
---

# api-tester

Point Nanobot at an OpenAPI spec. It generates tests, runs them, and gives you a coverage report.

## Usage
```
@Nanobot api-tester --spec openapi.yaml --base-url http://localhost:8000
@Nanobot api-tester --spec https://api.example.com/openapi.json --auth Bearer $TOKEN
@Nanobot api-tester --spec openapi.yaml --only-paths "/users,/orders"
```

## What It Does

1. **Parse**: Reads the OpenAPI spec (local file or URL, YAML or JSON)
2. **Plan**: For each operation, determines: happy path, required-fields-missing, invalid-type, auth-missing cases
3. **Generate**: Creates `tests/api/test_<tag>.py` files, one per tag, with parametric pytest cases
4. **Run**: Executes with `pytest -v --asyncio-mode=auto`
5. **Report**: Writes `API_TEST_REPORT.md` with pass/fail per endpoint, response time stats, and failures

## Files Created
```
tests/api/test_<tag>.py         # Generated pytest files, one per OpenAPI tag
API_TEST_REPORT.md              # Pass/fail + timing + known failures
conftest.py                     # httpx.AsyncClient fixture (if not present)
```

## Example Generated Test
```python
# tests/api/test_users.py (generated)
import pytest
import httpx

@pytest.mark.asyncio
@pytest.mark.parametrize("payload,expected", [
    ({"name": "Alice", "email": "alice@example.com"}, 201),
    ({}, 422),                                   # Missing required fields
    ({"name": "A" * 300, "email": "bad"}, 422),  # Validation errors
])
async def test_create_user(client: httpx.AsyncClient, payload, expected):
    r = await client.post("/users", json=payload)
    assert r.status_code == expected
```

## API_TEST_REPORT.md Contents
- Summary table: endpoint, method, tests run, passed, failed
- Response time percentiles (p50, p95, p99) per endpoint
- Full output of failed assertions

## Philosophy
Never hardcode expected values when the spec defines them. Nanobot derives test expectations from the spec's `required` fields, `enum` constraints, and `minimum/maximum` validations.
