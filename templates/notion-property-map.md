# Notion property map

Create one Notion database record per GitHub system. Store summaries and links only.

| Notion property | Type | GitHub source |
|---|---|---|
| Name | Title | `name` |
| System ID | Text | `id` |
| Category | Select | `category` |
| Status | Status | `status` |
| Owner | Person or text | `owner` |
| Completion | Number, percent | `completion_score` |
| Purpose | Text | `purpose` |
| Audience | Multi-select or text | `audience` |
| Next action | Text | `next_action` |
| Next review | Date | `next_review` |
| Labels | Multi-select | `labels` |
| GitHub record | URL | Primary detail file URL |

Recommended views: All systems, Incomplete systems, Completion roadmap, Frameworks, Workflows, Playbooks, Internal references, Personal/business systems, and Review due.
