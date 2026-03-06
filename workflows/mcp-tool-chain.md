# MCP Tool Chain — Nanobot

Configure and chain Model Context Protocol (MCP) tools so Nanobot can call external services, databases, and APIs natively.

## What is MCP?

MCP (Model Context Protocol) is the standard Anthropic defined for connecting LLMs to external tools. Nanobot exposes its skills as MCP tools, and can also consume external MCP servers.

## Trigger
- **Setup**: `@Nanobot mcp-tool-chain add <server-name>`
- **List**: `@Nanobot mcp-tool-chain list`
- **Run**: Tools are called automatically when Claude decides they're relevant

## Adding an MCP Server

### From a remote server
```
@Nanobot mcp-tool-chain add github --url https://mcp.github.com --auth $GITHUB_TOKEN
```

### From a local process
```
@Nanobot mcp-tool-chain add filesystem --command "python -m mcp_filesystem /workspace"
```

### From an npm package
```
@Nanobot mcp-tool-chain add memory --npm @modelcontextprotocol/server-memory
```

## Built-in MCP Tools (from Nanobot skills)

| Tool name | Provided by | What it does |
|-----------|-------------|-------------|
| `vault_search` | add-obsidian | Search Obsidian vault |
| `memory_read` | add-supabase | Read agent memory |
| `memory_write` | add-supabase | Write agent memory |
| `code_review` | code-reviewer | Review a code snippet |
| `run_tests` | api-tester | Run test suite |

## Chaining Tools

Nanobot chains tools automatically. Example:

```
You: @Nanobot find the note about our API rate limits and check if our current code respects them

Nanobot:
  1. vault_search("API rate limits") → found "API Notes.md"
  2. Reads rate limit specs from note
  3. Reads current code (via filesystem MCP tool)
  4. Compares → reports any violations
```

## Configuration File

```json
// config/mcp-servers.json
{
  "servers": [
    {
      "name": "filesystem",
      "command": "npx @modelcontextprotocol/server-filesystem /workspace",
      "env": {}
    },
    {
      "name": "github",
      "command": "npx @modelcontextprotocol/server-github",
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    }
  ]
}
```
