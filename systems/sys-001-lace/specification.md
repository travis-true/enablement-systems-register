# LACE v1.0 canonical specification

## 1. Purpose

The Learning Asset Creation Engine (LACE) is a reusable operating system for transforming approved knowledge, evidence, and learning-design decisions into consistent, accessible, traceable, and production-ready learning assets.

LACE provides the decision logic, production standards, quality controls, and handoffs needed to create an asset. It is format-neutral and can support documentation, performance support, facilitated learning, self-paced learning, multimedia, communications, and evaluation assets.

## 2. Outcomes

LACE must:

- select an asset appropriate to the performance need and use context;
- preserve source authority and expose uncertainty;
- produce build-ready content and visual specifications;
- apply plain-language, accessibility, technical, and production standards;
- maintain traceability from source through release;
- identify constraints, exceptions, and unresolved decisions;
- generate editable, distribution, evidence, and maintenance records;
- prevent release until applicable quality gates are satisfied.

## 3. Scope

### Included

- intake and production diagnosis;
- source extraction, authority mapping, and conflict handling;
- audience, task, workflow, environment, risk, and moment-of-need analysis;
- reuse assessment and asset-selection logic;
- asset-family and blueprint selection;
- content planning and atomization;
- writing and visual-production standards;
- screenshots, annotations, icons, illustrations, and diagrams;
- accessibility and controlled-data checks;
- build specifications and production handoff;
- rendering, inspection, repair, testing, and quality assurance;
- approval, release-package preparation, versioning, and maintenance metadata.

### Excluded

- portfolio prioritization and funding decisions;
- organization-specific policy creation;
- invention of missing source facts;
- final publishing authority;
- LMS configuration and administration;
- channel administration;
- unapproved branding or confidential source material in public derivatives.

## 4. Entry conditions

Work may enter LACE when the following are available or explicitly identified as missing:

- defined request, performance need, or desired outcome;
- intended audience and use context;
- authoritative source material;
- source owner or approving authority;
- approved upstream recommendation or design blueprint when required;
- known delivery, platform, brand, accessibility, and security constraints.

LACE must pause when an unresolved issue could materially change scope, accuracy, accessibility, approval, risk, or output.

## 5. Roles and decision rights

| Role | Responsibility | Decision right |
|---|---|---|
| Request owner | Defines the business or performance need | Confirms intended outcome and scope |
| Source owner or SME | Validates authoritative content | Resolves factual gaps and conflicts |
| Learning strategist/designer | Diagnoses need and selects the intervention | Approves learning and asset approach |
| Asset developer | Builds the asset using LACE standards | Makes bounded production decisions |
| Accessibility reviewer | Verifies accessible structure and interaction | Blocks release for material barriers |
| Brand/visual reviewer | Verifies applicable visual standards | Approves or returns visual treatment |
| Quality reviewer | Runs content, technical, and package gates | Assigns defect severity and readiness |
| Approver | Accepts residual constraints and release package | Authorizes release |
| Publisher/channel owner | Publishes the approved package | Controls destination and deployment |
| System owner | Maintains LACE, templates, schemas, and versions | Approves governed system changes |

One person may hold multiple roles, but source validation and final approval must remain explicit.

## 6. Inputs

LACE can accept:

- policies, standards, procedures, and SOPs;
- knowledge-base and service-management content;
- process maps, workflows, task analyses, and release notes;
- existing learning assets and approved reusable components;
- SME interviews, notes, transcripts, screenshots, and recordings;
- platform and delivery requirements;
- learning-design blueprints;
- brand, accessibility, privacy, security, and publishing requirements;
- approved measurement and maintenance expectations.

## 7. Source and evidence rules

1. Prefer the most authoritative, current, and applicable source.
2. Record the source owner, version/date, use restrictions, and known limitations.
3. Separate verified facts, recommendations, assumptions, and missing information.
4. Never silently resolve a material source conflict.
5. Do not invent missing instructions, interface labels, policy, data, or results.
6. Use visible placeholders such as `[TBD]` only when the output can safely proceed.
7. Exclude unsupported and reference-only content from authoritative instructions.
8. Maintain claim-level or section-level traceability appropriate to the asset risk.
9. Revalidate volatile interface labels, screenshots, links, and deployment behavior before release.
10. Protect restricted information and create only sanitized public derivatives where required.

## 8. Asset architecture

LACE uses six asset families.

| Family | Typical assets |
|---|---|
| Performance support and documentation | Job aid, QRG, SOP, checklist, decision tree, knowledge article |
| Instructor-led and virtual learning | Facilitator guide, participant guide, workshop, demonstration |
| Self-paced digital learning | Microlearning, course, scenario, assessment |
| Video and multimedia | Tutorial, explainer, animation, storyboard, audio |
| Communications and adoption | Announcement, campaign, tip series, manager guide, reinforcement |
| Planning and evaluation | Learning plan, curriculum map, evaluation, measurement instrument |

The asset decision must consider desired performance, audience, task complexity and frequency, workflow position, operational risk, moment of need, environment, maintenance burden, delivery constraints, and source readiness.

Production must use an active registered format build kit when one matches the approved asset decision. LACE v1.1 development currently approves `LACE-TMP-100`, `LACE-TMP-101`, `LACE-TMP-102`, and `LACE-TMP-400`. An asset without an active kit requires a documented human-approved production plan and cannot borrow another template identity.

## 9. Standard asset specification

Every asset build specification must define:

- asset ID, title, family, type, version, owner, and status;
- purpose and measurable intended outcome;
- audience, context, prerequisite knowledge, and moment of need;
- source authority and traceability method;
- included and excluded scope;
- content hierarchy and required components;
- writing, visual, brand, accessibility, technical, and platform requirements;
- screenshot, annotation, icon, illustration, and media requirements;
- interaction or assessment rules when applicable;
- editable, distribution, and evidence deliverables;
- acceptance criteria, reviewers, approver, and maintenance trigger;
- known constraints, assumptions, exceptions, and unresolved items.

## 10. Production workflow

### Stage 1 — Intake and diagnosis

1. Confirm the request and desired performance outcome.
2. Identify audience, task, workflow, environment, risk, and constraints.
3. Determine whether training, performance support, communication, or another intervention is appropriate.
4. Record the entry-gate result.

### Stage 2 — Source intelligence

1. Inventory sources and establish authority.
2. Extract relevant facts, steps, decisions, terminology, and evidence.
3. Identify conflicts, gaps, unsupported claims, and SME decisions.
4. Create the traceability and constraint record.

### Stage 3 — Reuse and asset decision

1. Search for approved reusable assets and components.
2. Assess currency, authority, fitness, licensing, and modification needs.
3. Select the smallest effective asset or coordinated asset set.
4. Evaluate `LACE-DE-001` using the approved machine-readable rules.
5. Record the route, primary asset, no more than three distinct-purpose companions, rejected alternatives, warnings, confidence, reviews, and approval in `LACE-TMP-009`.

### Stage 4 — Blueprint and content plan

1. Select the asset family, type, blueprint, and variant.
2. Define the information architecture and content sequence.
3. Atomize content into reusable units where valuable.
4. Define the build specification and acceptance criteria.

### Stage 5 — Content and visual production

1. Draft using plain-language and procedural-writing rules.
2. Apply visual hierarchy, design tokens, geometry, typography, color, spacing, and components.
3. Plan or create task-focused screenshots and media.
4. Apply accessibility, privacy, security, brand, and platform requirements.
5. Produce required editable and distribution outputs.

### Stage 6 — Render, inspect, and repair

1. Render or preview the asset in its delivery context.
2. Inspect content, layout, overflow, media, links, interaction, and accessibility.
3. Classify defects by severity.
4. Repair or regenerate affected components.
5. Re-render and repeat until the applicable gate is met.

### Stage 7 — Approval and handoff

1. Run visual, content, technical, accessibility, and package QA.
2. Assign a production-readiness status.
3. Record approvals, constraints, changes, and maintenance metadata.
4. Hand the approved release package to the publication workflow.

## 11. Writing and visual standards

LACE assets must apply:

- audience-appropriate plain language;
- direct task and decision language;
- explicit prerequisites, steps, results, and recovery guidance;
- manageable cognitive load and progressive disclosure;
- consistent headings, numbering, tables, callouts, and labels;
- governed design tokens, grids, typography, color, spacing, and components;
- no decoration that competes with comprehension;
- no reliance on color alone;
- readable tables with repeated header rows when applicable;
- alt text and meaningful labels;
- task-focused screenshots with documented purpose, capture guidance, callouts, and alt text;
- controlled icon, illustration, diagram, and media use;
- validated overflow, export, and distribution behavior.

## 12. Quality gates

### Required gates

- source and claim accuracy;
- blueprint and scope alignment;
- writing and instructional clarity;
- visual and brand conformance;
- accessibility;
- technical and platform behavior;
- links, screenshots, media, and interactions;
- package completeness and editability;
- approvals, traceability, versioning, and maintenance metadata.

### Defect policy

- **Critical:** unsafe, materially inaccurate, inaccessible for a core task, or prevents use. Release blocked.
- **Major:** significantly impairs comprehension, completion, consistency, or maintenance. Release blocked.
- **Minor:** limited impact and does not prevent intended use. May be accepted if documented.
- **Advisory:** improvement opportunity with no current release impact.

The canonical visual gate is **95/100 with no Critical or Major defect**. A broader governing system may require an equal or stronger release threshold. Any threshold conflict must be resolved explicitly rather than silently lowering the gate.

### Production-readiness statuses

- **Build-ready:** all entry and specification requirements are satisfied.
- **Build-ready with documented constraints:** production can proceed safely with approved limitations.
- **Not build-ready:** material information, approval, accessibility, source, or scope issues remain.

## 13. Outputs

A complete LACE release package contains, as applicable:

- final editable source;
- approved distribution file;
- asset build specification;
- source and evidence record;
- decision and constraint record;
- accessibility and quality results;
- screenshot/media inventory;
- approval record;
- change summary;
- version and maintenance record;
- publication handoff instructions.

## 14. Exception and escalation rules

Escalate when:

- sources conflict or lack authority;
- required facts, owners, or approvals are missing;
- requested content exceeds approved scope;
- accessibility requirements cannot be met;
- confidential or controlled information may be exposed;
- platform behavior cannot be verified;
- a requested format is unsupported;
- visual or package gates fail;
- downstream publishing would materially alter the approved asset.

The escalation record must identify the issue, impact, owner, decision required, safe interim state, and due date when known.

## 15. Governance and change control

- LACE uses semantic versioning.
- Changes to authority, entry conditions, asset taxonomy, required schema, decision logic, quality gates, or release requirements require a controlled version change.
- Asset examples and implementation guidance may change without redefining the system when they remain compatible.
- IDs are permanent and must not be reused.
- Template identifiers use the governed `LACE-TMP-###` namespace and the reserved family ranges defined in `template-namespace.md`.
- `template-register.yaml` is the sole authority for canonical template identities, versions, statuses, and legacy aliases.
- Predecessor IDs are traceability aliases only and are prohibited for new LACE production.
- Review LACE at least annually and after a major policy, platform, accessibility, brand, automation, or operating-model change.
- Preserve predecessor history and source attribution.

## 16. Measurement

Track measures appropriate to risk and maturity:

- cycle time from entry to build-ready package;
- first-pass quality rate;
- Critical, Major, and Minor defect rates;
- source-gap and conflict frequency;
- reuse rate;
- accessibility pass rate;
- approval rework;
- asset usage and task completion;
- maintenance timeliness;
- learner or user outcome measures defined upstream.

Metrics support improvement and do not override release evidence.

## 17. Automation boundary

LACE may automate intake normalization, source extraction, asset recommendations, specification assembly, drafting, rendering, validation, and package generation. Human decision rights remain required for material source conflicts, policy interpretation, high-risk content, accessibility exceptions, approval, and release authorization.

## 18. Definition of done

LACE v1.0 is complete when it has:

- a unique ID, owner, purpose, audience, and bounded scope;
- triggers and entry conditions;
- roles and decision rights;
- inputs, outputs, workflow, and decision logic;
- exception and escalation handling;
- reusable specifications and standards;
- version and review dates;
- completion evidence;
- registered relationships without duplicating governing systems.
