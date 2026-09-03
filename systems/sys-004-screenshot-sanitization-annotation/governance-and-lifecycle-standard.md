# Governance and lifecycle standard

## Roles

| Role | Authority |
|---|---|
| Requester | Defines task, audience, placement, and learner need |
| Capture owner | Verifies interface state and produces clean source |
| Privacy reviewer | Approves synthetic values and sanitization |
| Accessibility reviewer | Approves text alternatives and non-color cues |
| QA reviewer | Records defects and gate result |
| Release owner | Authorizes publication and retirement |

One person may hold several roles, but privacy review and release approval must be explicitly recorded.

## Source hierarchy

1. Approved product or policy source.
2. Verified live interface in an authorized test environment.
3. Approved screenshot specification.
4. Existing clean source and editable master.
5. Final derivative.

A final image never overrides a verified source.

## States

`proposed → approved → in_capture → in_review → released → retired`; `blocked` may be entered from any pre-release state.

## File states

- `<ID>_<slug>_source_v1.0.png` — clean, privacy-cleared source.
- `<ID>_<slug>_annotated-master_v1.0.pptx` — editable annotations and replacement patches.
- `<ID>_<slug>_final_v1.0.png` — approved derivative.
- `<ID>_<slug>_retired_v1.0.png` — traceable but prohibited from reuse.

## Recapture triggers

Review after an interface, workflow, version, permission, theme, localization, policy, branding, privacy, or accessibility change. Record the verification date even when no recapture is required.

## Hard stops

Do not release when interface truth is unverified, sensitive data remains, synthetic replacements can be mistaken for real identities, essential content is illegible, the text equivalent is missing, or approval is absent.
