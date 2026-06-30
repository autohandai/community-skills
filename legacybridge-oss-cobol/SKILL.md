---
name: legacybridge-oss-cobol
description: "Plan and execute AI-assisted COBOL to Java migrations with LegacyBridge OSS COBOL."
license: MIT
metadata:
  author: ltoscano
  version: "1.0.0"
  source: https://github.com/ltoscano/legacybridge-oss-cobol
---

# LegacyBridge OSS COBOL

## Overview

Use this skill when migrating COBOL applications to Java with an agent-assisted workflow. The upstream project, [ltoscano/legacybridge-oss-cobol](https://github.com/ltoscano/legacybridge-oss-cobol), describes AI-powered COBOL to Java migration using Atomic Agents and Instructor.

Compatibility: COBOL, Java, Python, Atomic Agents, and Instructor.

## Workflow

1. Identify the migration slice: a program, transaction, batch job, or bounded business capability.
2. Gather source COBOL, copybooks, sample inputs, expected outputs, database schemas, and operational documentation.
3. Generate a structured understanding of data definitions, control flow, file operations, database calls, and business rules.
4. Create Java equivalents incrementally, keeping one conversion unit small enough to review and test.
5. Build characterization tests from existing examples before refactoring generated Java into idiomatic application structure.
6. Compare output records, numeric precision, error behavior, and edge cases against the COBOL baseline.

## Guardrails

- Keep generated Java behavior-first until equivalence is proven; postpone architectural cleanup that could obscure semantic drift.
- Flag COBOL features that need manual review, including GO TO-heavy control flow, REDEFINES, OCCURS DEPENDING ON, packed decimals, and environment-specific I/O.
- Treat missing sample data as a blocker for equivalence claims, not as a reason to infer behavior.
- Read the upstream project README before using its tooling because setup and supported migration paths may change.

## Expected Output

Return a migration slice plan, parsed COBOL behavior summary, generated Java review notes, equivalence test checklist, and remaining manual-review items.
