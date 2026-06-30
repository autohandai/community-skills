---
name: cobol-o-matic
description: "Reverse-engineer COBOL systems into structured requirements, business rules, and dependency maps with cobol-o-matic."
license: MIT
metadata:
  author: dsheard
  version: "1.0.0"
  source: https://github.com/dsheard/cobol-o-matic
---

# cobol-o-matic

## Overview

Use this skill when a legacy COBOL codebase needs to be understood before a rewrite, migration, or documentation effort. The upstream project, [dsheard/cobol-o-matic](https://github.com/dsheard/cobol-o-matic), focuses on reverse-engineering COBOL applications into requirements, business rules, and dependency graphs using agentic analysis.

Compatibility: COBOL, Claude Agent SDK, and legacy modernization assessments.

## Workflow

1. Inventory the COBOL entry points, copybooks, JCL, file layouts, screens, batch jobs, and external integrations.
2. Run a read-only analysis first. Treat generated requirements and rules as hypotheses until they are reconciled against source code and production SMEs.
3. Extract business logic by program, paragraph, data structure, condition, file operation, and job step.
4. Build dependency maps that separate call relationships, data dependencies, batch sequencing, and external system touchpoints.
5. Produce migration-ready artifacts: glossary, business-rule catalog, interface inventory, data lineage notes, and test scenarios.

## Guardrails

- Preserve original COBOL semantics, especially packed decimal fields, implied decimals, EBCDIC assumptions, record layouts, and batch restart behavior.
- Do not treat AI-generated requirements as authoritative without source-line evidence.
- Keep modernization recommendations separate from reverse-engineering findings so stakeholders can review factual discovery independently from proposed changes.
- Link every extracted business rule back to source files, paragraphs, or data definitions.

## Expected Output

Return a concise modernization discovery pack with the source inventory, extracted rules, dependency graph summary, open questions, and recommended next analysis steps.
