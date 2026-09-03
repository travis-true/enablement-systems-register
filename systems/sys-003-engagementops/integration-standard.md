# EnablementOps–EngagementOps integration standard

Version: 0.6.0  
Effective date: 2026-09-03  
Owner: Travis True  
Status: Approved for SYS-002/SYS-003 integration

## Boundary

SYS-002 owns the capability or performance-enablement outcome. SYS-003 owns the optional audience-engagement strategy after an accepted activation handoff. Integration links records; it does not merge authority or duplicate source content.

## Handoff sequence

1. SYS-002 records the approved outcome, intended behavior, audience, source authority, dependencies, constraints, success relationship, and engagement trigger.
2. SYS-003 validates critical fields and records any gaps.
3. SYS-003 accepts, returns, or declines the request.
4. On acceptance, SYS-003 assigns the campaign ID, risk tier, owners, required reviews, and planning boundary.
5. SYS-003 creates linked campaign, asset, channel, calendar, measurement, localization, and readiness records as applicable.
6. SYS-003 returns status, launch dependency, engagement results, limitations, and sustain/close decision to SYS-002.
7. SYS-002 evaluates capability or performance implications using its own evidence.

Acceptance authorizes planning only. It never authorizes asset production, tracking, publication, or launch.

## Required SYS-002 to SYS-003 fields

- handoff ID and exact version;
- source and target system IDs;
- initiative and related record IDs;
- approved outcome and intended behavior;
- included and excluded audiences;
- engagement trigger and proposed call to action;
- authoritative sources, owners, versions, and verification dates;
- timing, dependencies, constraints, risks, and required reviewers;
- success relationship and known measurement limits;
- requester, receiver, disposition, and decision evidence;
- unresolved material and nonmaterial gaps.

Missing outcome, audience, trigger, call to action, source authority, owner, material constraint, or decision authority returns the handoff.

## Return contract

SYS-003 returns:

- campaign and linked-record IDs;
- risk, status, channels, touchpoints, owners, and schedule;
- required approvals and unresolved gaps;
- measure IDs, baseline status, and interpretation boundary;
- asset-production and publication dependencies;
- activation, pause, closure, sustainment, or retirement disposition;
- human-readable Markdown summary and machine-readable YAML or JSON record.

## Central registry

The campaign registry is the authoritative public-safe index for SYS-003 campaigns. It records stable IDs, versions, statuses, owners, related systems, record paths, channels, assets, measures, dates, classification, and lifecycle relationships.

Operational tools may mirror the registry for dashboards. A mirror cannot become authoritative through recency or automation.

## Campaign calendar

The central calendar indexes approved or proposed touchpoint windows. It records campaign, touchpoint, audience group, channel, date/time zone, owner, status, dependency, expiration, and collision review.

Calendar presence does not authorize launch. Schedule changes that affect audience, channel, sequence, frequency, accessibility, privacy, or approval scope require impact review.

## Collision and fatigue control

Before scheduling, review:

- same-audience and same-channel overlap;
- competing calls to action;
- frequency and quiet-period requirements;
- major organizational events;
- accessibility or localization lead time;
- channel capacity and owner conflicts;
- dependencies, embargoes, and expiration;
- measurement contamination.

A material conflict is resolved, accepted by the accountable owners, or blocks scheduling.

## Automation boundary

Automation may validate schemas, IDs, references, inventory, dates, collision flags, status coherence, and export structure. It may create drafts and summaries.

Automation cannot accept a handoff, assign specialist authority, approve risk, authorize data collection, resolve material conflicts, publish, launch, or close a campaign.
