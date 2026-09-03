# SYS-004 — Screenshot Sanitization & Annotation System

## Classification

A governed production system for converting an approved screenshot need into a privacy-safe, accurate, accessible, maintainable instructional image.

## Purpose

Control the complete screenshot lifecycle: intake, need decision, synthetic-data preparation, repeatable capture, sanitization, annotation, accessibility, quality review, release, inventory, and recapture.

## Boundary

SYS-004 governs screenshot production and evidence. It does not authorize access to source systems, change product truth, approve training content, or replace the publication controls owned by SYS-002 and WF-002.

Operational screenshots, employee data, internal interfaces, credentials, and proprietary source files are excluded from this public package. Only synthetic examples and metadata may be committed.

## Required workflow

1. Approve the screenshot need and specification.
2. Prepare an authorized test state with synthetic data.
3. Capture the smallest useful clean source.
4. inspect every visible region for sensitive or misleading content.
5. Replace unsafe content with opaque, visually matched synthetic content; never rely on blur.
6. Annotate only the learner-critical targets.
7. Provide adjacent instructions, alt text, and any required long description.
8. Complete QA and record the decision.
9. Release source, editable master, final derivative, record, and recapture trigger.
10. Retire or recapture when a trigger occurs.

## Release package

- privacy-cleared clean source;
- editable annotated master;
- final exported image;
- screenshot record;
- caption and alt text;
- QA evidence and approval;
- version and recapture metadata.

## Current maturity

Status: **maintenance**.  
Current governed release: **v1.0.0**.  
Version: **1.0.0**.

The Library folder was assessed as an operational working collection rather than a complete system package. This repository release supplies the missing canonical governance, reusable template, schema, example record, validation, public-safe pilot evidence, and release controls without publishing operational screenshots.
