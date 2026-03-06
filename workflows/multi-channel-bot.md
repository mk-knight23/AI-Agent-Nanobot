# Multi-Channel Bot — Nanobot

Run Nanobot across multiple communication channels simultaneously, with a unified conversation context and cross-channel routing.

## Trigger
- **Automatic**: Starts all registered channels when Nanobot launches
- **Manual**: `@Nanobot multi-channel status`

## Architecture

```
Telegram ───────┐
Slack ──────────┼──→  Channel Router  ──→  Nanobot Core  ──→  Response
Gmail ──────────┤           ↑
Custom HTTP ────┘     Context Manager
                      (unified history)
```

Each channel runs in its own `asyncio` task. All messages flow through the central `ChannelRouter` which maintains unified conversation context.

## Cross-Channel Features

### Unified Context
Messages from all channels are merged into a single conversation history. You can start a task in Slack and continue it in Telegram.

### Channel Routing
Direct output to a specific channel:
```
@Nanobot send the weekly report to email instead of Slack
```

### Priority Channels
Configure which channel gets important alerts:
```python
# config.py
ALERT_CHANNEL = "telegram"   # Urgent alerts always go to Telegram
DIGEST_CHANNEL = "slack"     # Digests go to Slack
REPORT_CHANNEL = "gmail"     # Reports go to email
```

## Setting Up Multi-Channel

1. Install desired channels: `/add-telegram`, `/add-slack`, `/add-gmail`
2. Configure priorities in `config.py`
3. Start Nanobot — all channels activate simultaneously

## Message Deduplication

If you send the same message to multiple channels (or a bot is in multiple Slack workspaces), Nanobot deduplicates by content hash + 60-second window. You won't get duplicate responses.

## Status Dashboard

```
@Nanobot multi-channel status

Channel Status:
  ✅ Telegram: connected (polling)
  ✅ Slack: connected (socket mode)
  ⚠️  Gmail: last poll 8 min ago (normal — 5 min interval)
  ❌ Custom HTTP: not configured

Messages today: 47
  Telegram: 31  |  Slack: 14  |  Gmail: 2
```
