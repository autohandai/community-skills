---
name: spring-boot-skills
description: "Use spring-boot-skills for production-grade Spring Boot agent guidance, modernization, testing, and operations."
license: MIT
metadata:
  author: rrezartprebreza
  version: "1.0.0"
  source: https://github.com/rrezartprebreza/spring-boot-skills
---

# Spring Boot Skills

## Overview

Use this skill when a Spring Boot repository needs production-grade coding-agent guidance from [rrezartprebreza/spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills). The upstream repository provides Claude Code skills for Spring Boot developers.

Compatibility: Spring Boot, Java, Maven, Gradle, testing, migration, and production operations.

## Workflow

1. Identify the Spring Boot version, Java version, dependency management style, profiles, and test strategy.
2. Check upstream skill instructions for the relevant concern: controllers, services, data access, security, testing, migration, or observability.
3. Keep changes aligned with existing architecture: layered services, hexagonal boundaries, or domain modules.
4. For migrations, plan dependency and configuration changes before touching application logic.
5. Validate with repository-native Maven or Gradle commands and targeted integration tests where available.

## Guardrails

- Do not introduce new frameworks or starters without a concrete need.
- Preserve configuration property names, profile behavior, database migrations, and API contracts.
- Treat generated code that affects transactions, security, or data access as high review priority.
- Make actuator, logging, and observability changes explicit.

## Expected Output

Return a Spring Boot implementation or migration plan with affected modules, commands, tests, and operational notes.
