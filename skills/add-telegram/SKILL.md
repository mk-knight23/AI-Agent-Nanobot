---
name: add-telegram
description: "Adds a Telegram bot channel to Nanobot. Installs python-telegram-bot (v20+, async), creates channels/telegram.py with an async handler, registers it in the channel router, and wires trigger-word filtering. Use when you want Nanobot to receive and respond to Telegram messages. Requires a bot token from @BotFather."
---

# add-telegram

Telegram integration for Nanobot: async Python bot, trigger filtering, thread-safe dispatch.

## Usage
```
/add-telegram
```

## Files Created
```
channels/telegram.py            # Async TelegramChannel using python-telegram-bot v20
```

## Files Modified
```
channels/__init__.py            # Register TelegramChannel in channel registry
config.py                       # Add TELEGRAM_BOT_TOKEN, NANOBOT_TRIGGER
requirements.txt                # Add python-telegram-bot>=20.0
```

## Environment Variables
```
TELEGRAM_BOT_TOKEN=your_bot_token_from_botfather
NANOBOT_TRIGGER=@Nanobot        # Default trigger word
```

## Step-by-Step Walkthrough

1. Message `@BotFather` on Telegram → `/newbot` → copy token
2. Run `/add-telegram`
3. Set `TELEGRAM_BOT_TOKEN` in `.env`
4. Start Nanobot: `python main.py`
5. Message your bot with `@Nanobot <your task>`

## Code Sample
```python
# channels/telegram.py (generated)
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

class TelegramChannel:
    def __init__(self, token: str, trigger: str = "@Nanobot"):
        self.app = Application.builder().token(token).build()
        self.trigger = trigger

    def register(self, handler):
        async def _handle(update: Update, context):
            text = update.message.text or ""
            if self.trigger not in text:
                return
            reply = await handler(text)
            await update.message.reply_text(reply)

        self.app.add_handler(MessageHandler(filters.TEXT, _handle))

    def run(self):
        self.app.run_polling(drop_pending_updates=True)
```

## Philosophy
python-telegram-bot v20+ is fully async — it integrates naturally with Nanobot's `asyncio` runtime without thread pool overhead.
