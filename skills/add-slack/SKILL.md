---
name: add-slack
description: "Adds Slack integration to Nanobot via the Slack Bolt SDK for Python (async mode). Creates channels/slack.py with Socket Mode support, listens for app_mention events, routes through the skill dispatcher, and replies in thread. Use when you want Nanobot in a Slack workspace. Requires a Slack app with app_mentions:read and chat:write scopes and Socket Mode enabled."
---

# add-slack

Nanobot in Slack: async Bolt framework, Socket Mode (no public URL), threaded replies.

## Usage
```
/add-slack
```

## Files Created
```
channels/slack.py               # Async SlackChannel using slack-bolt
```

## Files Modified
```
channels/__init__.py            # Register SlackChannel
config.py                       # Add SLACK_BOT_TOKEN, SLACK_APP_TOKEN
requirements.txt                # Add slack-bolt>=1.18
```

## Environment Variables
```
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-level-token
SLACK_SIGNING_SECRET=your_signing_secret
```

## Setup

1. [api.slack.com/apps](https://api.slack.com/apps) → Create App from Scratch
2. Socket Mode → Enable → App-Level Token with `connections:write` scope → copy as `SLACK_APP_TOKEN`
3. OAuth & Permissions → Scopes: `app_mentions:read`, `chat:write`, `channels:history`
4. Install to Workspace → copy Bot Token
5. Event Subscriptions → Subscribe to `app_mention`
6. Run `/add-slack`, set env vars, start Nanobot

## Code Sample
```python
# channels/slack.py (generated)
from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler

class SlackChannel:
    def __init__(self, bot_token: str, app_token: str, signing_secret: str):
        self.app = AsyncApp(token=bot_token, signing_secret=signing_secret)
        self.app_token = app_token

    def register(self, handler):
        @self.app.event("app_mention")
        async def handle_mention(event, say):
            reply = await handler(event["text"])
            await say(text=reply, thread_ts=event["ts"])

    async def run(self):
        handler = AsyncSocketModeHandler(self.app, self.app_token)
        await handler.start_async()
```
