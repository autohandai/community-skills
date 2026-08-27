---
name: atlas-cloud-media
description: Generate image and video media through Atlas Cloud with live model-schema validation.
license: MIT
compatibility: Python 3.10+ with network access
allowed-tools: Bash(python3 *)
metadata:
  author: binyangzhu000-sudo
  version: "1.0.0"
---

# Atlas Cloud Media

## Overview

Use Atlas Cloud as an optional provider for image or video generation. The included
script discovers the requested model in the live catalog, validates inputs against
that model's current OpenAPI schema, submits one generation request, and polls the
prediction with bounded GET requests.

## Setup

Set the API key in the environment. Do not pass it on the command line or write it
to project files.

```bash
export ATLASCLOUD_API_KEY="..."
```

## Discover Models

Always inspect the live catalog before choosing a model. Only use entries with
`display_console` set to `true`.

```bash
curl -fsS https://api.atlascloud.ai/api/v1/models \
  | python3 -c 'import json,sys; print("\n".join(m["model"] for m in json.load(sys.stdin)["data"] if m.get("display_console") and m.get("type") in {"Image", "Video"}))'
```

The catalog entry contains a `schema` URL. Read its
`components.schemas.Input.properties` before constructing `--input-json`; model
parameters and enum values can change.

## Generate Media

Pass only model-specific fields in `--input-json`; the script adds `model` after
validation. The model below is a placeholder and must be replaced with an exact ID
from the current catalog.

```bash
python3 {baseDir}/scripts/generate.py \
  --type image \
  --model '<live-image-model-id>' \
  --input-json '{"prompt":"a quiet mountain lake at sunrise"}'
```

For larger payloads, use a JSON file:

```bash
python3 {baseDir}/scripts/generate.py \
  --type video \
  --model '<live-video-model-id>' \
  --input-file request.json \
  --timeout 300
```

On success, the script prints each generated asset as `MEDIA_URL: <url>`.

## Operational Rules

1. Fetch the live model catalog and schema for every run.
2. Submit the billable POST exactly once; never retry it automatically.
3. Retry only prediction GET requests, within the configured timeout.
4. Treat `failed` or `canceled` predictions as terminal errors.
5. Keep Atlas Cloud optional when integrating it into an existing application.
6. Never log API keys or include them in commits, examples, or generated files.

## Troubleshooting

- `model is not available`: refresh the catalog and select a visible model of the requested type.
- `unsupported input fields`: compare the payload with the live schema URL reported for the model.
- `prediction timed out`: keep the prediction ID and check it later; do not submit the POST again.
- HTTP `401` or `403`: verify `ATLASCLOUD_API_KEY` and account access before another generation.
