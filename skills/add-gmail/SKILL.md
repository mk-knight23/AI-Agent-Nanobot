---
name: add-gmail
description: "Adds Gmail monitoring to Nanobot using the Google Gmail API with OAuth2. Creates channels/gmail.py that polls INBOX for unread messages, passes them to the agent, and sends replies after approval. Use when you want Nanobot to process and respond to emails. Requires a Google Cloud project with Gmail API enabled."
---

# add-gmail

Gmail inbox monitoring for Nanobot: async polling, AI-drafted replies, approval before send.

## Usage
```
/add-gmail
```

## Files Created
```
channels/gmail.py               # Async GmailChannel with OAuth2
auth/gmail_flow.py              # One-time OAuth2 authorization helper
```

## Files Modified
```
channels/__init__.py            # Register GmailChannel
config.py                       # Add Gmail auth config fields
requirements.txt                # Add google-api-python-client, google-auth-oauthlib
```

## Environment Variables
```
GMAIL_CREDENTIALS_JSON=/path/to/credentials.json   # Google OAuth2 client credentials
GMAIL_TOKEN_JSON=/path/to/token.json               # Auto-generated after first auth
GMAIL_ADDRESS=you@gmail.com
GMAIL_POLL_INTERVAL=300                             # Seconds between polls, default 300
GMAIL_PROCESSING_LABEL=nanobot                     # Apply this Gmail label to trigger processing
```

## Setup

1. Google Cloud Console → Enable Gmail API → OAuth2 credentials (Desktop) → Download JSON → save as `credentials.json`
2. Run `/add-gmail`
3. Run `python auth/gmail_flow.py` → browser opens → authorize → `token.json` created
4. Set env vars
5. Start Nanobot — polls Gmail every 5 minutes for `label:nanobot is:unread` emails

## Code Sample
```python
# channels/gmail.py (generated)
import asyncio, base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

class GmailChannel:
    def __init__(self, creds: Credentials):
        self.service = build("gmail", "v1", credentials=creds)

    async def poll(self):
        loop = asyncio.get_event_loop()
        messages = await loop.run_in_executor(
            None,
            lambda: self.service.users().messages().list(
                userId="me", q="label:nanobot is:unread"
            ).execute().get("messages", [])
        )
        return [await self._fetch(m["id"]) for m in messages]

    async def _fetch(self, message_id: str) -> dict:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            lambda: self.service.users().messages().get(
                userId="me", id=message_id, format="full"
            ).execute()
        )
```
