# German semantic audit in progress

Input versions: `dialogue.tsv` and `strings.json`, and their NSFW counterparts, hashed in STATUS.md. The full self pass is complete on the retained pre-correction inputs; this is not an independent acceptance receipt. First SFW story source-order rows 0–1784 (1,785 IDs) were read against the German text in context. UI source-key insertion-order rows 0–393 (394 keys) were also read. DLC delta source-order rows 0–254 (255 IDs, including aliases) and the Gallery UI key were read. Do not infer a full pass from drafting or machine checks.

## Findings applied in correction cycle 01

- `start_70f799c6`: English promises the best birthday outfit; the current German drops “best”. Proposed full text: `Er hat versprochen, dir das beste Geburtstagsgewand kostenlos zu nähen – als Geschenk. {w}Kannst du das glauben?` Preserve the wait tag. This ID is shared by both editions.
- `start_2fcee7f5`: “Feuer des Lagerfeuers” is awkward repetition. Proposed full text: `Da waren die Flammen des Lagerfeuers, an dem die feierliche Geburtstagsfeier aller an diesem Tag geborenen Dorfkinder stattfand.`

- `start_b0929960`: “vielstimmig” does not explicitly preserve the unsynchronized cheering. Proposed full text: `Die Menge – das ganze Dorf, das an Tischen um das Lagerfeuer saß – antwortete mit einem nicht ganz gleichzeitigen „Hurra“.`

- `start_fe91027e`: Pixie is speaking aboard the smaller shuttle, while `Schiff` denotes the larger craft in this later scene. Proposed full text: `Juno, ich muss dich warnen, an Bord des Shuttles befindet sich ein unbekanntes Virus.` Review the nearby ship/shuttle referent closure.

- `start_d1fc5d10`: the draft omits that he falls to his knees. Proposed full text: `Nachdem ich diese Worte gesagt hatte, stürmte ich aus dem Haus. Und sobald ich draußen war, fiel ich direkt auf dem schmutzigen, regennassen Boden auf die Knie und schrie aus voller Kehle.`

- `start_d2bb11c4`: the DLC strengthens the expletive compared with SFW; the draft weakens it to “Hölle”. Proposed full text: `Was zum Fick ist das?! Himmelsmutter!`
- `start_680f0a01`: “ein Ausatmen” is unidiomatic for involuntary exhalation. Proposed full text: `Ich konnte mir ein Keuchen nicht verkneifen:`

- `start_e80cad76`: the preceding line concerns his impending orgasm; masculine `ihn` introduces a specific referent absent from “it”. Proposed full text: `Ja, [pname], bitte, ich will es sehen ...`
- `start_587ea9bf`: “glänzte” omits that her skin is sweating. Proposed full text: `Ihre Haut war vor Erregung schweißbedeckt, Juno presste unmerklich die Hüften zusammen, ihre Knie zitterten leicht.`

- `start_5d08a2a6`: “ihre Berührung” shifts who touches whom; English says the narrator touches her. Proposed full text: `Mein Schwanz war schon allein davon hart, sie zu berühren und zu wissen, dass sie bei mir war, und mehr brauchte ich gerade nicht.`
- `start_5425eab6`: the source says the sensation forces the narrator to arch; the draft transfers that action to Juno. Proposed full text: `Sie zitterte bei dem Gefühl, wie mein Schwanz in ihr glitt und an empfindlichen Stellen rieb, während ich mich unwillkürlich krümmte.` Preserve this source anomaly and check scene context.

- `start_b767eb8b`: the source says the narrator tries to retain composure, but the German attributes that effort to Juno. Proposed full text: `Ich bewegte mich immer schneller, und obwohl ich versuchte, meine Fassung zu bewahren, kam Juno meinen Stößen entgegen, umhüllte mich mit der Hitze ihres Körpers und stöhnte laut, süß und aufrichtig.`

These 12 corrections were preflighted together and applied. The candidate and final text coverage/token checks passed, and the exact changed entries and untouched entries were compared. The original dependency selection was reconciled in `review-cycle-01/reconciled-v3/`: all newly selected context IDs were reviewed by the author against English, and the evidence reproduced byte for byte. `semantic-coverage.json` records exact self-audited authored ID sets; `review-cycle-01/reconciliation-receipt.json` binds this reconciliation. Independent review is not authorized in this session and remains pending.
