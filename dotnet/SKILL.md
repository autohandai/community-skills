---
name: dotnet
description: "C# language server (LSP) integration for coding agents and high-level .NET development skills."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet
---

# dotnet

## Overview

Use this skill when a .NET repository needs C# language-server grounding, project discovery, or high-level agent guidance from the upstream [dotnet/skills](https://github.com/dotnet/skills) project.

## Workflow

1. Identify the solution, project files, SDK version, target frameworks, workloads, and test projects.
2. Prefer language-server and `dotnet` CLI evidence over guessing symbols, references, or diagnostics.
3. Make changes in small slices, preserving public API, configuration, serialization, and deployment behavior.
4. Validate with the narrowest useful restore, build, test, or analyzer command.

## Guardrails

- Do not assume upstream plugins are installed locally.
- Match the repository's current SDK, target framework, nullable context, analyzers, and formatting.
- Record missing SDKs, workloads, packages, or LSP capabilities explicitly.

## Expected Output

Return .NET-focused code changes or guidance with project evidence, commands run, and validation results.
