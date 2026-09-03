# EngagementOps governance standard

Version: 0.2.0  
Effective date: 2026-09-03  
Owner: Travis True  
Status: Approved for SYS-003 development

## Purpose

Define the authority, source, approval, exception, and evidence controls required for EngagementOps work.

## Source-of-truth hierarchy

Use the highest applicable approved source. A lower tier may clarify presentation but cannot override a higher tier.

| Priority | Source class | Permitted use |
|---|---|---|
| 1 | Approved policy, standard, SOP, contractual requirement, controlled system record, or authoritative product/process owner decision | Governs required meaning, behavior, limits, and decisions |
| 2 | Current approved knowledge base, validated workflow, technical documentation, or release note | Governs current procedures, features, and operational details |
| 3 | Approved EnablementOps specification, LACE asset, campaign brief, or current Golden | Governs intended outcome, instructional relationship, approved expression, and production precedent |
| 4 | Documented SME or domain-owner clarification | Resolves ambiguity within the person's authority |
| 5 | Draft, informal note, search result, analytics inference, or generated suggestion | May inform investigation; never authorizes a claim or decision |

Every campaign identifies its controlling sources, owner, version or effective date, verification date, and known limitations.

### Conflict and currency rule

When sources conflict, are materially incomplete, or may be outdated:

1. stop affected drafting, scheduling, or publication;
2. record the conflict and impacted claims or actions;
3. route it to the authority responsible for the highest applicable source;
4. preserve the decision and supporting evidence;
5. revalidate affected content, assets, channels, and measures.

Silence, popularity, recency alone, or a lower-tier source cannot resolve the conflict.

## Required roles

| Role | Accountable responsibility |
|---|---|
| Initiative owner | Owns the approved organizational outcome, funding or capacity, and continuation decision |
| EngagementOps owner | Accepts activation and owns strategy, sequencing, governance, evidence, and closure |
| Campaign owner | Coordinates the approved campaign and maintains its governed records |
| Source/content owner | Approves factual meaning and source currency |
| Channel owner | Confirms channel access, specifications, scheduling, and platform constraints |
| Accessibility reviewer | Makes the recorded accessibility determination for the intended channels and assets |
| Privacy/security/legal/compliance reviewer | Decides issues within the reviewer's assigned authority when triggered |
| Brand reviewer | Decides brand compliance when required |
| Analytics owner | Approves measure definitions, collection method, access, interpretation, and retention handling |
| Release approver | Authorizes the exact campaign version and launch scope |
| Support owner | Owns response and escalation after activation |

One person may hold multiple roles only when permitted by the governing organization. Role combination does not remove required evidence or independent specialist review.

## Minimum approval evidence

A launch decision must identify:

- campaign ID and exact version;
- objective, audience, call to action, timing, and channels;
- controlling sources and verification dates;
- final assets and channel-ready variants;
- accessibility and triggered specialist determinations;
- privacy classification and data-handling decision;
- measures, baseline status, access, and retention class;
- unresolved limitations and authorized exceptions;
- approver identity, decision, date, scope, and expiration if conditional.

Approval applies only to the recorded version and scope. Material change returns the work to affected review gates.

## Decision states

- `draft` — incomplete and not approved for distribution.
- `in-review` — submitted to named reviewers.
- `returned` — material correction or clarification required.
- `approved` — approved for the recorded scope but not yet activated.
- `scheduled` — approved and assigned an authorized activation time.
- `active` — currently distributing approved touchpoints.
- `paused` — distribution temporarily stopped under recorded authority.
- `closed` — planned activity ended and closure review recorded.
- `superseded` — replaced by a named approved successor.
- `retired` — no longer approved for use.

## Exceptions

An exception must name the affected control, reason, risk, compensating control, owner, approver, start date, expiration, and correction or closure condition.

Exceptions cannot waive source authority, required legal/privacy/security decisions, human release authorization, or an unresolved Blocker/Critical defect. Expired exceptions automatically block affected activity.

## Evidence and audit trail

Material decisions are append-only. Corrections add a new dated entry and preserve the prior state. Records identify actor, action, time, reason, evidence, prior version, new version, and affected dependencies.

The governed GitHub repository is authoritative for the public-safe SYS-003 specification. Operational records and distributed files remain in the organization's approved systems of record and are referenced without exposing restricted locations or content.
