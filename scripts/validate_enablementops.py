#!/usr/bin/env python3
"""Validate SYS-002 schemas, controlled catalogs, pilot inventory, and semantics."""

from copy import deepcopy
from datetime import date, datetime
import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ROOT / "systems/sys-002-enablementops"

BASE_DOCUMENTS = {
    "template-family-catalog.yaml": "schemas/template-family-catalog.schema.json",
    "golden-example-register.yaml": "schemas/golden-example-register.schema.json",
    "qa-test-matrix.yaml": "schemas/qa-test-matrix.schema.json",
    "records/enablementops-production-record.yaml": "schemas/production-record.schema.json",
}


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_yaml_scalars(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize_yaml_scalars(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize_yaml_scalars(item) for item in value]
    return value


def schema_errors(data, schema, label):
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "root"
        errors.append(f"{label}:{location}: {error.message}")
    return errors


def production_errors(production, family_ids, matrix, label):
    errors = []
    primary = production["need"]["primary_family_id"]
    companions = production["need"]["companion_family_ids"]
    if primary not in family_ids:
        errors.append(f"{label}: unknown primary family {primary}")
    for family_id in companions:
        if family_id not in family_ids:
            errors.append(f"{label}: unknown companion family {family_id}")
    if primary in companions:
        errors.append(f"{label}: primary family cannot also be a companion")

    qa = production["qa"]
    release = production["release"]
    status = production["record"]["status"]
    if status == "released" and release["decision"] != "released":
        errors.append(f"{label}: released status requires a released decision")
    if release["decision"] == "released" and status != "released":
        errors.append(f"{label}: released decision requires released status")
    if release["decision"] in {"approved", "released"}:
        if qa["master_score"] < matrix["matrix"]["master_score_minimum"]:
            errors.append(f"{label}: released production record is below the master QA threshold")
        if qa["blockers"] or qa["critical_defects"]:
            errors.append(f"{label}: released production record has a blocker or Critical defect")
        if qa["major_defects"]:
            errors.append(f"{label}: released production record has unresolved Major defects")
        if qa["regression"] not in {"pass", "not-applicable"}:
            errors.append(f"{label}: released production record lacks a passing regression result")
        if not qa["human_approval"] or not release["approver"] or not release["approved_on"]:
            errors.append(f"{label}: released production record lacks recorded human approval")
        if not release["evidence"]:
            errors.append(f"{label}: released production record lacks evidence")
    return errors


def semantic_errors(catalog, goldens, matrix, productions, manifests):
    errors = []
    families = catalog["families"]
    family_ids = [item["id"] for item in families]
    variant_count = sum(len(item["variants"]) for item in families)
    if len(family_ids) != len(set(family_ids)):
        errors.append("template catalog family IDs must be unique")
    if len(family_ids) != catalog["catalog"]["family_count"]:
        errors.append("template catalog family_count does not match entries")
    if variant_count != catalog["catalog"]["variant_count"]:
        errors.append("template catalog variant_count does not match entries")

    golden_ids = [item["id"] for item in goldens["approved_goldens"]]
    reference_ids = [item["id"] for item in goldens["reference_examples"]]
    if len(golden_ids) != len(set(golden_ids)):
        errors.append("approved golden IDs must be unique")
    if len(reference_ids) != len(set(reference_ids)):
        errors.append("reference example IDs must be unique")
    for item in goldens["approved_goldens"] + goldens["reference_examples"]:
        if item["family_id"] not in family_ids:
            errors.append(f"{item['id']}: unknown family {item['family_id']}")
    if set(goldens["coverage"]["all_family_rules_tested"]) != set(family_ids):
        errors.append("golden register family coverage must match the catalog")
    layout_values = {item["layout_id"] for item in goldens["approved_goldens"]}
    if set(goldens["coverage"]["approved_golden_layouts"]) != layout_values:
        errors.append("approved_golden_layouts must match approved golden entries")

    if matrix["matrix"]["master_score_minimum"] < 0.90:
        errors.append("master QA threshold cannot be below 0.90")
    if matrix["matrix"]["visual_score_minimum"] < 95:
        errors.append("visual QA threshold cannot be below 95")
    if len(matrix["formats"]) != 8:
        errors.append("QA matrix must define exactly eight controlled format groups")

    record_ids = []
    for label, production in productions.items():
        record_ids.append(production["record"]["id"])
        errors.extend(production_errors(production, family_ids, matrix, label))
    if len(record_ids) != len(set(record_ids)):
        errors.append("production record IDs must be unique")

    for pilot_dir, manifest in manifests.items():
        expected = set(manifest["records"])
        actual = {
            path.relative_to(pilot_dir).as_posix()
            for path in (pilot_dir / "records").glob("*.yaml")
        }
        if manifest["expected_record_count"] != len(actual):
            errors.append(f"{pilot_dir.name}: expected_record_count does not match discovered records")
        if expected != actual:
            errors.append(f"{pilot_dir.name}: manifest inventory does not match discovered records")
        if manifest["regression"]["result"] != "pass":
            errors.append(f"{pilot_dir.name}: regression result must pass")
    return errors


def validate_documents(root=ROOT, overrides=None):
    system = root / "systems/sys-002-enablementops"
    overrides = overrides or {}
    loaded = {}
    errors = []
    for document_path, schema_path in BASE_DOCUMENTS.items():
        data = deepcopy(overrides.get(document_path)) if document_path in overrides else load_yaml(system / document_path)
        data = normalize_yaml_scalars(data)
        loaded[document_path] = data
        errors.extend(schema_errors(data, load_json(system / schema_path), document_path))

    productions = {"records/enablementops-production-record.yaml": loaded["records/enablementops-production-record.yaml"]}
    production_schema = load_json(system / "schemas/production-record.schema.json")
    manifests = {}
    for pilot_dir in sorted((system / "pilots").glob("*")) if (system / "pilots").exists() else []:
        if not pilot_dir.is_dir():
            continue
        manifest_path = pilot_dir / "manifest.yaml"
        if not manifest_path.exists():
            errors.append(f"{pilot_dir.name}: missing manifest.yaml")
            continue
        manifest = normalize_yaml_scalars(load_yaml(manifest_path))
        manifests[pilot_dir] = manifest
        required = {"pilot", "records", "expected_record_count", "regression", "release_boundary"}
        if not isinstance(manifest, dict) or not required.issubset(manifest):
            errors.append(f"{pilot_dir.name}: incomplete manifest")
            continue
        for record_path in sorted((pilot_dir / "records").glob("*.yaml")):
            label = record_path.relative_to(system).as_posix()
            data = deepcopy(overrides.get(label)) if label in overrides else load_yaml(record_path)
            data = normalize_yaml_scalars(data)
            productions[label] = data
            errors.extend(schema_errors(data, production_schema, label))

    if not errors:
        errors.extend(semantic_errors(
            loaded["template-family-catalog.yaml"],
            loaded["golden-example-register.yaml"],
            loaded["qa-test-matrix.yaml"],
            productions,
            manifests,
        ))
    return errors


def main():
    errors = validate_documents()
    if errors:
        print("EnablementOps validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    pilot_count = len(list((SYSTEM / "pilots").glob("*/manifest.yaml")))
    record_count = 1 + len(list((SYSTEM / "pilots").glob("*/records/*.yaml")))
    print(f"EnablementOps validation passed: 4 schemas, {record_count} production records, {pilot_count} pilot manifest, and semantic regression controls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
