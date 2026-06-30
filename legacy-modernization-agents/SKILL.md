---
name: legacy-modernization-agents
description: "Modernize COBOL systems to Java Quarkus or .NET with Microsoft Legacy Modernization Agents workflows."
license: MIT
metadata:
  author: Microsoft
  version: "1.0.0"
  source: https://github.com/Azure-Samples/Legacy-Modernization-Agents
---

# Legacy Modernization Agents

## Overview

Use this skill for AI-assisted modernization of COBOL and mainframe workloads into Java Quarkus, C#, or .NET services. The upstream sample, [Azure-Samples/Legacy-Modernization-Agents](https://github.com/Azure-Samples/Legacy-Modernization-Agents), provides modernization agents for analysis, conversion, and dependency mapping.

Compatibility: COBOL, Java, Quarkus, C#, .NET, and Microsoft Agent Framework.

## Workflow

1. Start with assessment: collect COBOL programs, copybooks, JCL, data files, transaction definitions, and current operational constraints.
2. Classify each component as preserve, wrap, refactor, rewrite, or retire before generating target code.
3. Map COBOL data definitions to target language types, preserving precision, signed numeric behavior, file layout offsets, and validation rules.
4. Convert business logic in small slices with tests that compare source behavior against generated Java or C# behavior.
5. Build integration adapters for files, batch schedules, databases, queues, and service boundaries after the core behavior is verified.
6. Record every generated artifact, manual decision, unresolved assumption, and test gap in the migration report.

## Guardrails

- Do not run destructive migrations against source repositories; write converted output to a separate target directory.
- Require executable characterization tests or reviewed examples before claiming functional equivalence.
- Preserve batch ordering, restart points, date handling, rounding behavior, and exception handling.
- Use the upstream repository as a sample implementation and check its README, prerequisites, and license state before reusing code directly.

## Expected Output

Produce a migration assessment, target architecture notes, converted code plan, test strategy, and a traceability matrix from COBOL assets to generated Java or C# artifacts.
