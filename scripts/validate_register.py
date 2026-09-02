#!/usr/bin/env python3
"""Validate register structure, references, and completion rules."""

from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required: python -m pip install PyYAML", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "register.yaml"
ID_RE = re.compile(r"^(SYS|FW|WF|PB)-\d{3}$")
VALID_CATEGORIES = {"system", "framework", "workflow", "playbook"}
VALID_STATUSES = {"candidate", "incomplete", "in_progress", "complete", "maintenance", "retired"}
REQUIRED = {
    "id", "name", "category", "status", "owner", "purpose", "audience", "scope",
    "completion_score", "related_systems", "artifacts", "evidence", "next_action",
    "version", "last_reviewed", "next_review", "labels",
}


def main() -> int:
    data = yaml.safe_load(REGISTER.read_text(encoding="utf-8"))
    systems = data.get("systems", [])
    errors = []
    ids = [item.get("id") for item in systems]

    if len(ids) != len(set(ids)):
        errors.append("System IDs must be unique.")

    known = set(ids)
    for index, item in enumerate(systems, start=1):
        sid = item.get("id", f"entry {index}")
        missing = REQUIRED - set(item)
        if missing:
            errors.append(f"{sid}: missing fields: {', '.join(sorted(missing))}")
        if not ID_RE.fullmatch(str(item.get("id", ""))):
            errors.append(f"{sid}: invalid ID format")
        if item.get("category") not in VALID_CATEGORIES:
            errors.append(f"{sid}: invalid category")
        if item.get("status") not in VALID_STATUSES:
            errors.append(f"{sid}: invalid status")
        score = item.get("completion_score")
        if not isinstance(score, int) or not 0 <= score <= 100:
            errors.append(f"{sid}: completion_score must be an integer from 0 to 100")
        if item.get("status") in {"complete", "maintenance"}:
            if score is None or score < 80:
                errors.append(f"{sid}: complete systems require a score of at least 80")
            if not item.get("evidence"):
                errors.append(f"{sid}: complete systems require evidence")
        for related in item.get("related_systems", []):
            if related not in known:
                errors.append(f"{sid}: unknown related system {related}")
        for artifact in item.get("artifacts", []):
            if artifact.startswith("http"):
                continue
            if not (ROOT / artifact).exists():
                errors.append(f"{sid}: artifact does not exist: {artifact}")
        for evidence in item.get("evidence", []):
            if evidence.startswith("http"):
                continue
            if not (ROOT / evidence).exists():
                errors.append(f"{sid}: evidence does not exist: {evidence}")

    if errors:
        print("Register validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Register validation passed: {len(systems)} systems.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
