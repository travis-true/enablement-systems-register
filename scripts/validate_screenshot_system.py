#!/usr/bin/env python3
from pathlib import Path
import json
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "systems/sys-004-screenshot-sanitization-annotation"
REQUIRED = [
    "README.md", "governance-and-lifecycle-standard.md",
    "privacy-and-replacement-standard.md", "annotation-and-accessibility-standard.md",
    "quality-assurance-standard.md", "templates/screenshot-specification.md",
    "schemas/screenshot-record.schema.json", "records/example-screenshot.yaml",
    "pilots/screenshot-pilot-001/manifest.yaml",
    "pilots/screenshot-pilot-001/qa-evidence.md",
    "releases/v1.0.0/release-manifest.yaml",
    "releases/v1.0.0/approval.md", "releases/v1.0.0/release-notes.md",
]
def validate():
    errors = [f"missing: {p}" for p in REQUIRED if not (BASE / p).is_file()]
    if errors:
        return errors
    schema = json.loads((BASE / "schemas/screenshot-record.schema.json").read_text())
    record = yaml.safe_load((BASE / "records/example-screenshot.yaml").read_text())
    if record.get("system_id") != "SYS-004": errors.append("record system_id must be SYS-004")
    if record.get("status") != "released": errors.append("example must be released")
    if record.get("privacy", {}).get("review_status") != "pass": errors.append("privacy must pass")
    if record.get("qa", {}).get("decision") != "pass": errors.append("QA must pass")
    for level in ("open_blocker", "open_critical", "open_major"):
        if record.get("qa", {}).get(level) != 0: errors.append(f"{level} must be zero")
    if not schema.get("$schema", "").endswith("2020-12/schema"): errors.append("schema draft mismatch")
    for key in ("source", "master", "final"):
        if key not in record.get("files", {}): errors.append(f"missing file state: {key}")
    return errors
if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(problems)); sys.exit(1)
    print("SYS-004 validation passed")
