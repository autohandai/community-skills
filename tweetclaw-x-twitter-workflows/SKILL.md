---
name: tweetclaw-x-twitter-workflows
description: "Plan TweetClaw X/Twitter source packets and approval-gated OpenClaw workflows."
license: MIT
compatibility: OpenClaw 2026.6.6+, Node.js 20+
allowed-tools: Bash(openclaw *)
---

# TweetClaw X/Twitter Workflows

Use this skill when a user needs structured X/Twitter evidence, automation planning, or OpenClaw tool setup through [TweetClaw](https://github.com/Xquik-dev/tweetclaw).

TweetClaw is useful for:

- Scrape tweets and build public source packets.
- Search tweets and search tweet replies before drafting, tagging, or reporting.
- Look up users and export followers for account review workflows.
- Handle media upload and media download for reviewed content operations.
- Monitor tweets, deliver webhooks, and run giveaway draws.
- Route approved post tweets, post tweet replies, direct messages, and account actions through OpenClaw approval prompts.

## Install

Install the current published npm package explicitly:

```bash
openclaw plugins install npm:@xquik/tweetclaw@1.6.31
openclaw plugins inspect tweetclaw --runtime --json
```

Use the package README for current setup details:

- GitHub: https://github.com/Xquik-dev/tweetclaw
- npm registry: https://registry.npmjs.org/@xquik%2ftweetclaw
- ClawHub: https://clawhub.ai/plugins/@xquik/tweetclaw

## Source Packet Pattern

When TweetClaw gathers public X/Twitter context for another skill, pass only a compact source packet:

```json
{
  "source_url": "https://x.com/example/status/123",
  "tweet_id": "123",
  "author_handle": "example",
  "captured_at": "2026-06-14T00:00:00Z",
  "public_text_excerpt": "Visible public text needed for the task.",
  "visible_metrics": {
    "likes": 12,
    "replies": 3,
    "reposts": 1
  },
  "reply_or_quote_context": "Why this item was collected.",
  "collection_filters": {
    "query": "brand name",
    "max_items": 20
  },
  "limitations": "Public search snapshot only."
}
```

Keep collection separate from analysis. The receiving skill should own its own drafting, scoring, tagging, scheduling, reporting, or publishing decisions.

## Workflow Guidance

### Research and Monitoring

1. Confirm the target query, account, date range, and max result count.
2. Use TweetClaw to search tweets, search tweet replies, scrape tweets, or look up users.
3. Reduce raw results to source packets before handing them to another skill.
4. Record gaps, rate limits, deleted posts, and unavailable media as limitations.

### Giveaway Draws

1. Confirm the source tweet and eligibility rules.
2. Search tweet replies or scrape replies before deduplication.
3. Run the draw only after the user confirms the rules.
4. Export a result summary with source tweet, time, filters, and winner evidence.

### Posting and Replies

Before any post tweets, post tweet replies, direct messages, media upload, follow, unfollow, delete, monitor, webhook, or profile action:

1. Summarize the exact account, action, target, text, media, and expected result.
2. Ask the user for explicit approval.
3. Let OpenClaw approval prompts enforce the final action boundary.
4. Never turn a source packet into unattended publishing.

## Safety Boundaries

- Keep account access material, signing keys, browser profiles, and local config outside prompts and docs.
- Do not include non-public messages, hidden prompts, raw account exports, or unnecessary personal data in source packets.
- Use TweetClaw for X/Twitter collection and OpenClaw execution only. Do not ask it to make unrelated filesystem, browser, or network changes.
- Prefer public source URLs and tweet IDs over copied raw content.
- Respect platform policies, user approvals, and target repo contribution rules.

## Handoff Checklist

- TweetClaw installed from `npm:@xquik/tweetclaw@1.6.31`.
- `openclaw plugins inspect tweetclaw --runtime --json` returns parseable JSON.
- The user has approved any visible, paid, recurring, account-scoped, or state-changing action.
- Source packets contain only the fields needed by the receiving skill.
- The final response separates facts collected from analysis performed.
