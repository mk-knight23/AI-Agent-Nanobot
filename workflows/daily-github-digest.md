# Daily GitHub Digest — Nanobot

Every morning, Nanobot fetches GitHub activity across your watched repos and delivers a structured digest.

## Trigger
- **Schedule**: Daily at 8:00 AM (`NANOBOT_DIGEST_TIME` env var)
- **Manual**: `@Nanobot run daily-github-digest`

## Prerequisites
- `GITHUB_TOKEN` in environment
- `github_repos` list in `config.py`
- At least one channel (Telegram, Slack, or Gmail)

## What Nanobot Does

1. Calls GitHub REST API for each watched repo
2. Collects: new issues, merged PRs, comments mentioning you, CI failures
3. Filters bot noise (Dependabot, CodeRabbit, GitHub Actions user)
4. Formats as a Markdown digest
5. Dispatches via all registered channels

## Example Output

```
📋 GitHub Digest — 2026-03-05

your-org/nanobot
  • PR #34 merged: "Add async IMAP channel"
  • Issue #67 opened: "Memory leak in long-running sessions"
  • ⚠ CI failed on branch feature/data-pipeline

anthropics/anthropic-sdk-python
  • New release: v0.40.0 — streaming improvements
```

## Configuration

```python
# config.py
GITHUB_WATCHED_REPOS = [
    "your-org/nanobot",
    "anthropics/anthropic-sdk-python",
]
GITHUB_DIGEST_TIME = "08:00"
GITHUB_SKIP_BOTS = True
```
