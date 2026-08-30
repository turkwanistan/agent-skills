# Conditional Prompt-Technique Policy

Use this reference only when a draft is complex enough that a prompting technique materially affects success. The default is not to add techniques; each one must solve a real failure risk.

| Technique | Default | Preserve/add when | Remove/avoid when |
| --- | --- | --- | --- |
| Outcome-first framing | Prefer | The goal is buried or fragmented | Already clear |
| Functional role | Conditional | Perspective, authority, audience, or domain duty changes the answer | Generic "world-class expert" decoration |
| Few-shot examples | Zero-shot first | A non-obvious pattern, exact classification boundary, or output behavior is hard to specify otherwise | Examples merely repeat instructions or add pattern noise |
| Delimiters / headings | Conditional | They separate instructions from large data/examples or make constraints parseable | Short/simple prompt |
| XML-like structure | Conditional | Target benefits and embedded sections are otherwise ambiguous | Decorative structure |
| Explicit decomposition | Conditional | Intermediate artifacts, distinct evaluators/tools, user-visible gates, or ordered dependencies matter | It only narrates internal reasoning |
| Visible reasoning / derivation | Preserve if requested | Explanation, calculation, proof, auditability, or teaching is the deliverable | Generic "think step by step" intended only to improve hidden reasoning |
| Self-review / reflection | Conditional | A concrete review artifact or failure check is required | Ritual "review three times" / blanket self-critique |
| Verification | Conditional | The task needs factual, test, schema, or current-state validation | Redundant with harness/model behavior or not part of success |
| Tool instructions | Conditional | Tool choice or source is required, or a tool boundary matters | Forced tool use with no task benefit |
| Freshness / current-state rule | Conditional | Present availability, prices, laws, schedules, status, news, or other changing facts define success | Static task or supplied-text transformation |
| Source / grounding rule | Conditional | Authority, provenance, or evidence quality materially defines success | User did not ask for research or sourcing |
| Output schema | Preserve/add when necessary | Downstream parser, copy/paste surface, fixed fields, or exact format matters | Decorative template that constrains useful content |
| Fallback / uncertainty behavior | Conditional | Missing evidence would otherwise cause guessing or unsafe action | No meaningful uncertainty path |
| Negative instructions | Use sparingly | A predictable failure must be explicitly prohibited | Long lists of unlikely mistakes |
| Priority order | Make explicit if known | User supplied competing priorities | Priority is unknown; never invent it |
| Long-context placement | Conditional | Critical instructions risk being lost among large embedded data | Small prompt |
| Repetition / emphasis | Minimize | Rare true invariant needs emphasis | Repeated `MUST`, `IMPORTANT`, `CRITICAL` adds no semantics |
| Model settings in prose | Avoid | The prompt itself is the only available control and the user explicitly needs it | Surface/harness already controls reasoning, tools, verbosity, etc. |

## Decision rule

Before adding or preserving a technique, ask only whether it provides a credible task-success benefit for this draft and target. If two formulations are likely to work equally well, choose the shorter and less procedural one.

## Examples are requirements, not decoration

A useful example should encode something that prose alone would leave ambiguous. Keep it minimal and representative. Do not invent domain facts merely to create an example.

## Process versus outcome

Prefer specifying the result and constraints over narrating how the model should think. Preserve explicit process requirements when the process itself is part of the user's decision, audit trail, safety boundary, or deliverable.

## Grounding and freshness

Do not inject research ceremony into ordinary transformations. Add grounding, source hierarchy, or current-state checks only when the outcome logically depends on external facts being authoritative or fresh.
