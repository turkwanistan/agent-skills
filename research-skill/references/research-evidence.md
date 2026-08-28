# Evidence Basis for Research Skill Design

This reference records the evidence-informed conclusions used to design `research-skill`. It is background for maintenance, auditing, and future revision; it does **not** need to be reread on every research invocation unless the agent is evaluating or changing the research method itself.

The current skill architecture was derived from the research and template developed in the August 2026 ChatGPT session that created this skill.

## Main conclusion

There is no credible evidence that one magic phrase or maximally long prompt universally optimizes current ChatGPT research across domains. The most defensible reusable architecture is a **hybrid control specification**:

- define the outcome and material constraints;
- require adaptive scope discovery;
- set strong evidence, provenance, contradiction, verification, and stopping standards;
- specify a decision-useful deliverable;
- leave the exact search sequence autonomous enough to adapt to discoveries.

The durable behaviors matter more than exact wording.

## Evidence that informed the design

### OpenAI product guidance

OpenAI's current ChatGPT guidance distinguishes quick Search from Deep Research-style workflows intended for complex multi-source investigation, synthesis, and documented reports. Current model-prompting guidance also favors clear outcomes, constraints, evidence rules, and success criteria while leaving capable reasoning systems room to choose an efficient path.

Key references:

- OpenAI Help — Deep research in ChatGPT: https://help.openai.com/en/articles/10500283
- OpenAI Academy — Research with ChatGPT: https://openai.com/academy/search-and-deep-research/
- OpenAI — BrowseComp: https://openai.com/index/browsecomp/

BrowseComp is especially relevant because difficult browsing requires persistence, search reformulation, and reasoning across fragmented evidence rather than merely issuing a single search query.

### Decomposition and adaptive retrieval

Question decomposition has empirical support for multi-hop retrieval. A 2025 ACL study found meaningful retrieval and answer-quality gains from decomposing complex questions into subquestions and reranking the combined evidence.

- Ammann, Golde & Akbik (ACL 2025), Question Decomposition for Retrieval-Augmented Generation: https://aclanthology.org/2025.acl-srw.32/

This supports decomposition as a useful tool when the question warrants it, not as a mandatory ceremony for every task.

### Citation correctness is a separate problem

Research-agent benchmarks show that report quality, citation coverage, and citation correctness are distinct dimensions. A source-rich answer can still contain incorrect attribution.

- DeepResearch Bench (2025): https://deepresearch-bench.github.io/
- Rao, Wong & Callison-Burch (2026), Detecting and Correcting Reference Hallucinations: https://arxiv.org/abs/2604.03173

The latter examined tens of thousands of citation URLs from commercial models/research agents and found nontrivial hallucinated or non-resolving references, while tool-assisted checking substantially reduced failures. This is why the skill includes a separate targeted verification pass and citation-support check.

### Retrieval, reranking, feedback, and citation verification

The 2026 OpenScholar work in *Nature* found substantial benefits from retrieval-oriented components including reranking, self-feedback, and citation verification in scientific literature synthesis. Ablations weakened correctness and/or citation performance.

- Asai et al. (Nature 2026), Synthesizing scientific literature with retrieval-augmented language models: https://www.nature.com/articles/s41586-025-10072-4

This supports treating retrieval, synthesis, and verification as distinct quality concerns rather than assuming one pass handles all three reliably.

### Generic chain-of-thought prompting is not a universal best practice

Recent evidence weakens the case for automatically adding phrases such as "think step by step" to modern reasoning-model prompts. Benefits vary by task/model and can be small or negative while increasing output or latency.

- Meincke et al. (2025), The Decreasing Value of Chain of Thought in Prompting: https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/
- Liu et al. (ICML 2025), Mind Your Step (by Step): https://proceedings.mlr.press/v267/liu25t.html

Therefore the skill asks for observable research behaviors—decomposition when useful, contradiction search, provenance tracing, quantitative reconciliation, and verification—rather than generic exposed reasoning instructions.

### Research output is not identical to human learning

A 2025 *PNAS Nexus* study found that people learning through LLM syntheses could develop shallower knowledge than people using conventional web links, despite the convenience of synthesis.

- Lee et al. (PNAS Nexus 2025), Experimental evidence of the effects of large language models versus web search on depth of learning: https://academic.oup.com/pnasnexus/article/4/10/pgaf316/8303888

This supports preserving a small `Most important sources` section so users can inspect the decisive original evidence themselves.

## Design consequences

The skill therefore intentionally includes:

1. optional clarification only when it has high expected information value;
2. unknown-unknown and alternative-framing discovery;
3. adaptive broad-to-deep retrieval rather than a fixed search script;
4. source selection matched to the claim;
5. provenance tracing for repeated important claims;
6. explicit counterevidence and competing-explanation search;
7. quantitative normalization and conflict reconciliation;
8. a separate verification pass;
9. evidence-saturation / marginal-value stopping rather than source quotas;
10. decision flip conditions where relevant;
11. dense, citation-grounded Markdown output with minimal filler.

It intentionally avoids as universal defaults:

- expert-persona theater;
- generic "think step by step" instructions;
- arbitrary minimum source/search counts;
- repeated emphasis or threats/rewards;
- fixed research taxonomies for every domain;
- excessively rigid search sequences;
- decorative confidence scores unsupported by calibration.

## Remaining uncertainty

No recent controlled cross-domain study establishes that one exact natural-language prompt is globally optimal for the current ChatGPT product. ChatGPT's models, browsing stack, Deep Research orchestration, and product defaults evolve.

Accordingly, `research-skill` should treat its behavioral standards as more durable than exact prompt wording. Future revisions should be driven by current product evidence and, ideally, regression tests across representative research tasks rather than prompt folklore.
