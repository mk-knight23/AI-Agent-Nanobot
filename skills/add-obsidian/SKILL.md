---
name: add-obsidian
description: "Mounts an Obsidian vault as a read-only knowledge base for Nanobot. Registers a vault_search tool (async, full-text, scores by match density) so the agent can search your notes during any task. Use when you want Nanobot to reference your personal Obsidian vault for context. Requires the vault accessible as a local directory."
---

# add-obsidian

Nanobot gets access to your Obsidian vault. Ask questions; it searches your notes, synthesizes answers.

## Usage
```
/add-obsidian
```

## Files Created
```
tools/vault_search.py           # Async vault_search tool with full-text scoring
```

## Files Modified
```
tools/__init__.py               # Register vault_search
config.py                       # Add OBSIDIAN_VAULT_PATH
```

## Environment Variables
```
OBSIDIAN_VAULT_PATH=/Users/yourname/Documents/Vault
VAULT_MAX_RESULTS=10
VAULT_EXCERPT_CHARS=400
```

## How It Works

1. The LLM receives `vault_search` as an available tool
2. When a question may be answered by your notes, the LLM calls `vault_search(query="...")`
3. Nanobot walks the vault, scores `.md` files by query keyword density
4. Returns top N results as `[{title, excerpt, path}]`
5. LLM reads excerpts and synthesizes a response

## Code Sample
```python
# tools/vault_search.py (generated)
import asyncio
from pathlib import Path
from typing import List, Dict

async def vault_search(query: str, vault_path: str, max_results: int = 10) -> List[Dict]:
    results = []
    terms = query.lower().split()
    path = Path(vault_path)

    for md_file in path.rglob("*.md"):
        content = md_file.read_text(errors="replace")
        lower = content.lower()
        score = sum(lower.count(t) for t in terms)
        if score > 0:
            idx = next((lower.find(t) for t in terms if t in lower), 0)
            excerpt = content[max(0, idx-100):idx+300]
            results.append({"title": md_file.stem, "excerpt": excerpt, "path": str(md_file), "score": score})

    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:max_results]
```

## Philosophy
Vault search is intentionally read-only — Nanobot never writes to your vault. The vault is your space; Nanobot is a reader, not an editor.
