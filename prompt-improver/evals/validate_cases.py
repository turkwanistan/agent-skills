#!/usr/bin/env python3
from pathlib import Path
import json

path = Path(__file__).with_name("cases.json")
cases = json.loads(path.read_text())
assert isinstance(cases, list) and cases, "cases.json must contain a non-empty list"
required = {"id", "target", "draft", "expected", "must_preserve", "must_not_add"}
ids = set()
for i, case in enumerate(cases):
    missing = required - case.keys()
    assert not missing, f"case {i} missing {sorted(missing)}"
    assert case["id"] not in ids, f"duplicate id: {case['id']}"
    ids.add(case["id"])
    assert isinstance(case["draft"], str) and case["draft"].strip()
    assert isinstance(case["expected"], str) and case["expected"].strip()
    assert isinstance(case["must_preserve"], list)
    assert isinstance(case["must_not_add"], list)
print(f"PASS: {len(cases)} prompt-improver regression cases")
