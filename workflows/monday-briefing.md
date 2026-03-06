# Monday Briefing — Nanobot

Start-of-week briefing covering weekend activity and priorities.

## Trigger
- **Schedule**: Every Monday at 8:00 AM
- **Manual**: `@Nanobot run monday-briefing`

## What Nanobot Covers

### Weekend Activity
- New GitHub issues and PRs
- Missed messages on Slack/Telegram
- Unread priority emails (if Gmail installed)

### This Week's Priorities
- Your assigned issues by priority
- PRs awaiting your review
- Upcoming milestones

### Dependency News
- New versions of packages in `requirements.txt`
- Security advisories for your dependencies

## Example Output

```
☕ Monday Briefing — March 10

Weekend:
  • 1 PR merged (teammate)
  • Issue #110 opened: "Add OpenAI provider support"
  • 8 Slack messages in #nanobot

This week:
  🔴 Issue #108 [HIGH]: Memory leak in session manager
  🟡 PR #95: Review requested by teammate
  🟢 Issue #100: Add data-pipeline skill (your next item)

Dependencies:
  • anthropic: 0.39.0 → 0.40.0 available
```
