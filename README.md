# Enablement Systems Register

The authoritative, version-controlled inventory of Travis True's reusable enablement frameworks, workflows, and playbooks. Notion may mirror summary fields for discovery and portfolio views; GitHub remains the source of truth.

## What belongs here

- **Frameworks** — principles and decision structures that guide work.
- **Workflows** — ordered steps that move work from trigger to outcome.
- **Playbooks** — reusable operating guidance combining roles, rules, judgment, examples, and exceptions.

Templates, evidence, and related artifacts support systems but are not registered as systems unless they independently meet one of these definitions.

## Repository map

```text
.
├── register.yaml              # Canonical system index
├── schema/                    # Machine-readable validation rules
├── frameworks/                # Framework documents or canonical packages
├── workflows/                 # Workflow documentation
├── playbooks/                 # Playbook documentation
├── templates/                 # Reusable authoring templates
├── evidence/                  # Public-safe completion evidence
├── archive/                   # Retired system records
├── scripts/                   # Validation utilities
└── .github/                   # Automation and issue forms
```

## Status model

| Status | Meaning |
|---|---|
| `candidate` | Identified but not yet assessed |
| `incomplete` | Defined, with material completion gaps |
| `in_progress` | Completion work is active |
| `complete` | Meets the definition of done and has evidence |
| `maintenance` | Complete and under scheduled review |
| `retired` | No longer approved for current use |

Completion scores are directional portfolio signals, not substitutes for evidence. A system cannot be `complete` or `maintenance` without at least one evidence reference.

## IDs and paths

- Framework: `FW-###`
- Workflow: `WF-###`
- Playbook: `PB-###`
- Detail path: `<id>-<short-slug>.md` for a single-file system or `<id>-<short-slug>/README.md` for a package, using lowercase IDs

IDs are permanent and never reused. Retired systems move to `archive/` but remain in the register.

## Public-safety boundary

This repository contains only public or sanitized descriptions. Do not commit confidential company information, employee data, internal screenshots, protected assets, credentials, or proprietary source material. Internal systems may be represented by a generic derivative and an `internal_reference` label without identifying the employer or storage location.

## Change process

1. Open a system issue or change request.
2. Update the detail path and `register.yaml` on a branch.
3. Run `python scripts/validate_register.py`.
4. Submit a pull request with evidence and impact notes.
5. Merge after review; then refresh the Notion summary record.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the definition of done and review rules.
