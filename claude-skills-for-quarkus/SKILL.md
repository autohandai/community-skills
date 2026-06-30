---
name: claude-skills-for-quarkus
description: "Use Claude skills for Quarkus to build domain-driven Quarkus applications and Java modernization workflows."
license: MIT
metadata:
  author: jeremyrdavis
  version: "1.0.0"
  source: https://github.com/jeremyrdavis/claude-skills-for-quarkus
---

# Claude Skills for Quarkus

## Overview

Use this skill when a Java repository needs Quarkus and domain-driven design guidance from [jeremyrdavis/claude-skills-for-quarkus](https://github.com/jeremyrdavis/claude-skills-for-quarkus). The upstream project focuses on building Quarkus applications with DDD-oriented agent support.

Compatibility: Quarkus, Java, domain-driven design, Maven, REST services, and modernization workflows.

## Workflow

1. Identify the Quarkus version, Java version, extension set, persistence layer, and runtime target.
2. Map the domain model before generating resources, services, repositories, or adapters.
3. Keep Quarkus idioms intact: configuration, CDI, REST endpoints, Panache or repository patterns, and test profiles.
4. For modernization, define the source framework and target Quarkus boundary before conversion.
5. Validate with the repository's Maven or Gradle commands and Quarkus tests.

## Guardrails

- Do not flatten domain boundaries into CRUD-only services unless the project already follows that style.
- Preserve API contracts, database migrations, and configuration property semantics.
- Check the upstream README before reusing Quarkus-specific instructions because supported patterns may change.
- Keep native-image assumptions separate from standard JVM runtime behavior.

## Expected Output

Return a Quarkus-focused plan or implementation with domain boundaries, affected files, validation commands, and migration risks.
