#!/usr/bin/env python3
"""Validate SYS-003 channel, campaign, and asset records."""

from copy import deepcopy
from datetime import date, datetime
import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ROOT / "systems/sys-003-engagementops"
DOCUMENTS = {
    "channel-profile-catalog.yaml": "schemas/channel-profile-catalog.schema.json",
    "records/example-campaign.yaml": "schemas/campaign-record.schema.json",
    "records/example-asset-specification.yaml": "schemas/asset-specification.schema.json",
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


def schema_errors(data, schema, label):
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "root"
        errors.append(f"{label}:{location}: {error.message}")
    return errors


def semantic_errors(catalog, campaign, asset):
    errors = []
    channels = catalog["channels"]
    channel_ids = [item["id"] for item in channels]
    if len(channel_ids) != len(set(channel_ids)):
        errors.append("channel IDs must be unique")
    if len(channels) != 8:
        errors.append("channel catalog must contain eight controlled channel classes")
    if len({item["channel_class"] for item in channels}) != 8:
        errors.append("each controlled channel class must appear exactly once")

    selected = set(campaign["strategy"]["channel_ids"])
    unknown = selected - set(channel_ids)
    if unknown:
        errors.append(f"campaign references unknown channels: {sorted(unknown)}")
    touchpoint_ids = [item["id"] for item in campaign["touchpoints"]]
    if len(touchpoint_ids) != len(set(touchpoint_ids)):
        errors.append("touchpoint IDs must be unique")
    referenced_assets = set()
    for touchpoint in campaign["touchpoints"]:
        if touchpoint["channel_id"] not in selected:
            errors.append(f"{touchpoint['id']}: channel is not selected by the campaign")
        referenced_assets.update(touchpoint["asset_ids"])

    if campaign["activation"]["start"] > campaign["activation"]["end"]:
        errors.append("campaign start cannot be after end")
    governed_states = {"approved", "scheduled", "active", "paused", "closed", "superseded", "retired"}
    if campaign["record"]["status"] in governed_states:
        if not campaign["governance"]["human_approval"] or not campaign["governance"]["release_approver"]:
            errors.append("governed campaign status requires recorded human approval")
    if campaign["strategy"]["risk_tier"] in {"R2", "R3"} and not campaign["governance"]["specialist_reviews"]:
        errors.append("R2/R3 campaign requires specialist reviews")

    if asset["record"]["campaign_id"] != campaign["record"]["id"]:
        errors.append("asset campaign reference does not match the campaign record")
    if asset["record"]["id"] not in referenced_assets:
        errors.append("asset is not referenced by a campaign touchpoint")
    asset_channels = set(asset["delivery"]["channel_ids"])
    if not asset_channels.issubset(selected):
        errors.append("asset references a channel not selected by the campaign")
    if asset["governance"]["fidelity"] in {"F2", "F3"} and not asset["governance"]["sme_review"]:
        errors.append("F2/F3 asset requires SME review")
    if asset["governance"]["fidelity"] == "F3" and not asset["governance"]["specialist_reviews"]:
        errors.append("F3 asset requires specialist review")
    if asset["record"]["status"] in {"approved", "active"}:
        if not asset["governance"]["approved"] or not asset["governance"]["approver"]:
            errors.append("approved/active asset requires recorded approval")
    return errors


def validate_documents(root=ROOT, overrides=None):
    system = root / "systems/sys-003-engagementops"
    overrides = overrides or {}
    loaded = {}
    errors = []
    for document, schema_path in DOCUMENTS.items():
        data = deepcopy(overrides.get(document)) if document in overrides else load_yaml(system / document)
        data = normalize(data)
        schema = json.loads((system / schema_path).read_text(encoding="utf-8"))
        loaded[document] = data
        errors.extend(schema_errors(data, schema, document))
    if not errors:
        errors.extend(semantic_errors(
            loaded["channel-profile-catalog.yaml"],
            loaded["records/example-campaign.yaml"],
            loaded["records/example-asset-specification.yaml"],
        ))
    return errors


def main():
    errors = validate_documents()
    if errors:
        print("EngagementOps validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("EngagementOps validation passed: 3 schemas, 8 channel profiles, 1 campaign record, 1 asset specification, and semantic cross-references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
