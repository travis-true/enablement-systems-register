# EnablementOps production standard

Version: 1.0.0  
Effective date: 2026-09-03  
Owner: Travis True  
Status: Approved for SYS-002 use

## Purpose

Control how an approved enablement need becomes a maintainable production package without duplicating the asset-construction authority of LACE (`SYS-001`).

## Authority boundary

| Decision or activity | Authority |
|---|---|
| Need, priority, outcome, audience, owner, timing, and approval | EnablementOps |
| Intake and triage | `WF-001` |
| Reuse search and fitness assessment | `WF-003` |
| Asset-family selection and package approval | EnablementOps using the controlled family catalog |
| Learning-asset construction, build kits, records, rendering, repair, and asset QA | LACE (`SYS-001`) |
| Governed publication | `WF-002` |
| Awareness, launch campaign, channel activation, and participation | EngagementOps when its activation trigger is met |
| Spaced practice and sustained behavioral reinforcement | ReinforcementOps when separately activated |
| Source truth, SME accuracy, compliance, accessibility, brand, and release approval | Assigned governance owners |

A component may add detail but cannot override this order.

## Required production gates

Every production package must pass these gates in order:

1. **Authorization** — the request, owner, priority, performance outcome, audience, deadline, and constraints are approved.
2. **Source readiness** — authoritative sources are identified; conflicts, assumptions, permissions, sensitivity, and verification needs are recorded.
3. **Reuse decision** — existing approved assets are reused, adapted, replaced, or rejected with rationale.
4. **Package selection** — one primary family and no more than three companions are selected unless an approved exception justifies more.
5. **Production specification** — format, channel, template/build kit, content budget, accessibility needs, review plan, filename, storage, and lifecycle triggers are defined.
6. **Build authorization** — production begins only after the package and specification are approved.
7. **Build and QA** — the applicable LACE build kit or the controlled fallback specification is used; source, technical, accessibility, visual, privacy, and functional checks are recorded.
8. **Release authorization** — unresolved defects, accepted exceptions, approvers, release files, and source files are recorded.
9. **Publication and handoff** — distribution location, support path, measurement owner, and discoverability metadata are confirmed.
10. **Lifecycle control** — review date, change triggers, version, replacement relationship, and archive action are recorded.

Failure at a required gate blocks advancement unless an authorized exception record identifies the owner, reason, risk, compensating control, and expiration.

## Universal production requirements

Every asset or production specification must address:

- title, asset ID, family ID, version, status, owner, and review trigger;
- audience, performance outcome, intended moment of use, and prerequisites;
- approved sources, verification date, unresolved conflicts, and assumptions;
- primary native format, distribution format, and editable source location;
- delivery channel, environment, platform/version context, and support path;
- plain language, usable structure, cognitive-load controls, and content budget;
- accessibility plan, including reading order, text alternatives, captions or transcripts, contrast, keyboard behavior, and accessible export checks as applicable;
- visual or media purpose; decorative elements do not justify production;
- privacy, data-handling, permission, licensing, and redaction checks;
- technical, SME, accessibility, brand, and release approvers as applicable;
- QA evidence, accepted exceptions, publication location, and maintenance triggers.

## Content and overproduction controls

- Select the smallest asset set that can produce the approved outcome.
- Do not duplicate identical content across formats; assign each asset a distinct function.
- Do not add video, simulation, gamification, custom visual, screenshot, icon, or assessment without a performance reason.
- Do not shrink type, compress spacing, remove required context, or overload screens to make content fit.
- Apply this overflow order: edit for relevance; split content; change to an approved larger layout; add a companion asset; request an exception.
- Reopen selection when the audience, outcome, source, risk, channel, platform, or format constraint materially changes.

## Source and storage model

- Governed reusable source, schemas, templates, and change history reside in the authoritative Git repository.
- Operational and published project files reside in the approved business-facing repository.
- Public repositories contain only public or sanitized material.
- Final distribution files never replace editable source files.
- Labels such as “final,” “new,” or “latest” do not establish authority; version, status, and approval records do.

## Automation maturity

- Level 2 template-guided production is the minimum supported automation level.
- Level 3 structured generation may be used only with an approved schema, stable template/build kit, validation, and human review.
- Visual assets target 85–90% automated completion; one focused human inspection remains required.
- Automation cannot bypass source, accessibility, privacy, visual, functional, or release gates.
