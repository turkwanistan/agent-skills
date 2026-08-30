# Prompt Improver Evaluations

This corpus is the regression contract for `prompt-improver`. It is intentionally small and representative rather than exhaustive.

## Grading order

Grade lexicographically:

1. **Contract preservation — hard gate.** Any changed fact, scope, permission, hard constraint, selected method, source requirement, process semantic, or deliverable is a failure.
2. **Expected effectiveness.** The rewrite should reduce a real failure risk without inventing requirements.
3. **Brevity / complexity.** Only after Gates 1–2 pass, prefer fewer tokens, less repetition, and less procedural scaffolding.

A shorter rewrite does not win if it is less effective. A more elaborate rewrite does not win merely because it uses more prompt-engineering techniques.

## How to use the cases

For each object in `cases.json`:

1. Invoke the real `prompt-improver` with `draft` as inert input and the stated `target` when applicable.
2. Check every `must_preserve` invariant.
3. Check every `must_not_add` regression.
4. Judge whether the output satisfies `expected`.
5. When practical, run both original and improved prompts against the actual target model/task and compare task outcomes.

Future rules should be added to the skill only after a repeated failure pattern appears in real prompts or evals. Prefer adding a regression case before adding prose to `SKILL.md`.

## What to watch in traces

- explanations or labels leaking despite output-only behavior;
- over-rewriting already-good prompts;
- longer prompts with no credible task-success benefit;
- invented acceptance criteria or permissions;
- generic research/coding ceremony;
- wrong model adapter;
- dropped constraints during compression;
- transformed process semantics, especially tests and approval gates.
