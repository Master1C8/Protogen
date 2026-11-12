# The shipped start label assigns the fallback at game/script.rpy:85.
init offset = 10

init python:
    j.name = "[gname!t]"

    def vnrevival_translate_default_player_name():
        if renpy.get_filename_line() == ("game/script.rpy", 85) and pname == "You":
            renpy.store.pname = renpy.translate_string("You")

    config.python_callbacks.append(vnrevival_translate_default_player_name)
