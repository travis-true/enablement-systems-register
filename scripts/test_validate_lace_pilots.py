from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

import yaml

from scripts.validate_lace_pilots import validate_pilot_records


SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["template_id", "template_version", "record_id", "system_id", "value"],
    "properties": {
        "template_id": {"const": "LACE-TMP-001"},
        "template_version": {"const": "1.0.0"},
        "record_id": {"type": "string", "minLength": 1},
        "system_id": {"const": "SYS-001"},
        "value": {"type": "string", "minLength": 1},
    },
}


class PilotRecordValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.lace = Path(self.temp.name) / "sys-001-lace"
        (self.lace / "schemas").mkdir(parents=True)
        self.records = self.lace / "pilots" / "lace-pilot-001" / "records"
        self.records.mkdir(parents=True)
        (self.lace / "schemas" / "record.schema.json").write_text(
            json.dumps(SCHEMA), encoding="utf-8"
        )
        register = {
            "templates": [{
                "id": "LACE-TMP-001",
                "version": "1.0.0",
                "status": "active",
                "schema_path": "schemas/record.schema.json",
            }]
        }
        (self.lace / "template-register.yaml").write_text(
            yaml.safe_dump(register), encoding="utf-8"
        )
        for name, record_id in (
            ("record.yaml", "REC-001"),
            ("build.yaml", "REC-002"),
            ("handoff.yaml", "REC-003"),
            ("release.yaml", "REC-004"),
            ("lifecycle.yaml", "REC-005"),
        ):
            self.write_record(name=name, record_id=record_id)
        self.write_index()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_record(self, name: str = "record.yaml", **changes: object) -> None:
        record = {
            "template_id": "LACE-TMP-001",
            "template_version": "1.0.0",
            "record_id": "REC-001",
            "system_id": "SYS-001",
            "value": "valid",
        }
        record.update(changes)
        (self.records / name).write_text(
            yaml.safe_dump(record), encoding="utf-8"
        )

    def write_index(self, shared: list[str] | None = None) -> None:
        index = {
            "pilot_id": "LACE-PILOT-001",
            "system_id": "SYS-001",
            "shared_records": shared if shared is not None else ["record.yaml"],
            "asset_records": {"asset": {
                "build_specification": "build.yaml",
                "handoff": "handoff.yaml",
                "release_manifest": "release.yaml",
            }},
            "lifecycle_review": "lifecycle.yaml",
        }
        (self.records / "record-index.yaml").write_text(
            yaml.safe_dump(index), encoding="utf-8"
        )

    def validate(self) -> list[str]:
        errors: list[str] = []
        validate_pilot_records(self.lace, errors)
        return errors

    def test_valid_record_is_discovered_and_validated(self) -> None:
        self.assertEqual([], self.validate())

    def test_schema_violation_fails(self) -> None:
        self.write_record(value="")
        self.assertTrue(any("minLength" in error or "non-empty" in error for error in self.validate()))

    def test_unknown_template_fails(self) -> None:
        self.write_record(template_id="LACE-TMP-999")
        self.assertTrue(any("unknown or inactive template_id" in error for error in self.validate()))

    def test_unindexed_record_fails(self) -> None:
        self.write_record(name="orphan.yaml", record_id="REC-006")
        self.assertTrue(any("governed record is not indexed" in error for error in self.validate()))

    def test_missing_index_fails(self) -> None:
        (self.records / "record-index.yaml").unlink()
        self.assertTrue(any("missing record-index.yaml" in error for error in self.validate()))


if __name__ == "__main__":
    unittest.main()
