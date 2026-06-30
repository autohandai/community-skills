---
name: atlas-toolkit-discovery
description: "Inventory COBOL estates and classify modernization go/no-go readiness with ATLAS toolkit discovery."
license: MIT
metadata:
  author: Vivantro
  version: "1.0.0"
  source: https://github.com/Vivantro/atlas-toolkit-discovery
---

# ATLAS Toolkit Discovery

## Overview

Use this skill during the discovery phase of COBOL modernization, before conversion work begins. The upstream repository, [Vivantro/atlas-toolkit-discovery](https://github.com/Vivantro/atlas-toolkit-discovery), is a sample skill for COBOL legacy inventory and go/no-go classification.

Compatibility: COBOL, legacy inventory, and modernization readiness assessment.

## Workflow

1. Collect source inventory: COBOL programs, copybooks, JCL, control cards, data definitions, test assets, and deployment notes.
2. Build a dependency index covering calls, copybook inclusion, file usage, database access, schedules, and external systems.
3. Score readiness by complexity, missing assets, test coverage, business criticality, operational risk, and SME availability.
4. Classify each application or component as go, conditional go, defer, or no-go for modernization.
5. Recommend the next step: deeper reverse engineering, wrapper strategy, data remediation, test-data recovery, or migration execution.

## Guardrails

- Do not start conversion until discovery has identified required copybooks, sample data, and integration dependencies.
- Keep readiness scoring evidence-based and include confidence levels.
- Separate technical complexity from business priority so decision makers can trade risk against value explicitly.
- Preserve unknowns as named risks rather than filling gaps with assumptions.

## Expected Output

Produce an inventory table, dependency summary, readiness classification, risk register, and recommended modernization sequence.
