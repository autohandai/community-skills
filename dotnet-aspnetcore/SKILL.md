---
name: dotnet-aspnetcore
description: "ASP.NET Core web development skills including middleware, endpoints, real-time communication, and API patterns."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-aspnetcore
---

# dotnet-aspnetcore

## Overview

Use this skill for ASP.NET Core web development, including middleware, minimal APIs, controllers, endpoint routing, SignalR, authentication, configuration, and API design using [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Inspect app startup, dependency injection, middleware order, endpoints, auth, configuration, and hosting model.
2. Preserve request/response contracts, route names, status codes, serialization, auth policies, and observability.
3. Add or update tests around endpoint behavior where the repository supports them.
4. Validate with build, tests, or a local smoke command when feasible.

## Guardrails

- Do not reorder middleware casually.
- Avoid changing public API contracts or auth behavior as an incidental side effect.
- Keep environment-specific configuration and secrets handling intact.

## Expected Output

Return ASP.NET Core changes or guidance with route, middleware, and validation notes.
