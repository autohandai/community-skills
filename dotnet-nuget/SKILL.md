---
name: dotnet-nuget
description: "NuGet and .NET package management: dependency management and modernization."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-nuget
---

# dotnet-nuget

## Overview

Use this skill for NuGet package management, dependency upgrades, central package management, restore failures, lock files, feeds, and package modernization with guidance from [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Inspect package references, `Directory.Packages.props`, lock files, NuGet config, feeds, and CI restore commands.
2. Identify direct and transitive dependencies before changing versions.
3. Preserve compatibility ranges, target frameworks, package source mapping, and private-feed configuration.
4. Validate with restore, build, tests, and package vulnerability checks where available.

## Guardrails

- Do not update unrelated packages in the same change.
- Avoid leaking private feed URLs, credentials, or tokens in output.
- Call out breaking changes and package downgrade or conflict risks.

## Expected Output

Return package changes or guidance with dependency rationale and validation results.
