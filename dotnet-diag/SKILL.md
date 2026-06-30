---
name: dotnet-diag
description: "Skills for .NET performance investigations, debugging, and incident analysis."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-diag
---

# dotnet-diag

## Overview

Use this skill for .NET diagnostics, performance investigations, runtime debugging, memory analysis, tracing, and incident response workflows from [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Capture the symptom, runtime version, hosting model, traffic pattern, and recent changes.
2. Prefer concrete evidence: logs, traces, dumps, metrics, profiler output, and reproducible commands.
3. Separate observation, hypothesis, experiment, and conclusion.
4. Recommend the smallest corrective change and the validation signal that proves it.

## Guardrails

- Do not claim root cause without evidence.
- Avoid introducing diagnostics that leak secrets or user data.
- Treat production incident commands as high impact and call out safety considerations.

## Expected Output

Return an evidence-led diagnosis, remediation path, and verification plan for the .NET issue.
