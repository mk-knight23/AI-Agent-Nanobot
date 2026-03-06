---
name: add-supabase
description: "Adds Supabase as Nanobot's persistent backend using the supabase-py client. Creates tables for agent memory, skill invocations, and conversation history. Registers memory_read and memory_write as tools so skills can persist state across sessions. Requires a Supabase project URL and anon key."
---

# add-supabase

Persistent memory for Nanobot: skills can store and retrieve structured state across restarts.

## Usage
```
/add-supabase
```

## Files Created
```
db/supabase_client.py           # Typed Supabase client wrapper
db/migrations/001_init.sql      # Schema: agent_memory, skill_invocations, conversations
tools/memory.py                 # memory_read / memory_write tools
```

## Files Modified
```
tools/__init__.py               # Register memory_read, memory_write
config.py                       # Add SUPABASE_URL, SUPABASE_ANON_KEY
requirements.txt                # Add supabase>=2.0
```

## Environment Variables
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your_anon_key
```

## Tables Created

Run `db/migrations/001_init.sql` in the Supabase SQL Editor:

```sql
CREATE TABLE agent_memory (
  key TEXT PRIMARY KEY,
  value JSONB NOT NULL,
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE skill_invocations (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  skill_name TEXT NOT NULL,
  input JSONB,
  duration_ms INTEGER,
  ts TIMESTAMPTZ DEFAULT now()
);
```

## Code Sample
```python
# db/supabase_client.py (generated)
from supabase import create_client, Client
import os

def get_client() -> Client:
    return create_client(
        os.environ["SUPABASE_URL"],
        os.environ["SUPABASE_ANON_KEY"]
    )

async def memory_get(key: str):
    client = get_client()
    result = client.table("agent_memory").select("value").eq("key", key).maybe_single().execute()
    return result.data["value"] if result.data else None

async def memory_set(key: str, value: dict):
    client = get_client()
    client.table("agent_memory").upsert({"key": key, "value": value}).execute()
```
