---
name: dotnet-upgrade
description: "Skills for migrating and upgrading .NET projects across framework versions, language features, and compatibility targets."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-upgrade
---

# dotnet-upgrade

## Overview

Use this skill for .NET upgrades across target frameworks, SDK versions, C# language features, dependencies, workloads, and compatibility targets using [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Inventory projects, target frameworks, SDK pinning, packages, analyzers, workloads, and CI environments.
2. Choose the smallest upgrade path that preserves runtime compatibility and deployment constraints.
3. Upgrade framework, packages, source, tests, and configuration in verifiable slices.
4. Validate with restore, build, test, and runtime smoke checks where possible.

## Guardrails

- Do not skip intermediate compatibility issues by only changing target framework names.
- Preserve public API, serialization, configuration, and database contracts.
- Document unsupported platforms, removed APIs, and workload requirements.

## Expected Output

Return an upgrade plan or implementation with compatibility notes, commands run, and remaining blockers.
