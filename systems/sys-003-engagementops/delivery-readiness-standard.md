# EngagementOps delivery-readiness standard

Version: 0.5.0  
Effective date: 2026-09-03  
Owner: Travis True  
Status: Approved for SYS-003 development

## Purpose

Convert governance requirements into enforceable pre-activation and post-change gates.

## Required review gates

| Gate | Applies when | Required authority |
|---|---|---|
| Source validation | Every campaign and material update | Source/content owner |
| Technical validation | Procedures, products, systems, workflows, or technical claims | Technical/operational owner |
| Compliance/legal/policy/security/privacy review | Triggered by subject, data, audience, channel, or risk | Assigned specialist authority |
| Accessibility review | Every delivered asset and channel experience | Accessibility reviewer |
| Brand/communications review | Required by the governing brand or communication standard | Brand/communications owner |
| Operational approval | F2/F3 content, workflow change, or operational consequence | SME/operational owner |
| Measurement approval | KPI commitment, tracking, comparison, or outcome claim | Analytics/program owner |
| Release approval | Every activation or material post-approval change | Authorized human approver |

Not-applicable requires a recorded rationale and accountable reviewer.

## P0 release-blocking controls

P0 controls must pass before activation:

- approved objective, audience, call to action, scope, owner, and exact version;
- authoritative current sources with conflicts resolved;
- required technical, F2/F3, and specialist validation;
- privacy classification, permissions, redaction, and data-collection authority;
- accessible asset and channel experience with equivalent access;
- rights and licensing verification;
- approved locale coverage or approved scope/fallback;
- channel ownership, scheduling, support, rollback, expiration, and withdrawal path;
- measurement authority when tracking or KPI commitments exist;
- version-bound human release approval;
- zero open Blocker or Critical defects.

## P1 required quality controls

P1 controls cover message clarity, cognitive load, brand, final-size rendering, links, channel specifications, metadata, discoverability, frequency/fatigue, cross-channel consistency, analytics verification, archival relationships, and affected Golden regression.

P1 must pass unless a named authority approves a time-bounded exception that is permitted by the governing control.

## Screenshot and recording controls

Before distribution:

- use approved or fictional data;
- remove personal, confidential, credential, account, device, location, notification, and hidden metadata;
- inspect crops, browser chrome, tabs, menus, taskbars, filenames, URLs, comments, revision history, audio, and background content;
- verify annotations do not obscure required controls or misstate the interface;
- record source/version/capture date and redaction reviewer;
- repeat review after resizing, editing, export, or channel upload.

Blur alone is not sufficient when underlying information remains recoverable or context still identifies a person or system.

## Rights

Record authority for fonts, icons, photographs, illustrations, audio, video, music, templates, trademarks, testimonials, user-generated content, and external quotations. Unresolved ownership blocks release.

## Approval record

The delivery-readiness record identifies every gate, result, reviewer, date, evidence, open defect, exception, post-approval change, regression result, approver, decision, scope, and expiration.

Approval states are blocked, returned, approved, or released. Elapsed time, silence, automation, scheduling, or platform access cannot change the decision.

## Post-approval change

A material change to instructions, profiles, datasets, references, message meaning, audience, channel, timing, tracking, model behavior, assets, or locale triggers impact analysis and the complete affected P0/P1 suite.

Release remains blocked until required regression passes with no open Critical defect and every affected authority reapproves the exact version.
