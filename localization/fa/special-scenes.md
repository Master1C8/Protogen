# Persian special-scene decisions

2026-11-13. Base registry SHA-256 `5d3950c98e01d34a49bca5ef8862c5ab5dcec2558c42f709748c68e5134af923`; DLC registry `2412020e4c4024a82dad7535976a6e1ff8239fec1214c4ac7c211492a75c6f8b`; Persian glossary layer `a4792595c0b4d64605638f3be597adec311c29b0960c9befa4c0b954ba45b3a8`. Author reviewed the 47 base timed rows against English and neighboring dialogue; actual wording is in dialogue.tsv. Full semantic and independent review remain pending.

- Player name: `My name is...` → `اسم من...`; `You` → `تو`. Preserve `pname`, `[pname]`, strip, 12-character cap and empty comparison. A custom name remains unchanged; blank selects fallback. Input and interpolation unverified.
- Juno: display `جونو`; preserve `gname`, `[gname]` and speaker ID `j`, with a locale display adapter separate from the identity. First and later nameplates require runtime checks.
- Save pages: `Page {}` → `صفحهٔ {}`; `Automatic saves` → `ذخیره‌های خودکار`; `Quick saves` → `ذخیره‌های سریع`; `empty slot` → `جای خالی`; `Load` → `بارگذاری`. Preserve `{}`, `<`, `>`, and `{#file_time}%A, %B %d %Y, %H:%M` exactly. Check occupied and empty slots and page variants later.
- Timing: preserve each `{w}` at its corresponding pause and `{cps=5}...{/cps}` exactly; the 47 source-bound target lines are in dialogue.tsv. DLC `start_7b64e49d` aliases base `start_f66bb6fe`; use the existing alias, no second copy. `Pixie` is the proper name `پیکسی`, not a generic noun. Recheck pacing and neighboring full scenes in semantic audit.
- Logo: preserve original `My Furry protogen` brand artwork and resource path. Watch cutscenes: retain both movie paths and playback/return bindings; project evidence records both videos without captions. Playback and display are unverified.

The decisions are author-reviewed, not independently reviewed. The registered source inventory excludes full literary review and remaining visual/audio discovery; reconcile any newly discovered case. Persian joining, ZWNJ, bidi, input, layout and runtime behavior remain unverified pending the joint pass.
