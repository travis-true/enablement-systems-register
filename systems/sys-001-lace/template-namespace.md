# LACE template-ID namespace

**Decision:** LACE-NDR-001  
**Status:** Approved  
**Applies to:** SYS-001  
**Effective date:** 2026-09-02

## Canonical syntax

Every reusable LACE template has one permanent identifier:

`LACE-TMP-###`

- `LACE` identifies the owning system.
- `TMP` identifies a reusable template.
- `###` is a three-digit number assigned once from the governed range.
- Canonical IDs are uppercase and must match `^LACE-TMP-[0-9]{3}$`.
- The ID identifies the template, not a completed instance created from it.

Examples:

- `LACE-TMP-001`
- `LACE-TMP-100`
- `LACE-TMP-400`

## Reserved ranges

| Range | Authority |
|---|---|
| 001–099 | System-control and lifecycle templates |
| 100–199 | Performance-support and documentation templates |
| 200–299 | Instructor-led and virtual-learning templates |
| 300–399 | Self-paced digital-learning templates |
| 400–499 | Video and multimedia templates |
| 500–599 | Communications and adoption templates |
| 600–699 | Planning and evaluation templates |
| 700–899 | Reserved for approved future families |
| 900–999 | Migration, compatibility, and exceptional controlled use |

A number cannot be assigned outside its range merely to resemble a predecessor ID.

## Assignment rules

1. The template register is the sole authority for canonical IDs.
2. Each canonical ID maps to exactly one template identity.
3. Each active template identity has exactly one canonical ID.
4. IDs are assigned sequentially within the applicable range.
5. Deleted, deprecated, superseded, and retired IDs are never reused.
6. A renamed template retains its ID.
7. A materially different purpose, required structure, output contract, or decision function requires a new ID.
8. A compatible revision retains the ID and changes the semantic version.
9. Variants remain under the parent ID when they share the same purpose and required output contract; otherwise they receive separate IDs.
10. Draft or planned entries may reserve an ID, but no production artifact may cite that ID until its register status is `active`.
11. Completed instances must carry their own asset or record ID and reference the template ID and version used.
12. File names begin with the lowercase canonical ID followed by a short slug, for example `lace-tmp-005-asset-build-specification.yaml`.

## Lifecycle

Allowed template statuses are:

- `planned` — ID reserved; template not approved for production.
- `active` — approved for current use.
- `deprecated` — still recognized, but new use is prohibited.
- `retired` — preserved for history; use is prohibited.
- `superseded` — replaced by a specified canonical ID.

Status changes do not change or release the identifier.

## Versioning

Templates use semantic versions:

- **Major:** incompatible required-field, structure, purpose, or output-contract change.
- **Minor:** backward-compatible capability or guidance addition.
- **Patch:** correction that does not change required behavior.

The canonical ID and version must appear together in generated records and asset manifests.

## Legacy aliases

Predecessor IDs remain searchable aliases only. They are not valid identifiers for new LACE production.

- An alias must map to one canonical ID.
- An alias must record its source system and original title.
- Ambiguous aliases may repeat across source systems only when the source system is also supplied.
- No alias establishes canonical numbering priority.
- Historical files are not renamed solely to imitate migration.
- New files, references, automations, and schemas must use the canonical ID.
- When legacy content is revised, its metadata must add the canonical ID while preserving the original alias for traceability.

## Collision handling

If a proposed ID, alias, title, or purpose conflicts:

1. Stop assignment.
2. Compare owner, purpose, required structure, output contract, and governing source.
3. Reuse the canonical ID only when all identity-defining attributes are equivalent.
4. Otherwise assign the next unused ID in the correct range.
5. Record the decision and any alias in the template register.
6. Never resolve a collision by changing zero padding or silently replacing an existing mapping.

## Governance

The SYS-001 owner approves additions, identity changes, deprecations, supersessions, and retirements. Pull-request review must confirm range, uniqueness, alias mapping, version, status, and file-path validity before the register changes.

The register at `template-register.yaml` is the machine-readable authority.
