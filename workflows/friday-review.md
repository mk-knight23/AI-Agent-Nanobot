# Friday Review — Nanobot

Weekly retrospective delivered every Friday afternoon. Nanobot reviews code velocity, open items, and surfaces blockers.

## Trigger
- **Schedule**: Every Friday at 4:00 PM
- **Manual**: `@Nanobot run friday-review`

## What Nanobot Reports

### Code Velocity
- PRs merged (count + list)
- Issues closed vs opened
- Average PR review time this week

### Open Items
- PRs open >3 days
- Issues assigned with no activity >2 days
- Conversations started but unresolved

### Blockers
- Failing CI on any tracked branch
- Dependency CVEs (if code-reviewer skill installed)
- PRs with unresolved review comments

### Next Week Preview
- Issues labeled `next-week`
- Upcoming milestones from GitHub

## Example Output

```
📅 Friday Review — Week of Mar 3–7

Velocity: 4 PRs merged | 7 issues closed | avg review time: 18h

Open items:
  ⚠ PR #89: "Refactor channel router" — 4 days open, 1 approval needed
  ⚠ Issue #102: Assigned to you, no update since Tuesday

Blockers:
  🔴 CI failing on main: test_data_pipeline timeout

Next week:
  • Milestone "v1.2.0" due March 15 — 3 open issues remaining
```
