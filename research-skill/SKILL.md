---
name: research-skill
description: Execute exhaustive, evidence-driven research from an explicit user request, optionally asking a small number of high-value scope questions, then save the finished report as Markdown and present it in chat. Use only when explicitly invoked as /research-skill, @research-skill, or through the host's explicit skill command.
---

# Research Skill

Execute the research. Do not merely rewrite the user's request into a better research prompt and stop there.

Treat the text after the invocation as the research task. The optional literal word `research` immediately after the skill name is syntactic sugar and does not change behavior.

Examples:

- `/research-skill research why dogs like to sleep by my feet`
- `/research-skill chickens`
- `@research-skill compare current local-first note-taking apps for a privacy-sensitive researcher`

This skill is deliberately a **hybrid research controller**: be strict about epistemic quality, verification, and deliverables while retaining autonomy over the exact search plan.

Before executing, read:

1. `references/research-protocol.md` for the durable research principles and quality gates.
2. `references/research-maxxing-template.md` as the canonical high-performance scaffold.

Use those references as a combined operating standard. Do not mechanically paste the entire template into the conversation or create an unnecessary intermediate prompt when you can execute its requirements directly.

## 1. Scope triage

First determine whether a clarification would have substantial expected value.

Ask **zero to three** concise questions in one batch only when the answers are likely to materially change the research scope, source set, comparison criteria, or recommendation. Typical high-value ambiguities include:

- multiple plausible meanings of the subject that lead to different research programs;
- a decision whose answer depends strongly on user-specific constraints;
- missing geography, jurisdiction, timeframe, population, technical environment, or budget that could flip the conclusion;
- an unclear target outcome where several materially different deliverables are plausible.

Do **not** ask generic questions merely because more detail could always be useful. A broad topic is not by itself a reason to delay research; if a broad survey is a reasonable interpretation, proceed with it.

When asking questions:

- keep them answerable in one reply;
- explain options tersely when useful;
- include a reasonable default assumption for each material ambiguity;
- allow the user to say `use defaults` or equivalent;
- do not ask for information already present in the request or conversation.

If the user explicitly requests no follow-up questions, skip this phase and make reasonable assumptions.

If no high-value clarification exists, begin research immediately.

## 2. Translate the request into a research brief

Infer the actual outcome the user needs: understanding, explanation, comparison, decision, forecast, troubleshooting, literature review, due diligence, or another goal.

Preserve explicit constraints. Leave unspecified dimensions open unless a reasonable assumption is needed. State only assumptions that materially affect the result.

Treat the user's framing as a starting point rather than a complete or necessarily correct research map. Identify unknown unknowns and adjacent factors capable of changing the answer.

Do not expose private chain-of-thought. The finished report should show evidence, reasoning at the level needed to justify conclusions, uncertainties, and source support—not an internal reasoning transcript.

## 3. Execute adaptive research

Use current web research extensively whenever the task benefits from external information. For substantial research, prefer the deepest available research/search capability rather than relying on memory.

Choose the search strategy autonomously. Use, when useful:

- broad exploratory searches;
- question decomposition;
- terminology and synonym expansion;
- specialist vocabulary discovered during research;
- multiple independent query formulations;
- primary-source targeting;
- multi-hop retrieval;
- backward and forward citation chasing;
- searches for critiques, contradictions, null results, failures, and alternative explanations;
- current-status verification;
- quantitative cross-checking;
- targeted searches to close remaining evidence gaps.

Let early findings reshape later searches. Do not remain anchored to the user's original wording or to the first plausible result cluster.

Do not use a minimum source count as a completion target.

## 4. Source and provenance standard

Match the evidence type to the claim.

Prefer original, primary, or authoritative evidence when appropriate and practical: original studies/data, official documentation, standards, government or regulatory material, filings, legislation, court decisions, trial registries, technical specifications, contemporaneous records, and firsthand statements.

Use high-quality secondary synthesis when it contributes context, comparison, interpretation, methodological critique, or orientation.

Use practitioner reports, forums, Reddit, reviews, and community evidence when they are appropriate for real-world experience, emerging failures, sentiment, or edge cases, but do not elevate anecdote beyond what it can establish.

For important repeated claims, trace provenance where practical. Distinguish independent corroboration from derivative repetition, syndicated material, common datasets, press-release propagation, and circular citation.

## 5. Adversarial research

Actively search for credible evidence capable of falsifying, weakening, qualifying, or materially changing the emerging conclusion.

Investigate serious competing explanations, methodological criticism, failed replications, contradictory or null evidence, alternative causal accounts, adverse outcomes, and credible expert disagreement when relevant.

Steelman serious alternatives before rejecting them. Represent disagreements in proportion to evidentiary support; do not manufacture false balance.

## 6. Quantitative rigor

For important quantitative claims, verify units, denominators, definitions, populations/samples, dates, geographic scope, methodology, revisions, and whether supposedly independent figures share the same underlying dataset.

Reconcile materially conflicting figures when feasible. Reproduce or sanity-check calculations when practical. Do not create precision unsupported by the evidence.

## 7. Verification pass

Before finalizing, perform a targeted independent verification pass on the claims most capable of changing the conclusion.

Verify material quotations, quantitative facts, dates, definitions, current-status claims, source attribution, and decisive assumptions. Confirm that each important citation actually supports the nearby claim.

Seek independent corroboration for high-impact claims when reasonably available. If evidence is weak, indirect, incomplete, or disputed, say so explicitly.

Do not treat failure to find evidence as proof of absence.

## 8. Completeness gate

Continue until all of the following are true to a reasonable research standard:

- important subquestions are adequately supported;
- specialist terminology and important adjacent considerations have been explored;
- the strongest evidence for the main conclusion is understood;
- material counterevidence and competing explanations have been investigated;
- important repeated claims have sufficient provenance tracing;
- material quantitative conflicts are reconciled or explained;
- major contradictions, uncertainties, and evidence gaps are explicit;
- additional searching is unlikely to materially change the conclusion, recommendation, or confidence.

Before stopping, ask at the research-process level whether any unresolved question, hidden assumption, missing source category, contradiction, or unexplored perspective could realistically flip the answer. If so, investigate it when feasible.

Do not confuse source count, search count, report length, or citation density with depth.

## 9. Build the report

Lead with the most important conclusions or recommendation.

Then provide enough analysis to demonstrate why the evidence supports them, including where relevant:

- decisive evidence;
- strongest counterevidence or competing explanations;
- important uncertainties and gaps;
- evidence strength and limitations;
- decision tradeoffs;
- sensitivity to assumptions;
- explicit flip conditions that would change the recommendation.

Clearly distinguish documented fact, empirical finding, synthesis/inference, practitioner or expert consensus, contested interpretation, and unresolved uncertainty.

Use inline citations or source links close to material factual claims. Verify cited sources actually support those claims.

Use tables only when they improve comparison or evidence interpretation. Omit generic filler, repeated conclusions, decorative frameworks, arbitrary confidence scores, and low-value source summaries.

End with:

1. `Most important sources` — the small set of sources that matter most, with a brief note on why each matters.
2. `Remaining uncertainties` — unresolved questions or missing evidence that would most improve confidence.
3. `What could change the conclusion` — when applicable, the facts, thresholds, assumptions, or future developments most capable of changing the answer.

## 10. Persist the canonical Markdown report

The persistent report directory is:

`/home/mcp/projects/projects/agent-skills/research-output/`

Create the report there through project-scoped Optiplex file-write capabilities. Do not modify Optiplex_MCP or any MCP configuration.

Filename convention:

`YYYY-MM-DD--<descriptive-topic-slug>.md`

Use a concise lowercase hyphenated slug, normally three to eight meaningful words. If the filename already exists for a distinct run, append `--2`, `--3`, and so on rather than overwriting it unless the user explicitly requested an update to the existing report.

The Markdown file is the canonical deliverable and must contain the complete report, not a stub or abbreviated summary.

Recommended document header:

```markdown
# <Research title>

- **Research question:** <resolved question>
- **Generated:** <date>
- **Scope:** <material scope, assumptions, or cutoff if needed>
```

Do not store hidden reasoning, scratch notes, or temporary search logs in `research-output/`.

## 11. Return the result in chat

After the canonical report is written:

- make the same Markdown available as a downloadable chat artifact when a user-visible file-creation capability is available;
- present the completed report in chat when it fits comfortably;
- for exceptionally long reports, present the complete executive conclusions and a structured synopsis in chat while attaching the full Markdown;
- always state the canonical Optiplex path;
- do not claim a downloadable attachment exists unless it was actually created.

The user should be able to review the substance immediately in chat and retain the full canonical `.md` report on Optiplex.

## 12. Safety and boundaries

All higher-priority system, safety, privacy, copyright, and tool rules remain in force.

Do not fabricate access to paywalled, private, deleted, or unavailable sources. Do not claim exhaustive certainty when material evidence remains inaccessible or unresolved.
