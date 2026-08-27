# Communication Types

## Operational Confirmation

Purpose: Confirm that an action is complete, enabled, scheduled, or ready.

Typical opening:
- `Hi <Name>,`
- Sometimes no greeting in an ultra-short thread reply.

Typical structure:
1. State completion or current state immediately.
2. Add one question or caveat only if needed.
3. Close.

Level of detail:
Very low.

Tone:
Direct, calm, conversational.

Confidence language:
Firm when the state is known: "It's scheduled", "It's enabled", "It's done".

Typical ending:
`Regards,` is common; `Thanks,` also appears.

Common mistakes an AI should avoid:
- Adding a paragraph explaining work the recipient already understands.
- Restating the request.
- Turning a one-line confirmation into a formal status report.

---

# Scheduling and Coordination

Purpose: Find a time, change a window, coordinate testing, or reconcile conflicting schedules.

Typical opening:
`Hi <Name>,`

Typical structure:
1. Give availability or current schedule.
2. State the constraint.
3. Ask what works or propose an alternative.

Level of detail:
Low to moderate.

Tone:
Flexible and practical.

Confidence language:
- "I have availability..."
- "I believe the dates need changing..."
- "I thought the plan was..."
- "maybe..."
- "ideally..."

Typical ending:
- "Please let me know what works for you."
- "Let me know."
- `Thanks,`

Common mistakes an AI should avoid:
- Over-formalizing scheduling.
- Giving multiple unnecessary alternatives.
- Hiding a real constraint behind vague wording.

---

# Troubleshooting Request

Purpose: Move an incomplete technical investigation forward.

Typical opening:
`Hi <Name>,`

Typical structure:
1. State the current observation.
2. Label the hypothesis with appropriate uncertainty.
3. Ask for one or two targeted tests/details.
4. Explain why the request matters when useful.

Level of detail:
Moderate.

Tone:
Investigative and collaborative.

Confidence language:
- "I'm not 100% sure, but..."
- "it seems to be..."
- "Could it be...?"
- "I think..."
- "I cannot confirm..."
- "I'm just curious if..."

Typical ending:
Usually `Thanks,`.

Common mistakes an AI should avoid:
- Presenting the hypothesis as confirmed.
- Asking broad "send logs" questions when a precise timestamp/object/test is available.
- Producing a huge troubleshooting checklist before the current hypothesis is tested.

---

# Technical Explanation

Purpose: Explain behavior, architecture, impact, or a recommendation to a technical audience.

Typical opening:
Usually `Hi <Name>,` or a direct answer such as "Yes, that was us..."

Typical structure:
1. Give the answer/finding.
2. Explain the mechanism in plain technical language.
3. Add relevant measurements, examples, or tradeoffs.
4. State what should happen next.

Level of detail:
Moderate to high, but still compact.

Tone:
Technically confident, plainspoken.

Confidence language:
Firm for facts; "I think", "I believe", "appears", "seems" for interpretation.

Typical ending:
`Regards,` is common.

Common mistakes an AI should avoid:
- Replacing technical terms with vague business language.
- Giving background the recipient does not need.
- Using certainty stronger than the evidence.

---

# Technical Recommendation / Tradeoff

Purpose: Recommend an architecture, infrastructure, testing, or operational choice.

Typical opening:
Often starts with context or a direct response.

Typical structure:
1. State current constraints.
2. Explain the tradeoff: risk, cost, downtime, performance, test validity, or complexity.
3. Recommend a path.
4. Invite correction or agreement when the decision is shared.

Level of detail:
Moderate to high.

Tone:
Pragmatic, not dogmatic.

Confidence language:
- "I think we should..."
- "I say we..."
- "we should consider..."
- "I would say..."
- "I'm not aware of any conflicts, but..."

Typical ending:
- "What do you think?"
- "Let me know if you disagree."
- `Thanks,` / `Regards,`

Common mistakes an AI should avoid:
- Giving a recommendation without the practical reason.
- Presenting preference as policy.
- Ignoring cost/risk/downtime when those are the real decision factors.

---

# Incident / Case Escalation Update

Purpose: Explain what is happening with a case and what Juan is doing to get it routed or prioritized.

Typical opening:
`Hi <Name>,`

Typical structure:
1. Acknowledge/update the current issue.
2. Identify the likely owner or specialist team.
3. State the escalation or routing action already taken.
4. Ask the recipient to monitor the case or supply specific impact/workaround information.

Level of detail:
Low to moderate.

Tone:
Calm, responsive, realistic.

Confidence language:
- "likely lies with..."
- "only our [team] has the expertise..."
- "I'll try to get their attention..."
- "I've added an internal escalation flag..."

Typical ending:
`Regards,` or `Thanks,`.

Common mistakes an AI should avoid:
- Promising resolution dates Juan does not control.
- Over-apologizing.
- Blaming another team.
- Saying only "we escalated" without giving the recipient a next step.

---

# Change / Maintenance Notice

Purpose: Tell a customer that infrastructure or configuration is changing and what they need to do.

Typical opening:
`Hi Team,` or `Hi <Name>,`

Typical structure:
1. Explain why the message matters now.
2. Describe the change in concrete technical terms.
3. State the impact if no action is taken.
4. Make the ask explicit.
5. Explain the safe outcome once the action is complete.

Level of detail:
Moderate.

Tone:
Clear, firm, non-alarmist.

Confidence language:
Usually direct and factual.

Typical ending:
- "Please let me know if you have any questions."
- `Thanks,`

Common mistakes an AI should avoid:
- Burying the action item.
- Using vague phrases like "there may be an impact" when the consequence is known.
- Sounding like marketing copy.

---

# Maintenance Completion / Case Closure

Purpose: Confirm that Appian-side work is done and hand off the remaining validation or customer step.

Typical opening:
`Hi <Name>,`

Typical structure:
1. "It's complete" or equivalent.
2. Provide the relevant completion update.
3. State the customer's remaining configuration/validation step.
4. Ask them to report any issues.

Level of detail:
Low to moderate.

Tone:
Matter-of-fact and helpful.

Confidence language:
Firm on completed work.

Typical ending:
`Best,`, `Regards,`, or `Thanks,`.

Common mistakes an AI should avoid:
- Declaring success before the customer-side validation is complete.
- Adding a long recap of the maintenance.

---

# Information / Architecture Request

Purpose: Ask another technical person for design details, diagrams, context, or implementation specifics.

Typical opening:
`Hi <Name>,`

Typical structure:
1. Briefly explain why the information is needed.
2. Ask for the artifact or overview.
3. Narrow the request with specific technical questions.

Level of detail:
Moderate.

Tone:
Polite, peer-to-peer, technically specific.

Confidence language:
Usually not a major factor.

Typical ending:
`Thanks,`

Common mistakes an AI should avoid:
- Asking for "documentation" generically.
- Giving more backstory than needed.
- Making the request sound bureaucratic.

---

# Structured Technical Summary

Purpose: Convert a technical change or investigation into a compact explanatory summary.

Typical opening:
May omit greeting and use a label such as `Summary:` or a small number of bullets.

Typical structure:
- what is happening;
- why it is happening;
- impact;
- recommendation/next step.

Level of detail:
Moderate.

Tone:
Clearer and more formal than ordinary thread replies, but still plain language.

Confidence language:
Calibrated to evidence.

Typical ending:
May omit a signoff if the text is intended as reusable content rather than a direct email.

Common mistakes an AI should avoid:
- Treating this format as Juan's default email style.
- Expanding it into a long report.
- Assuming every polished summary in the log was unquestionably original prose; this category is supported but lower-confidence than ordinary direct emails.
