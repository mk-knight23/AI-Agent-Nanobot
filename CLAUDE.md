# AI-Agent-Nanobot

Python-native AI agent. Multi-provider LLM support. Async-first architecture.

## Quick Context
- Runtime: Python 3.12+ with uv/poetry
- Providers: Claude, OpenAI, Gemini (swappable via config)
- Skills: transformations that add real capabilities
- Memory: SQLite + optional Supabase sync

## Key Skills
- `api-tester` — Auto-generates test suites from OpenAPI specs, runs them,- **Skills**:
  - `skills/code-reviewer`: Python-based logic review.
  - `skills/web-searcher`: Brave Search & live analysis.
  - `skills/notion-sync`: Task/Note management in Notion.
- **Workflows**:
  - `workflows/hr-campaign.md`: Autonomous HR outreach pipeline.
 across any codebase
- `data-pipeline` — CSV/JSON/Parquet ETL with Claude-driven transformation logic
- `doc-generator` — Generates full docs from source code (Sphinx/MkDocs output)
- `git-automator` — PR creation, commit messages, changelogs from git history
- Plus: add-telegram, add-gmail, add-slack, add-obsidian, add-supabase

## Active Channels
Configured via add-* skills. Default trigger: `@Nanobot`

## Architecture
- providers/ — LLM provider adapters
- skills/ — skill transformations
- workflows/ — recurring automation definitions
- config/ — provider + channel configuration
