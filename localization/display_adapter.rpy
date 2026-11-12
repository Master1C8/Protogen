# Both supported scripts use the same fallback assignment at different lines.
init offset = 10

init python:
    j.name = "[gname!t]"

    def vnrevival_translate_default_player_name():
        if renpy.get_filename_line() in (("game/script.rpy", 85), ("game/script.rpy", 81)) and pname == "You":
            renpy.store.pname = renpy.translate_string("You")

    config.python_callbacks.append(vnrevival_translate_default_player_name)
