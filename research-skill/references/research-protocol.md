# Research Protocol

This reference captures the durable research principles behind `research-skill`. It is not a script to reproduce verbatim. Use it to decide what quality behaviors matter for the current task.

## Core model

The strongest general architecture is **hybrid autonomy**:

- specify the research objective, material constraints, epistemic standards, verification requirements, stopping criteria, and deliverable clearly;
- leave the exact operational search sequence largely autonomous so discoveries can reshape later research.

Avoid both extremes:

- **under-specified autonomy**, where the agent gets only a topic and may converge too early;
- **procedural micromanagement**, where a rigid checklist prevents adaptation or wastes effort on irrelevant stages.

## High-leverage behaviors

### 1. Outcome-first framing

Infer what the research is actually for: understanding, explanation, comparison, decision, forecast, troubleshooting, literature review, due diligence, or another goal. Optimize the research for that outcome rather than producing a generic encyclopedia entry.

### 2. Unknown-unknown discovery

Treat the user's initial wording as incomplete. Look for hidden subquestions, prerequisite concepts, specialized terminology, competing hypotheses, adjacent disciplines, stakeholder perspectives, and factors capable of changing the conclusion.

### 3. Adaptive retrieval

Use early research to improve later research. Useful behaviors include question decomposition, broad-to-narrow searching, terminology expansion, independent query formulations, primary-source targeting, multi-hop retrieval, and gap-closing searches.

### 4. Source fitness, not a universal hierarchy

Choose sources according to the claim. Primary/original evidence is often preferred for facts that it directly establishes, but strong secondary synthesis can be superior for context, comparison, history, critique, or interpretation.

Community evidence can be valuable for real-world experience and emerging failure modes while remaining inappropriate as proof of formal specifications or causal claims.

### 5. Provenance tracing

Repeated claims are not automatically independent corroboration. When important, trace claims to the underlying study, dataset, filing, announcement, standard, or record. Watch for syndicated reporting, press-release propagation, common datasets, and circular citation.

### 6. Adversarial search

Do not only search for support. Deliberately seek the best credible evidence that could falsify, weaken, qualify, or reframe the emerging answer. Investigate methodological criticism, contradictory or null findings, failed replications, alternative causal explanations, and serious expert disagreement.

Do not manufacture false balance when the evidence is strongly asymmetric.

### 7. Verification as a separate quality gate

Retrieval and citation are not the same as verification. Before finalizing, check decisive claims, quotations, statistics, dates, definitions, current-status assertions, and citation support. Important citations should actually support the nearby claim.

### 8. Quantitative normalization

When numbers matter, compare like with like. Check units, denominators, definitions, samples/populations, geography, time periods, revisions, methodology, mean versus median, nominal versus real values, and whether multiple reported numbers share one underlying dataset.

### 9. Evidence-based stopping

Do not optimize for a source quota or search quota. Stop when important subquestions are supported, material contradictions and alternatives have been investigated, major gaps are understood, and more searching is unlikely to materially change the answer or confidence.

### 10. Decision flip conditions

For decision-oriented work, identify what new evidence, changed assumption, threshold, or constraint would change the recommendation. This is more useful than a decorative confidence score.

## Prompt folklore to avoid as defaults

Do not add these merely because they sound rigorous:

- "You are a world-class researcher."
- generic expert personas;
- "think step by step";
- "take your time";
- arbitrary minimum source counts;
- arbitrary search-count requirements;
- repeated all-caps emphasis;
- threats, rewards, or emotional pressure;
- "verify everything" when targeted verification can be specified precisely;
- giant fixed output schemas unrelated to the task;
- repeated instructions that consume attention without changing behavior.

A useful instruction should earn its place by changing research behavior, evidence quality, verification, completeness, or usefulness.

## Failure modes this protocol is designed to reduce

- shallow search;
- query anchoring;
- confirmation bias;
- popularity bias;
- source monoculture;
- citation laundering;
- circular sourcing;
- missing primary evidence;
- outdated information;
- unsupported synthesis;
- causal overreach;
- premature convergence;
- overconfidence;
- arbitrary source-count completion;
- quantity-over-quality sourcing;
- formatting overhead;
- verbosity masking weak evidence;
- overly literal adherence to the user's framing;
- failure to discover useful terminology;
- unresolved contradictions;
- failure to search beyond obvious sources.

## Clarification-value rule

Questions are useful when they have high expected information value, not merely because the user could always provide more detail.

Ask zero to three questions only when the answers could materially change:

- the research program;
- the relevant body of evidence;
- comparison criteria;
- decision outcome;
- legal/jurisdictional applicability;
- population or technical environment;
- timeframe or currentness standard.

Broad but coherent requests can proceed without clarification. If a default assumption is reasonable, use it rather than introducing avoidable friction.

## Reporting standard

A high-value report should make the following easy to see:

- the answer or recommendation;
- why the evidence supports it;
- the strongest counterevidence;
- what remains uncertain;
- which claims are facts versus inference;
- what would change the conclusion;
- which sources matter most.

Length is not a quality metric. Prefer dense, decision-useful synthesis over repetition.
