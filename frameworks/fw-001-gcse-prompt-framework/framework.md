# GCSE Prompt Framework

## Purpose

Use GCSE to turn an underspecified request into a clear instruction for a generative AI system. It works across tools and tasks such as drafting, summarizing, explaining, finding, rewriting, and analyzing information.

## The four elements

### Goal

State the action and desired result. Lead with a precise verb such as *draft*, *summarize*, *compare*, *analyze*, *rewrite*, or *create*.

Key question: **What exactly should the system do or produce?**

### Context

Provide only the background needed to perform the task well: purpose, audience, situation, terminology, constraints, timeframe, and relevant standards.

Key question: **What must the system understand to make the result fit the situation?**

### Source

Name or supply the material the system should use, such as selected text, a document, table, email thread, transcript, notes, webpage, or dataset. Identify which source governs when several sources conflict.

Key question: **What evidence or material should ground the response?**

If no source is available, use an actionable placeholder rather than inventing one:

`[Attach, paste, select, or reference the material the system should use.]`

### Expectation

Define what success looks like: format, structure, length, tone, detail, audience level, required sections, exclusions, quality criteria, and review needs.

Key question: **What should the finished response look and sound like?**

## Operating rules

- Preserve the user's legitimate intent.
- Use all four headings when consistency or reviewability matters.
- Separate unrelated goals into different prompts.
- Include only context that materially helps the task.
- Prefer a specific source; identify missing or conflicting source information.
- Use bracketed placeholders for information the user must supply.
- State what the system must not invent when accuracy matters.
- Keep consequential decisions with a responsible human reviewer.
- Use follow-up prompts to refine a useful first response.

## Quality standard

A complete GCSE prompt:

1. names a specific action and result;
2. supplies the purpose, audience, and relevant constraints;
3. identifies usable source material or an actionable placeholder;
4. defines the response format and quality requirements;
5. distinguishes facts from assumptions and unresolved gaps;
6. avoids unnecessary sensitive information; and
7. can be used after its placeholders are completed.

## Full pattern

```text
Goal

[State the action and desired result.]

Context

[Provide the purpose, audience, relevant background, constraints, and terminology.]

Source

[Identify or attach the material to use. State source priority when needed.]

Expectation

[Define format, structure, length, tone, detail, required content, exclusions, and quality checks. Instruct the system to identify unsupported or missing information rather than invent it.]
```

## When to adapt the pattern

- For a simple, low-risk task, keep each element to one sentence.
- For source-sensitive work, strengthen Source with scope, date, and priority rules.
- For a complex deliverable, strengthen Expectation with sections, acceptance criteria, and exclusions.
- For iterative work, use one GCSE prompt per stage and review before continuing.
