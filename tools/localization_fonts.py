"""Stage licensed fonts and bind rendering options to each Ren'Py locale."""

from hashlib import sha256
import json
from pathlib import Path
import shutil


FONT_PATH = Path("game/fonts/vnrevival")
ADAPTER_PATH = Path("game/vnrevival_protogen_fonts.rpy")
DEJAVU = "DejaVuSans.ttf"
FONT_LOCALES = {
    "ar": (DEJAVU, None, True, True, None),
    "el": (DEJAVU, None, False, False, None),
    "fa": (DEJAVU, None, True, True, None),
    "he": (DEJAVU, None, True, False, None),
    "hi": ("NotoSansDevanagari-Regular.ttf", (0x0900, 0x097f), False, True, None),
    "ja": ("NotoSansJP-Regular.otf", None, False, False, "japanese-normal"),
    "ko": ("NotoSansKR-Regular.otf", None, False, False, "korean-with-spaces"),
    "th": ("NotoSansThai-Regular.ttf", (0x0e00, 0x0e7f), False, True, None),
    "zh": ("NotoSansSC-Regular.otf", None, False, False, "eastasian"),
    "zh-TW": ("NotoSansTC-Regular.otf", None, False, False, "eastasian"),
}

# Runtime IDs for the 22 locales that previously used disposable QA IDs.
ADDITIONAL_LOCALES = {
    "ar": "arabic",
    "bg": "bulgarian",
    "el": "greek",
    "es-419": "spanish_latam",
    "fa": "persian",
    "fil": "filipino",
    "he": "hebrew",
    "hi": "hindi",
    "hu": "hungarian",
    "id": "indonesian",
    "ja": "japanese",
    "ko": "korean",
    "nl": "dutch",
    "ro": "romanian",
    "sr": "serbian",
    "sw": "swahili",
    "th": "thai",
    "tr": "turkish",
    "uk": "ukrainian",
    "vi": "vietnamese",
    "zh": "chinese_simplified",
    "zh-TW": "chinese_traditional",
}


def font_inputs(project, locale, source):
    """Read and verify the exact licensed assets before output is created."""
    if locale not in FONT_LOCALES:
        return {}
    receipt = json.loads((project / "localization/font-sources.json").read_text())
    candidate = receipt["candidates"].get(locale)
    if candidate is None:
        return {}
    if source is None:
        source = project / "text-assets/font-candidates.vUrRKa"
    files = {}
    for name, digest in (("file", "sha256"), ("license", "licenseSha256")):
        path = source / candidate[name]
        if not path.is_file():
            raise ValueError(f"Missing pinned font resource: {path}")
        if sha256(path.read_bytes()).hexdigest() != candidate[digest]:
            raise ValueError(f"Pinned font resource checksum differs: {path}")
        files[FONT_PATH / path.name] = path
    return files


def stage_fonts(project, output, locale, runtime_locale, locale_dir, files):
    for relative, source in files.items():
        path = output / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, path)

    (output / ADAPTER_PATH).write_bytes((project / "localization/font_adapter.rpy").read_bytes())
    if locale in FONT_LOCALES:
        face, script_range, rtl, shape, line_break = FONT_LOCALES[locale]
        if face != DEJAVU:
            face = (FONT_PATH.relative_to("game") / face).as_posix()
        arguments = (runtime_locale, face, script_range, rtl, shape, line_break)
        registration = "init 21 python:\n    vnrevival_fonts.register{!r}\n".format(arguments)
        (locale_dir / "vnrevival_protogen_rendering.rpy").write_text(registration, encoding="utf-8")
