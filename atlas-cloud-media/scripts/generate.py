#!/usr/bin/env python3
"""Submit one Atlas Cloud media job and poll its prediction with GET requests."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_BASE = "https://api.atlascloud.ai/api/v1"
CATALOG_URL = f"{API_BASE}/models"
ENDPOINTS = {
    "image": f"{API_BASE}/model/generateImage",
    "video": f"{API_BASE}/model/generateVideo",
}
TERMINAL_SUCCESS = {"completed", "succeeded"}
TERMINAL_FAILURE = {"failed", "canceled", "cancelled"}


def request_json(
    url: str,
    *,
    api_key: str | None = None,
    payload: dict[str, Any] | None = None,
    timeout: float = 30,
) -> dict[str, Any]:
    headers = {
        "Accept": "application/json",
        "User-Agent": "atlas-cloud-media-skill/1.0",
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    data = None
    method = "GET"
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
        method = "POST"

    request = Request(url, data=data, headers=headers, method=method)
    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:800]
        raise RuntimeError(f"HTTP {error.code} from {url}: {detail}") from error
    except URLError as error:
        raise RuntimeError(f"Network error from {url}: {error.reason}") from error
    except json.JSONDecodeError as error:
        raise RuntimeError(f"Invalid JSON from {url}: {error}") from error


def unwrap_data(response: dict[str, Any]) -> Any:
    code = response.get("code")
    if code is not None and str(code) != "200":
        raise RuntimeError(str(response.get("message") or f"Atlas Cloud API error {code}"))
    return response.get("data", response)


def find_model(catalog: dict[str, Any], model_id: str, media_type: str) -> dict[str, Any]:
    models = unwrap_data(catalog)
    if not isinstance(models, list):
        raise RuntimeError("Atlas Cloud catalog returned an unexpected shape")

    expected_type = media_type.casefold()
    for model in models:
        if not isinstance(model, dict) or model.get("model") != model_id:
            continue
        if not model.get("display_console"):
            raise RuntimeError(f"Model {model_id} is not available in the console")
        if str(model.get("type", "")).casefold() != expected_type:
            raise RuntimeError(f"Model {model_id} is not a {media_type} model")
        return model
    raise RuntimeError(f"Model {model_id} is not available in the live catalog")


def input_schema(model: dict[str, Any]) -> dict[str, Any]:
    schema_url = model.get("schema")
    if not isinstance(schema_url, str) or not schema_url.startswith("https://"):
        raise RuntimeError("Model catalog entry does not provide an HTTPS schema URL")
    schema = request_json(schema_url)
    try:
        value = schema["components"]["schemas"]["Input"]
    except (KeyError, TypeError) as error:
        raise RuntimeError(f"Model schema at {schema_url} has no Input definition") from error
    if not isinstance(value, dict):
        raise RuntimeError(f"Model schema at {schema_url} has an invalid Input definition")
    return value


def validate_payload(payload: dict[str, Any], schema: dict[str, Any], model_id: str) -> dict[str, Any]:
    properties = schema.get("properties") or {}
    if not isinstance(properties, dict):
        raise RuntimeError("Model Input schema has invalid properties")

    unknown = sorted(set(payload) - set(properties))
    if unknown:
        raise RuntimeError(f"Unsupported input fields: {', '.join(unknown)}")

    required = set(schema.get("required") or []) - {"model"}
    missing = sorted(field for field in required if field not in payload)
    if missing:
        raise RuntimeError(f"Missing required input fields: {', '.join(missing)}")

    request_payload = dict(payload)
    request_payload["model"] = model_id
    return request_payload


def prediction_data(response: dict[str, Any]) -> dict[str, Any]:
    data = unwrap_data(response)
    if not isinstance(data, dict):
        raise RuntimeError("Atlas Cloud prediction returned an unexpected shape")
    return data


def parse_input(args: argparse.Namespace) -> dict[str, Any]:
    raw = Path(args.input_file).read_text("utf-8") if args.input_file else args.input_json
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise RuntimeError("Generation input must be a JSON object")
    if "model" in value:
        raise RuntimeError("Do not include model in the input JSON; use --model")
    return value


def poll_prediction(api_key: str, prediction_id: str, timeout: float, interval: float) -> list[str]:
    deadline = time.monotonic() + timeout
    url = f"{API_BASE}/model/prediction/{prediction_id}"
    while time.monotonic() < deadline:
        response = request_json(url, api_key=api_key, timeout=min(30, max(1, timeout)))
        data = prediction_data(response)
        status = str(data.get("status", "")).casefold()
        if status in TERMINAL_SUCCESS:
            outputs = data.get("outputs") or []
            if not isinstance(outputs, list) or not all(isinstance(url, str) for url in outputs):
                raise RuntimeError("Completed prediction has invalid outputs")
            return outputs
        if status in TERMINAL_FAILURE:
            detail = data.get("error") or data.get("message") or "no failure detail"
            raise RuntimeError(f"Prediction {prediction_id} {status}: {detail}")
        time.sleep(interval)
    raise RuntimeError(
        f"Prediction {prediction_id} timed out; query it later instead of submitting again"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--type", choices=sorted(ENDPOINTS), required=True)
    parser.add_argument("--model", required=True, help="Exact model ID from the live catalog")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--input-json", help="Model-specific JSON object")
    input_group.add_argument("--input-file", help="Path to a model-specific JSON object")
    parser.add_argument("--timeout", type=float, default=180, help="Polling timeout in seconds")
    parser.add_argument("--poll-interval", type=float, default=3, help="Seconds between GET polls")
    args = parser.parse_args()

    if args.timeout <= 0 or args.poll_interval <= 0:
        parser.error("--timeout and --poll-interval must be positive")

    api_key = os.environ.get("ATLASCLOUD_API_KEY", "").strip()
    if not api_key:
        parser.error("ATLASCLOUD_API_KEY is required")

    payload = parse_input(args)
    model = find_model(request_json(CATALOG_URL), args.model, args.type)
    request_payload = validate_payload(payload, input_schema(model), args.model)

    # The generation POST is intentionally sent exactly once.
    submitted = prediction_data(
        request_json(ENDPOINTS[args.type], api_key=api_key, payload=request_payload, timeout=60)
    )
    prediction_id = submitted.get("id")
    if not isinstance(prediction_id, str) or not prediction_id:
        raise RuntimeError("Atlas Cloud did not return a prediction ID")
    print(f"PREDICTION_ID: {prediction_id}")

    status = str(submitted.get("status", "")).casefold()
    if status in TERMINAL_SUCCESS:
        outputs = submitted.get("outputs") or []
    elif status in TERMINAL_FAILURE:
        raise RuntimeError(f"Prediction {prediction_id} {status}")
    else:
        outputs = poll_prediction(api_key, prediction_id, args.timeout, args.poll_interval)

    if not outputs:
        raise RuntimeError(f"Prediction {prediction_id} completed without outputs")
    for output in outputs:
        print(f"MEDIA_URL: {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, json.JSONDecodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
