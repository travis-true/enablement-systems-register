# LACE v1.1.0 release notes

**Release date:** 2026-09-03  
**System:** SYS-001 — LACE Learning Asset Creation Engine  
**Release type:** Minor, backward-compatible functional improvement

## Basis

LACE-PILOT-001 successfully produced and verified one QRG, one detailed procedural guide, and one multimedia asset from the Week 1 Safe-Copilot source.

## Changes

- Require semantic-structure verification in editable and distribution formats; visible formatting alone is insufficient accessibility evidence.
- Require explicit separation of QA disposition from release authorization.
- Update LACE-TMP-102 to require verified semantic table headers.
- Add LACE-TMP-400 variant MM-1D for silent visual microlearning with equivalent text access.
- Make multimedia audio acceptance conditional when the approved asset contains audio.
- Add direct pilot evidence and move SYS-001 to maintenance at 100% completion.

## Compatibility

- Existing LACE identifiers remain unchanged.
- Existing control records and decision rules remain compatible.
- LACE-TMP-102 and LACE-TMP-400 advance to template version 1.1.0.
- All other active template versions remain unchanged.

## Verification

- LACE-PILOT-001 QA: PASS.
- Pilot defects remaining: 0 Blocker, 0 Critical, 0 Major, 0 Minor.
- Repository register and LACE validation: required before merge.

## Rollback

The v1.0.0 baseline remains recoverable through Git history. Roll back by reverting the v1.1.0 release commit; canonical IDs must not be reused or renumbered.
