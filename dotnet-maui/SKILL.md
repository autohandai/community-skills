---
name: dotnet-maui
description: "Skills for .NET MAUI development: environment setup, diagnostics, and troubleshooting."
license: MIT
metadata:
  author: dotnet
  version: "1.0.0"
  source: https://github.com/dotnet/skills/tree/main/plugins/dotnet-maui
---

# dotnet-maui

## Overview

Use this skill for .NET MAUI development, mobile and desktop workload setup, build diagnostics, simulator or device troubleshooting, and cross-platform UI issues using [dotnet/skills](https://github.com/dotnet/skills).

## Workflow

1. Inspect target platforms, workloads, SDK version, platform manifests, resources, and CI build setup.
2. Reproduce issues on the relevant platform target before changing shared code.
3. Keep platform-specific changes isolated and document workload or tooling prerequisites.
4. Validate with the narrowest applicable `dotnet build`, deploy, or test command.

## Guardrails

- Do not assume iOS, Android, macOS, or Windows workloads are installed.
- Preserve platform permissions, entitlements, manifests, and resource naming.
- Call out simulator, device, signing, and workload blockers clearly.

## Expected Output

Return MAUI-focused changes or troubleshooting steps with platform evidence and validation.
