---
name: dotnet-data
description: "Skills for .NET data access and Entity Framework related tasks."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-data
---

# dotnet-data

## Overview

Use this skill for .NET data-access work, especially Entity Framework Core modeling, migrations, queries, transactions, and repository data-flow analysis using guidance from [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Identify DbContext types, migrations, provider packages, connection configuration, and data-access boundaries.
2. Preserve schema compatibility, migration history, query semantics, and transaction behavior.
3. Use EF Core tooling and tests where available to verify model and migration changes.
4. Explain data-shape, performance, and compatibility risks explicitly.

## Guardrails

- Do not generate destructive migrations without user approval.
- Avoid changing persisted schema, indexes, or cascade behavior as an incidental side effect.
- Keep provider-specific behavior visible when SQL Server, PostgreSQL, SQLite, Cosmos, or other providers differ.

## Expected Output

Return focused data-access changes or guidance with schema impact, validation commands, and any migration notes.
