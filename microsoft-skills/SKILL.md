---
name: microsoft-skills
description: "Use microsoft/skills for Azure SDK grounding across .NET and Java agent coding workflows."
license: MIT
metadata:
  author: microsoft
  version: "1.0.0"
  source: https://github.com/microsoft/skills
---

# Microsoft Skills

## Overview

Use this skill when work needs Microsoft SDK grounding for coding agents, especially Azure SDK tasks across .NET and Java. The upstream [microsoft/skills](https://github.com/microsoft/skills) repository includes skills, MCP servers, custom agents, and agent instructions for SDK-focused development.

Compatibility: Azure SDK, .NET, Java, MCP servers, custom agents, and agent instruction files.

## Workflow

1. Identify the SDK family, target language, package versions, authentication model, and Azure service.
2. Read the relevant upstream skill or agent instructions before applying service-specific patterns.
3. Prefer official SDK APIs and examples over hand-rolled REST calls unless the SDK lacks coverage.
4. Validate with language-native tooling: `dotnet build/test` for .NET and Maven or Gradle tests for Java.
5. Document service prerequisites, identity permissions, and environment variables separately from source changes.

## Guardrails

- Do not assume Azure credentials, subscriptions, or cloud resources are available locally.
- Keep secret values out of code, generated docs, and command output.
- Match the repository's existing SDK major versions and dependency management approach.
- For migrations, preserve client behavior and retry/error handling semantics.

## Expected Output

Return SDK-grounded implementation guidance with package choices, authentication assumptions, validation commands, and source references.
