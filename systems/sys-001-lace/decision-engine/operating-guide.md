# LACE asset decision engine operating guide

**Engine:** LACE-DE-001  
**Rules:** `decision-rules.yaml`  
**Output:** LACE-TMP-009 Asset Decision Record

## Purpose

The decision engine converts validated intake data into a controlled intervention route, one primary asset recommendation, up to three nonduplicative companions, warnings, confidence, and required human reviews.

It recommends; it does not approve production.

## Required sequence

1. Validate the required input fields.
2. Evaluate blockers in descending priority.
3. If a blocker matches, stop and create a blocked LACE-TMP-009 record.
4. Evaluate route rules in descending priority and select the first match.
5. Evaluate primary-asset rules in descending priority.
6. Ignore asset rules incompatible with the selected route.
7. Select the first compatible matching asset rule.
8. Evaluate companion rules.
9. Remove a companion when it duplicates the primary asset, another companion, or a companion purpose.
10. Keep no more than three companions.
11. Apply warnings and required human-review triggers.
12. Apply tie-breakers when evidence supports equivalent candidates.
13. Assign confidence.
14. Create the LACE-TMP-009 record.
15. Obtain the required human approval before creating the asset build specification.

## Condition evaluation

Each rule declares:

- `priority` — higher numbers evaluate first;
- `match` — `all` requires every condition; `any` requires at least one;
- `when` — normalized field/operator/value conditions;
- an outcome, route, or recommendation.

An empty `when` list is an explicit fallback and matches only after higher-priority rules fail.

Supported operators are:

- `equals`
- `in`
- `not-in`
- `greater-than`
- `greater-than-or-equal`
- `less-than`
- `less-than-or-equal`
- `contains`

Unknown fields, operators, or vocabulary values invalidate the evaluation.

## Decision precedence

1. Mandatory intake, source, and accessibility blockers
2. Operational causes
3. Measurement needs
4. Awareness, update, and alignment needs
5. Point-of-work guidance
6. Training or blended needs
7. Asset-family and asset-type fit
8. Companion assets
9. Advisory confidence

A requested format cannot override the diagnosed cause or a blocker.

## Primary and companion controls

Every recommendation has no more than one primary asset.

A companion must serve exactly one distinct purpose:

- prepare;
- deliver;
- practice;
- assess;
- reinforce;
- administer;
- produce.

A recommendation may contain zero to three companions. Remove a companion when it repeats the primary asset’s content, audience, moment, or function. When the smallest effective solution is one asset, recommend one asset.

## Confidence

- **High:** required inputs complete, sources verified, no blockers, and a non-fallback route and asset rule control the result.
- **Medium:** sources are partial, but the recommendation is limited to verified content and human review is required.
- **Low:** a fallback or unresolved selection applies. Production cannot be approved.

Confidence never makes an incomplete decision ready.

## Overrides

The decision owner may propose an override, but the record must preserve:

- original recommendation;
- requested replacement;
- reason;
- tradeoffs and warnings;
- requestor;
- approving authority;
- approval date.

An override cannot waive source, accessibility, security, policy, or release blockers.

## Reopening a decision

Re-run the decision when a material change affects audience, outcome, delivery, format, scope, source authority, or risk. Supersede the prior decision record; do not overwrite it.

## Handoff

An approved LACE-TMP-009 decision becomes an input to LACE-TMP-005 Asset Build Specification. The build specification must preserve the selected route, primary asset, companions, warnings, constraints, source limitations, reviewers, and acceptance criteria.
