# ClawWork Coworker — Nanobot

Nanobot as an always-on AI coworker: available throughout your workday to assist with coding, research, writing, and decisions.

## Trigger
- **Continuous**: Runs while Nanobot is active, responds to direct messages via any registered channel
- **Mention**: Any message containing `@Nanobot` triggers the coworker mode

## What Makes It a "Coworker"

Unlike a command-mode agent that waits for explicit tasks, coworker mode:

1. **Maintains conversation context**: Remembers what you were working on earlier in the session
2. **Proactively suggests**: If you paste code with a bug, Nanobot mentions it
3. **Follows up**: If you asked it to research something, it follows up when done
4. **Learns preferences**: Stores your preferences in agent memory (requires `add-supabase`)

## Example Interactions

**Code pair programming:**
```
You: @Nanobot I'm trying to figure out why this async function is blocking
You: [pastes code]
Nanobot: The issue is on line 23 — `requests.get()` is synchronous. Replace with `await httpx.AsyncClient().get()`.
         Also, the loop on line 31 could be `asyncio.gather()` for 3x speedup.
```

**Research on demand:**
```
You: @Nanobot compare polars vs pandas for a 50M row dataset
Nanobot: [detailed comparison with benchmarks]
You: which would you use?
Nanobot: polars — the lazy evaluation alone saves memory on 50M rows, and your use case (filtering + groupby) is exactly where it wins.
```

**Decision support:**
```
You: @Nanobot should I use Redis or Supabase Realtime for pub/sub here?
Nanobot: Given your current stack (Supabase already installed), Supabase Realtime is the right call — no new service to manage, and for <1000 concurrent subscribers it won't bottleneck.
```

## Memory Configuration

Nanobot remembers preferences when Supabase is installed:

```python
# Stored preferences (auto-learned)
{
  "preferred_framework": "FastAPI",
  "code_style": "type hints required",
  "response_length": "concise",
  "timezone": "America/Los_Angeles"
}
```
