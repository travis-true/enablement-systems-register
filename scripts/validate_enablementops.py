#!/usr/bin/env python3
"""Validate SYS-002 schemas, controlled catalogs, and semantic relationships."""

from copy import deepcopy
from datetime import date, datetime
import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ROOT / "systems/sys-002-enablementops"

DOCUMENTS = {
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
    """Convert PyYAML date objects to the JSON-compatible strings schemas expect."""
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


def semantic_errors(catalog, goldens, matrix, production):
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
    coverage = goldens["coverage"]["all_family_rules_tested"]
    if set(coverage) != set(family_ids):
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

    primary = production["need"]["primary_family_id"]
    companions = production["need"]["companion_family_ids"]
    if primary not in family_ids:
        errors.append(f"production record: unknown primary family {primary}")
    for family_id in companions:
        if family_id not in family_ids:
            errors.append(f"production record: unknown companion family {family_id}")
    if primary in companions:
        errors.append("production record: primary family cannot also be a companion")

    qa = production["qa"]
    release = production["release"]
    if release["decision"] in {"approved", "released"}:
        if qa["master_score"] < matrix["matrix"]["master_score_minimum"]:
            errors.append("released production record is below the master QA threshold")
        if qa["blockers"] or qa["critical_defects"]:
            errors.append("released production record has a blocker or Critical defect")
        if qa["major_defects"]:
            errors.append("released production record has unresolved Major defects")
        if qa["regression"] not in {"pass", "not-applicable"}:
            errors.append("released production record lacks a passing regression result")
        if not qa["human_approval"] or not release["approver"] or not release["approved_on"]:
            errors.append("released production record lacks recorded human approval")
        if not release["evidence"]:
            errors.append("released production record lacks evidence")
    return errors


def validate_documents(root=ROOT, overrides=None):
    system = root / "systems/sys-002-enablementops"
    loaded = {}
    errors = []
    overrides = overrides or {}
    for document_path, schema_path in DOCUMENTS.items():
        data = deepcopy(overrides.get(document_path)) if document_path in overrides else load_yaml(system / document_path)
        data = normalize_yaml_scalars(data)
        schema = load_json(system / schema_path)
        loaded[document_path] = data
        errors.extend(schema_errors(data, schema, document_path))
    if not errors:
        errors.extend(semantic_errors(
            loaded["template-family-catalog.yaml"],
            loaded["golden-example-register.yaml"],
            loaded["qa-test-matrix.yaml"],
            loaded["records/enablementops-production-record.yaml"],
        ))
    return errors


def main():
    errors = validate_documents()
    if errors:
        print("EnablementOps validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("EnablementOps validation passed: 4 schemas, 4 records, and semantic cross-references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
