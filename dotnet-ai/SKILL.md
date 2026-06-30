---
name: dotnet-ai
description: "AI and ML skills for .NET: technology selection, LLM integration, agentic workflows, RAG pipelines, MCP, and classic ML with ML.NET."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-ai
---

# dotnet-ai

## Overview

Use this skill for AI and ML work in .NET, including LLM integration, agentic workflows, RAG pipelines, MCP servers or clients, embeddings, and ML.NET systems using [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Clarify the AI task, data flow, model/provider, latency, privacy, and evaluation constraints.
2. Choose .NET libraries and architecture that fit the repository's hosting model and deployment target.
3. Keep prompt, retrieval, tool, and model contracts explicit and testable.
4. Validate with unit tests, integration tests, evals, or deterministic smoke checks where possible.

## Guardrails

- Do not hard-code secrets, model credentials, or provider-specific assumptions.
- Keep user data, embeddings, logs, and prompts privacy-aware.
- Prefer measurable quality and latency criteria over vague AI behavior claims.

## Expected Output

Return a .NET AI implementation or plan with architecture, provider assumptions, and verification.
