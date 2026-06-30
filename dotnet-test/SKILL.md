---
name: dotnet-test
description: "Skills for running, generating, analyzing, and improving .NET tests: test execution, filtering, platform detection, coverage, testability, and MSTest workflows."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-test
---

# dotnet-test

## Overview

Use this skill for .NET test execution, generation, analysis, filtering, coverage, testability improvements, platform detection, and MSTest workflows using [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Identify test projects, frameworks, target frameworks, adapters, fixtures, data sources, and CI test commands.
2. Run or recommend the narrowest meaningful test command for the change.
3. Improve tests around behavior and contracts rather than implementation detail.
4. Report skipped, flaky, platform-specific, or environment-dependent tests plainly.

## Guardrails

- Do not silently switch test frameworks or runners.
- Preserve existing test naming, fixture setup, traits, categories, and CI filters.
- Avoid broad snapshots when focused assertions can prove behavior.

## Expected Output

Return test changes or analysis with commands, filters, coverage notes, and failure interpretation.
