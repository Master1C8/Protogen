init python in vnrevival_picker:
    import renpy
    from renpy.text import font
    from renpy.text.text import ON, log2vis

    def label_text(name, rtl):
        # The current locale controls Ren'Py's bidi pass for the whole screen.
        if rtl and not renpy.config.rtl:
            return log2vis(name, ON)[0]
        return name

    def text_properties(shape):
        if shape and getattr(font, "hbfont", None) is not None:
            return {"text_shaper": "harfbuzz"}
        return {}


screen vnrevival_language_picker():
    vbox:
        style_prefix "radio"
        xsize None
        label _("Language")
        hbox:
            xfill True
            box_wrap True
            spacing 24
            textbutton "English":
                id "vnrevival_language_english"
                action Language(None)
                text_font "DejaVuSans.ttf"
            for runtime, name, face, rtl, shape in vnrevival_picker_languages:
                if runtime in renpy.known_languages():
                    textbutton vnrevival_picker.label_text(name, rtl):
                        id ("vnrevival_language_" + runtime)
                        action Language(runtime)
                        text_font face
                        properties vnrevival_picker.text_properties(shape)
