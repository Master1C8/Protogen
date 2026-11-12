#!/usr/bin/env python3
"""Validate authored text and build additive Ren'Py localization scripts."""

import argparse
from collections import Counter
from hashlib import md5, sha256
import json
import os
from pathlib import Path
import re
from tempfile import NamedTemporaryFile

from extract_text import TEXT_TAG, digest, literals, pin_install, read, read_templates, require, validate
from install_language_picker import (
    PREFERENCES_PATH, PROJECT, SAMPLE_PATH, SAMPLE_SOURCE, install_files, picker_override,
)


LOCALES = {"ru": "russian", "pl": "polish"}
VERIFIED_TEXT_HASHES = {
    "russian": {
        "63866540a4fed4bc3d0b5da4b03edf8689ee1a54d3264034bf33124e177712ef",
        "fdf5e3c4d8848cb94a0e4354c077b2bd00a701bfabffa87153779ee72d889e30",
    },
    "polish": {
        "678485bc11a01839a078a73dcb386252dda771d6437fe56b6753c5afa4d682a1",
        "026c85dd913ddda722abfcef71db21565284d360d44cb40a12ca61d909400713",
    },
}
STORY_ROLES = {"dialogue", "narration"}
STRING_ROLES = {"engine-string", "input-prompt", "interface", "speaker-label"}
EXTRA_KEYS = {"Language", "Juno", "Damien", "Pixie"}
DISPLAY_PATH = Path("game/vnrevival_protogen_display.rpy")
GALLERY_RETURN = 'textbutton ("Back" if _preferences.language is None else _("Return"))'
PREVIOUS_GALLERY_RETURN = 'textbutton _("Back") text_color "#aaaaaa"'
FALLBACK_CONDITION = 'renpy.get_filename_line() in (("game/script.rpy", 85), ("game/script.rpy", 81))'
PREVIOUS_FALLBACK_CONDITION = 'renpy.get_filename_line() == ("game/script.rpy", 85)'
FALLBACK_COMMENT = "# Both supported scripts use the same fallback assignment at different lines."
PREVIOUS_FALLBACK_COMMENT = "# The shipped start label assigns the fallback at game/script.rpy:85."
POLISH_PICKER_OPTION = (
    '        if "polish" in renpy.known_languages():\n'
    '            textbutton "Polski" id "vnrevival_language_polish" action Language("polish")\n'
)


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


def edition_text(base, edition, path, draft):
    dialogue, strings = authored_text(base, path, draft)
    base_story = story_rows(base)
    edition_story = story_rows(edition)
    shared = base_story.keys() & edition_story.keys()
    for key in shared:
        fields = ("text", "role", "context", "preserveTokens")
        require(all(base_story[key][field] == edition_story[key][field] for field in fields),
                f"Shared story mapping changed: {key}")
    require(string_keys(base) <= string_keys(edition), "Edition removed a base UI key")
    delta = path / "nsfw"
    require((delta / "dialogue.tsv").is_file() and (delta / "strings.json").is_file(),
            f"Missing NSFW translation for {path.name}")
    extra_story = load_dialogue(delta / "dialogue.tsv")
    extra_strings = json.loads(read(delta / "strings.json"), object_pairs_hook=unique_strings)
    aliases = json.loads(read(PROJECT / "localization/nsfw-story-aliases.json"),
                         object_pairs_hook=unique_strings)
    for target, original in aliases.items():
        require(target in edition_story and target not in shared and original in base_story,
                f"Invalid NSFW alias: {target}")
        require(all(edition_story[target][field] == base_story[original][field]
                    for field in ("text", "role", "context", "preserveTokens")),
                f"NSFW alias differs from the base statement: {target}")
        require(target not in extra_story, f"NSFW alias also has authored text: {target}")
        if original in dialogue:
            extra_story[target] = dialogue[original]
    for rows, expected, kind in (
        (extra_story, edition_story.keys() - shared, "story rows"),
        (extra_strings, string_keys(edition) - string_keys(base), "UI keys"),
    ):
        require(rows.keys() <= expected, f"Unexpected NSFW {kind}: {sorted(rows.keys() - expected)}")
        require(draft or rows.keys() == expected, f"Missing NSFW {kind}: {len(expected - rows.keys())}")
    for key, value in extra_story.items():
        check_value(key, edition_story[key]["text"], value)
    for key, value in extra_strings.items():
        check_value(key, key, value)
    print(f"NSFW delta: {len(extra_story)}/{len(edition_story) - len(shared)} story rows, "
          f"{len(extra_strings)}/{len(string_keys(edition) - string_keys(base))} UI keys.")
    return ({key: value for key, value in dialogue.items() if key in shared} | extra_story,
            strings | extra_strings)


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


def replace_addon(path, expected, content):
    with NamedTemporaryFile(dir=path.parent, delete=False) as candidate:
        pending = Path(candidate.name)
        try:
            candidate.write(content)
            candidate.close()
            os.chmod(pending, path.stat().st_mode & 0o777)
            require(path.read_bytes() == expected, f"Add-on changed during installation: {path}")
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
    upgrades = {}
    for relative_path, current_fragment, previous_fragment in (
        (DISPLAY_PATH, GALLERY_RETURN + ' text_color "#aaaaaa"', PREVIOUS_GALLERY_RETURN),
        (PREFERENCES_PATH, POLISH_PICKER_OPTION, ""),
    ):
        path = root / relative_path
        if path not in files or not path.is_file():
            continue
        current = files[path]
        fragment = current_fragment.encode()
        if current.count(fragment) != 1:
            continue
        previous = current.replace(fragment, previous_fragment.encode(), 1)
        candidates = {previous}
        if relative_path == DISPLAY_PATH:
            for data in (previous, current):
                candidates.add(data.replace(FALLBACK_CONDITION.encode(), PREVIOUS_FALLBACK_CONDITION.encode())
                               .replace(FALLBACK_COMMENT.encode(), PREVIOUS_FALLBACK_COMMENT.encode()))
        previous = path.read_bytes()
        if previous not in candidates:
            continue
        compiled = path.with_suffix(".rpyc")
        if compiled.exists():
            binary = compiled.read_bytes()
            require(binary.startswith(b"RENPY RPC2") and binary.endswith(md5(previous).digest()),
                    f"Refusing to overwrite an add-on with mismatched bytecode: {path}")
            retired[compiled] = binary
        upgrades[path] = (previous, files.pop(path))

    for locale, hashes in VERIFIED_TEXT_HASHES.items():
        path = root / "game/tl" / locale / "vnrevival_protogen_text.rpy"
        if path not in files or not path.is_file():
            continue
        previous = path.read_bytes()
        if previous == files[path] or sha256(previous).hexdigest() not in hashes:
            continue
        compiled = path.with_suffix(".rpyc")
        if compiled.exists():
            binary = compiled.read_bytes()
            require(binary.startswith(b"RENPY RPC2") and binary.endswith(md5(previous).digest()),
                    f"Refusing to replace translated text with mismatched bytecode: {path}")
            retired[compiled] = binary
        upgrades[path] = (previous, files.pop(path))

    removed = {}
    updated = {}
    try:
        for path, (previous, current) in upgrades.items():
            replace_addon(path, previous, current)
            updated[path] = (previous, current)
        for path, data in retired.items():
            path.unlink()
            removed[path] = data
        install_files(files)
    except (OSError, ValueError):
        for path, (previous, current) in reversed(updated.items()):
            replace_addon(path, current, previous)
        for path, data in removed.items():
            with path.open("xb") as restored:
                restored.write(data)
        raise
    for path in updated:
        print(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("steam_install", type=Path)
    parser.add_argument("locale", choices=LOCALES)
    parser.add_argument("--bundle", type=Path, default=PROJECT / "text-assets")
    parser.add_argument("--nsfw-bundle", type=Path, help="Verified export of the supported Steam DLC")
    parser.add_argument("--steam-manifest", type=Path, help="Steam appmanifest for a detached depot")
    parser.add_argument("--draft", action="store_true", help="Validate a partial authored corpus")
    parser.add_argument("--output", type=Path, help="Build complete scripts in a fresh output directory")
    parser.add_argument("--install", action="store_true", help="Install the complete build into a closed game")
    args = parser.parse_args()
    require(not args.draft or args.output is None, "Draft validation does not produce installable files")
    require(not args.install or args.output is not None, "--install requires --output")
    root = args.steam_install.resolve()
    receipt = json.loads(read(PROJECT / "text-asset-receipt.json"))
    nsfw_receipt = json.loads(read(PROJECT / "text-asset-nsfw-receipt.json"))
    identity = pin_install(root, args.steam_manifest)
    require(identity in (receipt["sources"], nsfw_receipt["sources"]), "Unsupported installed source identity")
    is_nsfw = identity == nsfw_receipt["sources"]
    selected = args.nsfw_bundle if is_nsfw else args.bundle
    require(selected is not None, "This Steam DLC installation requires --nsfw-bundle")
    selected_receipt = nsfw_receipt if is_nsfw else receipt
    for path, expected in receipt["outputSha256"].items():
        require(digest(args.bundle / path) == expected, f"Base extraction mismatch: {path}")
    for path, expected in selected_receipt["outputSha256"].items():
        require(digest(selected / path) == expected, f"Edition extraction mismatch: {path}")
    validate(root, selected, args.steam_manifest)
    source = json.loads(read(args.bundle / "inventory.json"))
    path = PROJECT / "localization" / args.locale
    if is_nsfw:
        edition = json.loads(read(selected / "inventory.json"))
        dialogue, strings = edition_text(source, edition, path, args.draft)
    else:
        dialogue, strings = authored_text(source, path, args.draft)
    if args.output is not None:
        require(not args.output.exists(), f"Output already exists: {args.output}")
        build(selected, args.output, args.locale, dialogue, strings)
        if args.install:
            install(root, args.output)


if __name__ == "__main__":
    main()
