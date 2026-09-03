#!/usr/bin/env python3
"""Discover and validate every governed record in every LACE pilot package."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
LACE = ROOT / "systems" / "sys-001-lace"
INDEX_NAME = "record-index.yaml"
ASSET_RECORD_FIELDS = ("build_specification", "handoff", "release_manifest")


def load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: invalid YAML: {exc}")
        return None


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return None


def indexed_record_names(index: dict[str, Any], label: str, errors: list[str]) -> set[str]:
    names: list[Any] = []
    shared = index.get("shared_records")
    if not isinstance(shared, list):
        errors.append(f"{label}.shared_records: must be an array")
    else:
        names.extend(shared)

    assets = index.get("asset_records")
    if not isinstance(assets, dict) or not assets:
        errors.append(f"{label}.asset_records: must be a non-empty object")
    else:
        for asset_name, asset in assets.items():
            if not isinstance(asset, dict):
                errors.append(f"{label}.asset_records.{asset_name}: must be an object")
                continue
            for field in ASSET_RECORD_FIELDS:
                if field not in asset:
                    errors.append(f"{label}.asset_records.{asset_name}: missing {field}")
                else:
                    names.append(asset[field])

    if "lifecycle_review" not in index:
        errors.append(f"{label}: missing lifecycle_review")
    else:
        names.append(index["lifecycle_review"])

    valid: list[str] = []
    for value in names:
        if not isinstance(value, str) or not value.endswith(('.yaml', '.yml')):
            errors.append(f"{label}: invalid governed-record filename {value!r}")
        elif Path(value).name != value:
            errors.append(f"{label}: governed-record filename must not contain a path: {value}")
        else:
            valid.append(value)
    duplicates = sorted({name for name in valid if valid.count(name) > 1})
    for name in duplicates:
        errors.append(f"{label}: governed record indexed more than once: {name}")
    return set(valid)


def template_contracts(lace: Path, errors: list[str]) -> dict[str, dict[str, Any]]:
    register_path = lace / "template-register.yaml"
    register = load_yaml(register_path, errors)
    contracts: dict[str, dict[str, Any]] = {}
    if not isinstance(register, dict):
        return contracts
    for entry in register.get("templates", []):
        if not isinstance(entry, dict) or entry.get("status") != "active":
            continue
        template_id = entry.get("id")
        schema_path = entry.get("schema_path")
        if not isinstance(template_id, str) or not isinstance(schema_path, str):
            continue
        path = (lace / schema_path).resolve()
        try:
            path.relative_to(lace.resolve())
        except ValueError:
            errors.append(f"template {template_id}: schema path escapes LACE package")
            continue
        schema = load_json(path, errors)
        if not isinstance(schema, dict):
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:
            errors.append(f"template {template_id}: invalid schema: {exc}")
            continue
        contracts[template_id] = {"version": entry.get("version"), "schema": schema}
    return contracts


def validate_pilot_records(lace: Path, errors: list[str]) -> dict[str, int]:
    metrics = {"pilots": 0, "records": 0}
    contracts = template_contracts(lace, errors)
    seen_record_ids: dict[str, Path] = {}
    pilots_root = lace / "pilots"
    if not pilots_root.exists():
        return metrics

    for records_dir in sorted(p for p in pilots_root.glob("*/records") if p.is_dir()):
        metrics["pilots"] += 1
        pilot_dir = records_dir.parent
        pilot_id = pilot_dir.name.upper()
        index_path = records_dir / INDEX_NAME
        if not index_path.exists():
            errors.append(f"{pilot_dir}: missing {INDEX_NAME}")
            continue
        index = load_yaml(index_path, errors)
        if not isinstance(index, dict):
            continue
        label = str(index_path)
        if index.get("pilot_id") != pilot_id:
            errors.append(f"{label}: pilot_id must be {pilot_id}")
        if index.get("system_id") != "SYS-001":
            errors.append(f"{label}: system_id must be SYS-001")

        indexed = indexed_record_names(index, label, errors)
        discovered = {
            path.name
            for path in records_dir.glob("*.y*ml")
            if path.name != INDEX_NAME
        }
        for name in sorted(indexed - discovered):
            errors.append(f"{label}: indexed governed record is missing: {name}")
        for name in sorted(discovered - indexed):
            errors.append(f"{label}: governed record is not indexed: {name}")

        for name in sorted(discovered):
            path = records_dir / name
            record = load_yaml(path, errors)
            if not isinstance(record, dict):
                errors.append(f"{path}: governed record must be an object")
                continue
            metrics["records"] += 1
            template_id = record.get("template_id")
            contract = contracts.get(template_id)
            if not contract:
                errors.append(f"{path}: unknown or inactive template_id {template_id!r}")
                continue
            if record.get("template_version") != contract["version"]:
                errors.append(
                    f"{path}: template_version {record.get('template_version')!r} "
                    f"does not match registered version {contract['version']!r}"
                )
            if record.get("system_id") != "SYS-001":
                errors.append(f"{path}: system_id must be SYS-001")
            record_id = record.get("record_id")
            if not isinstance(record_id, str) or not record_id:
                errors.append(f"{path}: missing record_id")
            elif record_id in seen_record_ids:
                errors.append(
                    f"{path}: duplicate record_id {record_id}; first used by "
                    f"{seen_record_ids[record_id]}"
                )
            else:
                seen_record_ids[record_id] = path

            validator = Draft202012Validator(
                contract["schema"], format_checker=FormatChecker()
            )
            for failure in sorted(
                validator.iter_errors(record), key=lambda item: list(item.path)
            ):
                location = ".".join(str(part) for part in failure.path) or "<root>"
                errors.append(f"{path}.{location}: {failure.message}")
    return metrics


def main() -> int:
    errors: list[str] = []
    metrics = validate_pilot_records(LACE, errors)
    if errors:
        print("LACE pilot-record validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(
        "LACE pilot-record validation passed: "
        f"{metrics['pilots']} pilot package(s), {metrics['records']} governed record(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
