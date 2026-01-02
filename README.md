# Autohand Community Skills

A curated collection of skills for the [Autohand CLI](https://github.com/autohandai/autohand) coding agent.

## What are Skills?

Skills are structured knowledge files that teach Autohand how to work with specific technologies, frameworks, and patterns. They provide context, best practices, and code examples that help the AI assistant generate better code.

## Installation

Install skills directly from Autohand CLI:

```bash
# Open the skills browser
autohand --skill-install

# Or install a specific skill directly
autohand --skill-install typescript-refactoring-patterns

# Install to project level (instead of user level)
autohand --skill-install react-component-architecture --project
```

Or use the slash command within an Autohand session:

```
/skills install
```

## Available Skills

### Featured

| Skill | Description | Rating |
|-------|-------------|--------|
| [typescript-refactoring-patterns](./typescript-refactoring-patterns) | Expert TypeScript refactoring patterns for cleaner, type-safe code | ⭐ 4.9 |
| [react-component-architecture](./react-component-architecture) | Modern React component patterns with hooks, composition, and TypeScript | ⭐ 4.8 |
| [nextjs-app-router-mastery](./nextjs-app-router-mastery) | Next.js 14+ App Router patterns, server components, and data fetching | ⭐ 4.9 |
| [testing-strategies](./testing-strategies) | Comprehensive testing strategies with Vitest, Jest, and Testing Library | ⭐ 4.8 |
| [tailwind-ui-patterns](./tailwind-ui-patterns) | Tailwind CSS v4 patterns, component styling, and responsive design | ⭐ 4.8 |
| [cli-tool-development](./cli-tool-development) | Build professional CLI tools with Node.js, commander, and Ink | ⭐ 4.7 |

### Languages

| Skill | Description | Rating |
|-------|-------------|--------|
| [typescript-refactoring-patterns](./typescript-refactoring-patterns) | Expert TypeScript refactoring patterns | ⭐ 4.9 |
| [error-handling-patterns](./error-handling-patterns) | Robust error handling patterns for TypeScript | ⭐ 4.5 |

### Frameworks

| Skill | Description | Rating |
|-------|-------------|--------|
| [react-component-architecture](./react-component-architecture) | Modern React component patterns | ⭐ 4.8 |
| [nextjs-app-router-mastery](./nextjs-app-router-mastery) | Next.js 14+ App Router patterns | ⭐ 4.9 |
| [python-fastapi-patterns](./python-fastapi-patterns) | FastAPI best practices and async patterns | ⭐ 4.7 |
| [tailwind-ui-patterns](./tailwind-ui-patterns) | Tailwind CSS v4 patterns | ⭐ 4.8 |

### Workflows

| Skill | Description | Rating |
|-------|-------------|--------|
| [cli-tool-development](./cli-tool-development) | Build professional CLI tools | ⭐ 4.7 |
| [api-design-restful](./api-design-restful) | RESTful API design patterns | ⭐ 4.6 |
| [testing-strategies](./testing-strategies) | Comprehensive testing strategies | ⭐ 4.8 |
| [git-workflow-mastery](./git-workflow-mastery) | Advanced Git workflows | ⭐ 4.5 |
| [database-schema-design](./database-schema-design) | Database schema design patterns | ⭐ 4.6 |
| [documentation-writing](./documentation-writing) | Technical documentation best practices | ⭐ 4.4 |

## Skill Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md          # Main skill file (required)
├── templates/        # Optional templates
├── examples/         # Optional examples
└── README.md         # Optional additional docs
```

### SKILL.md Format

```markdown
---
name: skill-name
description: Brief description of the skill
license: MIT
compatibility: requirements (e.g., typescript 5+)
allowed-tools: read_file write_file apply_patch
---

# Skill Name

## Section 1
Content and code examples...

## Section 2
More content...
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. Fork this repository
2. Create a new skill directory with `SKILL.md`
3. Add your skill to `registry.json`
4. Submit a pull request

## License

MIT License - See [LICENSE](./LICENSE) for details.

Skills contributed by the community are licensed under their respective licenses as specified in each skill's frontmatter.
