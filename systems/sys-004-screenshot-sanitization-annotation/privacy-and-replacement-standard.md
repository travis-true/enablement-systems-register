# Privacy and replacement standard

## Capture rule

Prefer an approved test tenant, sandbox, mock environment, or reconstructed interface populated before capture with synthetic data. Capture real production data only when separately authorized and unavoidable.

## Inspection zones

Inspect the full frame, including headers, account switchers, avatars, browser tabs, URLs, filenames, document previews, notifications, chat history, calendars, task panes, status bars, background windows, metadata, and reflections.

## Replacement rules

- Use fictional people and organizations that cannot be confused with real employees or customers.
- Use `example.com` domains and reserved documentation identifiers.
- Use North American fictitious phone numbers only from 555-0100 through 555-0199.
- Replace rather than blur, pixelate, partially crop, or place a transparent overlay.
- Match typography, alignment, background, spacing, and interface state closely enough to preserve instructional meaning.
- Record each changed region and the synthetic value used.
- Remove hidden metadata when the export format can retain it.

## Prohibited content

Credentials, tokens, protected health or financial information, real customer or employee records, internal hostnames, security configurations, confidential project names, private communications, and unapproved brand assets.

## Review decision

`PASS` means every visible and embedded region is safe. `BLOCKED` means the source cannot be made safe without changing instructional truth. A crop is acceptable only when the removed region is unnecessary to orientation or action.
