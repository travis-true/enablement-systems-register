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
    "metric-catalog.yaml": "schemas/metric-catalog.schema.json",
    "records/example-measurement-plan.yaml": "schemas/measurement-plan.schema.json",
    "records/example-localization-profile.yaml": "schemas/localization-profile.schema.json",
    "records/example-delivery-readiness.yaml": "schemas/delivery-readiness-record.schema.json",
    "records/example-activation-handoff.yaml": "schemas/activation-handoff.schema.json",
    "campaign-registry.yaml": "schemas/campaign-registry.schema.json",
    "campaign-calendar.yaml": "schemas/campaign-calendar.schema.json",
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


def semantic_errors(catalog, campaign, asset, metric_catalog, measurement_plan, localization, readiness, handoff, registry, calendar):
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

    metric_ids = [item["id"] for item in metric_catalog["metrics"]]
    if len(metric_ids) != len(set(metric_ids)):
        errors.append("metric IDs must be unique")
    required_levels = {"reach", "engagement", "learning", "adoption", "performance", "sustainment"}
    if {item["level"] for item in metric_catalog["metrics"]} != required_levels:
        errors.append("metric catalog must cover all six measurement levels")
    if measurement_plan["record"]["campaign_id"] != campaign["record"]["id"]:
        errors.append("measurement plan campaign reference does not match")
    selected_metrics = [item["measure_id"] for item in measurement_plan["measures"]]
    if len(selected_metrics) != len(set(selected_metrics)):
        errors.append("measurement plan measure IDs must be unique")
    unknown_metrics = set(selected_metrics) - set(metric_ids)
    if unknown_metrics:
        errors.append(f"measurement plan references unknown metrics: {sorted(unknown_metrics)}")
    baseline = measurement_plan["baseline"]
    if baseline["status"] == "available" and (baseline["source"] is None or baseline["value"] is None):
        errors.append("available baseline requires a source and value")
    if measurement_plan["record"]["status"] in {"approved", "active", "closed"}:
        if not measurement_plan["governance"]["approved"] or not measurement_plan["governance"]["approver"]:
            errors.append("governed measurement plan requires recorded approval")
    if measurement_plan["decision"]["outcome"] != "not-decided":
        if not measurement_plan["decision"]["decided_on"] or not measurement_plan["decision"]["decision_owner"]:
            errors.append("measurement decision requires date and decision owner")

    if localization["record"]["campaign_id"] != campaign["record"]["id"]:
        errors.append("localization profile campaign reference does not match")
    if localization["locales"]["required"] and not localization["locales"]["targets"]:
        errors.append("required localization must identify target locales")
    if localization["record"]["status"] in {"approved", "active"}:
        if not localization["reviews"]["approved"] or not localization["reviews"]["approver"]:
            errors.append("approved/active localization requires recorded approval")
    if localization["fidelity"]["level"] in {"F2", "F3"} and "not-required" in localization["reviews"]["sme"]:
        errors.append("F2/F3 localization requires SME review")
    if localization["fidelity"]["level"] == "F3" and not localization["reviews"]["specialist"]:
        errors.append("F3 localization requires specialist review")

    if readiness["record"]["campaign_id"] != campaign["record"]["id"]:
        errors.append("delivery-readiness campaign reference does not match")
    gate_ids = [item["id"] for item in readiness["gates"]]
    required_gates = {"source", "technical", "specialist", "accessibility", "brand", "operational", "measurement", "release"}
    if set(gate_ids) != required_gates or len(gate_ids) != len(required_gates):
        errors.append("delivery readiness must contain each required gate exactly once")
    if readiness["screenshots"]["present"] and readiness["screenshots"]["redaction_review"] != "pass":
        errors.append("screenshots require a passing redaction review")
    if readiness["change_control"]["post_approval_change"]:
        if readiness["change_control"]["p0_regression"] != "pass" or readiness["change_control"]["p1_regression"] != "pass":
            errors.append("post-approval change requires passing P0/P1 regression")
    if readiness["release"]["decision"] in {"approved", "released"}:
        p0 = [item for item in readiness["gates"] if item["priority"] == "P0"]
        if any(item["result"] not in {"pass", "not-applicable"} for item in p0):
            errors.append("release has an incomplete or failing P0 gate")
        if readiness["defects"]["blocker"] or readiness["defects"]["critical"]:
            errors.append("release has an open Blocker or Critical defect")
        if not readiness["release"]["approver"] or not readiness["release"]["approved_on"]:
            errors.append("release requires recorded human approval")

    if handoff["request"]["campaign_id"] != campaign["record"]["id"]:
        errors.append("handoff campaign reference does not match")
    if handoff["record"]["status"] == "accepted":
        if handoff["disposition"]["decision"] != "accepted":
            errors.append("accepted handoff status requires accepted disposition")
        if handoff["disposition"]["material_gaps"]:
            errors.append("accepted handoff cannot contain material gaps")
        if not handoff["governance"]["receiver"] or not handoff["disposition"]["decided_on"]:
            errors.append("accepted handoff requires receiver and decision date")

    campaigns = registry["campaigns"]
    registry_ids = [item["id"] for item in campaigns]
    if len(registry_ids) != len(set(registry_ids)):
        errors.append("campaign registry IDs must be unique")
    matching = [item for item in campaigns if item["id"] == campaign["record"]["id"]]
    if len(matching) != 1:
        errors.append("campaign record must appear exactly once in registry")
    else:
        entry = matching[0]
        if entry["version"] != campaign["record"]["version"] or entry["status"] != campaign["record"]["status"]:
            errors.append("campaign registry version/status does not match campaign")
        if entry["handoff_id"] != handoff["record"]["id"]:
            errors.append("campaign registry handoff reference does not match")
        if set(entry["channel_ids"]) != set(campaign["strategy"]["channel_ids"]):
            errors.append("campaign registry channels do not match campaign")
        if set(entry["asset_ids"]) != referenced_assets:
            errors.append("campaign registry assets do not match touchpoints")
        if set(entry["measure_ids"]) != set(selected_metrics):
            errors.append("campaign registry measures do not match measurement plan")

    event_ids = [item["id"] for item in calendar["events"]]
    if len(event_ids) != len(set(event_ids)):
        errors.append("calendar event IDs must be unique")
    touchpoints = {item["id"]: item for item in campaign["touchpoints"]}
    seen_touchpoints = set()
    for event in calendar["events"]:
        if event["campaign_id"] != campaign["record"]["id"]:
            errors.append(f"{event['id']}: calendar campaign reference does not match")
        if event["touchpoint_id"] not in touchpoints:
            errors.append(f"{event['id']}: unknown touchpoint")
            continue
        seen_touchpoints.add(event["touchpoint_id"])
        touchpoint = touchpoints[event["touchpoint_id"]]
        if event["channel_id"] != touchpoint["channel_id"]:
            errors.append(f"{event['id']}: calendar channel does not match touchpoint")
        if event["scheduled_at"][:10] != touchpoint["scheduled_date"]:
            errors.append(f"{event['id']}: calendar date does not match touchpoint")
        if event["collision_status"] in {"review-required", "resolved", "accepted"} and not event["collision_evidence"]:
            errors.append(f"{event['id']}: collision status requires evidence")
    if seen_touchpoints != set(touchpoints):
        errors.append("calendar must include every campaign touchpoint")
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
            loaded["metric-catalog.yaml"],
            loaded["records/example-measurement-plan.yaml"],
            loaded["records/example-localization-profile.yaml"],
            loaded["records/example-delivery-readiness.yaml"],
            loaded["records/example-activation-handoff.yaml"],
            loaded["campaign-registry.yaml"],
            loaded["campaign-calendar.yaml"],
        ))
    return errors


def main():
    errors = validate_documents()
    if errors:
        print("EngagementOps validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("EngagementOps validation passed: 10 schemas, 8 channel profiles, 12 metrics, 6 governed records, 1 registry, 1 calendar, and cross-system semantics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
