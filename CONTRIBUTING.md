# Contributing to Autohand Community Skills

Thank you for your interest in contributing! Every skill helps make Autohand smarter for everyone.

## Ways to Contribute

- **Submit a new skill** — Share your expertise with the community
- **Improve existing skills** — Fix bugs, update examples, or add patterns
- **Report issues** — Found a problem? [Open an issue](../../issues/new/choose)
- **Review PRs** — Help review skill submissions from other contributors

## Creating a New Skill

### Option 1: Submit via Issue Template

The easiest way to contribute. [Open a new skill issue](../../issues/new?template=new-skill.yml) and fill out the form. A maintainer will create the PR for you.

### Option 2: Submit via Web

Use the [guided submission form](https://skilled.autohand.ai/submit) on skilled.autohand.ai.

### Option 3: Submit a Pull Request

1. **Fork** this repository
2. **Create** your skill directory:
   ```bash
   mkdir my-skill-name
   cd my-skill-name
   touch SKILL.md
   ```
3. **Write** your `SKILL.md` (see format below)
4. **Add** your skill to `registry.json`
5. **Submit** a pull request with title: `feat: add <skill-name> skill`

## SKILL.md Format

Every skill requires a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: my-skill-name
description: A brief description (under 100 characters)
license: MIT
compatibility: typescript 5+, nodejs 18+
allowed-tools: read_file write_file apply_patch run_command
---

# Skill Title

## Overview
Brief introduction to what this skill covers.

## Core Concepts
Key concepts and principles.

## Patterns
Code examples and patterns.

## Best Practices
Numbered list of recommendations.
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Skill identifier (kebab-case) |
| `description` | Yes | Brief description (under 100 characters) |
| `license` | Yes | An OSI-approved license (see [Licensing](#licensing)) |
| `compatibility` | Yes | Version requirements |
| `allowed-tools` | No | Tools the skill can use |

### Content Guidelines

- **Be concise** — Focus on practical patterns and examples
- **Use code blocks** — Show real, working code with language identifiers
- **Structure clearly** — Use headers for scanability
- **Stay current** — Reference latest stable versions
- **Be opinionated** — Share best practices, not just options
- **One focus per skill** — Each skill should cover a single technology or pattern

## Registry Entry

Add your skill to `registry.json`:

```json
{
  "id": "my-skill-name",
  "name": "my-skill-name",
  "description": "Brief description",
  "category": "frameworks",
  "tags": ["tag1", "tag2", "tag3"],
  "languages": ["typescript"],
  "frameworks": ["react"],
  "isFeatured": false,
  "isCurated": false,
  "rating": 0,
  "downloadCount": 0,
  "directory": "my-skill-name",
  "files": ["SKILL.md"],
  "version": "1.0.0",
  "license": "MIT",
  "author": "your-github-username"
}
```

### Categories

| Category | Description |
|----------|-------------|
| `languages` | Programming language patterns (TypeScript, Python, etc.) |
| `frameworks` | Framework-specific skills (React, Next.js, FastAPI, etc.) |
| `workflows` | Development workflows (testing, git, API design, etc.) |
| `cloud` | Cloud platforms (AWS, Azure, GCP, Kubernetes, etc.) |
| `marketing` | SEO, analytics, content strategy, A/B testing |
| `agent-skills` | Browser automation, email, evaluation, configuration |
| `design` | UI patterns, Tailwind, accessibility, responsive |
| `ai-tools` | LLM integration, image/video generation, embeddings |
| `quality` | Code review, linting, security, performance |
| `devops` | Docker, monitoring, infrastructure, observability |
| `documentation` | Technical writing, API docs, changelogs |
| `documents` | Document processing (PDF, DOCX, XLSX, etc.) |

### Tags

Use 3-5 relevant, lowercase tags:
- Technology names: `typescript`, `react`, `nodejs`
- Concepts: `patterns`, `testing`, `architecture`

## Multi-File Skills

Skills can include additional files beyond `SKILL.md`:

```
my-skill/
├── SKILL.md              # Required
├── templates/
│   ├── component.tsx
│   └── test.tsx
├── examples/
│   └── advanced-usage.md
└── README.md
```

Update the `files` array in your registry entry:
```json
"files": ["SKILL.md", "templates/component.tsx", "templates/test.tsx"]
```

## Quality Standards

### Code Examples
- Must be syntactically correct
- Include necessary imports
- Show realistic use cases
- Add comments for clarity

### Documentation
- Clear, concise writing
- Proper markdown formatting
- Working links
- No spelling errors

## Pull Request Process

1. **Title**: `feat: add <skill-name> skill`
2. **Description**: Include what the skill covers, why it's useful, and any prerequisites
3. **Checklist**:
   - [ ] `SKILL.md` follows the format with valid frontmatter
   - [ ] Skill added to `registry.json` with all required fields
   - [ ] Code examples are syntactically correct
   - [ ] No sensitive information (API keys, credentials, etc.)
   - [ ] Skill focuses on a single technology or pattern
   - [ ] License specified in frontmatter

## Updating Existing Skills

1. Fork and create a branch
2. Make your changes
3. Update `version` in the registry entry if the change is significant
4. Submit a PR with a clear description of what changed and why

## Licensing

This repository is licensed under the [MIT License](./LICENSE). The repository infrastructure, registry, and documentation are copyright Autohand AI.

**For contributed skills:**

- You retain authorship credit for skills you create — your GitHub username is recorded in the `author` field of `registry.json`
- You choose the license for your skill by specifying it in the `license` field of your `SKILL.md` frontmatter and `registry.json` entry
- Your chosen license must be an [OSI-approved open source license](https://opensource.org/licenses) (MIT, Apache-2.0, ISC, BSD-2-Clause, etc.)
- If no license is specified, MIT is assumed
- By submitting a skill, you confirm that you have the right to license the content under your chosen license
- Autohand AI may distribute, index, and serve your skill through the registry and [skilled.autohand.ai](https://skilled.autohand.ai) under the terms of your chosen license

## Review Process

Submissions are reviewed for:

- **Accuracy** — Code examples work correctly
- **Quality** — Well-written, clear documentation
- **Relevance** — Useful to the community
- **Originality** — Not duplicating existing skills
- **License** — Valid OSI-approved license specified

## Getting Help

- [Open an issue](../../issues/new/choose) for questions
- Check existing skills for format examples
- Join our [Discord community](https://discord.gg/MWTNudaj8E)

## Code of Conduct

All contributors are expected to follow our [Code of Conduct](./CODE_OF_CONDUCT.md). Please read it before participating.
