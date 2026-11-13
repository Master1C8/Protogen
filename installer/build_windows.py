#!/usr/bin/env python3
"""Build the offline Windows installer from the verified Protogen inputs."""

import argparse
import json
from pathlib import Path
from shutil import copy2, make_archive
import subprocess
import sys
from tempfile import TemporaryDirectory
import tarfile

PROJECT = Path(__file__).resolve().parents[1]
HERE = PROJECT / "installer"
sys.path.insert(0, str(PROJECT / "tools"))

from build_localization import authored_text, build, edition_text
from extract_text import digest, require, validate
from localization_languages import LOCALES

APP_ID = "2009010"
BUILD_ID = "11915262"
VERSION = "1.0.0"
SDK_SHA256 = "0043c0110654d9c526ddf6419c800fc99ddf35dea8993ebf2126c4b2f16c90c2"
RUNTIME = ".vnrevival-protogen/runtime"
EXE = "Protogen Localization Installer.exe"
ART = {
    "images/bg jet main.png": "5f036c2fdac5cb501434501cfcd18f757b3fc2f1a6a358027c14e54bf83a1fa0",
    "images/j front armor happy.png": "0d86e319b9afa83ad5f3ec3b56edbc8fbff6cd42731fbe919416a5486afd3908",
    "gui/window_icon.png": "9c8903906cc3cbca1e2a688309d501cf6276386c00ebcca5278d956dcb5aaf40",
}


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def files(root):
    return sorted(p for p in root.rglob("*") if p.is_file())


def package_files(root):
    return [{"path": p.relative_to(root).as_posix(), "sha256": digest(p)} for p in files(root)]


def edition_payload(name, root, bundle, base, steam_manifest, font_source, payload):
    suffix = "-nsfw" if name == "dlc" else ""
    expected = json.loads((PROJECT / f"text-asset{suffix}-receipt.json").read_text())
    for path, sha256 in expected["outputSha256"].items():
        require(digest(bundle / path) == sha256, f"{name}: extraction mismatch: {path}")
    validate(root, bundle, steam_manifest)
    source = json.loads((bundle / "inventory.json").read_text())
    target = payload / name
    for code in LOCALES:
        author = PROJECT / "localization" / code
        print(f"{name}/{code}: ", end="")
        dialogue, strings = (edition_text(base, source, author, False) if name == "dlc"
                             else authored_text(source, author, False))
        build(bundle, target, code, dialogue, strings, font_source)
    identity = {"game/script_version.txt": digest(root / "game/script_version.txt"),
                "MyFurryProtogen.exe": digest(root / "MyFurryProtogen.exe")}
    for path, hashes in expected["sources"].items():
        identity[path] = hashes["sha256"]
        identity[path + "c"] = hashes["compiledSha256"]
    return {"name": name, "original": identity, "files": package_files(target)}


def runtime_payload(archive, payload):
    require(digest(archive) == SDK_SHA256, "Ren'Py SDK archive does not match the verified build")
    target = payload / "common" / RUNTIME
    target.mkdir(parents=True)
    prefixes = ("renpy/", "lib/python3.9/", "lib/py3-windows-x86_64/")
    with tarfile.open(archive, "r:bz2") as sdk:
        for member in sdk:
            prefix, _, relative = member.name.partition("/")
            if prefix != "renpy-8.2.3-sdk" or not member.isfile():
                continue
            if relative not in ("renpy.py", "LICENSE.txt") and not relative.startswith(prefixes):
                continue
            if "__pycache__" in relative.split("/"):
                continue
            path = target / relative
            require(path.resolve().is_relative_to(target.resolve()), f"Unsafe SDK path: {relative}")
            path.parent.mkdir(parents=True, exist_ok=True)
            with sdk.extractfile(member) as src, path.open("xb") as dst:
                dst.write(src.read())
    # Start the init-code watchdog after compiling the scripts. On a slow
    # first launch, compilation of all locales can consume the engine's
    # pre-init deadline before any game code has run.
    main = target / "renpy/main.py"
    source = main.read_bytes()
    before = b'    log_clock("Loading script")'
    require(source.count(before) == 1, "Unexpected Ren'Py script-load boundary")
    main.write_bytes(source.replace(before, before + b"\n    renpy.execution.not_infinite_loop(60)"))

    required = ("lib/py3-windows-x86_64/pythonw.exe", "lib/python3.9/os.pyc",
                "lib/python3.9/encodings/__init__.pyc")
    require(all((target / path).is_file() for path in required), "Incomplete Ren'Py Windows runtime")
    return package_files(payload / "common")


def compile_window(root, out, work):
    art_paths = [root / "game" / relative for relative in ART]
    for path, sha256 in zip(art_paths, ART.values()):
        require(digest(path) == sha256, f"Unexpected artwork revision: {path}")
    background, portrait, icon = art_paths
    subprocess.run([
        "magick", str(background), "-resize", "310x520^", "-gravity", "center",
        "-extent", "310x520", "-fill", "#0B132C", "-colorize", "27%",
        "(", str(portrait), "-trim", "+repage", "-resize", "310x432", ")",
        "-gravity", "north", "-geometry", "+0+26", "-composite",
        "(", "-size", "310x212", "gradient:#0B132C00-#0B132C", ")",
        "-gravity", "south", "-composite", "-alpha", "off", f"BMP3:{work / 'Panel.bmp'}",
    ], check=True)
    subprocess.run(["magick", str(icon), "-define", "icon:auto-resize=256,128,64,48,32,16",
                    str(work / "Game.ico")], check=True)
    for name in ("Installer.manifest", "Installer.rc"):
        copy2(HERE / "windows" / name, work)
    subprocess.run(["x86_64-w64-mingw32-windres", "Installer.rc", "-O", "coff",
                    "-o", "InstallerResources.o"], cwd=work, check=True)
    subprocess.run([
        "x86_64-w64-mingw32-gcc", "-std=c11", "-O2", "-Wall", "-Wextra", "-Werror",
        "-municode", "-mwindows", str(HERE / "windows/ProtogenInstaller.c"),
        str(work / "InstallerResources.o"), "-o", str(out / EXE),
        "-lcomctl32", "-lshell32", "-lole32", "-lgdi32",
    ], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("base-game", "dlc-game", "base-bundle", "dlc-bundle", "steam-manifest",
                 "font-source", "sdk", "output"):
        parser.add_argument(f"--{name}", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    require(not output.exists() and not output.with_suffix(".zip").exists(), "Use a fresh output name")
    output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=output.parent, prefix=".building-") as tmp:
        work = Path(tmp)
        app = work / output.name
        resources = app / "Resources"
        payload = resources / "LocalizationPayload"
        payload.mkdir(parents=True)
        base = json.loads((args.base_bundle / "inventory.json").read_text())
        editions = [
            edition_payload(name, root, bundle, base, args.steam_manifest, args.font_source, payload)
            for name, root, bundle in (("base", args.base_game, args.base_bundle),
                                       ("dlc", args.dlc_game, args.dlc_bundle))
        ]
        runtime = runtime_payload(args.sdk, payload)
        write_json(resources / "PackageConfig.json", {
            "schemaVersion": 1, "packageID": "fun.vnrevival.protogen", "version": VERSION,
            "steamAppID": APP_ID, "steamBuildID": BUILD_ID, "runtimeVersion": "8.2.3.24061702",
            "languages": LOCALES, "editions": editions, "runtime": runtime,
        })
        compile_window(args.base_game, app, work)
        copy2(HERE / "windows/install.ps1", app)
        copy2(HERE / "PLAYER-GUIDE.txt", app / "Read me.txt")
        archive = Path(make_archive(str(work / output.name), "zip", app.parent, app.name))
        require(archive.stat().st_size <= 100_000_000, "Installer ZIP exceeds 100 MB")
        archive.rename(output.with_suffix(".zip"))
        app.rename(output)
    checksum = output.with_suffix(".sha256")
    checksum.write_text(f"{digest(output.with_suffix('.zip'))}  {output.with_suffix('.zip').name}\n")
    print(f"{output.with_suffix('.zip')}: {output.with_suffix('.zip').stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
