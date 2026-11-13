# My Furry Protogen localization installer

The Windows x64 installer adapts the native Win32 window, worker, folder picker,
status and retry flow, and PowerShell installation transaction from [The Murder
of Sonic the Hedgehog localization](https://github.com/Master1C8/the-murder-of-sonic-the-hedgehog-localization/tree/d9213cfbc4b650f73be80e46c54a340f26fd941a)
at `d9213cfbc4b650f73be80e46c54a340f26fd941a`. The original project is read-only
for this adaptation. The portrait, background and icon are from the verified
Protogen Steam build and their hashes are pinned by the builder.

- Steam app `2009010`, Windows build `11915262`. The exact compiled and source
  script identities distinguish the base game from the official DLC.
- Both editions contain all 30 localizations. Each installs as a complete set.
  The game handles language selection and persistence in Preferences → Language.
- The package adds a separate Windows Ren’Py 8.2.3 runtime for HarfBuzz.
  Its init-code watchdog gets a fresh deadline after script compilation.
  **Launch game** uses that runtime against the registered Steam installation.
  Steam Play continues to use the original 8.0.3 engine. The installer verifies the original executable
  and game scripts against both edition receipts.
- The installer verifies payload hashes, stages changes and keeps the rollback
  journal and per-installation receipt in local application data. It upgrades
  files listed in its receipt and adopts byte-identical packages. An unrecognized
  same-name file stops installation. Recognized bytecode is retired when its
  source changes. The installer leaves saves, official files and other mods alone.

See [the player guide](PLAYER-GUIDE.txt) for use and runtime notices.

## Build

Use Python 3.9+, ImageMagick and the x64 MinGW GCC and windres tools. The
command needs both verified Steam game editions, both pinned text exports,
the Steam manifest, the pinned fonts and the exact Ren’Py 8.2.3 SDK tarball.
The archive hash and the game-art inputs are checked before packaging. This
example uses the existing isolated input copies in this checkout.

```sh
qa=text-assets/edition-qa.0bfO9x
python3 -B installer/build_windows.py \
  --base-game "$qa/run-sfw" --dlc-game "$qa/run-nsfw" \
  --base-bundle text-assets --dlc-bundle "$qa/nsfw-export" \
  --steam-manifest "$qa/appmanifest_2009010.acf" \
  --font-source text-assets/font-candidates.vUrRKa \
  --sdk text-assets/harfbuzz-isolated/renpy-8.2.3-sdk.tar.bz2 \
  --output dist/Protogen-Localization-Installer-Windows-x64
```

Use `test_install.ps1` with the extracted package, both game input folders,
and a fresh work directory. The test constructs a disposable Steam library,
checks every installed hash, and tests the edition switch, repeated install,
checksum rejection, foreign-file collision and recovery from a partial update.
