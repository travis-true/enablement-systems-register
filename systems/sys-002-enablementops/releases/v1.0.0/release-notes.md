# EnablementOps v1.0.0 release notes

**Release date:** 2026-09-03  
**System:** SYS-002 — EnablementOps  
**Release type:** First governed production release

## Release basis

Steps 1–6 established the consolidated operating-system boundary, production standards, controlled template families, approved golden examples, cross-format quality gates, structured automation, and a three-path end-to-end pilot regression.

## Included capabilities

- Governed intake-to-lifecycle EnablementOps operating model.
- Seventeen controlled asset families and 33 variants.
- Production-tool profiles and uncovered-family fallback.
- Approved Golden controls and reference examples.
- Twelve-stage QA sequence and eight controlled format groups.
- JSON Schemas, semantic validation, negative tests, and continuous integration.
- End-to-end pilot records for QRG, detailed-guide, and multimedia paths.
- Explicit boundary between EnablementOps and optional EngagementOps activation.

## Release decision

SYS-002 v1.0.0 is authorized and published as the current governed EnablementOps release. The EO-PILOT-001 asset candidates remain blocked from publication because their separate release authorization was not verified.

## Compatibility and rollback

Canonical IDs remain unchanged. The v0.11.0 pre-release baseline remains recoverable through Git history. Roll back by reverting the v1.0.0 release changes; never reuse or renumber governed IDs.
