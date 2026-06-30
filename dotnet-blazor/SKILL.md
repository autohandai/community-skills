---
name: dotnet-blazor
description: "Skills for Blazor development: component authoring, interactivity, and web application patterns."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-blazor
---

# dotnet-blazor

## Overview

Use this skill for Blazor development, including Razor components, render modes, interactivity, forms, routing, state, JavaScript interop, and web application patterns using [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Identify hosting model, render mode, component structure, routing, state management, and shared UI conventions.
2. Keep component changes scoped and preserve parameters, cascading values, event callbacks, and validation behavior.
3. Test interactions with bUnit, app tests, or browser checks where available.
4. Validate accessibility, responsiveness, and server/client boundary assumptions.

## Guardrails

- Do not mix Blazor Server, WebAssembly, and interactive render-mode assumptions.
- Preserve form binding, validation messages, authorization views, and route behavior.
- Keep JavaScript interop contracts explicit and minimal.

## Expected Output

Return Blazor changes or guidance with component contracts and validation results.
