---
name: dotnet-msbuild
description: "Comprehensive MSBuild and .NET build skills: failure diagnosis, performance optimization, code quality, and modernization."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-msbuild
---

# dotnet-msbuild

## Overview

Use this skill for MSBuild and .NET build work, including build failures, slow builds, SDK-style modernization, analyzers, targets, props, and CI build behavior using [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Inspect `.sln`, `.csproj`, `Directory.Build.*`, `global.json`, package props, targets, and CI definitions.
2. Reproduce the build issue with the smallest command that exercises the failing target.
3. Diagnose property, item, target, SDK, package, and workload interactions with build logs when needed.
4. Validate changes with restore/build/test or the affected CI command.

## Guardrails

- Do not flatten project files or remove targets without proving they are unused.
- Preserve multi-targeting, packaging, analyzers, source generation, and CI behavior.
- Keep performance and modernization changes measurable.

## Expected Output

Return build-focused changes or guidance with the relevant MSBuild evidence and verification.
