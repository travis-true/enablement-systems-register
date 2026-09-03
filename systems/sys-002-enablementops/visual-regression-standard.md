# EnablementOps visual-regression standard

## Purpose

Detect unintended visual changes in generated, edited, or exported assets while preserving legitimate content and rendering variation.

## Required baselines

Use the active Approved Golden matching the layout, theme, channel, and exemplar family. If no matching Golden exists, use an explicitly approved Reference baseline and label the result non-governing.

## Trigger events

Run visual regression when any of these change:

- template, layout, component, theme, token, icon, or font;
- generator, rendering library, authoring tool, or export profile;
- schema, content budget, image placement, or responsive rule;
- accessibility remediation that affects presentation;
- reusable master or build-kit version.

## Required process

1. Record the baseline ID, candidate ID, versions, environment, tool, and export profile.
2. Generate or render every page, slide, screen, state, and required responsive size.
3. Compare page count, dimensions, structure, component placement, and expected content.
4. Run automated comparison when supported.
5. Inspect every output manually at intended use size and at 200% zoom.
6. Review differences for clipping, overlap, overflow, missing objects, substitution, broken glyphs, reflow, contrast, spacing, hierarchy, and image quality.
7. Classify each unexpected difference using the defect-severity standard.
8. Correct and rerun the complete affected comparison.
9. Record the final result and human approval.

## Pass criteria

- all expected outputs exist and open;
- page, slide, screen, and state counts match the specification;
- no unexpected content is missing or substituted;
- no clipping, overlap, off-canvas object, broken glyph, formula error, or unreadable text exists;
- required visual hierarchy and final-size readability are preserved;
- expected intentional differences are documented;
- zero Critical or Major visual defects remain;
- visual QA is at least 95/100;
- the human reviewer approves the comparison.

Pixel equality alone cannot establish a pass. Rendering engines may introduce harmless differences, and small pixel changes may conceal material defects.

## Evidence

Retain baseline and candidate identifiers, rendered comparisons, automated results when used, difference log, severity, corrections, environment, reviewer, date, and approval.
