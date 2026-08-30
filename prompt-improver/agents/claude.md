# Claude

Use this adapter when Claude is the target, even if the improver itself is running in another model or surface. Treat explicit `/prompt-improver` invocation like `@prompt-improver` where the host supports it.

- Prefer clear, direct goals with relevant context and explicit constraints; do not add generic expert personas or motivational language.
- Preserve useful examples when they encode a real pattern. Do not add examples merely as prompt-engineering ceremony.
- Use headings, delimiters, or XML-like structure only when they materially separate instructions, examples, or large embedded data; do not add them to simple prompts.
- Do not add blanket self-review, redundant verification loops, or unnecessary tool-use instructions. Preserve task-specific verification requirements the user actually asked for.
- Preserve implementation freedom unless the user selected the method or process.
- Preserve exact process semantics: "run the tests" must not become "confirm they pass", "make all tests pass", or any new acceptance requirement.
- Preserve explicit requests for explanations, rationale, intermediate artifacts, or staged gates when they are part of the deliverable.
- Keep action and approval boundaries explicit for agentic tasks without expanding permissions.
