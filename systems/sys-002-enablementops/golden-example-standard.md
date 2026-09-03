# EnablementOps golden-example standard

Version: 1.0.0  
Effective date: 2026-09-03  
Owner and approver: Travis True  
Status: Approved for SYS-002 use

## Purpose

Govern how completed enablement artifacts become reusable exemplars for production, QA, regression testing, and automation.

## Controlled status vocabulary

| Status | Meaning |
|---|---|
| Candidate | Complete artifact awaiting required review or approval. |
| Reference | Useful, verified example that does not govern future production. |
| Approved Golden | Latest explicitly approved exemplar for one canonical coverage key. |
| Superseded | Former Approved Golden replaced by a newer explicitly approved exemplar with the same coverage key. |
| Retired | No longer supported for new production or regression use. |

The latest completed file is not automatically golden. Completion, publication, or a high QA score does not substitute for explicit golden promotion.

## Canonical coverage key

Each golden is unique within:

`layout_id::theme_id::channel_id::exemplar_family`

A new example supersedes an existing golden only when all four values match. A different layout, theme, channel, or exemplar family creates a different coverage key.

The public register may replace confidential theme, channel, file paths, or project details with controlled sanitized values. The internal approval record remains authoritative for exact values and file hashes.

## Required promotion criteria

An example may become Approved Golden only when all criteria pass:

1. Family QA status is Pass.
2. Master QA score is at least 90%.
3. No blocking privacy, source, accessibility, technical, production, or functional defect remains.
4. Synthetic-data or privacy review is Pass.
5. Format-specific render, formula, media, or interaction checks are Pass as applicable.
6. Accessibility review is Pass.
7. Visual examples score at least 95/100 with zero Critical or Major visual defects.
8. Every rendered page, screen, or output is inspected at its intended use size.
9. Required editable sources and distribution outputs are retained.
10. Dependencies, template/build-kit version, schema version, sources, and review date are recorded.
11. Regression evidence is linked.
12. Travis True explicitly approves promotion and the approval date is recorded.

## Promotion workflow

1. Register the artifact as Candidate or Reference.
2. Confirm the intended canonical coverage key.
3. Collect required QA, privacy, accessibility, render, source, dependency, and regression evidence.
4. Identify any current golden with the same coverage key.
5. Complete the promotion record.
6. Obtain explicit owner approval.
7. Mark the new item Approved Golden.
8. Mark the former matching golden Superseded; retain its record and evidence.
9. Update affected templates, schemas, tests, automation, and documentation.
10. Set the next review and replacement triggers.

## Use rules

- Goldens validate output quality and expected behavior; they do not replace current source truth.
- Production begins from an approved template or build kit, not by copying uncontrolled golden content.
- A golden may cover only the layout, theme, channel, family, and behaviors recorded in its approval.
- Content facts, screenshots, platform behavior, support details, and policies must still be verified for each new asset.
- A Reference may guide judgment but cannot serve as the sole regression baseline.
- Automation changes must be tested against every affected active golden.
- A failed regression blocks release or requires an authorized exception.

## Review and retirement triggers

Review a golden when any of these change materially:

- layout or component structure;
- theme or brand implementation;
- delivery channel or export behavior;
- template, build kit, schema, or generator;
- accessibility requirement;
- production tool or rendering engine;
- supported platform or interface;
- privacy, source, licensing, or governance rule;
- family anatomy or content budget.

Retire a golden when it no longer represents supported production, cannot be safely maintained, or is replaced without a valid same-key supersession relationship.
