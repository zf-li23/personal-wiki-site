"""Four generations of lineage-tracing methods.

A, dye injection: a lineage tracer (fluorescent dextran or DiI) injected into one blastomere is inherited by
all its descendants, which form a labelled clone in the later embryo. B, interspecies chimera: a piece of
quail embryo grafted into a chick embryo; quail cells are recognized later by their condensed nucleolar
heterochromatin or by a quail-specific antibody (QCPN). C, genetic labelling with Cre-loxP: a cell-type
specific promoter drives CreER, which enters the nucleus only after tamoxifen; Cre excises the loxP-flanked
stop cassette in a reporter at the Rosa26 locus, and the cell and all its descendants then express the
fluorescent reporter permanently. D, CRISPR barcodes: Cas9 edits an array of target sites; edits accumulate
irreversibly over successive divisions, and the shared edits of the cells, read by sequencing, reconstruct
their lineage tree.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle

import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(30, 13.4)

# ------------------------------------------------------------------- A dye
bio.panel(ax, "A", (0.2, 13.2))
bio.label(ax, (3.8, 12.7), "Injected lineage tracer", size="small", bold=True)
c = (1.7, 9.8)
for k, (dx, dy) in enumerate([(-0.45, 0.45), (0.45, 0.45), (-0.45, -0.45), (0.45, -0.45)]):
    tok = "highlight" if k == 1 else "cytoplasm"
    ax.add_patch(Circle((c[0] + dx, c[1] + dy), 0.44, facecolor=P.fill(tok), edgecolor=P.edge("membrane"), lw=1.0, zorder=5))
ax.plot([c[0] + 1.6, c[0] + 0.6], [c[1] + 1.4, c[1] + 0.55], color=P.edge("neutral"), lw=2.0, zorder=6)
bio.label(ax, (c[0] + 1.75, c[1] + 1.55), "micropipette", size="tiny", ha="left")
bio.arrow(ax, (3.1, 9.8), (4.2, 9.8), kind="process")
e = (6.0, 9.8)
ax.add_patch(Ellipse(e, 3.0, 1.9, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.0, zorder=5))
rng = np.random.default_rng(2)
for _ in range(60):
    p = (e[0] + rng.uniform(-1.3, 1.3), e[1] + rng.uniform(-0.75, 0.75))
    if ((p[0] - e[0]) / 1.4) ** 2 + ((p[1] - e[1]) / 0.85) ** 2 > 1:
        continue
    tok = "highlight" if (p[0] > e[0] and p[1] > e[1] - 0.2) else "cytoplasm"
    ax.add_patch(Circle(p, 0.09, facecolor=P.fill(tok), edgecolor=P.edge(tok if tok == "highlight" else "membrane"), lw=0.5,
                        zorder=6))
bio.label(ax, (6.0, 8.3), "labelled clone", size="tiny", color=P.muted())
bio.label(ax, (3.8, 7.3), "dilutes with division; needs\naccessible, large cells", size="tiny", color=P.muted())

# ------------------------------------------------------------------- B chimera
bio.panel(ax, "B", (8.4, 13.2))
bio.label(ax, (11.8, 12.7), "Quail–chick chimera", size="small", bold=True)
ax.add_patch(Ellipse((9.8, 10.2), 1.6, 1.0, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=5))
bio.label(ax, (9.8, 11.0), "quail graft", size="tiny")
ax.add_patch(Ellipse((13.0, 10.0), 3.0, 1.9, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.0, zorder=5))
bio.label(ax, (13.0, 8.85), "chick host", size="tiny")
bio.arrow(ax, (10.7, 10.2), (12.6, 10.25), kind="process", bend=-0.2)
ax.add_patch(Ellipse((13.3, 10.1), 0.5, 0.35, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=6))
for k, (x, tok) in enumerate(((10.0, "highlight"), (13.0, "animal"))):
    ax.add_patch(Circle((x, 7.7), 0.45, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.0, zorder=5))
    if tok == "highlight":
        ax.add_patch(Circle((x + 0.05, 7.72), 0.16, facecolor=P.edge("chromatin"), edgecolor="none", zorder=6))
    else:
        for d in ((-0.15, 0.1), (0.12, -0.1), (0.1, 0.18), (-0.1, -0.15)):
            ax.add_patch(Circle((x + d[0], 7.7 + d[1]), 0.05, facecolor=P.fill("chromatin"), edgecolor="none", zorder=6))
bio.label(ax, (10.0, 7.0), "quail nucleus:\nheterochromatin mass", size="tiny")
bio.label(ax, (13.0, 7.0), "chick nucleus:\ndispersed", size="tiny")

# ------------------------------------------------------------------- C Cre-lox
bio.panel(ax, "C", (16.4, 13.2))
bio.label(ax, (22.6, 12.7), "Inducible genetic labelling (Cre-loxP)", size="small", bold=True)
G.construct(ax, 17.2, 11.4, [("promoter", "Prom X"), ("cds", "CreER", "enzyme")], unit=0.55)
bio.label(ax, (24.0, 11.4), "+ tamoxifen: CreER enters the nucleus", size="tiny", ha="left", color=P.muted())
G.construct(ax, 17.2, 9.6, [("promoter", "Rosa26"), ("lox", None), ("cds", "STOP", "negative"), ("lox", None),
                            ("cds", "reporter", "positive")], unit=0.55)
bio.label(ax, (24.0, 9.6), "before: reporter silent", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (20.0, 9.0), (20.0, 8.3), kind="process")
bio.label(ax, (20.2, 8.65), "Cre excises STOP", size="tiny", ha="left")
G.construct(ax, 17.2, 7.6, [("promoter", "Rosa26"), ("lox", None), ("cds", "reporter", "positive")], unit=0.55)
bio.label(ax, (24.0, 7.6), "after: cell and all descendants labelled", size="tiny", ha="left", color=P.muted())

# ------------------------------------------------------------------- D barcodes
bio.panel(ax, "D", (0.2, 6.0))
bio.label(ax, (8.0, 5.6), "CRISPR barcodes: edits accumulate and record the lineage", size="small", bold=True)
# a lineage tree drawn by hand: root at left, two divisions
nodes = {"r": (1.2, 2.8), "a": (4.0, 4.0), "b": (4.0, 1.6), "a1": (7.0, 4.6), "a2": (7.0, 3.4), "b1": (7.0, 2.2), "b2": (7.0, 1.0)}
for p, q in (("r", "a"), ("r", "b"), ("a", "a1"), ("a", "a2"), ("b", "b1"), ("b", "b2")):
    (x0, y0), (x1, y1) = nodes[p], nodes[q]
    ax.plot([x0, x0, x1], [y0, y1, y1], color=P.ink(), lw=1.2, zorder=4)


def barcode(x, y, edits):
    for k in range(6):
        tok = ["receptor", "antibody", "enzyme", "channel", "drug", "protein"][k] if edits[k] else "neutral"
        ax.add_patch(Rectangle((x + k * 0.42, y - 0.17), 0.38, 0.34, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, zorder=6))


codes = {"r": [0] * 6, "a": [1, 0, 0, 0, 0, 0], "b": [0, 0, 1, 0, 0, 0], "a1": [1, 1, 0, 0, 0, 0], "a2": [1, 0, 0, 0, 1, 0],
         "b1": [0, 0, 1, 1, 0, 0], "b2": [0, 0, 1, 0, 0, 1]}
for n, (x, y) in nodes.items():
    if n in ("r", "a", "b"):
        barcode(x - 1.1, y + 0.35, codes[n])
    else:
        barcode(x + 0.25, y, codes[n])
bio.label(ax, (1.2, 0.4), "unedited array", size="tiny", color=P.muted())
bio.label(ax, (13.0, 3.2), "shared edits = common ancestor;\nunique edits = recent divisions", size="tiny", ha="left",
          color=P.muted())
bio.label(ax, (13.0, 1.9), "read out with single-cell RNA sequencing:\nlineage and cell type of the same cells", size="tiny",
          ha="left", color=P.muted())
