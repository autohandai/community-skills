---
name: mainframe
description: "Use the Mainframe AI-native Bash runtime and bundled skills for legacy system analysis automation."
license: MIT
metadata:
  author: gtwatts
  version: "1.0.0"
  source: https://github.com/gtwatts/mainframe
---

# Mainframe

## Overview

Use this skill when mainframe or legacy-system work needs shell automation, structured command output, or reusable AI-agent tooling. The upstream repository, [gtwatts/mainframe](https://github.com/gtwatts/mainframe), describes an AI-native Bash runtime with pure Bash functions, LSP and MCP support, safe execution patterns, and bundled skills.

Compatibility: Bash, LSP, MCP, and mainframe or legacy automation workflows.

## Workflow

1. Identify the automation target: source inventory, log parsing, dependency extraction, command orchestration, or migration support.
2. Prefer read-only commands while discovering system state, datasets, source files, job logs, and generated artifacts.
3. Use structured output formats for agent consumption, especially JSON, delimited tables, and deterministic file paths.
4. Wrap fragile shell operations with explicit checks, dry-run modes, idempotency guards, and clear error reporting.
5. For migration work, use automation to collect evidence and prepare repeatable steps rather than silently transforming source systems.

## Guardrails

- Review upstream scripts before execution and adapt paths, credentials, and environment assumptions to the local system.
- Avoid shell pipelines that can partially mutate state without reporting failure.
- Keep generated automation small, inspectable, and reversible.
- Do not expose secrets, hostnames, dataset names, or access tokens in reports unless the user explicitly asks for sensitive operational detail.

## Expected Output

Return runnable automation steps, structured outputs, validation checks, and a concise explanation of how the automation supports the migration or mainframe task.
