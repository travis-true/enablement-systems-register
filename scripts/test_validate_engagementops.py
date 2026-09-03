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


if __name__ == "__main__":
    unittest.main()
