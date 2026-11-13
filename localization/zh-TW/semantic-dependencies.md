# zh-TW author review dependency closure

2026-11-13; Python 3.9.6. Paths are relative to the canonical checkout unless absolute. SHA-256 binds the author audit and strict text validation; prior coordinator-verified glossary layer hashes are retained in STATUS.md. This is not independent review, reinsertion, or runtime evidence.

```
1ad9c080caed30f47584a2a4062a1ab9ab665eba5bf7e8c35736c5ccfc05c0a8  text-assets/manifest.json
8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff  text-assets/inventory.json
f50583a62ea41e826c4668f8595592c60605ca0a3f48e2415a1f695846cd2afd  text-assets/preserve-exactly.json
5d3950c98e01d34a49bca5ef8862c5ab5dcec2558c42f709748c68e5134af923  text-assets/special-scenes.json
da9a7f72df14f7b725d7566ae0f1cac40f7390042d74b410c9aaf05a48063b6f  text-assets/edition-qa.0bfO9x/nsfw-export/manifest.json
b0feab1e5d5dfa697bbeee0a98a8dc310edd30ce6acc908aee8e776b5f0aa2ea  text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json
36446dab69a956c65997d173f6d088c617514e4afbafb5158f7d66772a406c22  text-assets/edition-qa.0bfO9x/nsfw-export/preserve-exactly.json
2412020e4c4024a82dad7535976a6e1ff8239fec1214c4ac7c211492a75c6f8b  text-assets/edition-qa.0bfO9x/nsfw-export/special-scenes.json
6b020423fc1c45e678c6c8ef6914161ed2978864f91c805d3c0d286c084b8f7c  localization/nsfw-story-aliases.json
18937f78194ea7503bf14c316b7db3789013ea9accd6e455eadfe2fd3f909d5d  tools/build_localization.py
db7ae33202a62d85f882e142e11bc60de8332c896e8b1077a1781ab43c5ce691  tools/extract_text.py
c567eec2abd882dad7e72193cb4619444096469f25a741409873c24846d16428  tools/install_language_picker.py
7086b09dd333fca216ede2db1fdefdc6de238b53014fef1ea1ffdc50b9e1b0a4  localization/zh-TW/dialogue.tsv
98fa66572c548fc6d4575a326e4123f86497847c7d93f2b50ff7ca4ff1c213c0  localization/zh-TW/strings.json
283efe7630ea848f1286f6bd47c78ac33f8233e73ece47c6f0085fd20f281f89  localization/zh-TW/nsfw/dialogue.tsv
d5dcd82847b73e68de082d9e112e6842a370742964571d7c008fbd706b0d07e0  localization/zh-TW/nsfw/strings.json
7339bb596100d2ae20b08d39576c54fae1f32e70d6b3f5b667bf9075e7741435  localization/zh-TW/special-scenes.md
2f1782e645cd8836cd1855d252592161d90a7159e4c27bdb8fc61d1661deac79  localization/zh-TW/semantic-coverage.json
3dbe7424e1eb48afc8fba71cef8412629f3894f85f9f525d9a67f8f3a7dc2619  localization/zh-TW/semantic-findings-034.json
5935841fb335bb53db74afe2134e70c45068ee8dbea7cf6a87f287aef794cddd  text-assets/multilingual-probe.L4KEcD/glossary-receipts.json
611e6dec103d1857ec8ed5ce8dc10470312c5ef6d981e1ef307474b44f85d926  /Users/antonkrutov/Desktop/SiteForMods/data/games/my-furry-protogen/glossary.json
126976849427c1a5de635d0cc6a7a378da6e315084cc5626b56fa7879e3a7ca2  /Users/antonkrutov/Desktop/SiteForMods/data/games/my-furry-protogen/glossary-translations.json
b952b5d3461a6d9a4103a0c947da28c7afc6860a9648c21a870274f7e923c59b  /Users/antonkrutov/Desktop/SiteForMods/data/games/my-furry-protogen/glossary-review.md
```

Reproduce strict text validation from the checkout:

```sh
PYTHONPATH=tools python3 -B - <<'PY'
import json
from pathlib import Path
from build_localization import edition_text
base = json.loads(Path("text-assets/inventory.json").read_text())
dlc = json.loads(Path("text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json").read_text())
edition_text(base, dlc, Path("localization/zh-TW"), False)
PY
```

The authored ID coverage sets were checked for uniqueness and exact equality with the four authored files. Protected source subsets were checked against each inventory (747 base, 744 DLC); no generated artifact was compared. The full English comparison records author review only; contextual timing and independent review remain pending.
