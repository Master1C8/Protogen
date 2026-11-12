screen vnrevival_language_picker():
    vbox:
        style_prefix "radio"
        label _("Language")
        textbutton "English" id "vnrevival_language_english" action Language(None)
        if "russian" in renpy.known_languages():
            textbutton "Русский" id "vnrevival_language_russian" action Language("russian")
