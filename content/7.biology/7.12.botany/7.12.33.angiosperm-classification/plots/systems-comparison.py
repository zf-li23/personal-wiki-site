# The same 26 families in three systems, each column in the linear sequence of its system: Engler
# (Syllabus, 12th ed., 1964), Cronquist (1981) and APG IV (2016). Brackets give the major groups of each
# system; lines join the same family and are coloured by its APG IV clade. The positions in the first two
# columns are the family numbers of the published family lists of the two systems.
import wikibio as bio

P = bio.P
CLADE_TOKEN = {"ANA": "neutral", "Magnoliids": "petal", "Monocots": "rna", "Early eudicots": "atp",
               "Superrosids": "plant", "Superasterids": "dna"}
# family: (Engler 1964 number, Cronquist 1981 number, APG IV order index (1-64), APG IV clade)
FAM = {
    "Casuarinaceae": (1, 63, 29, "Superrosids"), "Fagaceae": (9, 61, 28, "Superrosids"),
    "Moraceae": (13, 53, 26, "Superrosids"), "Salicaceae": (7, 131, 24.5, "Superrosids"),
    "Caryophyllaceae": (34, 75, 45, "Superasterids"), "Magnoliaceae": (40, 6, 6, "Magnoliids"),
    "Piperaceae": (70, 21, 5, "Magnoliids"), "Lauraceae": (56, 17, 7, "Magnoliids"),
    "Nymphaeaceae": (67, 26, 2, "ANA"), "Ranunculaceae": (62, 30, 21, "Early eudicots"),
    "Brassicaceae": (97, 134, 37, "Superrosids"), "Platanaceae": (102, 44, 22, "Early eudicots"),
    "Hamamelidaceae": (103, 45, 23, "Superrosids"), "Rosaceae": (115, 174, 26.5, "Superrosids"),
    "Fabaceae": (119, 182, 25, "Superrosids"), "Euphorbiaceae": (130, 232, 24, "Superrosids"),
    "Malvaceae": (173, 102, 36, "Superrosids"), "Cucurbitaceae": (203, 127, 27, "Superrosids"),
    "Apiaceae": (227, 269, 64, "Superasterids"), "Ericaceae": (231, 144, 47, "Superasterids"),
    "Oleaceae": (245, 293, 55, "Superasterids"), "Lamiaceae": (261, 287, 55.5, "Superasterids"),
    "Asteraceae": (291, 318, 59, "Superasterids"), "Liliaceae": (302, 369, 13, "Monocots"),
    "Orchidaceae": (344, 383, 14, "Monocots"), "Poaceae": (330, 352, 18, "Monocots"),
}
COLS = [("Engler (1964)", 3.2, 0), ("Cronquist (1981)", 12.6, 1), ("APG IV (2016)", 22.0, 2)]
GROUPS = [  # column, label, first rank, last rank
    (0, "Archichlamydeae", 0, 18), (0, "Metachlamydeae", 19, 22), (0, "Monocotyledoneae", 23, 25),
    (1, "Magnoliidae", 0, 4), (1, "Hamamelidae", 5, 9), (1, "Caryo.", 10, 10),
    (1, "Dilleniidae", 11, 15), (1, "Rosidae", 16, 19), (1, "Asteridae", 20, 22), (1, "Liliopsida", 23, 25),
    (2, "ANA grade", 0, 0), (2, "Magnoliids", 1, 3), (2, "Monocots", 4, 6), (2, "Early eudicots", 7, 8),
    (2, "Superrosids", 9, 19), (2, "Superasterids", 20, 25),
]
TOP, STEP = 26.8, 0.98
fig, ax = bio.canvas(27, 28.6)
pos = []
for title, x, k in COLS:
    order = sorted(FAM, key=lambda f: FAM[f][k])
    pos.append({f: (x, TOP - i * STEP) for i, f in enumerate(order)})
    bio.label(ax, (x, TOP + 1.1), title, size="title")
for f, (e, c, a, clade) in FAM.items():
    tok = CLADE_TOKEN[clade]
    for k in range(2):
        (x0, y0), (x1, y1) = pos[k][f], pos[k + 1][f]
        ax.plot([x0 + 2.1, x1 - 2.1], [y0, y1], color=P.edge(tok), lw=1.4, alpha=0.85, zorder=3)
for k, (title, x, _) in enumerate(COLS):
    for f, (xx, y) in pos[k].items():
        tok = CLADE_TOKEN[FAM[f][3]]
        bio.box(ax, (xx, y), 4.0, 0.72, token=tok, text=f, size="small")
for col, text, a, b in GROUPS:
    x = COLS[col][1] - 2.35 if col < 2 else COLS[col][1] + 2.35
    y0, y1 = TOP - a * STEP + 0.36, TOP - b * STEP - 0.36
    side = -1 if col < 2 else 1
    ax.plot([x, x + side * 0.18, x + side * 0.18, x], [y0, y0, y1, y1], color=P.muted(), lw=0.9, zorder=4)
    bio.label(ax, (x + side * 0.32, (y0 + y1) / 2), text, size="tiny", rotation=90, color=P.muted(), zorder=6)
for i, (clade, tok) in enumerate(CLADE_TOKEN.items()):
    x = 2.0 + i * 4.2
    ax.plot([x, x + 0.9], [0.6, 0.6], color=P.edge(tok), lw=2.2)
    bio.label(ax, (x + 1.05, 0.6), clade, size="small", ha="left")
