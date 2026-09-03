#!/usr/bin/env python3
"""Discover and validate every SYS-003 pilot package."""

from datetime import date, datetime
import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ROOT / "systems/sys-003-engagementops"
SCHEMAS = {
    "handoff": "activation-handoff.schema.json",
    "campaign": "campaign-record.schema.json",
    "measurement": "measurement-plan.schema.json",
    "localization": "localization-profile.schema.json",
    "readiness": "delivery-readiness-record.schema.json",
    "asset": "asset-specification.schema.json",
}


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def normalize(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize(item) for item in value]
    return value


def validate_schema(data, schema_name, label):
    schema = json.loads((SYSTEM / "schemas" / SCHEMAS[schema_name]).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{label}:{'.'.join(str(x) for x in error.path) or 'root'}: {error.message}"
        for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path))
    ]


def validate_pilot(pilot_dir, overrides=None):
    overrides = overrides or {}
    errors = []
    manifest = normalize(load_yaml(pilot_dir / "manifest.yaml"))
    record_map = manifest["records"]
    expected_records = {
        record_map["handoff"], record_map["campaign"], record_map["measurement"],
        record_map["localization"], record_map["readiness"], *record_map["assets"],
    }
    actual_records = {path.relative_to(pilot_dir).as_posix() for path in (pilot_dir / "records").glob("*.yaml")}
    if expected_records != actual_records:
        errors.append(f"{pilot_dir.name}: manifest record inventory mismatch")
    expected_assets = set(manifest["assets"])
    actual_assets = {path.relative_to(pilot_dir).as_posix() for path in (pilot_dir / "assets").glob("*") if path.is_file()}
    if expected_assets != actual_assets:
        errors.append(f"{pilot_dir.name}: manifest asset inventory mismatch")
    for required in [manifest["approval"], manifest["qa_evidence"]]:
        if not (pilot_dir / required).exists():
            errors.append(f"{pilot_dir.name}: missing {required}")

    def record(key, schema_name):
        rel = record_map[key]
        label = f"{pilot_dir.name}/{rel}"
        data = normalize(overrides.get(rel, load_yaml(pilot_dir / rel)))
        errors.extend(validate_schema(data, schema_name, label))
        return data

    handoff = record("handoff", "handoff")
    campaign = record("campaign", "campaign")
    measurement = record("measurement", "measurement")
    localization = record("localization", "localization")
    readiness = record("readiness", "readiness")
    assets = []
    for rel in record_map["assets"]:
        data = normalize(overrides.get(rel, load_yaml(pilot_dir / rel)))
        errors.extend(validate_schema(data, "asset", f"{pilot_dir.name}/{rel}"))
        assets.append(data)
    if errors:
        return errors

    campaign_id = campaign["record"]["id"]
    if manifest["pilot"]["campaign_id"] != campaign_id:
        errors.append("pilot manifest campaign ID does not match")
    for label, data in [("handoff", handoff), ("measurement", measurement), ("localization", localization), ("readiness", readiness)]:
        section = "request" if label == "handoff" else "record"
        if data[section]["campaign_id"] != campaign_id:
            errors.append(f"{label} campaign reference does not match")
    if handoff["record"]["status"] != "accepted" or handoff["disposition"]["material_gaps"]:
        errors.append("pilot handoff must be accepted with no material gaps")
    if not campaign["governance"]["human_approval"] or campaign["record"]["status"] != "active":
        errors.append("pilot campaign must be approved and active")

    asset_ids = [item["record"]["id"] for item in assets]
    if len(asset_ids) != len(set(asset_ids)):
        errors.append("pilot asset IDs must be unique")
    referenced_assets = {asset_id for tp in campaign["touchpoints"] for asset_id in tp["asset_ids"]}
    if set(asset_ids) != referenced_assets:
        errors.append("pilot asset inventory must match campaign touchpoints")
    for asset in assets:
        if asset["record"]["campaign_id"] != campaign_id:
            errors.append(f"{asset['record']['id']}: campaign reference does not match")
        if asset["record"]["status"] != "active" or not asset["governance"]["approved"] or not asset["governance"]["approver"]:
            errors.append(f"{asset['record']['id']}: asset must be approved and active")

    if measurement["record"]["status"] != "active" or not measurement["governance"]["approved"]:
        errors.append("pilot measurement plan must be approved and active")
    if readiness["record"]["status"] != "released" or readiness["release"]["decision"] != "released":
        errors.append("pilot readiness record must be released")
    p0 = [gate for gate in readiness["gates"] if gate["priority"] == "P0"]
    if any(gate["result"] not in {"pass", "not-applicable"} for gate in p0):
        errors.append("pilot has an incomplete or failing P0 gate")
    if readiness["defects"]["blocker"] or readiness["defects"]["critical"] or readiness["defects"]["major"]:
        errors.append("pilot has an open Blocker, Critical, or Major defect")
    if not readiness["release"]["approver"] or not readiness["release"]["approved_on"]:
        errors.append("pilot lacks human release approval")

    registry = normalize(load_yaml(SYSTEM / "campaign-registry.yaml"))
    entries = [item for item in registry["campaigns"] if item["id"] == campaign_id]
    if len(entries) != 1 or entries[0]["version"] != campaign["record"]["version"] or entries[0]["status"] != campaign["record"]["status"]:
        errors.append("pilot campaign registry entry is missing or inconsistent")
    calendar = normalize(load_yaml(SYSTEM / "campaign-calendar.yaml"))
    events = [item for item in calendar["events"] if item["campaign_id"] == campaign_id]
    touchpoints = {item["id"]: item for item in campaign["touchpoints"]}
    if {item["touchpoint_id"] for item in events} != set(touchpoints):
        errors.append("pilot calendar inventory does not match touchpoints")
    for event in events:
        tp = touchpoints.get(event["touchpoint_id"])
        if tp and (event["channel_id"] != tp["channel_id"] or event["scheduled_at"][:10] != tp["scheduled_date"]):
            errors.append(f"{event['id']}: pilot calendar does not match touchpoint")
    return errors


def validate_all(root=ROOT, pilot_overrides=None):
    global SYSTEM
    original = SYSTEM
    SYSTEM = root / "systems/sys-003-engagementops"
    try:
        pilots = sorted((SYSTEM / "pilots").glob("*/manifest.yaml"))
        if not pilots:
            return ["no EngagementOps pilot packages discovered"]
        errors = []
        for manifest in pilots:
            errors.extend(validate_pilot(manifest.parent, (pilot_overrides or {}).get(manifest.parent.name)))
        return errors
    finally:
        SYSTEM = original


def main():
    errors = validate_all()
    if errors:
        print("EngagementOps pilot validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    count = len(list((SYSTEM / "pilots").glob("*/manifest.yaml")))
    print(f"EngagementOps pilot validation passed: {count} pilot package, exact inventory, governed records, release gates, registry, and calendar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
