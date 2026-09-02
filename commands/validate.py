#!/usr/bin/env python3
"""Validate the command map, router cases, and core state templates."""

from collections import Counter, defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


spellbook = load_yaml(ROOT / "commands" / "spellbook.yaml")
cases_doc = load_yaml(ROOT / "commands" / "router_cases.yaml")
mastery = load_yaml(ROOT / "status" / "mastery.yaml")

assert spellbook["schema_version"] == 2
assert mastery["schema_version"] == 2
assert spellbook["trigger"]["keyword"] == "炼丹炉"
assert set(spellbook["trigger"]["modes"]) == {"INVOKE", "MENTION"}
assert len(spellbook["gateway_intents"]) == 5

commands = spellbook["commands"]
command_ids = {command["id"] for command in commands}
assert len(command_ids) == len(commands), "duplicate command id"

phrases = defaultdict(list)
for command in commands:
    phrases[command["canonical_phrase"]].append(command["id"])
    for alias in command["aliases"]:
        phrases[alias].append(command["id"])
    assert command["full_instruction"]["steps"], command["id"]
    assert "writes" in command["full_instruction"], command["id"]

conflicts = {phrase: ids for phrase, ids in phrases.items() if len(set(ids)) > 1}
assert not conflicts, f"phrase conflicts: {conflicts}"

gateway_membership = Counter()
for gateway, spec in spellbook["gateway_intents"].items():
    missing = set(spec["candidate_commands"]) - command_ids
    assert not missing, f"{gateway} references missing commands: {missing}"
    gateway_membership.update(spec["candidate_commands"])

overlap = {command_id: count for command_id, count in gateway_membership.items() if count > 1}
assert not overlap, f"commands in multiple gateways: {overlap}"
assert set(gateway_membership) == command_ids, "every command must have one default gateway"

formal_openbook_writers = []
for command in commands:
    writes = command["full_instruction"]["writes"]
    if "output/openbook/" in writes:
        formal_openbook_writers.append(command["id"])
assert formal_openbook_writers == ["OUTPUT-OPENBOOK"], formal_openbook_writers

case_ids = set()
for case in cases_doc["cases"]:
    assert case["id"] not in case_ids, f"duplicate router case: {case['id']}"
    case_ids.add(case["id"])
    assert isinstance(case["confirmation"], bool), case["id"]
    assert case["forbidden"], case["id"]
    if case["mode"] == "MENTION":
        assert case["gateway"] is None and case["primary_command"] is None, case["id"]
        continue
    assert case["mode"] == "INVOKE", case["id"]
    assert case["gateway"] in spellbook["gateway_intents"], case["id"]
    assert case["primary_command"] in command_ids, case["id"]
    for subcommand in case.get("subcommands", []):
        assert subcommand in command_ids, case["id"]

for chapter in mastery["chapters"]:
    assert set(chapter["contexts"]) == {"open_book", "closed_book"}, chapter["id"]

assert (ROOT / "output" / "openbook" / "update_queue.md").exists()

print(
    "VALIDATION_OK "
    f"gateways={len(spellbook['gateway_intents'])} "
    f"commands={len(commands)} "
    f"router_cases={len(cases_doc['cases'])} "
    f"formal_openbook_writers={formal_openbook_writers}"
)
