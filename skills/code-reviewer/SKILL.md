---
name: code-reviewer
description: "Runs static analysis (ruff, mypy, bandit) and AI-driven review on any Python codebase or diff. Identifies bugs, type issues, security vulnerabilities, and style violations. Outputs a CODE_REVIEW.md report with CRITICAL/HIGH/MEDIUM/LOW severity ratings and fixing suggestions. Use before committing or merging Python code. Works on files, directories, or git diffs."
---

# code-reviewer

Static analysis + AI review on Python code. Catches bugs, types, security issues, and style in one pass.

## Usage
```
@Nanobot code-reviewer --path src/
@Nanobot code-reviewer --diff HEAD~1..HEAD
@Nanobot code-reviewer --file src/auth/oauth.py
@Nanobot code-reviewer --strict               # Fail on MEDIUM+ issues
```

## What It Runs

| Tool | Purpose |
|------|---------|
| `ruff` | Style, imports, common bugs (PEP 8 compliance) |
| `mypy --strict` | Type checking, missing annotations |
| `bandit -ll` | Security: hardcoded secrets, injection, unsafe calls |
| AI review | Logic bugs, design issues, test coverage gaps |

## Files Created
```
CODE_REVIEW.md                  # Full report with severity-rated findings
```

## CODE_REVIEW.md Structure
```
## Summary
- CRITICAL: 0 | HIGH: 2 | MEDIUM: 5 | LOW: 8

## CRITICAL Issues
(none)

## HIGH Issues
### src/auth/oauth.py:47 — Hardcoded secret
**Issue**: `SECRET_KEY = "abc123"` hardcoded in source.
**Fix**: Use `os.environ["SECRET_KEY"]` with startup validation.

## Medium Issues
...
```

## Severity Classification
- **CRITICAL**: Security vulnerabilities, data loss risks
- **HIGH**: Bugs that will cause failures in production
- **MEDIUM**: Type errors, logic issues, missing validation
- **LOW**: Style, naming, missing docstrings

## Exit Codes (for CI)
```bash
python -m nanobot code-reviewer --path src/ --strict
# Exit 0: no MEDIUM+ issues
# Exit 1: issues found above threshold
```

## Philosophy
The AI review pass looks for what static tools miss: business logic bugs, incorrect algorithm assumptions, and cases where technically correct code produces wrong results for edge inputs.
