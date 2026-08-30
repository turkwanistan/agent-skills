# GPT-5.6

Use this adapter when GPT-5.6 / current ChatGPT reasoning behavior is the target, not merely because this skill happens to be executed by GPT.

- Prefer direct, natural, outcome-oriented prompts and zero-shot first.
- Preserve relevant context, hard constraints, success criteria, output contracts, freshness requirements, and autonomy boundaries when they materially define success.
- Leave implementation freedom unless the user selected a method or the path itself matters.
- Remove generic "think step by step", "think harder", repeated reasoning instructions, generic self-review loops, emotional pressure, excessive `MUST`/`CRITICAL`, and engineering ceremony whose only purpose is to make the model reason more.
- Do not move model/product controls into prompt prose when they are already controlled by the surface or harness.
- Do not add broad verbosity instructions unless output length is actually a requirement; make the requested artifact shape concrete instead.
- Keep examples only when they encode a product requirement, strict pattern, or measured failure mode. Do not add few-shot examples by default.
- Preserve visible derivations, explanations, tests, verification, or intermediate artifacts when the user explicitly requires them.
- For current-information tasks, make freshness or re-checking explicit only when strongly entailed by the requested outcome.
- For tool-using or coding agents, prioritize clear outcome, authority/source of truth, action boundaries, and completion conditions over narrated step-by-step procedure.
