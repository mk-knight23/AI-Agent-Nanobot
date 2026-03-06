---
name: web-searcher
description: "Brave Search and AI-driven web analysis skill. Performs live web searches, scrapes relevant page content, and provides synthesized answers with source citations. Can be used for research, fact-checking, and latest news updates. Supports filtering by domain, date range, and content type."
---

# web-searcher

Search the live web and synthesize answers from multiple sources.

## Usage
```
@Nanobot web-searcher --query "latest Rust 1.76 features"
@Nanobot web-searcher --query "NVIDIA earnings report" --site reuters.com
@Nanobot web-searcher --research "current state of agentic AI" --depth 3
```

## Features

| Tool | Purpose |
|------|---------|
| `Brave Search` | High-quality, ad-free web search results |
| `scrapper` | Markdown-optimized page content extraction |
| `synthesizer` | AI-driven multi-source analysis and summary |
| `citations` | Automatic source tracking and linking |

## Configuration
Requires `BRAVE_SEARCH_API_KEY` in `config.json` or as an environment variable.

## Philosophy
The `web-searcher` skill focuses on accuracy over speed. It doesn't just return the first search result; it cross-references information from at least 3 high-authority sources to ensure the synthesized answer is reliable and up-to-date.
