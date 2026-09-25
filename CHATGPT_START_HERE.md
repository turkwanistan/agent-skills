# ChatGPT Global Start Here

This file is the global bootstrap for ordinary ChatGPT sessions doing repository-backed work through the existing MCP tools. It does not change any MCP server or tool surface.

## Authority

For software, research, reverse-engineering, automation, and other repository-backed projects, the live repository and its current steering/state files outrank ChatGPT memory, prior-chat summaries, and stale prompts.

Use chat history only as supplemental context when the live repository cannot establish the needed state.

## Default entry path

When a user asks to continue, inspect, debug, implement, research for, plan for, or otherwise work on a repository-backed project:

1. Use **OptiPlex MCP** as the default discovery/bootstrap environment when available.
2. Identify the target project under the existing project workspace. Do not guess if repository discovery can resolve it.
3. Run the project's cheap preflight when available and inspect current Git status/HEAD before substantial work or mutation.
4. Preserve legitimate existing, concurrent, and untracked work. Never assume a clean tree.
5. Read the target repository's `START_HERE.md` when present and follow its routing exactly.
6. Read only the additional steering/state files it requires, commonly `AGENTS.md`, `STATUS.md`, current task/state files, active plans, and selected evidence.
7. Load relevant reusable skills from this `agent-skills` repository when the task or project routing calls for them.
8. Begin work only after current repository state, constraints, and next objective are sufficiently established.

Prefer progressive hydration over recursively reading an entire repository.

## Environment routing

Use the three existing environments according to current project steering and task needs:

- **OptiPlex MCP** — default control/discovery plane; repository inspection and normal project operations; structured Git; managed jobs/services; mediated browser work.
- **WSL-MCP** — use when the target project's live steering says its authoritative execution/runtime environment is WSL-MCP or the required capability exists there. Do not infer this from old chat history when the repo can say.
- **OptiPlex Lab** — disposable/high-permission environment for isolated experiments, heavyweight one-off processing, or transformations that should not directly become durable project state. Persist important findings back into the appropriate repository.

Do not modify an MCP server merely to perform normal project work or invoke a skill unless the user explicitly asks for MCP development.

## Skill routing

`SKILLS.md` is the compact registry. `CHATGPT_BOOTSTRAP.md` defines canonical skill-loading behavior. Each skill's authoritative instructions live at `<skill>/SKILL.md`.

Load skills only when relevant. In particular:

- When producing a substantial executor, orchestration, handoff, or research prompt intended for another AI/agent session, automatically load `prompt-improver` unless the user explicitly asks not to.
- When the user requests exhaustive evidence-driven public research, load `research-skill` unless a higher-priority instruction or task-specific workflow says otherwise.
- Honor explicit `@skill-name` or `/skill-name` requests as defined by `CHATGPT_BOOTSTRAP.md`.

## Durable state and handoffs

Do not make the current ChatGPT conversation the only place where important project state lives.

At natural milestone boundaries, before a requested handoff, or when a long/tool-heavy session is becoming noisy:

1. reconcile what was actually completed and verified;
2. update the project's existing durable status/handoff/state files using its own conventions;
3. record blockers, disproven paths worth avoiding, and the exact next action;
4. run project-defined validation appropriate to the milestone;
5. commit/push only when appropriate and allowed by the project's current rules;
6. recommend a fresh execution context when that would reduce context degradation.

As a soft signal rather than a hard cutoff, consider checkpoint/rollover around 15–20 user turns or roughly 75–100+ tool actions, especially at a natural boundary. Do not interrupt a productive debugging chain solely because a counter was reached.

## Research versus execution

For large research tasks, prefer:

`research -> durable research artifact -> plan/executor`

Do not carry hundreds of raw search results forward when a compact evidence-linked artifact can preserve the conclusions. Executors should consume current project state, the active plan, and relevant research artifacts rather than rerunning broad research by default.

## Failure/stuck behavior

After two materially identical failures, do not blindly repeat the same experiment. Reassess the hypothesis, identify what changed or was learned, choose a materially different diagnostic path, and checkpoint if context has become noisy.

## Fresh-session success criterion

A short request such as `continue opentivoo` should be enough for a fresh ChatGPT session to:

- bootstrap through OptiPlex MCP;
- locate the relevant repository;
- inspect current Git/project state;
- follow that repository's `START_HERE.md` routing;
- load relevant skills;
- determine the current objective/next action;
- continue without requiring the user to paste old chat context.

For ordinary questions unrelated to repository-backed work, do **not** perform this bootstrap.