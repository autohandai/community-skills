---
name: claude-code-java
description: "Use claude-code-java for reusable Java project agent infrastructure, conventions, testing, and migration workflows."
license: MIT
metadata:
  author: decebals
  version: "1.0.0"
  source: https://github.com/decebals/claude-code-java
---

# claude-code-java

## Overview

Use this skill when a Java project needs reusable coding-agent infrastructure from [decebals/claude-code-java](https://github.com/decebals/claude-code-java). The upstream project is optimized for Claude Code but its conventions are useful for Java agent workflows generally.

Compatibility: Java, Maven, Gradle, testing, refactoring, migration, and Claude Code-style workflows.

## Workflow

1. Identify the Java version, build tool, framework, module layout, and test stack.
2. Inspect upstream instructions before importing conventions into the local repository.
3. Keep work tool-native: use Maven or Gradle commands already present in the project.
4. For migration tasks, define the source and target versions, dependency changes, and compatibility risks first.
5. Validate compile, tests, formatting, and static analysis according to the local project.

## Guardrails

- Do not mix Maven and Gradle patterns unless the repository already does.
- Preserve package names, public APIs, serialization contracts, and configuration keys.
- Keep framework-specific assumptions explicit, especially for Spring Boot, Quarkus, Jakarta EE, and Micronaut.
- Treat generated agent instructions as project support material, not application runtime code.

## Expected Output

Return Java-focused implementation or migration guidance with build commands, risk notes, and validation evidence.
