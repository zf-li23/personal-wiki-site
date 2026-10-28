"""Reciprocal crosses distinguish four modes of inheritance of a recessive mutant trait.
Rows: autosomal recessive, X-linked recessive, organellar (maternal inheritance), maternal effect (recessive).
Columns: F1 of mutant female x wild-type male, F1 of the reciprocal cross, and F2 from intercrossing the F1 of
the first cross. Each cell shows four daughters (circles) and four sons (squares); filled symbols have the mutant
phenotype, in the expected proportions."""

import wikibio as bio
from wikibio import genetics as G

P = bio.P

rows = [
    ("Autosomal recessive", [(0, 0), (0, 0), (1, 1)], "F1 identical;\nF2 1/4 mutant in both sexes"),
    ("X-linked recessive", [(0, 4), (0, 0), (2, 2)], "F1 differ by sex\n(criss-cross inheritance)"),
    ("Organellar (maternal)", [(4, 4), (0, 0), (4, 4)], "progeny always resemble\nthe mother"),
    ("Maternal effect", [(4, 4), (0, 0), (0, 0)], "phenotype = mother's genotype;\nF3: 1/4 of broods mutant"),
]
cols = ["mutant female x wild-type male\nF1", "wild-type female x mutant male\nF1", "F1 x F1 (first cross)\nF2"]

fig, ax = bio.canvas(18.0, 9.6)
x0, dxc = 5.2, 4.3
for j, c in enumerate(cols):
    bio.label(ax, (x0 + j * dxc + 0.9, 9.0), c, size="small", bold=False)
ytop = 7.6
for i, (name, cells, note) in enumerate(rows):
    y = ytop - i * 2.0
    bio.label(ax, (0.2, y + 0.3), name, size="normal", ha="left")
    bio.label(ax, (0.2, y - 0.35), note, size="tiny", ha="left", va="center", color=P.muted())
    for j, (fm, mm) in enumerate(cells):
        cx = x0 + j * dxc
        for k in range(4):
            G.symbol(ax, (cx + k * 0.6, y + 0.32), sex="F", status="affected" if k < fm else "unaffected",
                     size=0.22, token="negative")
            G.symbol(ax, (cx + k * 0.6, y - 0.32), sex="M", status="affected" if k < mm else "unaffected",
                     size=0.22, token="negative")
    if i < len(rows) - 1:
        ax.plot([0.2, 17.8], [y - 1.0, y - 1.0], color=P.muted(), lw=0.4)
G.symbol(ax, (0.5, 0.3), sex="F", status="affected", size=0.2, token="negative")
G.symbol(ax, (1.0, 0.3), sex="M", status="affected", size=0.2, token="negative")
bio.label(ax, (1.4, 0.3), "mutant phenotype", size="tiny", ha="left")
G.symbol(ax, (4.0, 0.3), sex="F", size=0.2)
G.symbol(ax, (4.5, 0.3), sex="M", size=0.2)
bio.label(ax, (4.9, 0.3), "wild-type phenotype", size="tiny", ha="left")
