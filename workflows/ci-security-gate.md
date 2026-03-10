# CI Security Gate — Nanobot

Automated security scan that runs on every PR and blocks merge if CRITICAL or HIGH issues are found.

## Trigger
- **Event**: GitHub PR opened or updated
- **Blocks**: merge if security issues found above threshold
- **Notifies**: PR comment + Telegram alert for CRITICAL

## Pipeline

### Step 1: Dependency Audit
```bash
pip-audit --strict
safety check -r requirements.txt
```
- Fails on any CRITICAL CVE in dependencies
- Warns on HIGH CVEs (non-blocking but noted in PR comment)

### Step 2: Code Security Scan
```bash
bandit -ll -r src/          # CRITICAL/HIGH security patterns only
semgrep --config=auto src/  # OWASP rules
```

### Step 3: Secret Detection
```bash
detect-secrets scan --baseline .secrets.baseline
```
- Fails if any new secrets detected vs. baseline

### Step 4: AI Security Review
```python
@Nanobot code-reviewer --diff HEAD~1..HEAD --strict --security-only
```
- AI reviews the diff for: hardcoded values, unsafe deserialization,
  auth bypass patterns, injection risks

### Step 5: PR Comment
```markdown
## Nanobot Security Gate

✅ No CVEs found in dependencies
✅ No secrets detected
⚠️ 1 MEDIUM issue: `src/api/routes.py:47` — missing rate limit
✅ AI review passed

**Status: APPROVED** (MEDIUM issues non-blocking)
```

## GitHub Actions Integration
```yaml
# .github/workflows/security-gate.yml
on:
  pull_request:
    branches: [main]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install uv && uv sync
      - run: python -m nanobot ci-security-gate --pr ${{ github.event.number }}
```

## Thresholds
- **CRITICAL**: Blocks merge, creates GitHub issue, Telegram alert
- **HIGH**: Blocks merge, PR comment
- **MEDIUM**: Non-blocking, PR comment
- **LOW**: Silent pass
