# EnablementOps production-tool profiles

These profiles govern tool selection. Asset-specific build instructions remain in LACE.

| Tool or format | Approved role | Required control |
|---|---|---|
| Word / DOCX | Default editable source for structured documents, guides, scripts, storyboards, and specifications | Use semantic styles, accessible tables, controlled headers/footers, and separate export verification |
| PowerPoint / PPTX | Default editable source for presentations, visual communication, recognition assets, and the initial QRG automation target | Use governed layouts, editable objects, reading order, alt text, final-size inspection, and PDF verification |
| Excel / XLSX | Default editable source for inventories, trackers, item banks, scoring, schedules, and dashboards | Use named headers, labels in addition to color, documented formulas, data validation, and keyboard-readable structure |
| Markdown / YAML / JSON | Governed source, registers, schemas, automation inputs, and public-safe specifications | Validate syntax, schema, links, references, version, and source ownership |
| PDF | Controlled distribution format, never the only editable source | Generate from an accessible source and verify tags, order, headings, links, language, title, tables, and bookmarks as applicable |
| Google Docs, Slides, or Sheets | Collaboration or delivery derivative when required | Preserve the approved native-source relationship and repeat accessibility/export checks |
| InDesign | Exception for premium or unusually complex composition | Record why PowerPoint or Word is insufficient and identify the maintenance owner |
| Illustrator / SVG | Source of record for governed icons and reusable vector graphics | Preserve editable vector source, rights, visual grammar, semantic name, and approved exports |
| Raster image / PNG | Distribution derivative for screenshots, social graphics, or visual exports | Retain editable source, verify legibility at use size, document privacy review, and regenerate after source changes |
| Video / audio | Delivery format produced from an approved script, storyboard, and source package | Provide captions, transcript, essential visual description, rights verification, accessible controls, and editable project source |

## Selection rules

1. Choose the lowest-maintenance editable tool that meets the performance, accessibility, channel, and update requirements.
2. PowerPoint is the default for governed QRG visual automation; InDesign requires an exception.
3. Illustrator owns vector icon masters; raster exports are derivatives.
4. PDF is a distribution output, not an authoring master.
5. Structured automation begins at Level 2 and advances to Level 3 only after template and schema stability.
6. A tool change that alters layout, accessibility, editability, automation, or ownership reopens the production specification.
