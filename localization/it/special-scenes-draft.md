# Italian special-scene text decisions

Both edition registries were checked in turn 034. The source-to-target self-review covers the registered story occurrences; an additional exact bracket/brace-token comparison passed for player-name occurrences (79 base, 90 DLC) and dialogue-timing occurrences (47 base, 42 DLC). Runtime checks remain assigned to the coordinator.

- Player name: `My name is...` → `Mi chiamo...`; fallback `You` → `Tu`. Keep `[pname]`, the 12-character cap, stripping, empty comparison and nameplate binding. Check accented custom names and blank and whitespace-only entries in both editions.
- Juno nameplate: retain `[gname]`, `Juno`, assignment and speaker binding; check the first and later nameplates.
- Saves: `Page {}` → `Pagina {}`, `Automatic saves` → `Salvataggi automatici`, `Quick saves` → `Salvataggi rapidi`, `empty slot` → `slot vuoto`; preserve `{#file_time}%A, %B %d %Y, %H:%M`. Check actual locale display and occupied and empty slots on all page types.
- Timing: retain every wait and paired speed tag; check an actual pause and final slow ellipsis in the renderer.
- Main-menu title: retain original brand artwork; verify the complete logo and navigation.
- Cutscenes: preserve movie paths. The registry binds `watches.webm` to SHA-256 `f20f2e584d6739728c11024f41184103bf3414d02734d24ea72628cf7b37112c` and `watchesLong.webm` to `e0de56e28795bba9e415b40fe3c25df07dd9af8fd2a30b9d6ac907d5a41d3eeb`. Earlier project evidence reports no captions; visual verification of both videos and return to the next line remains with the coordinator.

These static decisions do not establish runtime or visual acceptance.
