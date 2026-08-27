---
name: memory-maintenance
description: Manually audit or clean Claude Code and Codex memory and instruction files. Invoke only as /memory-maintenance in Claude Code or $memory-maintenance in Codex; never trigger automatically.
disable-model-invocation: true
---

# Memory maintenance

Optimize permanent context for the fewest high-signal tokens. `AGENTS.md` is canonical policy; Claude/Codex generated memory is recall. No argument means read-only audit. Only the exact argument `apply` permits edits; reject other arguments and never infer apply mode.

## Cheap inventory

1. List paths, file types, byte sizes, and symlink targets before reading content: `~/.claude/CLAUDE.md`, `~/.claude/projects/*/memory/MEMORY.md`, `~/.codex/AGENTS.md`, `~/.codex/memories/{memory_summary.md,MEMORY.md}`, and `~/Projects/**/{AGENTS.md,CLAUDE.md}`. Exclude `.git`, `node_modules`, `vendor`, `addons`, build/cache trees, `ai-context-export`, and export/backup/generated copies unless explicitly in scope.
2. Read nearby project instructions before judging repository files. Read `~/Projects/docs/AGENT_MEMORY.md` when present.
3. Read Codex `memory_summary.md` before any other Codex memory. Search large files only for a specific indexed topic; never use empty, `.`/all-lines, heading-only, or broad catch-all patterns.
4. Treat every `~/.codex/memories/*` path as generated, read-only state: never edit, delete, rename, move, or recreate it.
5. Hard cap routine audits at 12 content files, 500 total lines, and four linked topic files. Never concatenate full instruction files; inspect headings and targeted ranges. Defer rather than exceed any cap.

## Classify

Route each questionable item once:

- Needed for almost every task, stable, verified, and non-obvious -> nearest `AGENTS.md`.
- Mandatory only for Claude -> `CLAUDE.md` or `.claude/rules/`; keep `CLAUDE.md` a thin `@AGENTS.md` adapter plus genuine Claude-only deltas.
- Repeatable multi-step procedure -> skill.
- Durable explanation or reference -> `docs/`.
- Useful learned, non-authoritative fact -> Claude auto-memory.
- Current task, status, backlog, or handoff -> `PLAN.md` or `PROGRESS.md`.
- Derivable, duplicate, stale, speculative, sensitive, unrelated, or low-value -> remove.

Prune directory tours, manifest-derived dependencies, generic advice, tool-enforced rules, old status, duplication, stale paths, unsupported conclusions, credentials, and personal/financial/health details. Keep verified recurring discoveries, environment quirks, repeated-error preventions, compact pointers, and stable constraints.

## Audit

- Verify proposed promotions against current code, manifests, tooling, or authoritative docs.
- Compare overlapping instruction chains; defer conflicts lacking decisive evidence.
- Never reveal sensitive values; report only the path and a sanitized issue.
- Count classifications, list only notable proposed actions, and make no writes of any kind.
- Count every Codex-generated-memory issue as `DEFER`, never `PRUNE` or `PROMOTE`.

## Apply

- Re-verify immediately before editing and preview the exact change set.
- May prune Claude auto-memory; promote verified rules to the nearest `AGENTS.md`; simplify duplicated `CLAUDE.md`; move clear procedures, references, or state to an existing skill, docs, `PLAN.md`, or `PROGRESS.md`; and repair obviously stale paths.
- Preserve managed/generated blocks and marker lines exactly. Do not restructure unrelated configuration or add permanent instructions without demonstrated recurring value.
- Defer unclear scope, ownership, truth, or destination. Re-read changed files afterward and confirm no Codex-generated memory changed.

## Output

Emit exactly the selected template: integer counts, no code fence, preamble, category headings,
summary, or follow-up. Replace the final placeholder with only notable action lines, or omit it.

Audit mode:

```text
Memory audit

PROMOTE: N
PRUNE: N
KEEP: N
DEFER: N

<only notable proposed actions>
```

Apply mode:

```text
Memory maintenance complete

Changed:
- <file>: <short reason>

Promoted: N
Pruned: N
Deferred: N
```

Use native shell/file tools only. Add no dependency, MCP, database, daemon, cron, or service.
