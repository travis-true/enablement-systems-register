# EnablementOps automation and schema guide

## Implemented capability

SYS-002 uses structured YAML records, JSON Schema validation, semantic cross-reference checks, negative regression tests, and continuous integration.

The automated gate validates:

- the 17-family and 33-variant catalog;
- family IDs, counts, roles, formats, and authority mappings;
- Approved Golden metadata, QA thresholds, unique IDs, layout coverage, and family references;
- QA formats, thresholds, mandatory scenarios, and release requirements;
- structured production-record fields and family references;
- release semantics that prevent approval below quality thresholds, with unresolved blocking defects, without regression, without evidence, or without human approval.

## Commands

```bash
python scripts/validate_enablementops.py
python -m unittest -v scripts/test_validate_enablementops.py
```

Both commands run in continuous integration on pull requests and pushes to the default branch.

## Automation boundary

- Level 2 template-guided production is supported.
- Level 2.5 structured intake and validation is implemented for SYS-002 records.
- Level 3 generation remains delegated to an approved LACE build kit or generator.
- No generated output may bypass human review, visual inspection, accessibility review, regression, or release authorization.
- A browser interface is not required for the governed automation layer and must not precede stable schemas and validation.

## Change control

Any schema change requires:

1. a version increment;
2. compatibility and migration impact review;
3. updated valid sample records;
4. positive and negative tests;
5. CI pass;
6. review of affected Goldens, templates, build kits, and documentation;
7. authorized approval.
