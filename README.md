# Agent Skills

Canonical standalone repository for reusable agent skills. It is intentionally independent from Optiplex_MCP and the Self-Building Computer; reading or invoking these skills does not require changing either system or the frozen Optiplex MCP tool surface.

## Canonical skills

- `prompt-improver/` — optimize an explicitly supplied draft prompt for task success first and brevity second while preserving its task contract.
- `juanify/` — rewrite professional text in Juan's established technical/customer communication style.
- `ponytail/` — apply a deliberately minimal, YAGNI-first approach to coding work.
- `ponytail-review/` — review code specifically for removable over-engineering and unnecessary complexity.
- `memory-maintenance/` — audit or explicitly apply maintenance to Claude Code/Codex memory and instruction files.
- `research-skill/` — execute exhaustive evidence-driven research from an explicit request, optionally ask a few high-value scope questions, save the canonical Markdown report under `research-output/`, and present the result in chat.
- `reddit-search/` — search Reddit broadly, inspect thread/comment evidence, audit query coverage, and synthesize recurring themes and disagreement without coupling the workflow to one Reddit transport.

Each skill is rooted at `<skill>/SKILL.md`; legitimate supporting files live beneath the same skill directory. See `SKILLS.md` for the compact registry and `CHATGPT_BOOTSTRAP.md` for fresh-session usage.

Generated research reports live in `research-output/` and are ignored by Git by default; the reusable skill definitions remain version-controlled independently from research results.
