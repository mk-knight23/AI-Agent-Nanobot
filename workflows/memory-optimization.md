# Memory Optimization — Nanobot

Monitor and optimize Nanobot's memory usage, context window utilization, and conversation history management for long-running sessions.

## Trigger
- **Background**: Runs automatically as a background coroutine
- **Manual**: `@Nanobot memory-optimization status`
- **Alert**: Triggered when context usage exceeds 70%

## What It Monitors

### Context Window
- Current token count vs model limit
- Oldest messages in conversation history
- Large tool results hogging context

### Python Memory
- `tracemalloc` heap snapshots every 10 minutes
- Pinpoints top allocation sites
- Alerts when RSS > configured threshold

### Agent Memory (Supabase)
- Total records in `agent_memory` table
- Last-accessed timestamps
- Items not accessed in >30 days (candidates for archiving)

## Automatic Actions

| Trigger | Action |
|---------|--------|
| Context > 70% | Summarize oldest 20% of conversation history |
| Context > 85% | Aggressive compression: summarize tool results inline |
| RSS > 200MB | `gc.collect()` + alert |
| Memory record stale >30 days | Move to `agent_memory_archive` table |

## Manual Controls

```
@Nanobot memory-optimization compact       # Compress context now
@Nanobot memory-optimization clear-stale  # Archive old memory records
@Nanobot memory-optimization report        # Show memory usage report
```

## Memory Report Example

```
🧠 Memory Report

Context: 42,300 / 200,000 tokens (21%)
  Oldest message: 2 hours ago
  Largest tool result: vault_search (8,400 tokens)

Python heap: 48MB RSS
  Top allocations:
    - conversation_history: 12MB
    - tool_results_cache: 8MB

Agent memory (Supabase): 143 records
  Stale (>30 days): 12 records → suggest archiving
```

## Context Summarization Strategy

When compressing, Nanobot preserves:
- The current task and recent decisions
- Any code that hasn't been committed yet
- Error messages and their resolutions
- Explicit user preferences stated in the session
