# The builder supplies the locale and its font settings in each package.
init 20 python in vnrevival_fonts:
    import renpy
    from renpy.text.font import FontGroup

    nunito = ("fonts/Nunito-SemiBold.ttf", "fonts/Nunito-Bold.ttf")
    regular = "DejaVuSans.ttf"
    bold = "DejaVuSans-Bold.ttf"
    symbols = (0x2714, 0x2718, 0x2b06, 0x2b07)
    original_rtl = renpy.config.rtl
    locales = {}

    def register(locale, face, script_range, rtl, shape, line_break):
        locales[locale] = (face, script_range, rtl, shape, line_break)

    def apply():
        locale = renpy.game.preferences.language
        face, script_range, rtl, shape, line_break = locales.get(
            locale, (None, None, False, False, None))
        renpy.config.rtl = original_rtl or rtl
        harfbuzz = getattr(renpy.text.font, "hbfont", None) is not None
        groups = {}
        for index, name in enumerate(nunito):
            fallback = (regular, bold)[index]
            group = FontGroup()
            for cp in symbols:
                group.add(fallback, cp, cp)
            if script_range:
                group.add(face, *script_range)
                group.add(fallback, None, None)
            else:
                target = fallback if face == regular else face
                group.add(target or name, None, None)
            groups[name] = group

        # Explicit game fonts are set on several unrelated UI style trees.
        # Add fresh property dictionaries so Ren'Py's language restore can
        # restore every original style before it calls us again.
        for style in renpy.style.styles.values():
            overrides = {}
            for properties in style.properties:
                for key, value in properties.items():
                    if key == "font" or key.endswith("_font"):
                        if isinstance(value, str) and value in groups:
                            overrides[key] = groups[value]
            if overrides:
                for key, value in overrides.items():
                    setattr(style, key, value)
        if line_break:
            renpy.store.style.default.language = line_break
        if rtl:
            renpy.store.style.say_dialogue.text_align = 1.0
        if shape and harfbuzz:
            renpy.store.style.default.shaper = "harfbuzz"

    renpy.config.change_language_callbacks.append(apply)

# Empty load slots are disabled, but their labels still need readable contrast.
style slot_time_text:
    size 24
    insensitive_color "#d0c8de"
    idle_color "#d0c8de"

style slot_name_text:
    size 24
    insensitive_color "#d0c8de"
    idle_color "#d0c8de"
