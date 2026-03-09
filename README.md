# Autohand Community Skills

A curated collection of 200+ skills for the [Autohand](https://autohand.ai) CLI coding agent.

Browse all skills at [skilled.autohand.ai](https://skilled.autohand.ai).

## What are Skills?

Skills are structured knowledge files that teach Autohand how to work with specific technologies, frameworks, and patterns. They provide context, best practices, and code examples that help the AI assistant generate better code from the start.

Instead of repeatedly explaining your stack, conventions, or architecture patterns, you install the relevant skills and Autohand immediately understands how to work within your project.

## Getting Started

### 1. Install Autohand

```bash
# Shell (macOS / Linux)
curl -fsSL https://autohand.ai/install | sh

# npm
npm install -g autohand

# bun
bun install -g autohand
```

### 2. Discover skills for your project

Autohand has two modes: **interactive** (slash commands inside a session) and **non-interactive** (flags passed directly).

#### Interactive mode

Start a session and use `/learn` to analyze your project:

```bash
autohand
> /learn
```

`/learn` uses a two-phase LLM-powered advisor:

1. **Analyze + Rank** — scans your project structure, audits installed skills for redundancy, and ranks community skills by relevance (0-100)
2. **Generate** — if no community skill scores above 60, offers to generate a custom skill tailored to your project

For a deeper scan that reads source files:

```
> /learn deep
```

To re-analyze and regenerate outdated skills:

```
> /learn update
```

#### Non-interactive mode

Run skill operations directly from the terminal without starting a session:

```bash
# Analyze project and install recommended skills
autohand --learn

# Re-analyze and regenerate outdated skills
autohand --learn-update

# Auto-generate 3 skills based on detected stack
autohand --auto-skill
```

### 3. Install specific skills

#### Interactive

```bash
autohand
> /skills install
```

Browse and install community skills interactively.

#### Non-interactive

```bash
# Install a specific skill
autohand --skill-install typescript-refactoring-patterns

# Install at project level (instead of user/global level)
autohand --skill-install react-component-architecture --project
```

## Managing Skills

Inside an Autohand session, use these `/skills` commands:

| Command | Description |
|---------|-------------|
| `/skills` | List all available skills |
| `/skills use <name>` | Activate a skill for the current session |
| `/skills deactivate <name>` | Deactivate an active skill |
| `/skills info <name>` | Show detailed skill information |
| `/skills install` | Browse and install community skills |
| `/skills new` | Create a new skill with a guided wizard |
| `/skills feedback <slug> <1-5>` | Rate a community skill |

## Skill Categories

| Category | Count | Description |
|----------|-------|-------------|
| Workflows | 42 | Git, CI/CD, testing, API design, deployment |
| Cloud | 40 | AWS, Azure, GCP, Kubernetes, Terraform |
| Marketing | 25 | SEO, analytics, content strategy, A/B testing |
| Agent Skills | 21 | Browser automation, email, evaluation, configuration |
| Frameworks | 16 | React, Next.js, Vue, FastAPI, Django, Rails |
| Design | 15 | UI patterns, Tailwind, accessibility, responsive |
| AI Tools | 12 | LLM integration, image/video generation, embeddings |
| Quality | 9 | Code review, linting, security, performance |
| DevOps | 9 | Docker, monitoring, infrastructure, observability |
| Documentation | 12 | Technical writing, API docs, changelogs |
| Languages | 4 | TypeScript, Python, Rust, Go patterns |

## Skill Structure

Each skill is a directory with a `SKILL.md` file:

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
metadata:
  author: your-name
  version: "1.0.0"
---

# Skill Name

## When to Use
Describe when this skill should be activated...

## Patterns
Concrete code examples and best practices...
```

### Skill Discovery Locations

Skills are loaded from these locations (later sources take precedence):

1. `~/.autohand/skills/` — user-level (global)
2. `<project>/.autohand/skills/` — project-level

## Contributing

We welcome contributions from the community. Every skill helps make Autohand smarter for everyone.

### Quick Start

1. **Fork** this repository
2. **Create** your skill directory:
   ```bash
   mkdir my-skill-name
   ```
3. **Write** your `SKILL.md` file with frontmatter metadata and content
4. **Add** your skill to `registry.json`:
   ```json
   {
     "id": "my-skill-name",
     "name": "My Skill Name",
     "description": "Brief description",
     "category": "workflows",
     "author": "your-github-username",
     "source": "community"
   }
   ```
5. **Submit** a pull request

### Writing Effective Skills

- Start with a clear description of what the skill covers and when to use it
- Include concrete code examples, not just abstract guidance
- Organize content with clear headings and sections
- Keep individual skills focused — one technology or pattern per skill
- Use fenced code blocks with language identifiers for syntax highlighting
- Test your skill by installing it locally: copy to `~/.autohand/skills/` and verify it works in a session

### Review Process

Pull requests are reviewed for:

- **Quality** — clear writing, concrete examples, actionable guidance
- **Accuracy** — correct patterns, up-to-date APIs, working code
- **Format** — valid frontmatter, proper SKILL.md structure
- **Scope** — focused on a single technology or pattern

You can also use the [Submit page](https://skilled.autohand.ai/submit) on skilled.autohand.ai for a guided walkthrough.

## Links

- [skilled.autohand.ai](https://skilled.autohand.ai) — Browse and search all skills
- [autohand.ai](https://autohand.ai) — Main Autohand website
- [CLI Documentation](https://autohand.ai/docs) — Full CLI reference
- [Discord](https://discord.gg/MWTNudaj8E) — Community chat

## License

MIT License — see [LICENSE](./LICENSE) for details.

Skills contributed by the community are licensed under their respective licenses as specified in each skill's frontmatter.
