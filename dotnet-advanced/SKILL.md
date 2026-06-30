---
name: dotnet-advanced
description: "Collection of .NET skills for handling specific .NET tasks for special scenarios."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-advanced
---

# dotnet-advanced

## Overview

Use this skill for specialized .NET work that falls outside ordinary code edits, including uncommon runtime behavior, advanced project layouts, or scenario-specific agent workflows from [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Define the special scenario and the affected projects, packages, runtime targets, and deployment path.
2. Inspect repository-local conventions before applying advanced .NET guidance.
3. Keep changes scoped to the scenario and avoid broad modernization unless required.
4. Validate with targeted commands and document residual risk.

## Guardrails

- Do not replace established project architecture for a narrow special case.
- Preserve compatibility contracts and runtime assumptions.
- Call out when an advanced path depends on SDK, workload, hosting, or platform features not present locally.

## Expected Output

Return a scenario-specific .NET implementation or plan with evidence, tradeoffs, and validation.
