#!/usr/bin/env python3
"""Regression tests for the SYS-002 validator."""

from copy import deepcopy
import importlib.util
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_enablementops", ROOT / "scripts/validate_enablementops.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
SYSTEM = ROOT / "systems/sys-002-enablementops"


def record(name):
    return yaml.safe_load((SYSTEM / name).read_text(encoding="utf-8"))


class EnablementOpsValidationTests(unittest.TestCase):
    def test_current_records_and_pilot_pass(self):
        self.assertEqual([], MODULE.validate_documents())

    def test_family_count_mismatch_fails(self):
        data = record("template-family-catalog.yaml")
        data["catalog"]["family_count"] = 16
        errors = MODULE.validate_documents(overrides={"template-family-catalog.yaml": data})
        self.assertTrue(any("family_count" in item for item in errors))

    def test_unknown_golden_family_fails(self):
        data = record("golden-example-register.yaml")
        data["approved_goldens"][0]["family_id"] = "F99"
        errors = MODULE.validate_documents(overrides={"golden-example-register.yaml": data})
        self.assertTrue(any("does not match" in item or "unknown family" in item for item in errors))

    def test_visual_threshold_regression_fails(self):
        data = record("qa-test-matrix.yaml")
        data["matrix"]["visual_score_minimum"] = 90
        errors = MODULE.validate_documents(overrides={"qa-test-matrix.yaml": data})
        self.assertTrue(any("minimum of 95" in item or "below 95" in item for item in errors))

    def test_unapproved_release_fails(self):
        data = record("records/enablementops-production-record.yaml")
        data["record"]["status"] = "released"
        data["release"]["decision"] = "released"
        errors = MODULE.validate_documents(overrides={"records/enablementops-production-record.yaml": data})
        self.assertTrue(any("released production record" in item for item in errors))

    def test_pilot_unknown_family_fails(self):
        path = "pilots/enablementops-pilot-001/records/eo-pr-002-qrg.yaml"
        data = record(path)
        data["need"]["primary_family_id"] = "F99"
        errors = MODULE.validate_documents(overrides={path: data})
        self.assertTrue(any("does not match" in item or "unknown primary family" in item for item in errors))

    def test_pilot_duplicate_record_id_fails(self):
        path = "pilots/enablementops-pilot-001/records/eo-pr-003-detailed-guide.yaml"
        data = record(path)
        data["record"]["id"] = "EO-PR-002"
        errors = MODULE.validate_documents(overrides={path: data})
        self.assertTrue(any("IDs must be unique" in item for item in errors))

    def test_release_status_decision_mismatch_fails(self):
        path = "pilots/enablementops-pilot-001/records/eo-pr-004-multimedia.yaml"
        data = record(path)
        data["record"]["status"] = "released"
        errors = MODULE.validate_documents(overrides={path: data})
        self.assertTrue(any("released status requires" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
