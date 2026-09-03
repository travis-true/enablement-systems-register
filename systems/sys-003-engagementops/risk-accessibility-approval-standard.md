# EngagementOps risk, accessibility, privacy, and approval standard

Version: 0.2.0  
Effective date: 2026-09-03  
Owner: Travis True  
Status: Approved for SYS-003 development

## Risk tiers

| Tier | Characteristics | Minimum review |
|---|---|---|
| R1 — routine | Approved source, established audience/channel, low consequence, no personal or restricted data | Campaign owner, source owner, channel owner, accessibility review, release approver |
| R2 — elevated | New audience/channel, broad reach, behavioral request, measurement, material adaptation, or moderate reputational/operational consequence | R1 plus affected brand, analytics, privacy, security, technical, policy, or compliance review |
| R3 — high | External audience, sensitive topic, regulated or legal meaning, personal/restricted data, high consequence, novel automation, or difficult rollback | All affected specialist authorities and explicit senior release authority |

Risk is assigned by the accountable owner with required specialist input. Uncertainty defaults to the higher applicable review tier until resolved.

## Accessibility ownership

The campaign owner is accountable for obtaining accessibility evidence. The named accessibility reviewer owns the accessibility determination; tool results do not.

Digital engagement targets WCAG 2.2 Level AA unless a stricter applicable standard governs. Channel-native limitations must be documented and cannot be hidden by providing an inaccessible primary path. Equivalent access, keyboard use, focus, reading order, contrast, text alternatives, captions/transcripts, link purpose, zoom/reflow, motion, timing, and error recovery are tested as applicable.

LACE remains authoritative for asset-specific accessibility QA. EngagementOps verifies that approved assets remain accessible after channel adaptation, scheduling, embedding, or distribution.

## Privacy, redaction, and data minimization

Before activation:

- classify content and intended audience;
- use only the minimum data required for the approved purpose;
- prefer aggregate or de-identified measurement;
- prohibit credentials, protected personal data, confidential source material, or internal locations in public artifacts;
- remove hidden metadata, comments, revision history, and unintended identifiers from distributed files;
- verify permissions, consent or other authority when required;
- define collection purpose, fields, access, retention class, and disposition;
- use fictional or approved examples;
- record redaction method and reviewer when redaction is required.

EngagementOps does not determine whether a legal basis, consent, disclosure, or regulatory requirement applies. The authorized privacy, legal, security, or compliance reviewer makes that decision.

## Approval service targets

Service targets begin only when a complete review package is accepted.

| Review path | Initial response target | Decision target |
|---|---:|---:|
| R1 routine | 1 business day | 3 business days |
| R2 elevated | 2 business days | 5 business days |
| R3 high | 3 business days | Set by required authorities after intake |
| Corrected resubmission | 1 business day | 2 business days when scope is unchanged |
| Time-critical request | Same business day when accepted | Recorded by the required approvers |

These are operating targets, not automatic approvals. A missed target creates escalation to the campaign and initiative owners; it never authorizes launch.

## Approval outcomes

- **Approve** — exact version and scope may proceed.
- **Approve with conditions** — time-bounded conditions and verification owner are recorded.
- **Return** — identified corrections or missing evidence must be resolved.
- **Reject** — the proposal may not proceed; rationale and reconsideration path are recorded.
- **Pause/withdraw** — an active approval is suspended or revoked.

A material post-approval change requires impact review and renewed approval from every affected authority.

## Escalation

Escalate unresolved source, accessibility, privacy, security, legal, compliance, technical, rights, brand, channel, measurement, or authority issues to the responsible owner. EngagementOps coordinates the record but cannot decide outside its authority.

No escalation path permits bypassing a hard stop.
