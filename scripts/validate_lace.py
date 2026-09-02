#!/usr/bin/env python3
"""Validate the canonical LACE package and executable decision controls."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import json
import re
import sys
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[1]
LACE = ROOT / "systems" / "sys-001-lace"
TEMPLATE_REGISTER = LACE / "template-register.yaml"
DECISION_RULES = LACE / "decision-engine" / "decision-rules.yaml"
DECISION_TESTS = LACE / "decision-engine" / "test-cases.yaml"

REQUIRED_PACKAGE_FILES = {
    "README.md",
    "specification.md",
    "source-crosswalk.md",
    "template-namespace.md",
    "template-register.yaml",
    "control-records.md",
    "schemas/decision-rules.schema.json",
    "schemas/build-kit-profile.schema.json",
    "decision-engine/decision-rules.yaml",
    "decision-engine/operating-guide.md",
    "decision-engine/test-cases.yaml",
    "build-kits/README.md",
}

ALLOWED_OPERATORS = {
    "equals",
    "in",
    "not-in",
    "greater-than",
    "greater-than-or-equal",
    "less-than",
    "less-than-or-equal",
    "contains",
}
DERIVED_DECISION_FIELDS = {"route", "asset_type"}
LOCAL_LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
        return None


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None


def validate_schema(schema: dict[str, Any], label: str, errors: list[str]) -> bool:
    try:
        Draft202012Validator.check_schema(schema)
        return True
    except SchemaError as exc:
        errors.append(f"{label}: invalid JSON Schema: {exc.message}")
        return False


def validate_instance(
    instance: Any,
    schema: dict[str, Any],
    label: str,
    errors: list[str],
) -> list[str]:
    found = []
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        found.append(f"{label}.{location}: {error.message}")
    errors.extend(found)
    return found


def front_matter(path: Path, errors: list[str]) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path.relative_to(ROOT)}: missing YAML front matter")
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{path.relative_to(ROOT)}: incomplete YAML front matter")
        return None
    try:
        data = yaml.safe_load(parts[1])
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid front matter: {exc}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{path.relative_to(ROOT)}: front matter must be an object")
        return None
    return data


def safe_lace_path(relative_path: str, label: str, errors: list[str]) -> Path | None:
    candidate = (LACE / relative_path).resolve()
    try:
        candidate.relative_to(LACE.resolve())
    except ValueError:
        errors.append(f"{label}: path escapes the LACE package: {relative_path}")
        return None
    if not candidate.exists():
        errors.append(f"{label}: missing artifact: {relative_path}")
        return None
    return candidate


def parse_range(value: str, label: str, errors: list[str]) -> tuple[int, int] | None:
    match = re.fullmatch(r"(\d{3})-(\d{3})", str(value))
    if not match:
        errors.append(f"{label}: invalid range {value}")
        return None
    start, end = map(int, match.groups())
    if start > end:
        errors.append(f"{label}: reversed range {value}")
        return None
    return start, end


def condition_matches(inputs: dict[str, Any], condition: dict[str, Any]) -> bool:
    field = condition["field"]
    operator = condition["operator"]
    expected = condition["value"]
    actual = inputs.get(field)

    if operator == "equals":
        return actual == expected
    if operator == "in":
        return actual in expected
    if operator == "not-in":
        return actual not in expected
    if operator == "contains":
        return expected in actual
    if operator == "greater-than":
        return actual > expected
    if operator == "greater-than-or-equal":
        return actual >= expected
    if operator == "less-than":
        return actual < expected
    if operator == "less-than-or-equal":
        return actual <= expected
    raise ValueError(f"unsupported operator: {operator}")


def rule_matches(inputs: dict[str, Any], rule: dict[str, Any]) -> bool:
    conditions = rule.get("when", [])
    if not conditions:
        return True
    results = [condition_matches(inputs, condition) for condition in conditions]
    return all(results) if rule["match"] == "all" else any(results)


def evaluate_decision(inputs: dict[str, Any], rules: dict[str, Any]) -> dict[str, Any]:
    required = rules["input_contract"]["required"]
    missing = [field for field in required if field not in inputs]
    if missing:
        return {"status": "blocked", "error": f"missing:{','.join(missing)}"}

    for rule in sorted(rules["blockers"], key=lambda item: -item["priority"]):
        if rule_matches(inputs, rule):
            return {"status": "blocked", "blocker_rule": rule["id"]}

    route_rule = next(
        rule
        for rule in sorted(rules["route_rules"], key=lambda item: -item["priority"])
        if rule_matches(inputs, rule)
    )
    derived = dict(inputs)
    derived["route"] = route_rule["route"]

    asset_rule = next(
        rule
        for rule in sorted(rules["primary_asset_rules"], key=lambda item: -item["priority"])
        if derived["route"] in rule["compatible_routes"] and rule_matches(derived, rule)
    )
    recommendation = asset_rule["recommendation"]
    derived["asset_type"] = recommendation["asset_type"]

    companions = []
    used_purposes: set[str] = set()
    used_assets = {(recommendation["family"], recommendation["asset_type"])}
    for rule in rules["companion_rules"]:
        companion = rule["recommendation"]
        asset_key = (companion["family"], companion["asset_type"])
        if (
            rule_matches(derived, rule)
            and rule["purpose"] not in used_purposes
            and asset_key not in used_assets
            and len(companions) < rules["engine"]["maximum_companions"]
        ):
            companions.append(rule)
            used_purposes.add(rule["purpose"])
            used_assets.add(asset_key)

    warning_rules = [
        rule["id"] for rule in rules["warnings"] if rule_matches(derived, rule)
    ]
    confidence_rule = next(
        rule
        for rule in sorted(rules["confidence_rules"], key=lambda item: -item["priority"])
        if rule_matches(derived, rule)
    )
    human_reviews = [
        rule["reviewer"]
        for rule in rules["human_review_rules"]
        if rule_matches(derived, rule)
    ]

    return {
        "status": "recommendation-ready",
        "route_rule": route_rule["id"],
        "route": route_rule["route"],
        "asset_rule": asset_rule["id"],
        "family": recommendation["family"],
        "asset_type": recommendation["asset_type"],
        "template_id": recommendation["template_id"],
        "companion_count": len(companions),
        "companion_purposes": [item["purpose"] for item in companions],
        "warning_rules": warning_rules,
        "confidence": confidence_rule["confidence"],
        "human_reviews": human_reviews,
    }


def validate_internal_links(errors: list[str]) -> int:
    checked = 0
    for path in LACE.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw_target in LOCAL_LINK_RE.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target:
                continue
            checked += 1
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"{path.relative_to(ROOT)}: local link escapes repository: {raw_target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: broken local link: {raw_target}"
                )
    return checked


def main() -> int:
    errors: list[str] = []
    metrics = {
        "schemas": 0,
        "templates": 0,
        "active_templates": 0,
        "decision_rules": 0,
        "decision_cases": 0,
        "build_kits": 0,
        "local_links": 0,
    }

    for relative_path in sorted(REQUIRED_PACKAGE_FILES):
        if not (LACE / relative_path).exists():
            errors.append(f"SYS-001 package missing required file: {relative_path}")

    schemas: dict[Path, dict[str, Any]] = {}
    for path in sorted((LACE / "schemas").glob("*.schema.json")):
        schema = load_json(path, errors)
        if isinstance(schema, dict) and validate_schema(
            schema, str(path.relative_to(ROOT)), errors
        ):
            schemas[path.resolve()] = schema
            metrics["schemas"] += 1

    register = load_yaml(TEMPLATE_REGISTER, errors)
    known_template_ids: set[str] = set()
    active_template_ids: set[str] = set()

    if isinstance(register, dict):
        namespace = register.get("namespace", {})
        pattern_text = namespace.get("id_pattern", "")
        try:
            id_pattern = re.compile(pattern_text)
        except re.error as exc:
            errors.append(f"template-register.yaml: invalid id_pattern: {exc}")
            id_pattern = re.compile(r"a^")

        allowed_statuses = set(register.get("allowed_statuses", []))
        family_ranges: dict[str, tuple[int, int]] = {}
        for index, item in enumerate(register.get("ranges", []), start=1):
            parsed = parse_range(item.get("range", ""), f"ranges[{index}]", errors)
            if parsed:
                family_ranges[item.get("family", "")] = parsed

        alias_owners: dict[tuple[str, str], str] = {}
        templates = register.get("templates", [])
        metrics["templates"] = len(templates)

        for index, item in enumerate(templates, start=1):
            label = f"template-register.yaml.templates[{index}]"
            template_id = item.get("id", "")
            if not id_pattern.fullmatch(str(template_id)):
                errors.append(f"{label}: invalid canonical ID {template_id}")
            if template_id in known_template_ids:
                errors.append(f"{label}: duplicate canonical ID {template_id}")
            known_template_ids.add(template_id)

            status = item.get("status")
            if status not in allowed_statuses:
                errors.append(f"{label}: invalid status {status}")

            family = item.get("family")
            family_range = family_ranges.get(family)
            if not family_range:
                errors.append(f"{label}: no governed range for family {family}")
            else:
                number = int(template_id.rsplit("-", 1)[-1])
                if not family_range[0] <= number <= family_range[1]:
                    errors.append(
                        f"{label}: {template_id} is outside the {family} range"
                    )

            for alias in item.get("legacy_aliases", []):
                alias_key = (alias.get("source_system", ""), alias.get("id", ""))
                if not all(alias_key):
                    errors.append(f"{label}: incomplete legacy alias")
                prior = alias_owners.get(alias_key)
                if prior and prior != template_id:
                    errors.append(
                        f"{label}: alias {alias_key} already maps to {prior}"
                    )
                alias_owners[alias_key] = template_id

            if status != "active":
                continue

            metrics["active_templates"] += 1
            active_template_ids.add(template_id)
            schema_path = safe_lace_path(
                item.get("schema_path", ""), f"{label}.schema_path", errors
            )
            template_path = safe_lace_path(
                item.get("template_path", ""), f"{label}.template_path", errors
            )
            profile_relative = item.get("profile_path")
            profile_path = (
                safe_lace_path(profile_relative, f"{label}.profile_path", errors)
                if profile_relative
                else None
            )
            if not schema_path or not template_path:
                continue
            schema = schemas.get(schema_path.resolve())
            if not schema:
                errors.append(f"{label}: schema is not a valid registered schema")
                continue

            if profile_path:
                profile = load_yaml(profile_path, errors)
                if profile is not None:
                    validate_instance(profile, schema, str(profile_path.relative_to(ROOT)), errors)
                    metrics["build_kits"] += 1
                    if profile.get("template_id") != template_id:
                        errors.append(f"{label}: profile template ID mismatch")
                    if profile.get("template_version") != item.get("version"):
                        errors.append(f"{label}: profile version mismatch")
                metadata = front_matter(template_path, errors)
            else:
                record = load_yaml(template_path, errors)
                if record is not None:
                    validate_instance(record, schema, str(template_path.relative_to(ROOT)), errors)
                    if record.get("template_id") != template_id:
                        errors.append(f"{label}: record template ID mismatch")
                    if record.get("template_version") != item.get("version"):
                        errors.append(f"{label}: record template version mismatch")
                metadata = None

            if metadata is not None:
                if metadata.get("template_id") != template_id:
                    errors.append(f"{label}: content template ID mismatch")
                if metadata.get("template_version") != item.get("version"):
                    errors.append(f"{label}: content template version mismatch")

    rules_schema_path = (LACE / "schemas" / "decision-rules.schema.json").resolve()
    rules = load_yaml(DECISION_RULES, errors)
    if isinstance(rules, dict) and rules_schema_path in schemas:
        validate_instance(
            rules,
            schemas[rules_schema_path],
            str(DECISION_RULES.relative_to(ROOT)),
            errors,
        )

        rule_ids: set[str] = set()
        allowed_fields = set(rules["input_contract"]["required"]) | DERIVED_DECISION_FIELDS
        rule_sections = (
            "blockers",
            "route_rules",
            "primary_asset_rules",
            "companion_rules",
            "warnings",
            "confidence_rules",
            "human_review_rules",
        )
        for section in rule_sections:
            for rule in rules[section]:
                rule_id = rule["id"]
                if rule_id in rule_ids:
                    errors.append(f"decision-rules.yaml: duplicate rule ID {rule_id}")
                rule_ids.add(rule_id)
                for condition in rule.get("when", []):
                    if condition["field"] not in allowed_fields:
                        errors.append(
                            f"{rule_id}: unknown condition field {condition['field']}"
                        )
                    if condition["operator"] not in ALLOWED_OPERATORS:
                        errors.append(
                            f"{rule_id}: unsupported operator {condition['operator']}"
                        )
                recommendation = rule.get("recommendation")
                if recommendation:
                    referenced_id = recommendation.get("template_id")
                    if referenced_id and referenced_id not in active_template_ids:
                        errors.append(
                            f"{rule_id}: references inactive or unknown template {referenced_id}"
                        )

        metrics["decision_rules"] = len(rule_ids)
        tests = load_yaml(DECISION_TESTS, errors)
        if isinstance(tests, dict):
            defaults = tests.get("defaults", {})
            cases = tests.get("cases", [])
            metrics["decision_cases"] = len(cases)
            for case in cases:
                inputs = dict(defaults)
                inputs.update(case.get("inputs", {}))
                try:
                    actual = evaluate_decision(inputs, rules)
                except Exception as exc:
                    errors.append(f"{case.get('id')}: evaluation error: {exc}")
                    continue
                for key, expected in case.get("expected", {}).items():
                    if actual.get(key) != expected:
                        errors.append(
                            f"{case.get('id')}: expected {key}={expected!r}, "
                            f"got {actual.get(key)!r}"
                        )

    asset_schema_path = (LACE / "schemas" / "asset-build-specification.schema.json").resolve()
    asset_template_path = LACE / "records" / "lace-tmp-005-asset-build-specification.yaml"
    if asset_schema_path in schemas and asset_template_path.exists():
        invalid_asset = load_yaml(asset_template_path, errors)
        if isinstance(invalid_asset, dict):
            invalid_asset = deepcopy(invalid_asset)
            invalid_asset["readiness_status"] = "build-ready"
            gate_errors: list[str] = []
            validate_instance(
                invalid_asset,
                schemas[asset_schema_path],
                "negative-build-ready-test",
                gate_errors,
            )
            if not gate_errors:
                errors.append("asset schema accepted build-ready with unresolved items")

    release_schema_path = (LACE / "schemas" / "release-manifest.schema.json").resolve()
    release_template_path = LACE / "records" / "lace-tmp-008-release-manifest.yaml"
    if release_schema_path in schemas and release_template_path.exists():
        invalid_release = load_yaml(release_template_path, errors)
        if isinstance(invalid_release, dict):
            invalid_release = deepcopy(invalid_release)
            invalid_release["readiness_status"] = "release-ready"
            gate_errors: list[str] = []
            validate_instance(
                invalid_release,
                schemas[release_schema_path],
                "negative-release-ready-test",
                gate_errors,
            )
            if not gate_errors:
                errors.append("release schema accepted release-ready with failed gates")

    metrics["local_links"] = validate_internal_links(errors)

    if errors:
        print("LACE validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(
        "LACE validation passed: "
        f"{metrics['schemas']} schemas, "
        f"{metrics['templates']} templates "
        f"({metrics['active_templates']} active), "
        f"{metrics['decision_rules']} decision rules, "
        f"{metrics['decision_cases']} decision cases, "
        f"{metrics['build_kits']} build kits, "
        f"{metrics['local_links']} local links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
