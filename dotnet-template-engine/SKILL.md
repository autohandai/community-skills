---
name: dotnet-template-engine
description: ".NET Template Engine skills: template discovery, project scaffolding, and template authoring."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-template-engine
---

# dotnet-template-engine

## Overview

Use this skill for .NET Template Engine work, including template discovery, `dotnet new` scaffolding, template authoring, symbols, constraints, and template package validation using [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Inspect existing templates, `.template.config`, symbols, sources, constraints, and packaging metadata.
2. Scaffold or modify templates in a way that matches repository conventions.
3. Validate generated output, not only the template source.
4. Document installation, invocation, and parameter behavior.

## Guardrails

- Do not break existing template short names, identities, or package IDs without a migration note.
- Avoid embedding local absolute paths or secrets in generated output.
- Keep generated projects buildable with the advertised SDK and workloads.

## Expected Output

Return template changes or guidance with sample invocation and generated-output validation.
