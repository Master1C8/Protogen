#!/usr/bin/env python3
"""Reproduce the independent-review inputs for Polish editorial cycle 01."""

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

from build_localization import EXTRA_KEYS, PROJECT, load_dialogue, require, story_rows, string_keys


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def hash_bytes(data):
    return sha256(data).hexdigest()


def expand(keys, ranges):
    result = set()
    for first, last in ranges:
        require(1 <= first <= last <= len(keys), f"Invalid range {first}–{last}")
        result.update(keys[first - 1:last])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Fresh directory for review inputs")
    args = parser.parse_args()
    root = PROJECT / "localization/pl"
    bundle = PROJECT / "text-assets"
    spec_path = root / "review-dependencies.json"
    receipt_path = root / "semantic-review.json"
    spec = json.loads(spec_path.read_bytes())
    receipt = json.loads(receipt_path.read_bytes())
    inv_bytes = (bundle / "inventory.json").read_bytes()
    scene_bytes = (bundle / "special-scenes.json").read_bytes()
    require(hash_bytes(inv_bytes) == receipt["inventorySha256"], "Inventory changed")
    require(hash_bytes(scene_bytes) == receipt["specialScenesSha256"], "Scene registry changed")
    for name, expected in receipt["currentSha256"].items():
        require(hash_bytes((root / name).read_bytes()) == expected, f"Reviewed input changed: {name}")

    inventory = json.loads(inv_bytes)
    scenes = json.loads(scene_bytes)["cases"]
    story = story_rows(inventory)
    dialogue = load_dialogue(root / "dialogue.tsv")
    strings = json.loads((root / "strings.json").read_bytes())
    require(story.keys() == dialogue.keys(), "Story coverage changed")
    require(string_keys(inventory) == strings.keys(), "UI coverage changed")
    story_order = list(story)
    ui_order = list(strings)
    canonical_ui = list(dict.fromkeys(
        row["text"] for row in inventory if row["text"] in strings
        and row["role"] in ("engine-string", "input-prompt", "interface", "speaker-label")
    ))
    canonical_ui.extend(sorted(EXTRA_KEYS - set(canonical_ui)))
    require(set(canonical_ui) == strings.keys(), "Canonical UI order is incomplete")
    old = {}
    for name, expected in receipt["reviewedSha256"].items():
        raw = subprocess.check_output(
            ["git", "show", f'{receipt["baselineCommit"]}:localization/pl/{name}'], cwd=PROJECT
        )
        require(hash_bytes(raw) == expected, f"Baseline changed: {name}")
        old[name] = raw.decode()
    old_story = dict(line.split("\t", 1) for line in old["dialogue.tsv"].splitlines())
    old_ui = json.loads(old["strings.json"])
    changed_story = [key for key in story if old_story[key] != dialogue[key]]
    changed_ui = [key for key in strings if old_ui[key] != strings[key]]
    require(changed_story == receipt["changedStoryIds"], "Story diff changed")
    require(changed_ui == receipt["changedUiKeys"], "UI diff changed")

    changed_source = {story[key]["text"].strip() for key in changed_story}
    changed_targets = {value for key in changed_story for value in (old_story[key], dialogue[key])}
    components = {
        "storyExchanges": expand(story_order, spec["storyExchanges"]),
        "storyRepetitions": {
            key for key, row in story.items()
            if row["text"].strip() in changed_source
            or old_story[key] in changed_targets or dialogue[key] in changed_targets
        },
        "storyRegressions": expand(story_order, spec["storyRegressions"]),
    }
    require(set(changed_story) <= components["storyExchanges"], "An edit lacks an exchange")
    for name, ranges in spec["storyCallbacks"].items():
        components[f"storyCallback/{name}"] = expand(story_order, ranges)
    for name, patterns in spec["storyGlossaryPatterns"].items():
        pattern = re.compile("|".join(patterns), re.IGNORECASE)
        components[f"storyGlossary/{name}"] = {
            key for key, row in story.items()
            if any(pattern.search(value) for value in (row["text"], old_story[key], dialogue[key]))
        }
    story_runtime = {key for case in scenes for key in case["occurrences"] if key in story}
    components["storyRuntime"] = story_runtime

    ui_components = {name: expand(ui_order, ranges) for name, ranges in spec["uiBindings"].items()}
    selected_ui = set().union(*ui_components.values())
    require(set(changed_ui) <= selected_ui, "An edit lacks a UI binding")
    selected_story = set().union(*components.values())
    context_ids = {key for case in scenes for key in case["occurrences"] if key not in story}
    ordered = {
        "changed-story.json": changed_story,
        "changed-ui.json": [key for key in canonical_ui if key in changed_ui],
        "closure-story.json": [key for key in story_order if key in selected_story],
        "closure-ui.json": [key for key in canonical_ui if key in selected_ui],
        "components.json": {
            "story": {name: [key for key in story_order if key in keys]
                      for name, keys in components.items()},
            "ui": {name: [key for key in canonical_ui if key in keys]
                   for name, keys in ui_components.items()},
        },
        "runtime-context.json": {
            "cases": scenes, "occurrences": [row for row in inventory if row["id"] in context_ids]
        },
    }
    require(len(ordered["runtime-context.json"]["occurrences"]) == len(context_ids),
            "A scene context ID is unbound")
    occurrences = {key: [] for key in selected_ui}
    for row in inventory:
        if row["text"] in occurrences and row["role"] not in ("dialogue", "narration"):
            occurrences[row["text"]].append(row)
    if "Language" in occurrences:
        picker = PROJECT / "localization/language_picker.rpy"
        line, = (n for n, text in enumerate(picker.read_text().splitlines(), 1)
                 if text.strip() == 'label _("Language")')
        occurrences["Language"].append({
            "path": str(picker.relative_to(PROJECT)), "line": line, "role": "interface",
        })
    require(all(occurrences.values()), "A UI key lacks a display source binding")
    ordered["story-review.json"] = [
        dict(story[key], before=old_story[key], after=dialogue[key])
        for key in ordered["closure-story.json"]
    ]
    ordered["ui-review.json"] = [
        dict(key=key, occurrences=[row for row in occurrences[key] if row["role"] != "preserve-exactly"],
             protectedContext=[row for row in occurrences[key] if row["role"] == "preserve-exactly"],
             before=old_ui[key], after=strings[key])
        for key in ordered["closure-ui.json"]
    ]
    files = {name: json_bytes(value) for name, value in ordered.items()}
    manifest = {
        "locale": receipt["locale"],
        "steamBuild": receipt["steamBuild"],
        "newline": "LF",
        "encoding": "UTF-8",
        "reviewReceiptSha256": hash_bytes(receipt_path.read_bytes()),
        "dependencySpecSha256": hash_bytes(spec_path.read_bytes()),
        "generatorSha256": hash_bytes(Path(__file__).read_bytes()),
        "counts": {name: len(ordered[name]) for name in (
            "changed-story.json", "changed-ui.json", "closure-story.json", "closure-ui.json"
        )},
        "sha256": {name: hash_bytes(data) for name, data in files.items()},
    }
    args.output.mkdir()
    for name, data in files.items():
        (args.output / name).write_bytes(data)
    (args.output / "manifest.json").write_bytes(json_bytes(manifest))
    print(manifest["counts"])


if __name__ == "__main__":
    main()
