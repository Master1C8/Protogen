# Temporary CrossOver QA script. Keep this outside the installed player payload.
python early hide:
    import os
    import renpy

    def vnrevival_isolated_save_init(engine=renpy, paths=os.path,
                                    original_init=renpy.savelocation.init):
        module = engine.savelocation
        scratch = engine.game.args.savedir
        if not scratch or not paths.isabs(scratch) or not paths.isfile(paths.join(scratch, ".vnrevival-qa")):
            raise RuntimeError("CrossOver QA requires a marked scratch --savedir.")

        original_location = module.FileLocation
        game_mirror = paths.normcase(paths.abspath(paths.join(engine.config.gamedir, "saves")))
        if paths.normcase(paths.abspath(scratch)) == game_mirror:
            raise RuntimeError("CrossOver QA scratch directory matches the player save mirror.")
        scratch_mirror = paths.join(scratch, "game-local-mirror")

        class IsolatedFileLocation(original_location):
            def __init__(self, directory):
                if paths.normcase(paths.abspath(directory)) == game_mirror:
                    directory = scratch_mirror
                super().__init__(directory)

        module.FileLocation = IsolatedFileLocation
        try:
            original_init()
        finally:
            module.FileLocation = original_location

        locations = {paths.normcase(paths.abspath(location.directory))
                     for location in engine.loadsave.location.active_locations()}
        expected = {paths.normcase(paths.abspath(path)) for path in (scratch, scratch_mirror)}
        if locations != expected:
            raise RuntimeError("CrossOver QA save locations do not match the scratch directory.")

    renpy.savelocation.init = vnrevival_isolated_save_init
