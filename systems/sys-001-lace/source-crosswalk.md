# LACE source consolidation crosswalk

This crosswalk records how predecessor material was consolidated into SYS-001 without treating every predecessor rule as equally authoritative.

## Authority order

1. Applicable law, policy, security, privacy, and accessibility requirements
2. Approved L&D Operating System governance and upstream decisions
3. TAB Core governance, source, release, family, screenshot, icon, package-QA, and regression rules
4. Approved Phase 5 asset architecture, production specification, entry, handoff, and readiness rules
5. LDCS/TAB Studio production detail
6. Approved asset-specific template and implementation guidance
7. Examples and historical practice

A lower source cannot silently override a higher source.

## Consolidation map

| LACE v1.0 capability | LDCS contribution | TAB Studio/TAB Core contribution | Phase 5 contribution | Canonical decision |
|---|---|---|---|---|
| Intake and diagnosis | Intake, audience, task, workflow, risk, and environment analysis | Governance and source-authority controls | Approved upstream blueprint and entry conditions | Combined as Stage 1 with an explicit entry gate |
| Source intelligence | Extraction, mapping, conflict handling, SME validation | Authoritative source and release rules | Source/evidence completeness and pause conditions | Combined as Stage 2 and the source/evidence rules |
| Asset decision | Decision engine and 16 blueprints | Authoritative 17-family architecture | Six production-facing asset families | Six high-level families govern; detailed blueprints operate beneath them |
| Writing system | Plain language, procedures, cognitive load | Package-level quality controls | Content acceptance criteria | Consolidated into mandatory writing standards |
| Visual system | Tokens, grids, typography, color, spacing, components, composition, overflow, export | Screenshot, icon, visual QA, and regression authority | Accessibility and production requirements | Consolidated with TAB authority and LDCS implementation detail |
| Production specification | Blueprint and content-plan detail | Governed family and component rules | Standard build-specification schema | Phase 5 schema governs the minimum required specification |
| Runtime workflow | Assemble, build, render, inspect, repair, regenerate | Release and regression controls | Production handoff and readiness statuses | Consolidated into seven stages |
| Quality assurance | Master QA, testing, gold standards | Package QA and broad release authority | Acceptance criteria and handoff gate | Visual gate set at 95/100 with no Critical or Major defect |
| Release and maintenance | Lifecycle and version control | Release authority | Approval, change, and maintenance records | LACE prepares the package; publication remains downstream |
| Automation | Runtime assembly and repair concepts | Planned production/regression direction | Manual controlled baseline | Automation permitted within explicit human decision boundaries |

## Predecessor identifier handling

Historical LACE asset drafts used identifiers including:

- `TMP-0002` — Job Aid, Task-Based, with QRG-style tables
- `TMP-0003` — QRG, Compact

The L&D Operating System implementation toolkit separately used:

- `TMP-001` — Applicability Assessment
- `TMP-002` — Entry Gate Record
- `TMP-007` — Asset Build Specification
- `TMP-009` — Workflow and Handoff Record
- `PIL-003` — Controlled Evidence Index

These are treated as predecessor identifiers, not interchangeable canonical IDs. LACE v1.0 requires a future controlled template-register crosswalk before automation relies on template IDs.

## Historical evidence of use

The heading “LACE governance notes” appeared in July 2026 drafts including:

- Finding Files
- Finding Meetings
- Drafting Documents
- Search Quick Reference Guide
- Search Deep Dive

Those notes applied asset-type selection, task-focused screenshot planning, accessibility requirements, review controls, link and interface validation, and sensitivity-label checks.

## Decisions preserved

- TAB remains authoritative for governance and release controls.
- LDCS supplies detailed production and visual intelligence.
- LDCS blueprints do not replace the governed asset-family architecture.
- Phase 5 governs production specifications and build readiness.
- EngagementOps remains an optional downstream or companion capability.
- Final publication authority stays outside LACE.
- Public versions must exclude confidential organizational details.

## Deferred implementation work

The following items are implementation improvements, not blockers to the canonical specification:

- canonical template register and predecessor-ID mapping;
- editable presentation and document master families;
- governed vector component library;
- machine-readable generation schemas;
- automated rendering and visual regression;
- lightweight internal asset-generator interface;
- measured production pilot using the consolidated specification.
