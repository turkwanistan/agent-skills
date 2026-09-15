import json
import tempfile
import unittest
from pathlib import Path
import importlib.util

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "reddit_artifacts.py"
SPEC = importlib.util.spec_from_file_location("reddit_artifacts", MODULE_PATH)
reddit_artifacts = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(reddit_artifacts)


class CanonicalizeTests(unittest.TestCase):
    def test_normalizes_reddit_hosts_and_strips_slug_query(self):
        value = reddit_artifacts.canonicalize_thread_url(
            "https://old.reddit.com/r/TestSub/comments/AbC123/a_title/def456/?utm_source=x#frag"
        )
        self.assertEqual(value, "https://www.reddit.com/r/TestSub/comments/AbC123")

    def test_normalizes_shortlink(self):
        self.assertEqual(
            reddit_artifacts.canonicalize_thread_url("https://redd.it/abc123"),
            "https://www.reddit.com/comments/abc123",
        )

    def test_rejects_non_reddit_host(self):
        with self.assertRaises(ValueError):
            reddit_artifacts.canonicalize_thread_url("https://example.com/comments/abc")


class ArtifactTests(unittest.TestCase):
    def test_validate_and_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            candidates = [
                {
                    "post_id": "abc123",
                    "canonical_url": "https://www.reddit.com/r/foo/comments/abc123",
                    "subreddit": "foo",
                    "retrieval_status": "read",
                    "comments_examined": 12,
                    "branches_examined": 3,
                },
                {
                    "post_id": "def456",
                    "canonical_url": "https://www.reddit.com/r/bar/comments/def456",
                    "subreddit": "bar",
                    "retrieval_status": "discovered",
                },
            ]
            evidence = [
                {"evidence_id": "abc123:c1", "post_id": "abc123", "comment_id": "c1"},
                {"evidence_id": "def456:c2", "post_id": "def456", "comment_id": "c2"},
            ]
            (run_dir / "candidates.jsonl").write_text(
                "".join(json.dumps(row) + "\n" for row in candidates), encoding="utf-8"
            )
            (run_dir / "evidence.jsonl").write_text(
                "".join(json.dumps(row) + "\n" for row in evidence), encoding="utf-8"
            )
            (run_dir / "coverage.json").write_text(
                json.dumps(
                    {
                        "query_batches": [
                            {"label": "exact", "new_high_value_threads": 2},
                            {"label": "adversarial", "new_high_value_threads": 0},
                        ],
                        "channels_used": ["web_search", "live_reddit", "web_search"],
                        "remaining_gaps": ["older versions"],
                    }
                ),
                encoding="utf-8",
            )

            validation = reddit_artifacts.validate_run(run_dir)
            self.assertEqual(validation["warnings"], [])

            summary = reddit_artifacts.summarize_run(run_dir)
            self.assertEqual(summary["unique_threads"], 2)
            self.assertEqual(summary["subreddits"], ["bar", "foo"])
            self.assertEqual(summary["threads_inspected"], 1)
            self.assertEqual(summary["comments_examined"], 12)
            self.assertEqual(summary["branches_examined"], 3)
            self.assertEqual(summary["evidence_items"], 2)
            self.assertEqual(summary["evidence_threads"], 2)
            self.assertEqual(summary["query_batches"], 2)
            self.assertEqual(summary["new_high_value_threads_by_batch"], [2, 0])
            self.assertEqual(summary["last_two_high_value_yield"], [2, 0])
            self.assertEqual(summary["channels_used"], ["live_reddit", "web_search"])

    def test_duplicate_candidate_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            rows = [
                {"post_id": "abc123", "canonical_url": "https://www.reddit.com/r/foo/comments/abc123"},
                {"post_id": "ABC123", "canonical_url": "https://old.reddit.com/r/foo/comments/abc123/title"},
            ]
            (run_dir / "candidates.jsonl").write_text(
                "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
            )
            with self.assertRaises(ValueError):
                reddit_artifacts.validate_run(run_dir)


if __name__ == "__main__":
    unittest.main()
