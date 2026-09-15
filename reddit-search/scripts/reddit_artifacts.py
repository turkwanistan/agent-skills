#!/usr/bin/env python3
"""Deterministic helpers for reddit-search artifacts.

This module deliberately does not fetch Reddit. It canonicalizes Reddit URLs,
validates JSON/JSONL research artifacts, and summarizes coverage bookkeeping.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit

REDDIT_HOSTS = {
    "reddit.com",
    "www.reddit.com",
    "old.reddit.com",
    "new.reddit.com",
    "np.reddit.com",
    "m.reddit.com",
}


def canonicalize_thread_url(value: str) -> str:
    """Return a canonical post-level Reddit URL suitable for deduplication."""
    raw = value.strip()
    if not raw:
        raise ValueError("empty URL")
    if "://" not in raw:
        raw = "https://" + raw

    parsed = urlsplit(raw)
    host = (parsed.hostname or "").lower()
    parts = [part for part in parsed.path.split("/") if part]

    if host == "redd.it":
        if not parts:
            raise ValueError("redd.it URL has no post id")
        return f"https://www.reddit.com/comments/{parts[0]}"

    if host not in REDDIT_HOSTS:
        raise ValueError(f"not a recognized Reddit host: {host or '<missing>'}")

    try:
        comments_index = parts.index("comments")
    except ValueError as exc:
        raise ValueError("URL does not contain a Reddit comments/post path") from exc

    if comments_index + 1 >= len(parts):
        raise ValueError("Reddit comments URL has no post id")

    post_id = parts[comments_index + 1]
    if comments_index >= 2 and parts[comments_index - 2] == "r":
        subreddit = parts[comments_index - 1]
        return f"https://www.reddit.com/r/{subreddit}/comments/{post_id}"
    return f"https://www.reddit.com/comments/{post_id}"


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for lineno, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{lineno}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object")
            rows.append(value)
    return rows


def _candidate_key(row: dict[str, Any]) -> str | None:
    post_id = str(row.get("post_id") or "").strip()
    if post_id:
        return "post:" + post_id.lower()
    url = str(row.get("canonical_url") or row.get("url") or "").strip()
    if not url:
        return None
    return "url:" + canonicalize_thread_url(url).lower()


def _evidence_key(row: dict[str, Any]) -> str | None:
    evidence_id = str(row.get("evidence_id") or "").strip()
    if evidence_id:
        return "evidence:" + evidence_id.lower()
    comment_id = str(row.get("comment_id") or "").strip()
    if comment_id:
        return "comment:" + comment_id.lower()
    permalink = str(row.get("permalink") or "").strip()
    return "permalink:" + permalink.lower() if permalink else None


def _duplicates(keys: Iterable[str | None]) -> list[str]:
    counts = Counter(key for key in keys if key)
    return sorted(key for key, count in counts.items() if count > 1)


def validate_run(run_dir: Path) -> dict[str, Any]:
    if not run_dir.is_dir():
        raise ValueError(f"not a directory: {run_dir}")

    result: dict[str, Any] = {"run_dir": str(run_dir), "files": {}, "warnings": []}

    for name in ("research_config.json", "coverage.json", "analysis.json"):
        path = run_dir / name
        if not path.exists():
            continue
        value = _read_json(path)
        if not isinstance(value, dict):
            raise ValueError(f"{path}: expected top-level JSON object")
        result["files"][name] = "ok"

    candidates_path = run_dir / "candidates.jsonl"
    if candidates_path.exists():
        candidates = _read_jsonl(candidates_path)
        duplicate_keys = _duplicates(_candidate_key(row) for row in candidates)
        if duplicate_keys:
            raise ValueError(
                f"{candidates_path}: duplicate candidate keys: {', '.join(duplicate_keys[:10])}"
            )
        for index, row in enumerate(candidates, 1):
            url = str(row.get("canonical_url") or row.get("url") or "").strip()
            if url:
                canonical = canonicalize_thread_url(url)
                if row.get("canonical_url") and row["canonical_url"] != canonical:
                    result["warnings"].append(
                        f"candidates.jsonl:{index}: canonical_url should be {canonical}"
                    )
            if not _candidate_key(row):
                result["warnings"].append(
                    f"candidates.jsonl:{index}: missing post_id and canonical URL"
                )
        result["files"]["candidates.jsonl"] = {"rows": len(candidates)}

    evidence_path = run_dir / "evidence.jsonl"
    if evidence_path.exists():
        evidence = _read_jsonl(evidence_path)
        duplicate_keys = _duplicates(_evidence_key(row) for row in evidence)
        if duplicate_keys:
            raise ValueError(
                f"{evidence_path}: duplicate evidence keys: {', '.join(duplicate_keys[:10])}"
            )
        for index, row in enumerate(evidence, 1):
            if not _evidence_key(row):
                result["warnings"].append(
                    f"evidence.jsonl:{index}: missing evidence_id/comment_id/permalink"
                )
            if not (row.get("post_id") or row.get("thread_url") or row.get("permalink")):
                result["warnings"].append(
                    f"evidence.jsonl:{index}: missing link to parent thread"
                )
        result["files"]["evidence.jsonl"] = {"rows": len(evidence)}

    if not result["files"]:
        result["warnings"].append("no recognized reddit-search artifacts found")
    return result


def summarize_run(run_dir: Path) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "run_dir": str(run_dir),
        "unique_threads": 0,
        "subreddits": [],
        "evidence_items": 0,
        "evidence_threads": 0,
        "query_batches": 0,
        "query_families": 0,
        "new_high_value_threads_by_batch": [],
        "remaining_gaps": [],
    }

    candidates_path = run_dir / "candidates.jsonl"
    if candidates_path.exists():
        candidates = _read_jsonl(candidates_path)
        keys = {_candidate_key(row) for row in candidates}
        summary["unique_threads"] = len({key for key in keys if key})
        summary["subreddits"] = sorted(
            {str(row["subreddit"]) for row in candidates if row.get("subreddit")}
        )

    evidence_path = run_dir / "evidence.jsonl"
    if evidence_path.exists():
        evidence = _read_jsonl(evidence_path)
        summary["evidence_items"] = len(evidence)
        summary["evidence_threads"] = len(
            {
                str(row.get("post_id") or row.get("thread_url") or "").strip()
                for row in evidence
                if row.get("post_id") or row.get("thread_url")
            }
        )

    coverage_path = run_dir / "coverage.json"
    if coverage_path.exists():
        coverage = _read_json(coverage_path)
        if not isinstance(coverage, dict):
            raise ValueError(f"{coverage_path}: expected top-level JSON object")
        batches = coverage.get("query_batches") or []
        if not isinstance(batches, list):
            raise ValueError(f"{coverage_path}: query_batches must be a list")
        summary["query_batches"] = len(batches)
        query_families: set[str] = set()
        yields: list[int | None] = []
        for batch in batches:
            if not isinstance(batch, dict):
                continue
            label = batch.get("label")
            if label:
                query_families.add(str(label))
            value = batch.get("new_high_value_threads")
            yields.append(value if isinstance(value, int) else None)
        summary["query_families"] = len(query_families)
        summary["new_high_value_threads_by_batch"] = yields
        gaps = coverage.get("remaining_gaps") or []
        if isinstance(gaps, list):
            summary["remaining_gaps"] = [str(item) for item in gaps]

    return summary


def _json_dump(value: Any) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    normalize = subparsers.add_parser("normalize", help="canonicalize a Reddit thread URL")
    normalize.add_argument("url")

    validate = subparsers.add_parser("validate", help="validate a reddit-search run directory")
    validate.add_argument("run_dir", type=Path)

    summary = subparsers.add_parser("summary", help="summarize deterministic run coverage")
    summary.add_argument("run_dir", type=Path)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "normalize":
            print(canonicalize_thread_url(args.url))
        elif args.command == "validate":
            _json_dump(validate_run(args.run_dir))
        elif args.command == "summary":
            _json_dump(summarize_run(args.run_dir))
        else:  # pragma: no cover - argparse guarantees a known command.
            raise AssertionError(args.command)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
