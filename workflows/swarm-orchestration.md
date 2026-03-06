# Swarm Orchestration — Nanobot

Nanobot as orchestrator: decomposes complex tasks into parallel Python async workers for maximum throughput.

## Trigger
- **Manual**: `@Nanobot swarm "<goal>"`

## Architecture

Nanobot uses `asyncio.gather()` to run worker coroutines in parallel, with shared state managed via `asyncio.Queue` or Supabase (if installed).

```python
# Internal swarm execution
results = await asyncio.gather(*[
    worker(subtask) for subtask in decompose(goal)
])
synthesis = await orchestrate(goal, results)
```

## Swarm Patterns

### Parallel Analysis
```
@Nanobot swarm "analyze these 5 log files and find the common error pattern"
```
5 worker tasks run concurrently, orchestrator identifies the common thread.

### Multi-Provider Comparison
```
@Nanobot swarm "compare the output quality of Claude, GPT-4, and Gemini on these 10 test prompts"
```
3 provider workers run in parallel, orchestrator scores and compares.

### Bulk Processing
```
@Nanobot swarm "run code-reviewer on all 12 PRs in our backlog"
```
12 concurrent reviews with consolidated report.

## Configuration

```python
# config.py
SWARM_MAX_WORKERS = 5
SWARM_WORKER_MODEL = "claude-haiku-4-5"  # Cost-efficient
SWARM_ORCHESTRATOR_MODEL = "claude-sonnet-4-5"
SWARM_TIMEOUT = 300
```

## Monitoring

Active swarm tasks are logged to `logs/swarm.jsonl`. If Supabase is installed, task state is persisted to the `skill_invocations` table for post-mortem analysis.
