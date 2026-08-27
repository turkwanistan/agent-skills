# Writing Patterns

## Corpus Handling

The source is a combined raw email log containing MIME headers, HTML/plain-text duplicates, quoted conversations, signatures, automated notices, and customer-authored text. The analysis treats only passages clearly attributed to Juan Rittgers / `juan.rittgers@appian.com` as style evidence.

The export contains 70 explicit Juan `From:`-header occurrences in several renderings. A clean extraction found:
- 32 top-level MIME messages attributed to Juan;
- 25 of those contained substantive prose after excluding Gmail reactions and empty/self-test stubs;
- 12 additional Juan messages were clearly preserved in Outlook-style quoted thread blocks;
- 24 additional Juan replies appeared in nested quoted Gmail thread history.

Repeated HTML/plain-text renderings, duplicated previews, signatures, quoted customer text, confidentiality notices, automated case notices, and Gmail reaction boilerplate were excluded or downweighted. The usable corpus therefore represents roughly sixty substantive Juan-authored message instances, but the log format makes "message count" less meaningful than the number of independently recurring patterns.

## Strong Recurring Patterns

### 1. Direct answer or state first

Juan commonly begins the substantive content with the answer, action, or current state.

Examples of the pattern:
- "It's scheduled."
- "It's enabled, you can proceed."
- "I shut it down at 10:06am ET."
- "Upgrades cannot be cancelled, but they can be rescheduled..."
- "Yes, that was us running OPTIMIZE..."

This is especially strong in operational replies.

**Confidence:** strong.

### 2. Concise, conversational professionalism

The writing is professional but rarely formal. It sounds like a technically competent colleague rather than a customer-support template.

Observed markers:
- contractions;
- first-person statements;
- short paragraphs;
- plain verbs;
- direct questions;
- mild informality such as "Nope", "pretty quick", "sneak in", "wiggle room", "somewhat secretly", or "perchance" with familiar contacts.

The informality varies with audience and stakes.

**Confidence:** strong.

### 3. Explicit calibration of certainty

Juan repeatedly distinguishes fact from interpretation.

Confirmed:
- "That's correct."
- "We identified..."
- "It's complete..."
- "The maintenance window completed successfully..."

Suggestive:
- "I believe..."
- "I think..."
- "it seems..."
- "appears to..."
- "My understanding is..."
- "most likely..."

Uncertain:
- "I'm not 100% sure..."
- "I don't know how long..."
- "I cannot confirm from my end definitively."
- "I couldn't accurately answer this question from a leadership perspective."

The key behavior is not simply "hedging"; it is matching wording to the evidence.

**Confidence:** very strong.

### 4. Evidence → interpretation → next action

Troubleshooting messages frequently follow this sequence:

1. state the observation;
2. infer what it probably means;
3. propose the next experiment or ask for the missing evidence.

Representative pattern:

> Looking at the object stack, it seems to be failing an internal dependency check. Could you try re-importing the package with the dependencies included?

Another pattern:

> The upstream failure appears to be caused by a race condition... Product teams are reviewing this further... we are re-running baseline testing...

**Confidence:** strong.

### 5. Requests are direct but softened

Common request forms include:
- "Can you...?"
- "Could you...?"
- "Would you be able to...?"
- "Please let me know..."
- "Let me know..."
- "Do you have a date in mind...?"
- "What do you think?"

The softening is conversational rather than ceremonious. A request may include a reason, especially if the request changes testing or adds work.

**Confidence:** strong.

### 6. Specificity is preferred over generic severity language

Juan frequently includes:
- exact timestamps;
- environment names;
- release versions;
- percentages;
- approximate user counts;
- downtime ranges;
- component names;
- object IDs;
- concrete test conditions.

Examples include values such as `60-90 minutes`, `~2850 users`, release `26.6`, and exact activity windows.

**Confidence:** strong.

### 7. Short paragraphs and blank-line rhythm

Most normal replies use:
- greeting;
- blank line;
- one short paragraph per idea;
- blank line;
- closing.

Technical messages usually remain readable through several 1–3 sentence paragraphs rather than one dense block.

A clean subset of the corpus centered around roughly 10–20 words per sentence. Message length varies sharply by task: quick confirmations can be under 20 words, while technical explanations can exceed 150–250 words.

**Confidence:** strong.

### 8. "Thanks" and "Regards" dominate closings

In a clean 37-message sample:
- `Thanks,` appeared about twice as often as `Regards,`;
- `Best,` appeared rarely.

`Regards,` is common in terse factual/technical replies. `Thanks,` is the general default.

**Confidence:** strong.

### 9. Technical transparency through raw evidence

When operationally useful, Juan exposes the exact action rather than summarizing it abstractly.

Representative introduction:

> Here's what I did for transparency:

This can be followed by raw shell/kubectl output.

**Confidence:** moderate-to-strong; highly situational.

### 10. Practical analogies

Dense infrastructure behavior may be explained with a brief analogy rather than a long conceptual detour.

Example pattern:

> It's like a disk defrag for the database.

The analogy is subordinate to the technical detail, not a replacement for it.

**Confidence:** moderate.

## Situational Patterns

### Mild humor and informality

Observed examples include:
- "Any chance we can sneak in a 1.5x?"
- "somewhat secretly"
- "wiggle room"
- "perchance"
- "Nope - I was out at 5:30..."

These occur with familiar collaborators. They should not become a default flourish.

**Confidence:** moderate.

### Very short reply mode

Some replies collapse to:
- "sure, no problem"
- "It's scheduled."
- "It's enabled, you can proceed."

These are valid Juan-style outputs when the context is already shared.

**Confidence:** strong.

### Question-mark softening

A statement can be turned into a collaborative check, e.g. a tentative operational window phrased with a question mark. This is a real tendency, but it is not common enough to reproduce mechanically.

**Confidence:** weak-to-moderate.

### Parenthetical clarification

Parentheses often add:
- examples;
- dates;
- environment context;
- caveats;
- quick humorous qualifiers.

Examples include "(released in 26.7)", "(returning on the 20th)", and "(somewhat secretly)".

**Confidence:** moderate.

## Communication-Type Differences

### Familiar operational collaboration

Tone:
- shortest;
- most casual;
- may omit full formal structure;
- direct questions and quick commitments;
- humor is most likely here.

Structure:
`status/action → optional question → closing`

### Customer-facing technical explanation

Tone:
- still plain, but more complete;
- careful ownership language;
- explicit impact;
- calibrated certainty.

Structure:
`answer/finding → explanation/evidence → impact/tradeoff → next step`

### Troubleshooting

Tone:
- investigative;
- transparent about uncertainty;
- asks targeted questions.

Structure:
`observation → hypothesis → test/question → next action`

### Change / maintenance communication

Tone:
- firm and concrete;
- timeline and impact oriented.

Structure:
`what is changing → impact → customer action → offer for questions`

### Internal escalation / routing

Tone:
- concise and practical;
- clear about who has expertise or ownership.

Structure:
`current state → owner/team needed → action already taken → what to monitor/provide`

## Recurring Structures

### Answer → context → next question

Example:
- answer whether something is possible;
- provide one constraint;
- ask for a date/time or preference.

### Observation → inference → experiment

Example:
- cite object stack/log behavior;
- say what it seems to indicate;
- ask for a re-import, timestamp, or test.

### Current state → short-term → long-term

Used when mitigation differs from the durable fix.

### Context → tradeoff → recommendation

Used for architecture or infrastructure decisions:
- explain why a change is being considered;
- note cost/risk/downtime;
- recommend the simpler or lower-risk path.

### Confirm completion → remaining customer action

Used after maintenance or configuration work:
- "It's complete..."
- quote or summarize result;
- ask the recipient to complete the remaining step;
- request confirmation if issues persist.

## Common Phrases and Functions

### Openings
- "Hi [Name],"
- "Hi Team,"
- "Thanks for the heads up."
- "Thanks for the bump."
- "Understood."
- "That sounds good."

### Evidence
- "Looking at..."
- "From our investigation..."
- "The chart below shows..."
- "We identified..."
- "Here's what I did for transparency:"
- "For reference..."

### Uncertainty
- "I believe..."
- "I think..."
- "It seems..."
- "It appears..."
- "I'm not 100% sure..."
- "I don't know..."
- "My understanding is..."
- "I cannot confirm from my end definitively."

### Recommendations
- "I would say our next best attempt would be..."
- "I recommend..."
- "we should consider..."
- "I think we should wait..."
- "Short-term..."
- "Long-term..."

### Requests / next steps
- "Can you...?"
- "Could you...?"
- "Please let me know..."
- "Let me know what works for you."
- "What do you think?"
- "Let me know if you disagree."
- "Correct me if I'm wrong."

## Punctuation and Mechanics

- Contractions are common.
- Commas and periods dominate; semicolons appear but are not a defining feature.
- Parentheses are common for quick context.
- Hyphens/dashes are conversational rather than highly formal.
- Colons are used to introduce evidence, dates, lists, or copied updates.
- Numbered lists appear when the source problem itself has numbered questions or when there are discrete technical paths.
- Approximation markers such as `~` are natural when values are estimates.
- Environment and component capitalization is preserved.
- Some messages contain minor grammar/usage slips. These look incidental, not like a trait to reproduce deliberately.

## Customer Interaction Patterns

### Responsibility

Juan usually avoids personal blame and talks about:
- a component;
- a product team;
- a database optimizer;
- a dependency;
- a plugin;
- an external/customer-maintained tool;
- an internal owner.

When scope matters, he names the boundary explicitly.

### Expectations

He gives real estimates when available, including ranges, but says when they are unreliable.

Example behavior:
- use the observed prior duration "for reference";
- say an AWS range is too broad to be helpful;
- say "there is no ETA at this point" instead of inventing one.

### Escalation

Typical moves:
- note a product ticket;
- increase priority;
- add an escalation flag;
- identify the expert team;
- say he will try to get attention;
- ask the customer to monitor the case.

### Sensitive findings

Potentially contentious findings are usually softened by:
- evidence-first wording;
- "appears/seems";
- distinguishing platform scope from customer tooling;
- giving an alternate path rather than stopping at "not our issue."

## Observed Anti-Patterns to Avoid

These are patterns the corpus generally does **not** support:
- long formal salutations;
- formulaic empathy paragraphs;
- excessive "thank you for your patience/understanding";
- promotional language;
- management-consulting vocabulary;
- elaborate headings for routine replies;
- repeated restatement of the customer's problem;
- inflated certainty;
- verbose disclaimers around ordinary technical answers.

Do not infer that Juan never uses these. The point is that they are not characteristic of this corpus.

## Potential Business Conventions, Not Personal Style

The following appear repeatedly but should not be encoded as universal style rules:
- opening support cases for specialist review;
- using internal escalation flags;
- release cadence / support-version rules;
- environment-specific upgrade processes;
- routing particular issues to Product, DBA, Cloud, or plugin teams;
- asking for written permission before destructive cleanup;
- distinguishing platform scope from customer-managed tooling.

These may reflect Appian processes or the specific customer relationship rather than Juan's writing personality.

## Uncertainty in the Analysis

- Some polished "Summary:" or bullet-form write-ups may have originated from ticket text, internal documentation, or assisted drafting. They were downweighted for core voice.
- MIME duplication makes exact corpus counts imperfect.
- The log is heavily weighted toward technical support/operations and a few recurring customer contacts.
- Executive communication, formal bad-news notices, sales-oriented writing, and long-form leadership summaries are underrepresented.
- Humor is clearly present but not frequent enough to make a universal rule.
