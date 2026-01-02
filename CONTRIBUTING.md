# Contributing to Autohand Community Skills

Thank you for your interest in contributing to the Autohand community skills collection!

## How to Contribute

### Creating a New Skill

1. **Fork this repository**

2. **Create a new skill directory**
   ```bash
   mkdir my-new-skill
   cd my-new-skill
   touch SKILL.md
   ```

3. **Write your SKILL.md file** following the format below

4. **Add your skill to registry.json**

5. **Submit a pull request**

## Skill File Format

Every skill must have a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: my-skill-name
description: A brief description (under 100 characters)
license: MIT
compatibility: requirements (e.g., typescript 5+, nodejs 18+)
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
| `description` | Yes | Brief description (< 100 chars) |
| `license` | Yes | License (MIT recommended) |
| `compatibility` | Yes | Version requirements |
| `allowed-tools` | No | Tools the skill can use |

### Content Guidelines

- **Be concise** - Focus on practical patterns and examples
- **Use code blocks** - Show real, working code
- **Structure clearly** - Use headers for scanability
- **Stay current** - Reference latest stable versions
- **Be opinionated** - Share best practices, not just options

## Registry Entry

Add your skill to `registry.json`:

```json
{
  "id": "my-skill-name",
  "name": "my-skill-name",
  "description": "Brief description",
  "category": "frameworks",
  "tags": ["tag1", "tag2"],
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

- `languages` - Programming language patterns (TypeScript, Python, etc.)
- `frameworks` - Framework-specific skills (React, Next.js, FastAPI, etc.)
- `workflows` - Development workflows (testing, git, API design, etc.)

### Tags

Use relevant, lowercase tags:
- Technology names: `typescript`, `react`, `nodejs`
- Concepts: `patterns`, `testing`, `architecture`
- Keep to 3-5 tags

## Multi-File Skills

Skills can include additional files:

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

Update `files` array in registry:
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

2. **Description**: Include:
   - What the skill covers
   - Why it's useful
   - Any prerequisites

3. **Checklist**:
   - [ ] SKILL.md follows the format
   - [ ] Added to registry.json
   - [ ] Code examples are correct
   - [ ] No sensitive information

## Updating Existing Skills

1. Fork and create a branch
2. Make your changes
3. Update version in registry if significant
4. Submit PR with clear description of changes

## Review Process

Submissions are reviewed for:

- **Accuracy** - Code examples work correctly
- **Quality** - Well-written, clear documentation
- **Relevance** - Useful to the community
- **Originality** - Not duplicating existing skills

## Getting Help

- Open an issue for questions
- Check existing skills for examples
- Join our Discord community

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn

Thank you for contributing!
