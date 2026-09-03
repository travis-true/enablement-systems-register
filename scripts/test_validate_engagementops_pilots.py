#!/usr/bin/env python3
"""Regression tests for SYS-003 pilot packages."""

import importlib.util
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_engagementops_pilots", ROOT / "scripts/validate_engagementops_pilots.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
PILOT = ROOT / "systems/sys-003-engagementops/pilots/engagementops-pilot-001"


def record(path):
    return yaml.safe_load((PILOT / path).read_text(encoding="utf-8"))


class EngagementOpsPilotTests(unittest.TestCase):
    def test_current_pilot_passes(self):
        self.assertEqual([], MODULE.validate_all())

    def test_material_handoff_gap_fails(self):
        data = record("records/handoff.yaml")
        data["disposition"]["material_gaps"] = ["Missing authority"]
        errors = MODULE.validate_all(pilot_overrides={"engagementops-pilot-001": {"records/handoff.yaml": data}})
        self.assertTrue(any("material gaps" in item for item in errors))

    def test_unapproved_campaign_fails(self):
        data = record("records/campaign.yaml")
        data["governance"]["human_approval"] = False
        errors = MODULE.validate_all(pilot_overrides={"engagementops-pilot-001": {"records/campaign.yaml": data}})
        self.assertTrue(any("approved and active" in item for item in errors))

    def test_unapproved_asset_fails(self):
        data = record("records/asset-faq.yaml")
        data["governance"]["approved"] = False
        errors = MODULE.validate_all(pilot_overrides={"engagementops-pilot-001": {"records/asset-faq.yaml": data}})
        self.assertTrue(any("asset must be approved" in item for item in errors))

    def test_open_critical_defect_fails(self):
        data = record("records/readiness.yaml")
        data["defects"]["critical"] = 1
        errors = MODULE.validate_all(pilot_overrides={"engagementops-pilot-001": {"records/readiness.yaml": data}})
        self.assertTrue(any("open Blocker, Critical, or Major" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
