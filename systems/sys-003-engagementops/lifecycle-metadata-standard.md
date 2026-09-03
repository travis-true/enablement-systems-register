# EngagementOps lifecycle and metadata standard

Version: 0.2.0  
Effective date: 2026-09-03  
Owner: Travis True  
Status: Approved for SYS-003 development

## Identifier and version rules

Identifiers are permanent and never reused:

- campaign: `EO-CMP-###`;
- touchpoint: `EO-TP-###`;
- campaign asset: `EO-AST-###`;
- channel profile: `EO-CH-###`;
- measure: `EO-MET-###`;
- approval or exception: `EO-DEC-###`.

Use semantic versions for governed campaigns and reusable assets. A material meaning, audience, call-to-action, channel, timing, source, risk, measure, or approval change requires a new version and affected revalidation.

Recommended filenames use `<id>_<short-name>_v<version>_<status>.<ext>`. Filenames aid discovery but do not replace metadata.

## Required campaign metadata

Every campaign record includes:

- stable ID, title, type, version, and lifecycle status;
- owner, creator, reviewers, approver, and support owner;
- related initiative and system identifiers;
- objective, audience, exclusions, call to action, and success relationship;
- source authority, origin, effective/version dates, and verification date;
- classification, access, privacy, accessibility, rights, brand, and localization status;
- channels, touchpoints, assets, dependencies, and schedule;
- measure definitions, baseline status, collection authority, access, and limitations;
- created, updated, approved, activation, expiration, closure, and next-review dates as applicable;
- retention class, disposition authority, archival location class, and deletion restriction;
- supersedes/superseded-by relationships;
- material history and open issues or exceptions.

Unknown values are recorded as `unknown`, `not-applicable` with rationale, or a blocking gap. They are not silently omitted.

## Asset and touchpoint metadata

Each asset and touchpoint records its parent campaign, purpose, audience, call to action, channel, sequence position, owner, source, version, status, format, accessibility evidence, classification, approval, activation window, expiration, dependencies, replacement relationship, and final disposition.

A copy exported to another channel remains linked to its parent and source version. Channel adaptation never creates authority to change controlled meaning.

## Lifecycle gates

1. **Proposed** — stable ID assigned; outcome and ownership identified.
2. **Qualified** — activation criteria met; boundaries, sources, risks, and required reviewers identified.
3. **Planned** — strategy, sequence, channels, measures, support, and lifecycle plan complete.
4. **Produced** — governed assets and variants built by the appropriate authority.
5. **Reviewed** — source, accessibility, privacy, rights, brand, technical, channel, and measurement reviews completed as triggered.
6. **Approved** — exact version and launch scope authorized by a human.
7. **Active** — approved touchpoints operating within scope and dates.
8. **Evaluated** — results, limitations, incidents, and continuation decision recorded.
9. **Closed or sustained** — ownership and disposition confirmed.
10. **Superseded or retired** — dependencies transitioned and final authorization recorded.

A later gate cannot cure missing authority from an earlier gate.

## Review and maintenance triggers

Review occurs on the recorded date and sooner after:

- controlling-source, policy, product, process, audience, or ownership change;
- material channel or platform change;
- accessibility, privacy, security, legal, compliance, rights, or brand finding;
- inaccurate, outdated, broken, inaccessible, or misdirected content;
- unexpected audience response, fatigue, complaint, incident, or measurement anomaly;
- material performance change or failure to meet the approved call to action;
- dependency supersession or retirement;
- exception expiration.

Continued operation requires recorded human confirmation. Automated activity or lack of complaints does not establish continued approval.

## Retention and disposition

SYS-003 does not invent legal or organizational retention periods. Each record must resolve to an approved retention class and disposition authority before collecting personal or restricted data.

At minimum:

- preserve approval, source, version, exception, incident, and closure evidence through the active lifecycle and required review;
- restrict deletion while a hold, investigation, open issue, dependency, or governing schedule applies;
- minimize duplicate operational copies;
- revoke access and disable integrations when no longer required;
- dispose only under recorded authority;
- preserve public system specifications and identifier history through Git history.

## Supersession and retirement

Before superseding or retiring a campaign, asset, channel, measure, or integration:

1. complete impact and dependency review;
2. identify and validate the successor, if any;
3. confirm owner, transition plan, communications, and support;
4. stop schedules, revoke unnecessary access, and disable integrations;
5. migrate or redirect active dependencies and test the transition;
6. record retention, archive, and disposition decisions;
7. define rollback or contingency;
8. obtain final human authorization;
9. update status and bidirectional replacement links;
10. preserve the material history.

Moving a file or changing a status alone does not retire governed work.
