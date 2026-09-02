# Consolidation and merge decisions

## Release decision

The three supplied packages were consolidated into one canonical, tool-neutral framework. The strongest supported version of overlapping content was retained; unique, compatible material was incorporated into the appropriate package file.

## Source-package coverage

| Source emphasis | Canonical location |
|---|---|
| Four-element definition and full prompt pattern | `framework.md` |
| Quick reference and common fixes | `quick-reference.md` |
| Copy-ready template | `templates/prompt-template.md` |
| Worked examples | `examples/example-prompts.md` |
| Practice and adoption activities | `practice/practice-activities.md` |
| Privacy, grounding, source priority, and review controls | `governance/safety-and-quality.md` |
| Build, explain, improve, optimize, validate, safeguard, and curate workflows | `implementation/operating-guide.md` |

## Normalization decisions

- Generalized the framework from a single product ecosystem to generative AI tools.
- Standardized the headings as Goal, Context, Source, and Expectation.
- Treated all four elements as the canonical pattern while allowing concise implementations for low-risk tasks.
- Replaced fixed intake scripts with a task-centered minimum-information intake.
- Preserved source priority, privacy, people-related safeguards, anti-fabrication controls, and human review.
- Removed source inventories, unavailable binary references, duplicate versions, package-production notes, and organization-specific implementations.
- Rewrote examples as fictional, portable scenarios.

## Version rationale

Version 2.0.0 reflects a complete structural replacement of the previous single-file record with a consolidated canonical package.
