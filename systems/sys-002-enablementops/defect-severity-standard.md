# EnablementOps defect-severity and disposition standard

## Severity

| Severity | Definition | Release effect |
|---|---|---|
| Blocker | The file or workflow cannot be opened, used, completed, scored, navigated, or safely distributed. | Release stops immediately. |
| Critical | A likely serious error, false instruction, authority failure, material risk, or major accessibility barrier. | Release stops until resolved and independently retested, or the finding is formally rejected with evidence. |
| Major | Materially reduces accuracy, effectiveness, usability, accessibility, traceability, functionality, or maintainability. | Normally blocks release; an exception requires accountable approval and compensating control. |
| Minor | Limited defect that does not prevent successful use or materially change meaning. | May release only with an approved disposition and follow-up when appropriate. |
| Advisory | Non-defect preference or improvement opportunity. | Record when useful; does not block release. |

Classify impact, not repair effort. Use the highest credible severity when a finding affects multiple domains. Do not lower severity because correction is inconvenient or a deadline is near.

## Finding status

`Open → Assigned → In Progress → Ready for Verification → Resolved`

Alternate terminal dispositions are:

- **Accepted Exception** — residual risk is approved, time-bounded, and mitigated.
- **Rejected** — evidence establishes that the finding is not a defect.
- **Deferred** — correction is postponed with impact, owner, due date, interim control, and approval.
- **Duplicate** — another issue fully represents the finding.

## Required disposition evidence

| Disposition | Required evidence |
|---|---|
| Resolve | Corrected source, change description, verification result, reviewer, and regression result |
| Accept exception | Severity, rationale, affected users, residual risk, compensating control, approver, owner, expiration, and review trigger |
| Reject | Technical or governing rationale plus reviewer and owner agreement |
| Defer | Reason, impact, owner, target date, interim control, and approval |
| Duplicate | Primary issue ID and confirmation that it covers the full scope |

When no authorized approver is available, the affected release remains blocked.
