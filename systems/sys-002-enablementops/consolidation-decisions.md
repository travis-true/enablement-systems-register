# EnablementOps consolidation decisions

## Decision record

| ID | Decision | Result |
|---|---|---|
| EO-CD-001 | Reclassify EnablementOps from framework to operating system. | Canonical ID is `SYS-002`; historical `FW-004` is retired and not reused. |
| EO-CD-002 | Separate the system from its components. | Frameworks, workflows, playbooks, standards, templates, schemas, automation, and evidence remain subordinate or related records. |
| EO-CD-003 | Preserve the distinction between EnablementOps and the L&D Operating System. | `FW-002` remains a registered lifecycle-governance framework; it supports but does not equal `SYS-002`. |
| EO-CD-004 | Preserve LACE as a distinct component system. | `SYS-001` governs learning-asset creation and can operate within EnablementOps. |
| EO-CD-005 | Preserve EngagementOps as an optional companion system. | It activates only for engagement or adoption needs and remains outside mandatory EnablementOps scope. |
| EO-CD-006 | Preserve ReinforcementOps as a distinct companion domain. | It is named in the layer model but is not treated as a registered complete system until separately defined. |
| EO-CD-007 | Control terminology in one canonical file. | `terminology.md` is authoritative for EnablementOps terms; component documents reference it rather than redefining terms. |
| EO-CD-008 | Separate mandatory rules from recommendations. | Normative language must identify requirements; guidance must remain explicitly non-mandatory. |

## Consolidated authority

For EnablementOps classification, scope, boundary, and vocabulary, the authority order is:

1. `register.yaml`
2. `systems/sys-002-enablementops/README.md`
3. `systems/sys-002-enablementops/terminology.md`
4. Component-system and related framework, workflow, and playbook records
5. Historical or archived source material

A lower-ranked source cannot override a higher-ranked source.

## Unresolved items routed to later completion steps

The following gaps are intentionally not solved in this terminology step:

- production standards and template families;
- approved golden examples;
- visual and functional QA controls;
- automation and machine-readable schemas;
- pilot and regression evidence;
- formal complete-version release.
