# LACE automated validation

The repository runs LACE validation on every pull request and every push to `main`.

## Required command

```bash
python scripts/validate_lace.py
```

Install the runtime dependencies before local execution:

```bash
python -m pip install PyYAML jsonschema
```

## Blocking checks

The validator fails when it finds:

- invalid JSON or YAML;
- an invalid JSON Schema;
- missing critical LACE package files;
- malformed, duplicate, out-of-range, or improperly reused template IDs;
- incomplete or conflicting legacy aliases;
- an active template with missing schema, profile, or template files;
- template ID or version disagreement;
- a reusable record or build-kit profile that violates its schema;
- duplicate decision-rule IDs;
- unknown decision fields or operators;
- decision rules referencing inactive or unknown templates;
- controlled decision-test mismatches;
- a build-ready state with unresolved items;
- a release-ready state with failed gates or remaining Critical/Major defects;
- broken or repository-escaping local Markdown links.

## Validation boundary

Automated validation proves structural and rule integrity. It does not independently prove source accuracy, instructional effectiveness, visual quality, accessibility of a rendered artifact, approval, or successful publication. Those require the recorded human and artifact-level gates defined by LACE.
