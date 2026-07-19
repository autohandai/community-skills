---
name: xquik-x-data
description: X/Twitter data extraction, monitoring, REST API, MCP, and webhooks with Xquik
license: MIT
compatibility: REST API, MCP-compatible clients, Node.js 18+
allowed-tools: read_file write_file apply_patch run_command
---

# Xquik X Data

## Overview

Xquik provides X/Twitter data workflows for agents and apps through REST API endpoints, an MCP server, webhooks, SDKs, and an installable skill package. Use this skill when a project needs source-backed X/Twitter search, profile lookup, follower exports, account monitoring, media downloads, or structured extraction workflows.

Source links:

- Repository: https://github.com/Xquik-dev/x-twitter-scraper
- API docs: https://docs.xquik.com/api-reference/overview
- MCP docs: https://docs.xquik.com/mcp/overview
- OpenAPI schema: https://xquik.com/openapi.json

## When To Use

- Build X/Twitter data extraction into an agent, workflow, or internal tool.
- Query public X/Twitter data through Xquik's REST API or MCP server.
- Export followers, media, search results, profiles, or engagement metrics.
- Monitor accounts or keywords and deliver updates through webhooks.

## Integration Patterns

### REST API

Use the public API docs and OpenAPI schema to choose the smallest endpoint that returns the data you need. Keep credentials in environment variables, never in source files.

```bash
curl -fsSL https://xquik.com/openapi.json > xquik-openapi.json
```

### MCP Server

Use the MCP docs when the agent runtime supports remote MCP configuration. Prefer the documented OAuth and protected-resource metadata over hand-written assumptions.

### Webhooks

For monitors, register webhook delivery only for the events your workflow consumes. Verify signatures before processing inbound events.

## Best Practices

1. Keep API keys in a secret manager or local environment variable.
2. Request only the fields and result sizes needed for the workflow.
3. Normalize IDs, timestamps, and pagination tokens before storing results.
4. Handle rate limits and transient failures with bounded retries.
5. Link back to public docs instead of copying endpoint details into long-lived prompts.

Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.
