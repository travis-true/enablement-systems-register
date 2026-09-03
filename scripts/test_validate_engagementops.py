#!/usr/bin/env python3
"""Regression tests for SYS-003 structured campaign controls."""

import importlib.util
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_engagementops", ROOT / "scripts/validate_engagementops.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
SYSTEM = ROOT / "systems/sys-003-engagementops"


def record(path):
    return yaml.safe_load((SYSTEM / path).read_text(encoding="utf-8"))


class EngagementOpsValidationTests(unittest.TestCase):
    def test_current_records_pass(self):
        self.assertEqual([], MODULE.validate_documents())

    def test_duplicate_channel_id_fails(self):
        data = record("channel-profile-catalog.yaml")
        data["channels"][1]["id"] = data["channels"][0]["id"]
        errors = MODULE.validate_documents(overrides={"channel-profile-catalog.yaml": data})
        self.assertTrue(any("channel IDs must be unique" in item for item in errors))

    def test_unknown_campaign_channel_fails(self):
        data = record("records/example-campaign.yaml")
        data["strategy"]["channel_ids"][0] = "EO-CH-999"
        errors = MODULE.validate_documents(overrides={"records/example-campaign.yaml": data})
        self.assertTrue(any("unknown channels" in item for item in errors))

    def test_unapproved_active_campaign_fails(self):
        data = record("records/example-campaign.yaml")
        data["record"]["status"] = "active"
        errors = MODULE.validate_documents(overrides={"records/example-campaign.yaml": data})
        self.assertTrue(any("human approval" in item for item in errors))

    def test_risk_without_specialist_review_fails(self):
        data = record("records/example-campaign.yaml")
        data["strategy"]["risk_tier"] = "R2"
        errors = MODULE.validate_documents(overrides={"records/example-campaign.yaml": data})
        self.assertTrue(any("specialist reviews" in item for item in errors))

    def test_f3_without_reviews_fails(self):
        data = record("records/example-asset-specification.yaml")
        data["governance"]["fidelity"] = "F3"
        errors = MODULE.validate_documents(overrides={"records/example-asset-specification.yaml": data})
        self.assertTrue(any("SME review" in item or "specialist review" in item for item in errors))

    def test_unapproved_active_asset_fails(self):
        data = record("records/example-asset-specification.yaml")
        data["record"]["status"] = "active"
        errors = MODULE.validate_documents(overrides={"records/example-asset-specification.yaml": data})
        self.assertTrue(any("recorded approval" in item for item in errors))


    def test_unknown_measure_fails(self):
        data = record("records/example-measurement-plan.yaml")
        data["measures"][0]["measure_id"] = "EO-MET-999"
        errors = MODULE.validate_documents(overrides={"records/example-measurement-plan.yaml": data})
        self.assertTrue(any("unknown metrics" in item for item in errors))

    def test_available_baseline_without_value_fails(self):
        data = record("records/example-measurement-plan.yaml")
        data["baseline"]["status"] = "available"
        data["baseline"]["source"] = "approved source"
        errors = MODULE.validate_documents(overrides={"records/example-measurement-plan.yaml": data})
        self.assertTrue(any("baseline requires" in item for item in errors))

    def test_unapproved_active_measurement_plan_fails(self):
        data = record("records/example-measurement-plan.yaml")
        data["record"]["status"] = "active"
        errors = MODULE.validate_documents(overrides={"records/example-measurement-plan.yaml": data})
        self.assertTrue(any("measurement plan requires recorded approval" in item for item in errors))

    def test_decision_without_owner_fails(self):
        data = record("records/example-measurement-plan.yaml")
        data["decision"]["outcome"] = "continue"
        data["decision"]["decided_on"] = "2026-10-31"
        errors = MODULE.validate_documents(overrides={"records/example-measurement-plan.yaml": data})
        self.assertTrue(any("decision requires date and decision owner" in item for item in errors))


    def test_required_localization_without_targets_fails(self):
        data = record("records/example-localization-profile.yaml")
        data["locales"]["required"] = True
        errors = MODULE.validate_documents(overrides={"records/example-localization-profile.yaml": data})
        self.assertTrue(any("target locales" in item for item in errors))

    def test_f3_localization_without_specialist_fails(self):
        data = record("records/example-localization-profile.yaml")
        data["fidelity"]["level"] = "F3"
        errors = MODULE.validate_documents(overrides={"records/example-localization-profile.yaml": data})
        self.assertTrue(any("F3 localization requires specialist" in item for item in errors))

    def test_screenshot_without_redaction_review_fails(self):
        data = record("records/example-delivery-readiness.yaml")
        data["screenshots"]["present"] = True
        data["screenshots"]["redaction_review"] = "not-run"
        errors = MODULE.validate_documents(overrides={"records/example-delivery-readiness.yaml": data})
        self.assertTrue(any("passing redaction review" in item for item in errors))

    def test_post_approval_change_without_regression_fails(self):
        data = record("records/example-delivery-readiness.yaml")
        data["change_control"]["post_approval_change"] = True
        data["change_control"]["p0_regression"] = "pass"
        data["change_control"]["p1_regression"] = "not-run"
        errors = MODULE.validate_documents(overrides={"records/example-delivery-readiness.yaml": data})
        self.assertTrue(any("P0/P1 regression" in item for item in errors))

    def test_release_without_human_approval_fails(self):
        data = record("records/example-delivery-readiness.yaml")
        data["release"]["decision"] = "released"
        errors = MODULE.validate_documents(overrides={"records/example-delivery-readiness.yaml": data})
        self.assertTrue(any("P0 gate" in item or "human approval" in item for item in errors))


    def test_accepted_handoff_with_material_gap_fails(self):
        data = record("records/example-activation-handoff.yaml")
        data["disposition"]["material_gaps"] = ["Missing approval authority"]
        errors = MODULE.validate_documents(overrides={"records/example-activation-handoff.yaml": data})
        self.assertTrue(any("material gaps" in item for item in errors))

    def test_registry_status_mismatch_fails(self):
        data = record("campaign-registry.yaml")
        data["campaigns"][0]["status"] = "active"
        errors = MODULE.validate_documents(overrides={"campaign-registry.yaml": data})
        self.assertTrue(any("version/status" in item for item in errors))

    def test_calendar_unknown_touchpoint_fails(self):
        data = record("campaign-calendar.yaml")
        data["events"][0]["touchpoint_id"] = "EO-TP-999"
        errors = MODULE.validate_documents(overrides={"campaign-calendar.yaml": data})
        self.assertTrue(any("unknown touchpoint" in item for item in errors))

    def test_calendar_date_mismatch_fails(self):
        data = record("campaign-calendar.yaml")
        data["events"][0]["scheduled_at"] = "2026-10-02T15:00:00Z"
        errors = MODULE.validate_documents(overrides={"campaign-calendar.yaml": data})
        self.assertTrue(any("calendar date" in item for item in errors))

    def test_collision_review_without_evidence_fails(self):
        data = record("campaign-calendar.yaml")
        data["events"][0]["collision_status"] = "review-required"
        data["events"][0]["collision_evidence"] = []
        errors = MODULE.validate_documents(overrides={"campaign-calendar.yaml": data})
        self.assertTrue(any("collision status requires evidence" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
