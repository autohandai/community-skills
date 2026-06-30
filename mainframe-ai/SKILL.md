---
name: mainframe-ai
description: "Use AI assistance for IBM z/OS and mainframe modernization tasks from the mainframe-ai project."
license: MIT
metadata:
  author: W00t3k
  version: "1.0.0"
  source: https://github.com/W00t3k/mainframe-ai
---

# mainframe-ai

## Overview

Use this skill when a task involves AI-assisted IBM z/OS or mainframe analysis, operations support, or modernization planning. The upstream project, [W00t3k/mainframe-ai](https://github.com/W00t3k/mainframe-ai), is oriented around mainframe assistant workflows.

Compatibility: IBM z/OS, COBOL, JCL, and mainframe operations.

## Workflow

1. Establish the operating context: z/OS subsystem, batch job, dataset, CICS transaction, Db2 object, VSAM file, or COBOL program.
2. Gather read-only evidence first, including JCL, PROC definitions, SYSOUT snippets, job history, abend codes, copybooks, and runbooks.
3. Translate mainframe artifacts into explicit operational facts: job purpose, inputs, outputs, schedules, dependencies, and failure modes.
4. For modernization tasks, map each artifact to a target disposition: retain, document, wrap, automate, convert, or retire.
5. Produce operator-safe next steps with commands or code clearly separated from analysis.

## Guardrails

- Treat production mainframe actions as high risk. Prefer read-only inspection and require human approval before suggesting state-changing commands.
- Preserve dataset naming, generation data group behavior, job restart semantics, and security controls.
- Do not infer abend root cause from a code alone; correlate with JCL, logs, program changes, and data conditions.
- Check the upstream repository before relying on any command examples or assistant integration details.

## Expected Output

Return an evidence-backed mainframe analysis with affected artifacts, operational interpretation, modernization options, risks, and next actions.
