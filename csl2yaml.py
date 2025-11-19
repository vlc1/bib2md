#!/usr/bin/env python3
"""
csl_to_yaml.py

Convert a CSL-JSON file (a list of citation objects) into Pandoc-ready YAML
suitable for a `references:` section. The first fields are ordered as:

  1. id
  2. type
  3. title
  4. author
  5. container-title
  6. issued

Remaining fields follow in sorted order.

Usage:
    python csl_to_yaml.py input.csl > references.yaml
"""
import json
import sys
import yaml

PRIMARY_ORDER = [
    "id",
    "type",
    "title",
    "author",
    "container-title",
    "issued",
]


def load_csl(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = [data]
    return data


def simplify_date(date_obj):
    """
    Convert CSL date-parts format like {"date-parts": [[2005, 11, 19]]}
    into {"year": 2005, "month": 11, "day": 19} when possible.
    If the format is unexpected, return it unchanged.
    """
    if not isinstance(date_obj, dict):
        return date_obj

    dp = date_obj.get("date-parts")
    if not dp or not isinstance(dp, list) or not dp[0]:
        return date_obj

    parts = dp[0]
    out = {}
    if len(parts) >= 1:
        try:
            out["year"] = int(parts[0])
        except (ValueError, TypeError):
            out["year"] = parts[0]
    if len(parts) >= 2:
        try:
            out["month"] = int(parts[1])
        except (ValueError, TypeError):
            out["month"] = parts[1]
    if len(parts) >= 3:
        try:
            out["day"] = int(parts[2])
        except (ValueError, TypeError):
            out["day"] = parts[2]
    return out


def normalize_entry(entry):
    """
    Normalize an entry: simplify date fields and produce a plain dict
    with the requested ordering for the first fields. Remaining fields
    are appended in sorted order.
    """
    normalized = dict(entry)  # shallow copy

    # Simplify common date fields for readability
    for key in ("issued", "accessed", "event-date", "published"):
        if key in normalized:
            normalized[key] = simplify_date(normalized[key])

    # Build a plain dict in the desired order (dict preserves insertion order)
    ordered_plain = {}

    # Add primary fields in the exact order requested
    for k in PRIMARY_ORDER:
        if k in normalized:
            ordered_plain[k] = normalized.pop(k)

    # Append remaining fields in sorted order (stable)
    for k in sorted(normalized.keys()):
        ordered_plain[k] = normalized[k]

    return ordered_plain


def main():
    if len(sys.argv) != 2:
        print("Usage: python csl2yaml.py input.csl", file=sys.stderr)
        sys.exit(1)

    csl_items = load_csl(sys.argv[1])
    yaml_ready = [normalize_entry(it) for it in csl_items]

    # Use safe_dump to avoid Python-specific tags and ensure readable block style
    print(
        yaml.safe_dump(
            yaml_ready,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
        )
    )


if __name__ == "__main__":
    main()
