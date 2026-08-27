# Agent Skills

Canonical standalone repository for reusable agent skills. It is intentionally independent from Optiplex_MCP and the Self-Building Computer; reading or invoking these skills does not require changing either system or the frozen Optiplex MCP tool surface.

## Canonical skills

- `prompt-improver/` — tighten an explicitly supplied draft prompt while preserving its meaning and constraints.
- `juanify/` — rewrite professional text in Juan's established technical/customer communication style.
- `ponytail/` — apply a deliberately minimal, YAGNI-first approach to coding work.
- `ponytail-review/` — review code specifically for removable over-engineering and unnecessary complexity.
- `memory-maintenance/` — audit or explicitly apply maintenance to Claude Code/Codex memory and instruction files.

Each skill is rooted at `<skill>/SKILL.md`; legitimate supporting files live beneath the same skill directory. See `SKILLS.md` for the compact registry and `CHATGPT_BOOTSTRAP.md` for fresh-session usage.
