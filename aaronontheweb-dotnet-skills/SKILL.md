---
name: aaronontheweb-dotnet-skills
description: "Use Aaronontheweb dotnet-skills for Claude Code-oriented .NET maintenance, refactoring, and agent workflows."
license: MIT
metadata:
  author: Aaronontheweb
  version: "1.0.0"
  source: https://github.com/Aaronontheweb/dotnet-skills
---

# Aaronontheweb dotnet-skills

## Overview

Use this skill when a .NET project needs maintenance, refactoring, testing, or agent workflow guidance based on [Aaronontheweb/dotnet-skills](https://github.com/Aaronontheweb/dotnet-skills). The upstream project is organized for Claude Code skills and sub-agents for .NET developers.

Compatibility: .NET, C#, maintenance workflows, refactoring, tests, and Claude Code-style agents.

## Workflow

1. Start from the failing behavior, maintenance goal, or refactoring objective.
2. Inspect project structure and build conventions before applying upstream instructions.
3. Keep changes narrow: update one library, test suite, public API, or maintenance concern at a time.
4. Use tests and analyzers as the primary validation surface.
5. When a maintenance task crosses multiple projects, record affected assemblies and dependency edges.

## Guardrails

- Do not rewrite architecture when the request is a maintenance task.
- Preserve public APIs unless the user explicitly approves breaking changes.
- Keep generated sub-agent instructions separate from production source code.
- Check upstream README and skill folders before relying on repository-specific commands.

## Expected Output

Return a focused .NET maintenance plan or patch with validation commands, affected projects, and any remaining risks.
