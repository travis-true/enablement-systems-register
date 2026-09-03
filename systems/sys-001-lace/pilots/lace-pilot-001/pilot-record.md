# LACE Step 6 pilot — Copilot safe use

## Pilot control

- System: `SYS-001`
- Pilot topic: Copilot Expansion Workshop — Week 1 Safe-Copilot
- Source baseline: `Week1_Safe-Copilot_Quick-Reference_v2.0.pdf` (updated June 2026)
- Audience: general workplace Copilot users
- Purpose: help users prompt, refine, and review Copilot output safely
- Public-sanitization rule: remove organization names, contacts, customer/member classifications, and internal policy paths
- Release boundary: this pilot validates LACE v1.0 production behavior; it does not authorize LACE v1.1.0

## Asset routing

| Asset | Canonical template | Job |
|---|---|---|
| Compact QRG | `LACE-TMP-101` | Point-of-need reminder for the prompt-refine-review loop |
| Detailed guide | `LACE-TMP-102` | Full procedure, examples, safety checks, and boundaries |
| Instructional multimedia | `LACE-TMP-400` | Short self-paced reinforcement of the three-step behavior |

## Source assertions

The pilot uses only these source-supported assertions:

- users guide Copilot and remain accountable for review and judgment;
- prompts should include Goal, Context, Source, and Expectation;
- users can create, catch up, and ask with approved information;
- first results should be refined with focused follow-up instructions;
- outputs require accuracy, fit, data, and judgment checks;
- policy or platform warnings must be read and followed;
- when permission is uncertain, pause and exclude the information until confirmed.

No universal escalation contact is asserted because the source does not provide one.

## Planned acceptance evidence

- editable and distribution formats open successfully;
- all presentation slides and document/PDF pages are rendered and visually inspected;
- QRG and multimedia text remain legible at output size;
- detailed-guide headings and table header pass structural accessibility checks;
- multimedia package includes editable source, MP4, WebVTT captions, transcript, and storyboard;
- repository LACE validation passes after pilot evidence is added.
