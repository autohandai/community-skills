---
name: dotnet-test-migration
description: "Skills and an orchestrator agent for migrating .NET test frameworks and platforms: MSTest and xUnit version upgrades, xUnit-to-MSTest conversion, and VSTest to Microsoft.Testing.Platform."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-test-migration
---

# dotnet-test-migration

## Overview

Use this skill for .NET test migrations, including MSTest upgrades, xUnit upgrades, xUnit-to-MSTest conversions, and VSTest to Microsoft.Testing.Platform migrations using [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Inventory test frameworks, adapters, assertions, fixtures, categories, parallelization, and CI runner behavior.
2. Choose a migration sequence that keeps tests runnable after each slice.
3. Convert framework attributes, assertions, lifecycle hooks, data tests, and runner configuration deliberately.
4. Validate migrated tests with before-and-after command output where possible.

## Guardrails

- Do not mix migration types without explaining the sequencing.
- Preserve test intent, filtering semantics, categories, and CI reporting.
- Call out unsupported framework features or manual follow-up work.

## Expected Output

Return a test-migration plan or implementation with changed contracts, commands, and remaining gaps.
