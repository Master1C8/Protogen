#!/usr/bin/env python3
"""Export and validate the text in the installed Steam build of My Furry Protogen."""

import argparse
import ast
from collections import Counter
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import tokenize

APP = "2009010"
BUILD = "11915262"
LANGUAGE = "protogen_source"
SOURCE_FILES = (
    "game/script.rpy", "game/screens.rpy", "game/gui.rpy",
    "game/options.rpy", "game/tl/None/common.rpym",
)
TEMPLATES = ("common.rpy", "options.rpy", "screens.rpy", "script.rpy")
WINE = Path("/Applications/CrossOver.app/Contents/SharedSupport/CrossOver/bin/wine")
TEXT_TAG = re.compile(r"\{[^{}]*\}|\[[^\[\]]+\]|%[a-zA-Z]")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return path.read_text(encoding="utf-8-sig")


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def literals(source):
    return [token for token in tokenize.generate_tokens(io.StringIO(source).readline)
            if token.type == tokenize.STRING]


def literal_value(token):
    return ast.literal_eval(token.string)


def runtime_say(token):
    # Ren'Py 8.0.3 Lexer.string collapses whitespace before unescaping.
    require(token.string[0] in "\"'", f"Unsupported say literal at {token.start}")
    escaped = re.sub(r"\s+", " ", token.string[1:-1])
    replacements = {"{": "{{", "[": "[[", "%": "%%", "n": "\n"}

    def unescape(match):
        if match[2]:
            return chr(int(match[2], 16))
        return replacements.get(match[1], match[1])

    return re.sub(r"\\(u([0-9a-fA-F]{1,4})|.)", unescape, escaped)


def native_export(root, stage, bottle):
    for directory in ("lib", "renpy"):
        shutil.copytree(root / directory, stage / directory)
    shutil.copyfile(root / "MyFurryProtogen.py", stage / "MyFurryProtogen.py")
    for name in SOURCE_FILES:
        target = stage / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / name, target)

    win = "Z:" + str(stage.resolve()).replace("/", "\\")
    command = [
        str(WINE), "--bottle", bottle, "--workdir", str(stage.resolve()),
        "--cx-app", win + r"\lib\py3-windows-x86_64\python.exe",
        win + r"\MyFurryProtogen.py", win,
    ]
    env = dict(os.environ, SDL_VIDEODRIVER="dummy", SDL_AUDIODRIVER="dummy")
    for args in (("dialogue", "None", "--strings"), ("translate", LANGUAGE, "--no-todo")):
        subprocess.run(
            [*command, *args, "--savedir", win + r"\scratch-saves"],
            env=env, check=True, timeout=90,
        )


def pin_install(root, steam_manifest=None):
    manifest = read(steam_manifest or root.parent.parent / f"appmanifest_{APP}.acf")
    require(re.search(rf'"buildid"\s+"{BUILD}"', manifest), f"Expected Steam build {BUILD}")
    require(read(root / "game/script_version.txt").strip() == "(8, 0, 3)", "Unexpected script engine")
    receipt = {}
    for name in SOURCE_FILES:
        source = root / name
        compiled = root / (name + "c")
        binary = compiled.read_bytes()
        require(binary.startswith(b"RENPY RPC2"), f"Unrecognized compiled header: {name}")
        require(hashlib.md5(source.read_bytes()).digest() == binary[-16:],
                f"Installed compiled-source digest mismatch: {name}")
        receipt[name] = {"sha256": digest(source), "compiledSha256": digest(compiled)}
    return receipt


def read_templates(bundle):
    dialogue, interface, common = {}, {}, {}
    for name in TEMPLATES:
        source = read(bundle / "renpy-templates" / name)
        for match in re.finditer(rf"^# (game/.+?):(\d+)\ntranslate {LANGUAGE} (\w+):\n\n    # [^\n]*\n    (.+)$",
                                 source, re.M):
            path, line, identifier, statement = match.groups()
            tokens = literals(statement + "\n")
            require(len(tokens) == 1 and identifier not in dialogue,
                    f"Unexpected dialogue statement for {identifier}")
            dialogue[identifier] = (path, int(line), literal_value(tokens[0]), statement)
        for match in re.finditer(r"^    # (.+?):(\d+)\n    old (.+)\n    new (.+)$", source, re.M):
            path, line, old, new = match.groups()
            value = ast.literal_eval(old)
            require(value == ast.literal_eval(new), f"Template alters source at {path}:{line}")
            target = common if name == "common.rpy" else interface
            key = path, int(line), value
            require(key not in target, f"Duplicate string binding at {path}:{line}")
            target[key] = value
    return dialogue, interface, common


def native_dialogue(bundle, template, interface):
    lines = read(bundle / "renpy-dialogue.tab").split("\n")
    require(lines.pop(0) == "Identifier\tCharacter\tDialogue\tFilename\tLine Number\tRen'Py Script",
            "Unrecognized Ren'Py dialogue header")
    dialogue, strings = {}, set()
    tsv_interface = {(path, line, value.replace("\n", r"\n")) for path, line, value in interface}
    for row in filter(None, lines):
        identifier, speaker, value, path, line, *statement = row.split("\t")
        if not identifier:
            key = path, int(line), value
            require(not statement and key in tsv_interface and key not in strings,
                    f"Unknown native string at {path}:{line}")
            strings.add(key)
            continue
        require(len(statement) == 1 and identifier not in dialogue, f"Duplicate or invalid {identifier}")
        require(identifier in template, f"Missing template dialogue {identifier}")
        t_path, t_line, t_value, t_statement = template[identifier]
        token = literals(t_statement + "\n")[0]
        tsv_statement = t_statement[:token.start[1]] + '"[what]"' + t_statement[token.end[1]:]
        require((t_path, t_line, t_value, tsv_statement) == (path, int(line), value, statement[0]),
                f"Native exports disagree on {identifier}")
        dialogue[identifier] = (path, int(line), speaker, value)
    require(dialogue.keys() == template.keys(), "Dialogue export and template IDs differ")
    return dialogue, strings


def classify(path, token, say_by_location, interface_values):
    prefix = token.line[:token.start[1]].strip()
    value = literal_value(token)
    position = path, token.start[0]
    if position in say_by_location:
        identifier, speaker, expected = say_by_location[position]
        require(prefix.split()[:1] == ([speaker] if speaker else []) and runtime_say(token) == expected,
                f"Source statement does not match Ren'Py dialogue {identifier}")
        return ("dialogue" if speaker else "narration"), expected, identifier, speaker

    if re.search(r"\b(?:_|__|___|_p)\(\s*$", prefix):
        if path == "game/options.rpy" and prefix == "define gui.about = _p(":
            require(not value.strip(), "Previously empty About placeholder now contains text")
            return "preserve-exactly", value, None, "unused empty About placeholder"
        require(value in interface_values, f"Unbound translation marker at {path}:{token.start[0]}")
        return "interface", value, None, "Ren’Py string translation key"

    if path == "game/script.rpy":
        if re.fullmatch(r"define \w+ = Character\(", prefix):
            if value in ("[gname]", "[pname]", "Pixie", "Damien"):
                return "preserve-exactly", value, None, "displayed name identity or interpolation"
            require(value in ("Dad", "Mom", "Elder"), f"Unrecognized Character name: {value}")
            return "speaker-label", value, None, "display name, separate from speaker identifier"
        if prefix == "$ pname = renpy.input(":
            return "input-prompt", value, None, "displayed first-run name prompt"
        if prefix == "$ pname =":
            return "speaker-label", value, None, "fallback player name shown in dialogue and nameplates"
        require(prefix.startswith(("define ", "if pname ==", "$ gname =", "$ renpy.movie_cutscene(")),
                f"Unclassified script literal at {token.start}")
        return "preserve-exactly", value, None, "asset path, engine argument, identity, or comparison value"

    if path.endswith("common.rpym"):
        require(prefix in ("old", "new"), f"Unclassified common entry at {token.start}")
        return ("engine-string" if prefix == "new" else "preserve-exactly"), value, None, (
            "default engine display value" if prefix == "new" else "exact engine lookup key")

    if path == "game/screens.rpy":
        if prefix in ("text", "textbutton", "label"):
            if value in {"Back", "Made by", "Art", "Music", "Additional help"}:
                return "interface", value, None, "unmarked screen caption"
            require(value in {"[config.name!t]", "[config.version]", "[page]", "[message!tq]",
                              "H", "S", "V", "▸"} or value.startswith("{color=#9933ff}"),
                    f"Unclassified screen display literal at {token.start}: {value!r}")
            return "preserve-exactly", value, None, "render binding, glyph, keyboard label, or credit name"
        return "preserve-exactly", value, None, "screen option, style, action, state, or resource identifier"

    return "preserve-exactly", value, None, "configuration, style, build option, or resource identifier"


def inventory(bundle, root):
    template, interface, common = read_templates(bundle)
    dialogue, tsv_strings = native_dialogue(bundle, template, interface)
    by_location = {(path, line): (identifier, speaker, text)
                   for identifier, (path, line, speaker, text) in dialogue.items()}
    require(len(by_location) == len(dialogue), "Dialogue line locations are ambiguous")
    result = []
    interface_values = set(interface.values())
    for path in SOURCE_FILES:
        source = read(bundle / "original" / path)
        for token in literals(source):
            role, value, native_id, context = classify(
                path, token, by_location, interface_values)
            line, column = token.start
            item = {
                "id": native_id or f"{path}:{line}:{column + 1}",
                "path": path,
                "line": line,
                "column": column + 1,
                "endLine": token.end[0],
                "endColumn": token.end[1] + 1,
                "role": role,
                "text": value,
                "sourceLiteral": token.string,
                "preserveTokens": TEXT_TAG.findall(value) if role != "preserve-exactly" else [],
                "context": context,
            }
            result.append(item)

    require(len({row["id"] for row in result}) == len(result), "Duplicate inventory IDs")
    require({row["id"] for row in result if row["role"] in ("dialogue", "narration")} == dialogue.keys(),
            "Source token coverage differs from native dialogue")
    require(set(interface) <= {(row["path"], row["line"], row["text"]) for row in result},
            "Native translation template has a string without a source token")
    engine_keys = [row["text"] for row in result if row["path"].endswith("common.rpym")]
    require(engine_keys[::2] == engine_keys[1::2], "Shipped default engine translations are not identity values")
    extra_common = [(path, line, value) for path, line, value in common if value not in engine_keys]
    require({value for _, _, value in extra_common} == {
        "High Contrast Text", "Open [text] directory.", "accessibility menu",
        "audio when minimized", "high contrast text", "main volume", "mute main", "renderer menu",
    }, "Generated engine strings differ from the reviewed set")
    for path, line, value in extra_common:
        matches = [token for token in literals(read(root / path))
                   if token.start[0] == line and literal_value(token) == value]
        require(len(matches) == 1, f"Missing engine source binding at {path}:{line}")
        token = matches[0]
        is_preference = path.endswith("00preferences.rpy")
        result.append({
            "id": f"{path}:{line}:{token.start[1] + 1}",
            "path": path, "line": line, "column": token.start[1] + 1,
            "endLine": token.end[0], "endColumn": token.end[1] + 1,
            "role": "preserve-exactly" if is_preference else "engine-string",
            "text": value, "sourceLiteral": token.string, "preserveTokens": TEXT_TAG.findall(value),
            "context": "engine preference dispatch key" if is_preference else "engine accessibility display text",
        })
    return result, {"nativeDialogue": len(dialogue), "nativeTsvStrings": len(tsv_strings),
                    "nativeTemplateGameStrings": len(interface), "nativeTemplateCommonStrings": len(common),
                    "nativeCommonOnly": len(extra_common)}


def special_cases(bundle, root, rows):
    def at(path, lines):
        return [row["id"] for row in rows if row["path"] == path and row["line"] in lines]

    script = "game/script.rpy"
    screens = "game/screens.rpy"
    media = ["game/images/watches.webm", "game/images/watchesLong.webm"]
    return {
        "schemaVersion": 1, "steamBuildId": BUILD,
        "inventorySha256": digest(bundle / "inventory.json"),
        "coverage": {
            "inspected": ["dialogue and narration syntax, tags and interpolation", "script control flow",
                          "screen text, actions, format expressions, and default engine string table",
                          "main-menu, in-game menu, and gallery background artwork"],
            "excluded": ["full literary review of the story", "remaining image and video text review",
                         "audio transcription",
                         "DLC outside installed depot 2009011", "runtime reachability and rendering"],
        },
        "cases": [
            {
                "id": "player-name",
                "occurrences": at(script, {13, 82, 84, 85}) + [
                    row["id"] for row in rows if row["role"] in ("dialogue", "narration")
                    and "[pname]" in row["preserveTokens"]],
                "behavior": "Input is capped at 12 characters and stripped. Empty input selects the default name. The name is reused in the nameplate and later dialogue.",
                "route": "Translate prompt and fallback display label. Preserve the empty-string comparison, variable name, and interpolation. Review address forms around the variable.",
                "checks": ["Enter a custom name and confirm it survives in a nameplate and later lines.",
                           "Submit blank and whitespace-only names and verify the fallback appears."],
            },
            {
                "id": "juno-nameplate",
                "occurrences": at(script, {8, 79}),
                "behavior": "Character j displays [gname], which is assigned Juno at start.",
                "route": "Preserve the binding and separate any future localized display name from the speaker ID.",
                "checks": ["Verify Juno’s first and later nameplates use the same name with speaker ID j intact."],
            },
            {
                "id": "save-formats",
                "occurrences": at(screens, {721, 763, 790}),
                "behavior": "Save page names interpolate the page index and occupied slots format a timestamp. Empty slots use their own caption.",
                "route": "Preserve the replacement field and date directives, then review locale order and platform behavior.",
                "checks": ["Compare ordinary, quick and automatic pages and occupied versus empty slots."],
            },
            {
                "id": "dialogue-timing",
                "occurrences": [row["id"] for row in rows if row["role"] in ("dialogue", "narration")
                                and any(t == "{w}" or "cps" in t for t in row["preserveTokens"])],
                "behavior": "Inline wait tags pause display and the final ellipsis uses a scoped speed tag.",
                "route": "Keep paired tags and preserve each intended pause in context.",
                "checks": ["Verify a timed dialogue advance and the final slow ellipsis in the actual renderer."],
            },
            {
                "id": "main-menu-logo",
                "occurrences": at("game/gui.rpy", {91}),
                "assets": [{"path": "game/gui/main_menu.png", "sha256": digest(root / "game/gui/main_menu.png")}],
                "sourceText": "My Furry\nprotogen",
                "behavior": "The visible main-menu title is drawn into the background image.",
                "route": "Preserve the brand artwork unless a localized logo is explicitly planned.",
                "checks": ["Confirm the menu still displays the complete logo and its navigation text."],
            },
            {
                "id": "watch-cutscenes",
                "occurrences": [row["id"] for row in rows if row["path"] == script and row["text"] == "watches.webm"],
                "assets": [{"path": name, "sha256": digest(root / name)} for name in media],
                "behavior": "The script repeatedly calls the same movie. A second similarly named video is shipped.",
                "route": "Keep movie paths. Inspect both videos for embedded text separately before accepting visual coverage.",
                "checks": ["Verify a watched scene returns to the next scripted line and inspect both videos for baked-in wording."],
            },
        ],
        "status": {"staticBindings": "passed", "localeAdaptation": "not-run",
                   "reinsertion": "not-run", "runtime": "not-run", "visual": "not-run"},
    }


def snapshot(root, stage, output):
    require(not output.exists(), f"Output already exists: {output}")
    source_files = pin_install(root)
    with tempfile.TemporaryDirectory(prefix=".protogen-export-", dir=output.parent) as temporary:
        bundle = Path(temporary) / "bundle"
        (bundle / "renpy-templates").mkdir(parents=True)
        for name in SOURCE_FILES:
            target = bundle / "original" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / name, target)
        shutil.copyfile(stage / "dialogue.tab", bundle / "renpy-dialogue.tab")
        for name in TEMPLATES:
            shutil.copyfile(stage / "game/tl" / LANGUAGE / name, bundle / "renpy-templates" / name)
        rows, native_counts = inventory(bundle, root)
        dump(bundle / "inventory.json", rows)
        dump(bundle / "preserve-exactly.json", [row for row in rows if row["role"] == "preserve-exactly"])
        dump(bundle / "special-scenes.json", special_cases(bundle, root, rows))
        dump(bundle / "manifest.json", {
            "schemaVersion": 1, "game": "My Furry Protogen", "steamAppId": APP,
            "steamBuildId": BUILD, "sourceLanguage": "en", "renpy": "8.0.3.22090809",
            "sources": source_files, "counts": dict(Counter(row["role"] for row in rows)),
            "native": native_counts,
            "outputSha256": {str(p.relative_to(bundle)): digest(p)
                             for p in sorted(bundle.rglob("*")) if p.is_file()},
        })
        validate(root, bundle)
        bundle.rename(output)


def validate(root, bundle, steam_manifest=None):
    source_files = pin_install(root, steam_manifest)
    manifest = json.loads(read(bundle / "manifest.json"))
    require(manifest["sources"] == source_files, "Installed source identity changed")
    for name in SOURCE_FILES:
        require((root / name).read_bytes() == (bundle / "original" / name).read_bytes(),
                f"Original byte comparison failed: {name}")
    for name, expected in manifest["outputSha256"].items():
        require(digest(bundle / name) == expected, f"Output checksum mismatch: {name}")
    rows, native_counts = inventory(bundle, root)
    require(rows == json.loads(read(bundle / "inventory.json")), "Inventory/source mapping differs")
    require(native_counts == manifest["native"], "Native counts changed")
    require(dict(Counter(row["role"] for row in rows)) == manifest["counts"], "Role counts changed")
    exact = [row for row in rows if row["role"] == "preserve-exactly"]
    require(exact == json.loads(read(bundle / "preserve-exactly.json")), "Protected fields differ")
    registry = json.loads(read(bundle / "special-scenes.json"))
    require(registry == special_cases(bundle, root, rows), "Special-scene registry differs")
    known = {row["id"] for row in rows}
    for case in registry["cases"]:
        ids = case["occurrences"]
        require(ids and len(set(ids)) == len(ids) and set(ids) <= known,
                f"Unbound special scene: {case['id']}")
    print(f"Verified Steam build {BUILD}: {len(rows)} literals, {len(exact)} protected, "
          f"{native_counts['nativeDialogue']} native dialogue/narration rows.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("extract", "verify"))
    parser.add_argument("game_root", type=Path)
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--bottle", default="Steam")
    parser.add_argument("--engine-stage", type=Path, help="Reuse a completed temporary engine export")
    args = parser.parse_args()
    root, bundle = args.game_root.resolve(), args.bundle.resolve()
    if args.action == "verify":
        validate(root, bundle)
    elif args.engine_stage:
        snapshot(root, args.engine_stage.resolve(), bundle)
    else:
        pin_install(root)
        with tempfile.TemporaryDirectory(prefix="protogen-renpy-") as directory:
            stage = Path(directory)
            native_export(root, stage, args.bottle)
            snapshot(root, stage, bundle)


if __name__ == "__main__":
    main()
