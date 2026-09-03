# EnablementOps quality-assurance and release standard

Version: 1.0.0  
Effective date: 2026-09-03  
Owner: Travis True  
Status: Approved for SYS-002 use

## Purpose

Govern visual, functional, instructional, technical, accessibility, privacy, packaging, and release quality across EnablementOps outputs.

LACE (`SYS-001`) remains authoritative for asset-specific validation, rendering, repair, and build-kit checks. This standard defines the cross-system acceptance layer and evidence required before release.

## Required QA sequence

1. **Requirements QA** — approved need, audience, outcome, constraints, family, and acceptance criteria are complete.
2. **Source and technical QA** — claims, procedures, versions, formulas, answers, links, and system behavior are verified.
3. **Family QA** — the selected family and variant meet their template/build-kit requirements.
4. **Accessibility and UDL QA** — automated checks and applicable manual tests are complete.
5. **Privacy, safety, and rights QA** — sensitive data, synthetic examples, permissions, licenses, and restricted content are reviewed.
6. **Native-file QA** — the editable source opens, remains editable, and functions correctly.
7. **Rendered-output QA** — every released output is generated, opened, and inspected independently from its source.
8. **Visual QA** — hierarchy, balance, spacing, density, contrast, typography, imagery, and final-size readability are reviewed.
9. **Functional QA** — navigation, links, controls, formulas, scoring, media, interactions, downloads, and completion behavior are tested.
10. **Package QA** — filenames, versions, manifests, sources, evidence, companions, and archive relationships are complete.
11. **Regression QA** — affected active Goldens and required negative scenarios pass.
12. **Human release decision** — findings, exceptions, evidence, and approvers are recorded.

A clean editable source does not establish a clean export. Both must be tested.

## Release thresholds

An asset or package may be released only when:

- the weighted master QA score is at least 90%;
- every applicable Critical or blocking criterion passes;
- no Blocker or unresolved Critical defect remains;
- each Major defect is corrected and verified or has an authorized, time-bounded exception;
- every applicable criterion is reviewed or justified as Not Applicable;
- visual assets score at least 95/100 with zero Critical or Major visual defects;
- required negative tests demonstrate correct stop, refusal, return, or escalation behavior;
- regression tests pass and dependencies are confirmed;
- evidence is complete;
- an authorized human approves the tested version.

A score never overrides a blocking privacy, source, accessibility, technical, production, functional, or authority failure.

## Quality domains

| Domain | Required evidence |
|---|---|
| Requirements | Approved intake, outcome, family, constraints, and acceptance criteria |
| Instructional alignment | Outcome alignment, realistic practice or support, and transfer rationale |
| Content | Complete sequence, consistent terms, plain language, and cognitive-load control |
| Sources | Authority, currency, verification, conflicts, assumptions, and supported claims |
| Technical accuracy | Verified procedures, answers, formulas, scoring, behaviors, and limits |
| Visual design | Governed layout, final-size inspection, hierarchy, balance, spacing, and contrast |
| Accessibility and UDL | Automated result plus manual structure, reading order, keyboard, alternative, and usability evidence |
| Privacy and safety | Synthetic or approved data, redaction, metadata, permissions, and safe distribution |
| Rights | Recorded licenses and approved use of fonts, icons, images, media, and external sources |
| Production | Editable native file plus clean rendered/exported outputs |
| Functionality | Links, navigation, controls, formulas, scoring, media, interactions, and error handling |
| Package | Required files, manifests, names, versions, status, and storage |
| Issues and exceptions | Severity, owner, status, correction, verification, approval, and expiration |
| Approval and maintenance | Reviewers, release decision, support path, review date, and replacement triggers |

## Evidence rules

- Record actual evidence, not only a Pass label.
- Evidence identifies the tested file/version, method, result, reviewer, date, and related issue.
- Automated checkers supplement but do not replace manual review.
- Not Applicable requires a rationale.
- Corrected findings require independent verification and affected regression checks.
- Release evidence must be retained with the governed source package.
