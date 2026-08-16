#!/usr/bin/env python3
"""Fetch a minimal OpenWeather One Call API 4.0 historical weather window.

The API key is read only from OPENWEATHERMAP_API_KEY. Coordinates are rounded
before the request and the output intentionally omits the requested location.
"""

# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from email.message import Message
from typing import Any, Dict, List, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ENDPOINT = "https://api.openweathermap.org/data/4.0/onecall/timeline/1h"
MAX_WINDOW_MINUTES = 24 * 60
MAX_RESPONSE_BYTES = 2_000_000


def parse_timestamp(value: str) -> datetime:
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError("start must be ISO 8601, for example 2026-08-16T01:00:00Z") from exc
    if parsed.tzinfo is None:
        raise ValueError("start must include a timezone")
    return parsed.astimezone(timezone.utc)


def round_coordinate(value: str, minimum: float, maximum: float) -> float:
    try:
        coordinate = float(value)
    except ValueError as exc:
        raise ValueError("coordinates must be numeric") from exc
    if not minimum <= coordinate <= maximum:
        raise ValueError("coordinate is outside its valid range")
    rounded = round(coordinate, 1)
    return 0.0 if rounded == 0 else rounded


def build_url(latitude: float, longitude: float, start: datetime, api_key: str) -> str:
    query = urlencode(
        {
            "lat": f"{latitude:.1f}",
            "lon": f"{longitude:.1f}",
            "start": str(int(start.timestamp())),
            "units": "metric",
            "appid": api_key,
        }
    )
    return f"{ENDPOINT}?{query}"


def content_length(headers: Message) -> Optional[int]:
    raw_length = headers.get("Content-Length")
    if raw_length is None:
        return None
    try:
        return int(raw_length)
    except ValueError:
        return None


def fetch_json(url: str) -> Dict[str, Any]:
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "coros-workout-review/openweather4",
        },
    )
    try:
        with urlopen(request, timeout=20) as response:
            length = content_length(response.headers)
            if length is not None and length > MAX_RESPONSE_BYTES:
                raise RuntimeError("OpenWeatherMap response is too large")
            payload = response.read(MAX_RESPONSE_BYTES + 1)
    except HTTPError as exc:
        raise RuntimeError(f"OpenWeatherMap HTTP {exc.code}") from None
    except URLError:
        raise RuntimeError("OpenWeatherMap network error") from None
    except TimeoutError:
        raise RuntimeError("OpenWeatherMap request timed out") from None

    if len(payload) > MAX_RESPONSE_BYTES:
        raise RuntimeError("OpenWeatherMap response is too large")
    try:
        decoded = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("OpenWeatherMap returned invalid JSON") from exc
    if not isinstance(decoded, dict):
        raise RuntimeError("OpenWeatherMap returned an unexpected response")
    return decoded


def numeric(value: Any) -> Optional[float]:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def iso_utc(timestamp: int) -> str:
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat().replace("+00:00", "Z")


def extract_records(payload: Dict[str, Any], start: datetime, duration_minutes: int) -> List[Dict[str, Any]]:
    data = payload.get("data")
    if not isinstance(data, list):
        return []
    start_epoch = int(start.timestamp())
    end_epoch = start_epoch + duration_minutes * 60
    records: List[Dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        raw_timestamp = numeric(item.get("dt"))
        if raw_timestamp is None:
            continue
        timestamp = int(raw_timestamp)
        if timestamp < start_epoch or timestamp > end_epoch:
            continue
        temperature = numeric(item.get("temp"))
        humidity = numeric(item.get("humidity"))
        if temperature is None and humidity is None:
            continue
        record: Dict[str, Any] = {
            "timestamp_utc": iso_utc(timestamp),
        }
        if temperature is not None:
            record["temperature_c"] = temperature
        if humidity is not None and 0 <= humidity <= 100:
            record["humidity_percent"] = humidity
        if len(record) > 1:
            records.append(record)
    return records


def output_json(value: Dict[str, Any]) -> None:
    json.dump(value, sys.stdout, ensure_ascii=False, separators=(",", ":"))
    sys.stdout.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lat", required=True, help="Approximate latitude; it is rounded to 0.1 degree")
    parser.add_argument("--lon", required=True, help="Approximate longitude; it is rounded to 0.1 degree")
    parser.add_argument("--start", required=True, help="Activity start time with timezone, such as 2026-08-16T01:00:00Z")
    parser.add_argument("--duration-minutes", type=int, default=180)
    parser.add_argument("--dry-run", action="store_true", help="Print redacted request parameters without calling the API")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        latitude = round_coordinate(args.lat, -90, 90)
        longitude = round_coordinate(args.lon, -180, 180)
        start = parse_timestamp(args.start)
        if not 1 <= args.duration_minutes <= MAX_WINDOW_MINUTES:
            raise ValueError(f"duration-minutes must be between 1 and {MAX_WINDOW_MINUTES}")
    except ValueError as exc:
        print(f"配置错误：{exc}", file=sys.stderr)
        return 2

    api_key = os.environ.get("OPENWEATHERMAP_API_KEY", "").strip()
    if args.dry_run:
        output_json(
            {
                "endpoint": ENDPOINT,
                "query": {
                    "lat": latitude,
                    "lon": longitude,
                    "start": int(start.timestamp()),
                    "units": "metric",
                    "appid": "<redacted>",
                },
            }
        )
        return 0
    if not api_key:
        print("未找到 OPENWEATHERMAP_API_KEY；请在本机密钥管理器或环境中配置，不要粘贴到聊天。", file=sys.stderr)
        return 2

    try:
        payload = fetch_json(build_url(latitude, longitude, start, api_key))
        records = extract_records(payload, start, args.duration_minutes)
    except RuntimeError as exc:
        print(f"天气补全失败：{exc}", file=sys.stderr)
        return 3

    output_json(
        {
            "source": "OpenWeatherMap One Call API 4.0",
            "location_precision": "rounded_to_0.1_degree",
            "units": {"temperature": "celsius", "humidity": "percent"},
            "window_start_utc": start.isoformat().replace("+00:00", "Z"),
            "duration_minutes": args.duration_minutes,
            "records": records,
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
