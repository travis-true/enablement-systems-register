# EngagementOps measurement and analytics standard

Version: 0.4.0  
Effective date: 2026-09-03  
Owner: Travis True  
Status: Approved for SYS-003 development

## Purpose

Govern how EngagementOps defines, collects, interprets, reports, and retains evidence without overstating what engagement activity proves.

## Measurement ladder

| Level | Question | Examples | Claim boundary |
|---|---|---|---|
| Reach | Did the intended audience have an opportunity to encounter the touchpoint? | eligible recipients, delivered messages, unique views, impressions | Does not prove attention or understanding |
| Engagement | Did the audience interact with the touchpoint? | clicks, reactions, replies, swipe completion, dwell time | Does not prove learning or adoption |
| Learning | Did knowledge, confidence, or demonstrated understanding change? | recall, quiz performance, confidence with limitations | Governed by EnablementOps when tied to learning outcomes |
| Adoption | Did people perform and repeat the intended behavior or workflow? | workflow completion, feature use, repeat use | Requires behavioral or system evidence, not communication activity |
| Performance | Did work results change? | time, error rate, support volume, quality, manager-observed behavior | Requires appropriate design and cannot be attributed to EngagementOps alone without evidence |
| Sustainment | Did participation, use, or performance persist? | continued use, reduced decay, recurring participation, drop-off | Requires a defined follow-up window and comparable evidence |

EngagementOps directly owns reach and engagement measurement. Learning, adoption, performance, and sustainment measures require the accountable EnablementOps, program, operational, or analytics owner.

## Required measure definition

Every governed measure records:

- stable measure ID and ladder level;
- operational definition;
- population, numerator, denominator, unit, and direction;
- collection source and collection method;
- baseline value, period, source, or explicit `not-available` rationale;
- target or decision threshold and its approving authority;
- collection frequency and reporting window;
- owner, analyst, audience, access, privacy classification, retention class, and disposition authority;
- exclusions, missing-data handling, limitations, and claims the measure cannot support;
- relationship to the campaign objective and business or enablement outcome.

Counts without an eligible population are not rates. Percentages must identify numerator, denominator, period, and exclusions.

## Baselines and targets

Use a pre-campaign or other approved comparison baseline when a change claim is intended. If no defensible baseline exists:

1. mark baseline status `not-available`;
2. explain why;
3. report observed activity without claiming change;
4. establish a future baseline when feasible.

Targets must be approved by the analytics or program owner. A target is not retroactively adjusted to create success. Directional signals are labeled as such and never presented as validated outcomes.

## Collection authority and minimization

Before collection, record the approved purpose, source, fields, population, access, aggregation level, privacy classification, retention class, and disposition authority.

Use realistically collectable measures and prefer aggregate or de-identified data. Do not collect personal or restricted data merely because a platform exposes it. Platform defaults, tracking availability, or administrator access do not create collection authority.

Analytics platforms and source systems are configuration choices. SYS-003 does not declare a universal platform or retention period.

## Attribution and interpretation

Reports distinguish:

- observed fact;
- calculated result;
- comparison;
- inference;
- causal claim.

A causal claim requires an approved evaluation design capable of supporting it. Otherwise use bounded language such as “associated with,” “observed during,” or “reported by.”

Reach and engagement never substitute for learning, adoption, performance, or sustainment. Confidence is self-report unless paired with stronger evidence. Manager observation identifies reported behavior, not verified system use, unless the method establishes otherwise.

## A/B and comparison tests

A comparison test requires:

- one primary variable;
- defined hypothesis and success measure;
- comparable eligible groups or periods;
- allocation method;
- minimum observation rule established before launch;
- contamination and confound review;
- privacy and approval evidence;
- predeclared decision rule.

Changing multiple material variables makes attribution indeterminate and must be reported as such.

## Reporting

Every report includes the campaign/version, reporting window, population, sources, refresh date, baseline status, definitions, results, missing data, limitations, incidents, and authorized interpretation.

Small groups and potentially identifying breakdowns are suppressed or combined according to the applicable privacy decision. Dashboards display freshness and do not imply real-time accuracy unless verified.

## Decision outcomes

Measurement review records one of:

- continue as approved;
- adjust and reapprove affected scope;
- pause and investigate;
- close as planned;
- transition to sustainment;
- stop or retire.

The decision owner records the evidence used, limitations, date, affected versions, and follow-up.
