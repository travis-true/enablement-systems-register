# LACE control records

These eight records are the minimum control set for moving work through LACE. Each YAML template has a standalone JSON Schema with the same required data contract.

| Order | Template | Record | Required use |
|---:|---|---|---|
| 1 | LACE-TMP-001 | Applicability Assessment | Determine whether a learning asset is an appropriate response |
| 2 | LACE-TMP-003 | Request and Intake Record | Capture the need, outcome, audience, task, risk, constraints, and sources |
| 3 | LACE-TMP-002 | Entry Gate Record | Authorize work to enter production or stop it |
| 4 | LACE-TMP-004 | Controlled Evidence Index | Establish source authority, permitted use, claims, and limitations |
| 5 | LACE-TMP-009 | Asset Decision Record | Preserve the governed route, primary asset, companions, warnings, confidence, and approval |
| 6 | LACE-TMP-005 | Asset Build Specification | Define the production contract and acceptance criteria |
| 7 | LACE-TMP-006 | Workflow and Handoff Record | Transfer controlled work between stages and owners |
| 8 | LACE-TMP-008 | Release Manifest | Prove package completeness and readiness for publication handoff |
| 9 | LACE-TMP-007 | Lifecycle Review Record | Retain, revise, replace, retire, or escalate a released asset |

## Use rules

1. Copy the YAML template; never overwrite the canonical template.
2. Replace all instructional placeholder values.
3. Preserve `template_id`, `template_version`, and `system_id`.
4. Assign a unique record ID under the operating environment’s governed record-ID standard.
5. Validate the completed record against its paired JSON Schema.
6. Resolve every schema error before approval.
7. Do not mark a record `approved` without the named owner or decision authority.
8. Preserve superseded records and their relationship to the replacement.
9. A release manifest cannot be `release-ready` when Critical or Major defects remain.
10. Publication occurs through the downstream publication workflow, not through LACE itself.

## Readiness boundary

Validated structure does not prove factual accuracy, accessibility, approval, or release readiness. Those decisions remain governed by the source, quality, accessibility, and approval controls in the LACE specification.
