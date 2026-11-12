#!/usr/bin/env python3
"""Validate authored text and build additive Ren'Py localization scripts."""

import argparse
from collections import Counter
from hashlib import md5
import json
import os
from pathlib import Path
import re
from tempfile import NamedTemporaryFile

from extract_text import TEXT_TAG, digest, literals, read, read_templates, require, validate
from install_language_picker import (
    PREFERENCES_PATH, PROJECT, SAMPLE_PATH, SAMPLE_SOURCE, install_files, picker_override,
)


LOCALES = {"ru": "russian", "pl": "polish"}
STORY_ROLES = {"dialogue", "narration"}
STRING_ROLES = {"engine-string", "input-prompt", "interface", "speaker-label"}
EXTRA_KEYS = {"Language", "Juno", "Damien", "Pixie"}
DISPLAY_PATH = Path("game/vnrevival_protogen_display.rpy")
GALLERY_RETURN = 'textbutton ("Back" if _preferences.language is None else _("Return"))'
PREVIOUS_GALLERY_RETURN = 'textbutton _("Back") text_color "#aaaaaa"'


def story_rows(source):
    return {row["id"]: row for row in source if row["role"] in STORY_ROLES}


def string_keys(source):
    return set(row["text"] for row in source if row["role"] in STRING_ROLES) | EXTRA_KEYS


def load_dialogue(path):
    result = {}
    for number, line in enumerate(read(path).split("\n"), 1):
        if not line:
            continue
        key, separator, value = line.partition("\t")
        require(separator and value.strip() and "\t" not in value and key not in result,
                f"{path}:{number}: expected a unique ID and nonempty dialogue")
        result[key] = value
    return result


def unique_strings(pairs):
    result = dict(pairs)
    require(len(result) == len(pairs), "Duplicate translation string key")
    return result


def quote(value):
    return json.dumps(value, ensure_ascii=False)


def check_value(key, source, target):
    require(isinstance(target, str) and target.strip(), f"Empty translation for {key}")
    require(Counter(TEXT_TAG.findall(target)) == Counter(TEXT_TAG.findall(source)),
            f"Changed markup, placeholders or date directives for {key}")
    require(target.count("{}") == source.count("{}"),
            f"Changed positional format placeholders for {key}")


def authored_text(source, path, draft):
    story = story_rows(source)
    keys = string_keys(source)
    dialogue = load_dialogue(path / "dialogue.tsv")
    strings = json.loads(read(path / "strings.json"), object_pairs_hook=unique_strings)
    for rows, expected, kind in ((dialogue, story.keys(), "dialogue"), (strings, keys, "strings")):
        require(rows.keys() <= expected, f"Unexpected {kind}: {sorted(rows.keys() - expected)}")
        if not draft:
            require(rows.keys() == expected, f"Missing {kind}: {len(expected - rows.keys())}")
    for key, target in dialogue.items():
        check_value(key, story[key]["text"], target)
    for key, target in strings.items():
        check_value(repr(key), key, target)
    print(f"Story {len(dialogue)}/{len(story)}. String keys {len(strings)}/{len(keys)}.")
    return dialogue, strings


def screen_overrides(source):
    names = {
        # The other Back buttons roll the story back. The gallery returns to its caller.
        "gallery": {'textbutton "Back"': GALLERY_RETURN},
        "about": {
            f'text "{label}"': f'text _("{label}")'
            for label in ("Made by", "Art", "Music", "Additional help")
        },
        "input": {"text prompt style": "text renpy.translate_string(prompt) style"},
    }
    screens = []
    for name, replacements in names.items():
        pattern = rf"^screen {name}\([^\n]*\):\n(?:^[ \t]+[^\n]*\n|^\n)*"
        match = re.search(pattern, source, re.M)
        require(match is not None, f"Missing screen {name}")
        original = match[0]
        updated = original
        for literal, replacement in replacements.items():
            require(updated.count(literal) == 1, f"Unexpected binding {name}: {literal}")
            updated = updated.replace(literal, replacement)
        screens.append(updated.rstrip())
    return "\n\n".join(screens)


def build(bundle, output, locale, dialogue, strings):
    runtime_locale = LOCALES[locale]
    template, _, _ = read_templates(bundle)
    lines = [f"translate {runtime_locale} strings:"]
    for key, value in sorted(strings.items()):
        lines.extend(("", f"    old {quote(key)}", f"    new {quote(value)}"))
    for key, (_, _, _, source) in template.items():
        if key not in dialogue:
            continue
        token, = literals(source + "\n")
        statement = source[:token.start[1]] + quote(dialogue[key]) + source[token.end[1]:]
        lines.extend(("", f"translate {runtime_locale} {key}:", f"    {statement}"))
    locale_dir = output / "game/tl" / runtime_locale
    locale_dir.mkdir(parents=True)
    (locale_dir / "vnrevival_protogen_text.rpy").write_text("\n".join(lines) + "\n", encoding="utf-8")

    screens = read(bundle / "original/game/screens.rpy")
    (output / PREFERENCES_PATH).write_text(picker_override(screens), encoding="utf-8")
    adapter = read(PROJECT / "localization/display_adapter.rpy")
    (output / DISPLAY_PATH).write_text(
        adapter.rstrip() + "\n\n" + screen_overrides(screens) + "\n", encoding="utf-8"
    )


def replace_display(path, expected, content):
    with NamedTemporaryFile(dir=path.parent, delete=False) as candidate:
        pending = Path(candidate.name)
        try:
            candidate.write(content)
            candidate.close()
            os.chmod(pending, path.stat().st_mode & 0o777)
            require(path.read_bytes() == expected, f"Display changed during installation: {path}")
            os.replace(pending, path)
        finally:
            pending.unlink(missing_ok=True)


def install(root, output):
    sample = root / SAMPLE_PATH
    compiled_sample = sample.with_suffix(".rpyc")
    sample_bytes = SAMPLE_SOURCE.read_bytes()
    retired = {}
    if sample.exists():
        retired[sample] = sample.read_bytes()
        require(retired[sample] == sample_bytes, f"Refusing to remove different sample: {sample}")
    if compiled_sample.exists():
        binary = compiled_sample.read_bytes()
        require(binary.startswith(b"RENPY RPC2") and binary.endswith(md5(sample_bytes).digest()),
                f"Refusing to remove different compiled sample: {compiled_sample}")
        retired[compiled_sample] = binary

    files = {root / p.relative_to(output): p.read_bytes() for p in sorted(output.rglob("*.rpy"))}
    display = root / DISPLAY_PATH
    pending_display = None
    if display.is_file() and display in files:
        old_display = display.read_bytes()
        new_display = files[display]
        new_gallery_return = (GALLERY_RETURN + ' text_color "#aaaaaa"').encode()
        if new_display.count(new_gallery_return) == 1 and old_display == new_display.replace(
                new_gallery_return, PREVIOUS_GALLERY_RETURN.encode(), 1):
            compiled_display = display.with_suffix(".rpyc")
            if compiled_display.exists():
                binary = compiled_display.read_bytes()
                require(binary.startswith(b"RENPY RPC2") and binary.endswith(md5(old_display).digest()),
                        f"Refusing to overwrite a display with mismatched bytecode: {display}")
            pending_display = files.pop(display)
    removed = {}
    updated_display = False
    try:
        if pending_display is not None:
            replace_display(display, old_display, pending_display)
            updated_display = True
        for path, data in retired.items():
            path.unlink()
            removed[path] = data
        install_files(files)
    except (OSError, ValueError):
        if updated_display:
            replace_display(display, pending_display, old_display)
        for path, data in removed.items():
            with path.open("xb") as restored:
                restored.write(data)
        raise
    if updated_display:
        print(display)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("steam_install", type=Path)
    parser.add_argument("locale", choices=LOCALES)
    parser.add_argument("--bundle", type=Path, default=PROJECT / "text-assets")
    parser.add_argument("--draft", action="store_true", help="Validate a partial authored corpus")
    parser.add_argument("--output", type=Path, help="Build complete scripts in a fresh output directory")
    parser.add_argument("--install", action="store_true", help="Install the complete build into a closed game")
    args = parser.parse_args()
    require(not args.draft or args.output is None, "Draft validation does not produce installable files")
    require(not args.install or args.output is not None, "--install requires --output")
    validate(args.steam_install.resolve(), args.bundle)
    receipt = json.loads(read(PROJECT / "text-asset-receipt.json"))
    require(digest(args.bundle / "inventory.json") == receipt["outputSha256"]["inventory.json"],
            "Source inventory differs from the canonical extraction receipt")
    source = json.loads(read(args.bundle / "inventory.json"))
    dialogue, strings = authored_text(source, PROJECT / "localization" / args.locale, args.draft)
    if args.output is not None:
        require(not args.output.exists(), f"Output already exists: {args.output}")
        build(args.bundle, args.output, args.locale, dialogue, strings)
        if args.install:
            install(args.steam_install.resolve(), args.output)


if __name__ == "__main__":
    main()
