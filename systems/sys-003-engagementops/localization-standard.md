# EngagementOps localization standard

Version: 0.5.0  
Effective date: 2026-09-03  
Owner: Travis True  
Status: Approved for SYS-003 development

## Activation

Localization review is required when an audience has an authorized language, regional, cultural, legal, accessibility, date/time, number, currency, reading-level, or channel requirement that differs from the source version.

SYS-003 does not define a universal language list. Each campaign records the approved source locale, target locales, audience basis, priority, owner, reviewers, delivery channels, and fallback.

## Required locale profile

Each locale profile records:

- campaign and locale-profile IDs;
- source and target locale using approved organizational conventions;
- audience and business basis;
- translation, transcreation, or exact-preservation mode;
- fidelity level and protected terminology;
- source version and translation-memory/glossary authority when used;
- translator or localization owner;
- linguistic, source/SME, accessibility, brand, and triggered specialist reviewers;
- channel, layout, date/time, number, currency, reading-direction, font, media, caption, transcript, and text-expansion requirements;
- localized asset IDs and version relationships;
- review results, approval, expiration, fallback, and disposition.

## Fidelity

- F0 informational content may be condensed when approved meaning remains intact.
- F1 must preserve sequence and decision points.
- F2 must preserve exact steps and requires SME validation.
- F3 permits no simplification without approved source language and formal specialist review.

Machine translation may create a draft. It cannot approve terminology, fidelity, accessibility, regulated meaning, or release.

## Workflow

1. Confirm the locale need and authority.
2. Freeze the approved source version.
3. Select translation, transcreation, or exact-preservation mode.
4. Apply the controlled glossary and protected terms.
5. Produce the localized draft with bidirectional source references.
6. Complete linguistic and fidelity review.
7. Complete accessibility and channel rendering review.
8. Complete triggered brand, privacy, legal, compliance, policy, security, or technical review.
9. Obtain version-bound human approval.
10. Publish only the approved locale/version and preserve its lifecycle links.

A source change triggers impact review for every active locale. F2/F3 changes require affected SME/specialist review and P0/P1 regression.

## Accessibility and channel adaptation

Localization review includes reading direction, line breaks, text expansion, font support, captions, transcript, alt text, pronunciation, meaningful link text, keyboard order, screen-reader language, date/time/number expression, and final-size rendering.

A translated text file does not prove that the localized channel experience is accessible.

## Fallback and unsupported locales

The locale profile defines an approved fallback that does not misrepresent availability. If a required locale or equivalent-access path cannot be provided, affected activation remains blocked or the audience/scope must be explicitly changed and reapproved.

## Lifecycle

Localized variants never detach from the controlled source. Supersession, withdrawal, correction, and retirement update source/target relationships, active channels, caches, schedules, support guidance, and archival records.
