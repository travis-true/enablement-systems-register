# SYS-001 — LACE Learning Asset Creation Engine

**Version:** 1.0.0  
**Status:** Complete  
**Owner:** Travis True  
**Classification:** Public-safe  
**Canonical effective date:** 2026-09-02

LACE is the governed production system that converts approved source material and learning-design decisions into consistent, accessible, traceable, build-ready learning and performance-support assets.

## Canonical package

- [Canonical specification](specification.md)
- [Source consolidation crosswalk](source-crosswalk.md)
- [Template-ID namespace](template-namespace.md)
- [Canonical template register](template-register.yaml)
- [Control-record operating sequence](control-records.md)
- [JSON Schemas](schemas/)
- [Reusable YAML records](records/)
- [Asset decision rules](decision-engine/decision-rules.yaml)
- [Decision-engine operating guide](decision-engine/operating-guide.md)
- [Decision-engine test cases](decision-engine/test-cases.yaml)
- [Completion evidence](../../evidence/sys-001-completion.md)

## System boundary

LACE begins when a learning or performance need and its governing sources are available for analysis. It ends when the resulting asset package passes its required quality gates and is approved for release or returned with documented constraints.

LACE does not replace portfolio governance, request prioritization, publishing authority, LMS administration, organizational policy, or channel ownership.

## Relationship to registered systems

- **FW-002 — L&D Operating System:** governs the broader lifecycle in which LACE operates.
- **WF-002 — Governed Training Asset Publication:** controls final verification, approval, publication, and measurement.
- **WF-003 — Reuse Before Restarting:** supplies reusable approved material before new production begins.
- **PB-001 — Employee Training Reference Production:** applies LACE to detailed employee reference assets.

## Authority model

This specification consolidates three predecessor bodies of work:

1. **Learning Document Creation System (LDCS):** detailed intake, source analysis, decision logic, blueprints, writing, design, QA, testing, and runtime assembly.
2. **TAB Studio:** production and visual-system direction, with TAB Core retaining authority for governance, source rules, release rules, asset families, screenshots, icons, package QA, and regression controls.
3. **L&D Operating System Phase 5:** approved asset architecture, production specifications, entry gates, handoff requirements, acceptance criteria, and production-readiness statuses.

Where predecessor material conflicts, the authority order in the canonical specification applies.
