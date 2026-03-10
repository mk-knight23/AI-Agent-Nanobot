# Repository Upgrade Cycle — Nanobot

Automated weekly pass across all connected repositories: dependency updates, code review, documentation refresh, and deployment.

## Schedule
- **Trigger**: Sunday 2:00 AM (cron)
- **Duration**: ~45 minutes
- **Model**: Haiku (workers) + Sonnet (synthesis)

## Pipeline

### Phase 1: Discovery (5 min)
```python
repos = await discover_repos(config["github_token"])
stale = [r for r in repos if r.last_updated > timedelta(days=30)]
```

### Phase 2: Per-Repo Upgrade (parallel workers)
For each stale repo:
1. `pip-audit` — check for vulnerable deps
2. Update `requirements.txt` / `pyproject.toml` to latest stable
3. Run `code-reviewer` — flag CRITICAL/HIGH issues
4. Run `doc-generator` — refresh README if stale
5. Create PR with all changes

### Phase 3: Batch Processing (10 min)
```python
@Nanobot batch-processor --input repo_list.json \
  --task "summarize top 3 improvements needed per repo"
```

### Phase 4: Synthesis (5 min)
- Sonnet reviews all per-repo summaries
- Generates `UPGRADE_REPORT.md` with ecosystem-wide priorities
- Sends Telegram digest: top 5 repos needing attention

## Configuration
```python
# config/upgrade-cycle.py
REPOS = "all"  # or list of specific repos
SKIP = ["archived", "experimental"]
PR_DRAFT = True   # Create as draft PR — human reviews before merge
CHANNELS = ["telegram"]
```

## Output
```
reports/
├── upgrade_summary_YYYY-MM-DD.md
├── per_repo/
│   ├── nanobot-core_upgrade.md
│   └── ...
└── UPGRADE_REPORT.md    # Ecosystem-wide synthesis
```
