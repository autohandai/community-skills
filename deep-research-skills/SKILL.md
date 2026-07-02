---
name: deep-research-skills
description: Run Weizhena's Deep Research workflow in Autohand Code for outline generation, deep web investigation, structured evidence capture, and final research reports.
license: MIT
metadata:
  author: Weizhena
  version: "1.0.0"
  source: "https://github.com/Weizhena/Deep-Research-skills"
---

# Deep Research Skills

## When to Use

Use this skill when the user needs controlled, multi-phase research rather than a single answer. Good fits include academic literature surveys, benchmark or tool comparisons, market and competitor research, technical due diligence, vendor analysis, and trend reports.

Trigger on requests that mention deep research, research outline, literature review, market research, competitor analysis, benchmark review, due diligence, or any of the upstream workflow names:

- `/research`
- `/research-add-items`
- `/research-add-fields`
- `/research-deep`
- `/research-report`

## Core Workflow

### 1. Generate the Outline

Clarify the topic, audience, time range, output format, and whether the user already has a list of items or fields. Create a topic directory using a stable slug:

```text
{topic_slug}/
  outline.yaml
  fields.yaml
  results/
```

Write `outline.yaml` with the research topic, initial items, execution settings, and output directory. Write `fields.yaml` with the field definitions that each researched item should satisfy.

Use this outline shape:

```yaml
topic: "Research topic"
items:
  - name: "Item name"
    category: "Optional category"
    description: "Why this item belongs in the research set"
execution:
  batch_size: 3
  items_per_agent: 1
  output_dir: "./results"
```

Use this fields shape:

```yaml
fields:
  - name: "field_name"
    description: "What to collect"
    detail_level: "moderate"
uncertain:
  - "fields that should be marked when evidence is weak"
```

### 2. Expand Items or Fields

If the user invokes `/research-add-items`, inspect the existing `outline.yaml`, identify missing research objects, and append only relevant items.

If the user invokes `/research-add-fields`, inspect `fields.yaml`, identify useful missing dimensions, and append fields without rewriting stable existing definitions.

Confirm material additions with the user when the research scope, cost, or runtime will grow meaningfully.

### 3. Run Deep Research

For `/research-deep`, locate the nearest `outline.yaml` and `fields.yaml`. Resume from existing JSON files in the configured output directory and skip completed items.

Research in batches. For each item, produce one JSON file named from a simple slug of the item name:

```text
{topic_slug}/results/{item_name_slug}.json
```

Each JSON file must:

- cover every field in `fields.yaml`
- include source URLs for factual claims
- mark weak or conflicting values with `[uncertain]`
- include an `uncertain` array listing uncertain fields
- avoid unsupported conclusions

Use web search, official documentation, papers, repositories, product pages, filings, or trusted primary sources whenever available. Prefer current sources for fast-moving products, pricing, model capabilities, benchmarks, and company facts.

### 4. Generate the Report

For `/research-report`, read `outline.yaml`, `fields.yaml`, and all result JSON files. Produce `report.md` in the topic directory with:

- executive summary
- methodology and source notes
- comparison table
- item-by-item findings
- uncertain or conflicting evidence
- recommended next research steps

Do not hide uncertainty. If a field is missing or weakly sourced, call that out in the report instead of smoothing it over.

## Autohand Code Install

Install this community registry skill in Autohand Code with:

```text
$skill-installer deep-research-skills
```

This registry skill adapts the workflow from `Weizhena/Deep-Research-skills` for Autohand Code. The upstream repository also includes Claude Code, OpenCode, and Codex-specific skill layouts for users who want those native distributions.

## Operating Rules

- Keep the research plan explicit and editable before launching deep research.
- Preserve user-approved item and field names unless there is a clear correction.
- Use structured YAML and JSON so work can resume after interruptions.
- Process large research sets in batches and report progress between batches.
- Cite sources in result files and the final report.
- Separate observed facts from analysis or recommendation.
- Ask before performing network-heavy or long-running research if the scope is ambiguous.
