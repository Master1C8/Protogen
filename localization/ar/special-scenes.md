# Arabic special-scene decisions

Reviewed against both registries: base SHA-256 `5d3950c98e01d34a49bca5ef8862c5ab5dcec2558c42f709748c68e5134af923`; DLC `2412020e4c4024a82dad7535976a6e1ff8239fec1214c4ac7c211492a75c6f8b`. Use logical Unicode; do not visually reverse text. These decisions settle text and bindings, not runtime acceptance.

- Player name: `My name is...` → `اسمي...`; fallback `You` → `أنت`. Preserve `[pname]`, input limit, stripping, empty comparison and nameplate binding. Do not inflect the entered name. Player is male; use masculine agreement. Check blank and custom names, including mixed-direction names, in the later joint pass.
- Juno: display `جونو`, preserve `[gname]`, assignment and speaker ID `j`; do not alter control values. She is female. Verify first and subsequent nameplates at runtime.
- Save formats: `Page {}` → `الصفحة {}`, `Automatic saves` → `الحفظ التلقائي`, `Quick saves` → `الحفظ السريع`, `empty slot` → `خانة فارغة`. Retain `{#file_time}%A, %B %d %Y, %H:%M` exactly. Preserve format fields and directives; inspect date order, direction and occupied/empty slots in the joint pass.
- Dialogue timing: retain each `{w}` at its intended dramatic break and preserve the exact paired speed tags and ellipsis. Translate each passage in its scene context, including edition-specific variants. Mechanical tag checks do not verify timed behavior.
- Main-menu logo: retain the original `My Furry protogen` brand artwork, with no image text substitution. Verify its display and navigation later.
- Watch cutscenes: retain movie paths; previously reviewed videos contain no captions. Verify return to the next line during runtime QA.

The existing substitution and tag bindings are the intended adapters; the isolated HarfBuzz test demonstrates a shaping path, not the final package. Preserve `Pixie` as the proper name `بيكسي` in display text and retain technical identifiers. Use shared IDs and the existing DLC aliases without authoring duplicate aliases. Editable input, bidi layout, fonts, both editions and CrossOver remain pending coordinator verification.
