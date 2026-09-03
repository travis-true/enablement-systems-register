# EngagementOps export contract

Every governed system-to-system exchange provides both:

1. machine-readable YAML or JSON conforming to the applicable SYS-003 schema;
2. human-readable Markdown summarizing the same IDs, version, authority, status, decisions, gaps, and evidence.

Required export metadata:

- schema name and version;
- record ID and version;
- source and target system;
- created/updated date and actor;
- classification and access boundary;
- status and authority;
- related record IDs and canonical paths;
- unresolved material and nonmaterial gaps;
- checksum or immutable revision reference when supported.

Exports are snapshots, not new authorities. Receiving systems validate schema, version, classification, relationships, and decision state before use. Unknown schema versions, missing critical fields, unresolved material gaps, or invalid references are returned without activation.
