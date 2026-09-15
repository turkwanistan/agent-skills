# Reddit-search durable artifacts

Use this reference for substantial, deep, or explicitly exhaustive `reddit-search` runs. Small searches do not need a directory full of bookkeeping.

## Default run directory

When working in the canonical `agent-skills` repository, use:

`reddit-search-output/YYYY-MM-DD--<topic-slug>/`

The directory is intentionally ignored by Git. It is a durable local research handoff, not versioned source code.

Recommended files:

- `research_config.json` — resolved question, timeframe, modes, known entities/aliases, enabled discovery/retrieval channels;
- `candidates.jsonl` — one normalized discovered thread per line;
- `evidence.jsonl` — one high-value evidence item/comment per line;
- `coverage.json` — query batches and marginal discovery yield;
- `analysis.json` — model-produced themes/stances referencing evidence IDs;
- `report.md` — user-facing synthesis when a persistent report is useful;
- `STATUS.md` — optional checkpoint for a long/resumable run.

Do not store hidden reasoning or scratch chain-of-thought in these files.

## Candidate record

Keep fields optional when unavailable rather than inventing values.

```json
{
  "post_id": "abc123",
  "canonical_url": "https://www.reddit.com/r/example/comments/abc123",
  "subreddit": "example",
  "title": "...",
  "created_at": "2026-09-15T12:00:00Z",
  "score": 42,
  "comment_count": 97,
  "discovered_by": ["product exact-name reliability", "r/example failure"],
  "source_class": "live_reddit",
  "relevance": "detailed long-term owner thread",
  "retrieval_status": "read",
  "comments_examined": 35,
  "branches_examined": 8
}
```

`source_class` examples: `live_reddit`, `web_index`, `authorized_api`, `archive`, `browser`.

Prefer `post_id` as the stable dedupe key. Otherwise use the canonical thread URL.

## Evidence record

```json
{
  "evidence_id": "abc123:def456",
  "post_id": "abc123",
  "comment_id": "def456",
  "permalink": "https://www.reddit.com/r/example/comments/abc123/title/def456/",
  "subreddit": "example",
  "created_at": "2026-09-15T13:00:00Z",
  "theme": "battery longevity",
  "stance": "negative",
  "evidence_type": "firsthand",
  "context": "model v2; 18 months ownership",
  "summary": "Owner reports a large capacity decline after roughly 18 months.",
  "excerpt": "optional short exact excerpt",
  "source_class": "live_reddit"
}
```

Use `stance` values that fit the task; do not force everything into positive/negative. Useful values include `positive`, `negative`, `mixed`, `neutral`, `uncertain`, `supports`, `contradicts`, and task-specific directions.

`evidence_type` commonly includes `firsthand`, `secondhand`, `speculation`, `linked_evidence`, `question`, or `moderator/official_statement`.

## Coverage record

```json
{
  "query_batches": [
    {
      "label": "exact names + reliability",
      "queries": ["..."],
      "channels": ["web_search"],
      "new_unique_threads": 14,
      "new_high_value_threads": 6,
      "new_communities": ["example", "another"],
      "new_themes": ["battery longevity"],
      "new_counterevidence": 1
    }
  ],
  "channels_used": ["web_search", "live_reddit"],
  "threads_discovered": 27,
  "threads_inspected": 16,
  "communities_represented": 4,
  "comments_examined": 143,
  "branches_examined": 31,
  "remaining_gaps": ["little evidence for model v3"],
  "saturation_note": "Later comparison/adversarial batches produced no new major themes; model-v3 coverage remains thin."
}
```

The model, not the helper script, decides whether research is saturated. The helper only reports bookkeeping facts.

## Analysis record

Keep analysis derived from evidence IDs so conclusions can be regenerated without reacquiring Reddit. For recommendation/sentiment/trend work, make recurrence explicit enough to support report language such as “recurring,” “polarizing,” or “strongest in the sample.”

```json
{
  "themes": [
    {
      "theme": "battery longevity",
      "summary": "...",
      "independent_threads": 5,
      "communities": ["example", "another"],
      "signal_type": "cross_thread_recurrence",
      "direction": "mostly_negative",
      "time_span": "2026-07 through 2026-09",
      "evidence_ids": ["abc123:def456"],
      "counterevidence_ids": ["ghi789:jkl012"],
      "limitations": ["mostly model v2 reports"]
    }
  ]
}
```

Do not infer broad prevalence from `independent_threads` or comment counts. These fields describe the retrieved Reddit sample only.

For recommendation-style runs, `analysis.json` may use `items` instead of `themes` with the same recurrence fields. Useful `signal_type` values include `current_momentum`, `cross_thread_recurrence`, `evergreen_recurrence`, and combinations when justified. A qualitative superlative or frequency claim in `report.md` should be traceable to these counts; if the counts cannot support it, weaken the wording.

## Helper script

`scripts/reddit_artifacts.py` uses only the Python standard library.

Examples:

```bash
python reddit-search/scripts/reddit_artifacts.py normalize 'https://old.reddit.com/r/foo/comments/abc123/title/?utm_source=x'
python reddit-search/scripts/reddit_artifacts.py validate reddit-search-output/2026-09-15--topic
python reddit-search/scripts/reddit_artifacts.py summary reddit-search-output/2026-09-15--topic
```

`normalize` canonicalizes a Reddit thread URL for deduplication. `validate` checks JSON/JSONL shape, duplicate candidate/evidence keys, and Reddit URL consistency without requiring every optional artifact. `summary` emits deterministic coverage counts useful for a checkpoint or report coverage note.

The helper is intentionally not a Reddit downloader. Retrieval remains replaceable.
