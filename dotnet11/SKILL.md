---
name: dotnet11
description: "Skills for new .NET 11 APIs and language features."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet11
---

# dotnet11

## Overview

Use this skill when adopting or evaluating new .NET 11 APIs, SDK behavior, runtime changes, and C# language features from [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Confirm the repository can target .NET 11 through SDK, CI, hosting, package, and runtime availability.
2. Identify the exact .NET 11 API or language feature and the compatibility fallback if needed.
3. Keep adoption incremental and avoid broad target-framework changes without a migration plan.
4. Validate with restore, build, tests, and runtime checks under the intended SDK.

## Guardrails

- Do not use .NET 11-only APIs in projects that must run on earlier target frameworks.
- Call out preview, SDK, workload, or hosting requirements explicitly.
- Preserve public API and deployment compatibility unless the upgrade contract says otherwise.

## Expected Output

Return .NET 11 guidance or implementation with compatibility notes and validation.
