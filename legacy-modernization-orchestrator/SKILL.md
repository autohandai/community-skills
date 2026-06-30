---
name: legacy-modernization-orchestrator
description: "Orchestrate multi-agent legacy modernization assessment, planning, and code-conversion workflows."
license: MIT
metadata:
  author: atesibrahim
  version: "1.0.0"
  source: https://github.com/atesibrahim/legacy-modernization-orchestrator
---

# Legacy Modernization Orchestrator

## Overview

Use this skill to coordinate a multi-step modernization effort across discovery, assessment, conversion, testing, and handoff. The upstream project, [atesibrahim/legacy-modernization-orchestrator](https://github.com/atesibrahim/legacy-modernization-orchestrator), provides a general legacy modernization orchestration reference for agent-assisted work.

Compatibility: COBOL, legacy modernization, Codex, Claude, and Copilot.

## Workflow

1. Define the modernization objective, target platform, scope boundaries, success criteria, and non-goals.
2. Build the asset inventory and classify each component by business function, technical complexity, dependency risk, and testability.
3. Assign workstreams for discovery, rule extraction, code conversion, data migration, interface mapping, test generation, and documentation.
4. Run conversion in bounded slices with a traceability record from source artifact to target artifact.
5. Gate each slice on evidence: reviewed generated code, parity tests, stakeholder signoff, and unresolved-risk tracking.
6. Produce an executive status summary and an engineer-facing handoff after each milestone.

## Guardrails

- Do not let orchestration hide uncertainty. Each agent or workstream should report assumptions, evidence, and confidence separately.
- Keep legacy behavior preservation as the default unless stakeholders explicitly approve behavior changes.
- Require rollback or coexistence planning for phased migration.
- Read the upstream README and agent instructions before reusing orchestration prompts, scripts, or templates.

## Expected Output

Return a modernization plan with workstreams, dependency map, migration backlog, acceptance gates, risk register, and current status.
