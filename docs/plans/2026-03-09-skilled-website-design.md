# skilled.autohand.ai - Design Document

**Date:** 2026-03-09
**Status:** Approved
**Repo:** autohandai/skilled (private)
**Domain:** skilled.autohand.ai

## Overview

A skills directory and CLI showcase website for Autohand Code. Combines a skills.sh-style leaderboard with Autohand's terminal-first brand identity, featuring an interactive `/learn` command demo that drives CLI adoption.

## Tech Stack

- **Frontend:** Vue 3 (Composition API) + Vite + Tailwind CSS v4
- **Hosting:** Cloudflare Pages
- **API:** Cloudflare Workers (Functions)
- **Database:** D1 (SQLite) for install tracking
- **Cache:** KV Store for skill data
- **Data Source:** community-skills/registry.json (build-time import)

## Routes

| Route | Purpose |
|-------|---------|
| `/` | Home: hero + leaderboard + CLI showcase |
| `/skill/:id` | Skill detail page with SKILL.md content |
| `/categories/:cat` | Filtered skills by category |
| `/learn` | Interactive /learn command showcase |
| `/submit` | How to submit a skill (links to GH PR) |
| `/docs` | Skill authoring guide + CLI reference |

## Visual Design

### Theme Support
Dark mode (default) and light mode, using CSS variables with `data-theme` attribute.

### Colors

**Dark Mode (Default):**
- Background primary: `#121212`
- Background secondary (cards): `#171A1F`
- Text primary: `#E9EDF1`
- Text secondary: `#B6BCC6`
- Accent: `#8FB3E0` (blue)
- Borders: `#2A2E36`
- Terminal bg: `#0A0A0C`

**Light Mode:**
- Background primary: `#F4F7F5`
- Background secondary: `#FFFFFF`
- Text primary: `#08090A`
- Text secondary: `#575A5E`
- Accent: `#222823`
- Borders: `#A7A2A9`

### Typography
- Headlines: Space Grotesk (300-700)
- Body: IBM Plex Sans (300-600)
- Code/Terminal: JetBrains Mono (400-500)
- Scale: clamp()-based fluid sizing

### Components
- Terminal window chrome (red/yellow/green dots, `#0A0A0C` bg)
- Glass-morphism header (backdrop-blur 12px)
- 2px border-radius (sharp, minimal)
- Card hover lift (-2px translateY)
- Copy-to-clipboard code blocks
- Category pill badges

## Page Designs

### Home Page

**1. Sticky Header**
- Autohand logo (left)
- Nav: Skills, /learn, Docs, Submit (center)
- Search bar with `/` keyboard shortcut (right)
- Theme toggle (dark/light)

**2. Hero Section**
- Terminal window showing animated `autohand code /learn` flow
- Tagline: "The Skills Ecosystem for Autohand Code"
- Subtitle explaining what skills are
- Install CTA: `curl -fsSL https://autohand.ai/install | sh`

**3. Agent Support Bar**
- Horizontal strip showing compatible agents/editors
- Autohand Code as primary, with community agent logos

**4. Skills Leaderboard**
- **Tabs:** All Time | Trending (24h) | Hot | New
- **Layout:** Category sidebar (desktop) / dropdown (mobile) + table
- **Table columns:** Rank | Name | Source | Category (pill) | Installs
- **Search:** Fuzzy search with Fuse.js, real-time filtering
- **Categories:** cloud, marketing, design, frameworks, workflows, ai-tools, agent-skills, documents, quality, devops, documentation, languages, community
- **Pagination:** "Load more" button or infinite scroll

**5. CTA Section**
- Two-column: Install command (left) + `/learn` demo (right)
- Package manager tabs (shell, npm, yarn, pnpm, bun)

**6. Footer**
- Autohand branding, links, GitHub link to community-skills

### Skill Detail Page (`/skill/:id`)

- Skill name (h1), description, install count badge
- Source repo link + author
- Install command: `autohand code --skill-install <skill-name>` (copy button)
- SKILL.md content rendered as markdown (with syntax highlighting via Shiki)
- Related skills grid (same category/tags)
- "Try /learn" CTA

### `/learn` Interactive Showcase

Full-width terminal simulation with animated typing effect showing:
```
$ autohand code /learn
Analyzing repository...
Detected: Vue 3, Tailwind CSS, TypeScript
Found 3 matching skills:

| Skill                        | Match | Installs |
|------------------------------|-------|----------|
| vercel-react-best-practices  | 98%   | 185.7K   |
| tailwind-design-system       | 95%   | 15.7K    |
| typescript-advanced-types    | 92%   | 12.1K    |

? Select skills to install (space to select, enter to confirm)
> [x] vercel-react-best-practices
  [x] tailwind-design-system
  [ ] typescript-advanced-types
```

Below terminal:
- Explanation of `/learn` command
- `--yolo-skills` flag documentation
- Install Autohand Code CTA

### `/docs` Page

Sections:
1. What are Skills?
2. Creating a Skill (SKILL.md format, frontmatter reference)
3. Submitting a Skill (PR to community-skills repo)
4. CLI Commands Reference (`/learn`, `--skill-install`, `--yolo-skills`)
5. API Reference

### `/submit` Page

- Step-by-step guide to submitting a skill
- Link to community-skills CONTRIBUTING.md
- PR template link
- Skill authoring tips

## Data Architecture

```
Cloudflare Pages
├── Vue 3 SPA (static build)
│   └── Reads registry.json at build time
│       └── Generates skill pages
├── Workers API (/api/*)
│   ├── GET  /api/skills          → List/search/filter skills
│   ├── GET  /api/skills/:id      → Single skill detail
│   ├── POST /api/track-install   → Record install event
│   └── GET  /api/trending        → Trending skills (24h/7d)
├── D1 Database
│   └── installs table (skill_id, timestamp, source)
└── KV Store
    └── Cached registry data for API responses
```

**Build pipeline:**
1. GitHub Action on community-skills push triggers rebuild
2. Build script fetches registry.json + all SKILL.md files
3. Generates static pages for each skill
4. Deploys to Cloudflare Pages

**Install tracking:**
1. CLI sends POST to `/api/track-install` on skill install
2. Workers writes to D1 with timestamp
3. Trending endpoint aggregates by time window

## Categories

| ID | Name | Icon |
|----|------|------|
| cloud | Cloud | cloud |
| marketing | Marketing | megaphone |
| design | Design | palette |
| frameworks | Frameworks | layers |
| workflows | Workflows | workflow |
| ai-tools | AI Tools | sparkles |
| agent-skills | Agent Skills | bot |
| documents | Documents | file-text |
| quality | Quality | shield-check |
| devops | DevOps | server |
| documentation | Documentation | book |
| languages | Languages | code |
| community | Community | users |

## Key Differentiators from skills.sh

1. **CLI-first branding** - Terminal aesthetics throughout, not just a data table
2. **`/learn` showcase** - Interactive demo of the killer feature
3. **Autohand Code integration** - All install commands reference `autohand code`
4. **Dark + light theme** - Not just dark mode
5. **Cloudflare-native** - Workers API for real-time tracking
