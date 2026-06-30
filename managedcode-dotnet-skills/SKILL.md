---
name: managedcode-dotnet-skills
description: "Use ManagedCode dotnet-skills for installable .NET agent skills, CLI workflows, and migration-oriented guidance."
license: MIT
metadata:
  author: managedcode
  version: "1.0.0"
  source: https://github.com/managedcode/dotnet-skills
---

# ManagedCode dotnet-skills

## Overview

Use this skill when a .NET project needs an installable skill catalog or CLI-oriented agent workflow from [managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills). The upstream repository targets Codex, Claude Code, GitHub Copilot, and Gemini.

Compatibility: .NET, C#, CLI-based skill installation, migration workflows, and multi-agent coding assistants.

## Workflow

1. Inspect the solution structure, SDK version, package centralization, test framework, and CI before choosing any upstream skill.
2. For migration tasks, classify the migration target first: framework upgrade, library replacement, Azure migration, architecture modernization, or test modernization.
3. Use the upstream catalog as a reference, then adapt instructions to the local repository conventions.
4. Validate with `dotnet restore`, `dotnet build`, and the narrowest relevant `dotnet test` command.
5. Capture migration decisions in a short compatibility note covering breaking changes and remaining manual work.

## Guardrails

- Do not install or execute upstream CLI tooling without checking the README and local project constraints.
- Treat generated migration output as a draft until tests prove behavior parity.
- Preserve nullable context, analyzers, editorconfig rules, and package versioning strategy.
- Keep source and generated migration artifacts separated when experimenting.

## Expected Output

Return a migration or implementation checklist, commands, validation evidence, and any upstream skill or CLI reference used.
