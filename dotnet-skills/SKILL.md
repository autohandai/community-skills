---
name: dotnet-skills
description: "Use dotnet/skills for .NET and C# coding-agent guidance, plugins, project analysis, and modernization workflows."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills
---

# dotnet/skills

## Overview

Use this skill when a .NET or C# repository needs coding-agent guidance from the upstream [dotnet/skills](https://github.com/dotnet/skills) project. The upstream repository provides skills and plugins intended to ground agents in .NET development conventions.

Compatibility: .NET, C#, coding-agent plugins, Codex, Claude Code, and GitHub Copilot-style workflows.

## Workflow

1. Identify the .NET project shape: solution files, SDK version, target frameworks, test projects, analyzers, and package management.
2. Read upstream instructions before reusing a plugin or skill because install paths and supported agents may change.
3. Use repository-local evidence first: `global.json`, `.sln`, `.csproj`, `Directory.Build.*`, `Directory.Packages.props`, tests, and CI.
4. Apply .NET guidance incrementally: restore, build, test, inspect warnings, then change code in small slices.
5. For modernization, preserve public contracts, serialization formats, configuration names, and deployment assumptions.

## Guardrails

- Do not assume all upstream plugins are installed in the current workspace.
- Keep generated code aligned with the target framework already used by the repository.
- Prefer built-in .NET tooling (`dotnet restore`, `dotnet build`, `dotnet test`, analyzers) for validation.
- Record unresolved SDK, workload, or package compatibility issues explicitly.

## Expected Output

Return a .NET-focused implementation or modernization plan with project evidence, commands run, compatibility notes, and validation results.
