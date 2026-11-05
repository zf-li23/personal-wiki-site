"""Left: stratigraphic ranges of seed plants and their relatives on the ICS time scale (approximate; dashed:
records that are disputed or inferred from molecular clocks only). Progymnosperms and the earliest seed
plants are Devonian; seed ferns and cordaites dominate the Carboniferous and Permian; Glossopteris marks
the Permian of Gondwana; Bennettitales and Caytoniales are Mesozoic; the five living lineages (cycads,
ginkgo, conifers, gnetophytes, angiosperms) persist to the present. Right: relationships of the living
lineages (living gymnosperms monophyletic; gnetophytes shown as sister to Pinaceae, the gnepine
hypothesis, which is supported by many but not all phylogenomic analyses)."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(32, 14)
X0, X1 = 6.2, 21.5
A0 = 400.0


def x(a):
    return X0 + (A0 - a) / A0 * (X1 - X0)


yb = phylo.geo_scale(ax, (X0, X1), (A0, 0), 13.4, ranks=("era", "period"), height=0.5, size="tiny")
rows = [  # name, (solid ranges), (dashed ranges), token, italic
    ("Progymnosperms", [(393, 330)], [], "bract", False),
    (r"$\it{Runcaria}$ (proto-ovule)", [(386, 383)], [], "ovule", False),
    (r"Early seed ferns ($\it{Elkinsia}$, $\it{Lyginopteris}$)", [(365, 300)], [], "ovule", False),
    ("Medullosales", [(330, 270)], [], "ovule", False),
    ("Cordaitales", [(325, 252)], [], "animal", False),
    (r"Glossopteridales ($\it{Glossopteris}$)", [(299, 252)], [(252, 235)], "ovule", False),
    ("Bennettitales", [(237, 70)], [], "petal", False),
    ("Caytoniales", [(230, 100)], [], "petal", False),
    ("Cycads", [(300, 0)], [], "plant", False),
    ("Ginkgo lineage", [(290, 0)], [], "positive", False),
    ("Conifers", [(310, 0)], [], "animal", False),
    ("Gnetophytes", [(145, 0)], [(230, 145)], "highlight", False),
    ("Angiosperms", [(135, 0)], [(250, 135)], "tepal", False),
]
y = yb - 0.45
for name, solid, dashed, tok, it in rows:
    for a0, a1 in solid:
        ax.plot([x(a0), x(a1)], [y, y], color=P.fill(tok), lw=7, solid_capstyle="butt", zorder=6)
        ax.plot([x(a0), x(a1)], [y, y], color=P.edge(tok), lw=0.6, zorder=7)
    for a0, a1 in dashed:
        ax.plot([x(a0), x(a1)], [y, y], color=P.edge(tok), lw=1.6, ls=(0, (2, 1.5)), zorder=6)
    bio.label(ax, (X0 - 0.2, y), name, size="small", ha="right", italic=it)
    y -= 0.82
for a in (400, 300, 200, 100, 0):
    ax.plot([x(a), x(a)], [y + 0.4, yb], color=P.muted(), lw=0.3, ls=":", zorder=2)
    bio.label(ax, (x(a), y + 0.05), f"{a}", size="tiny", color=P.muted())
bio.label(ax, ((X0 + X1) / 2, y - 0.45), "Ma", size="tiny", color=P.muted())

NEWICK = "(Angiosperms,((Cycads,Ginkgo)CG,((Gnetophytes,Pinaceae)Gnepine,Cupressophytes)Conifers)Gymnosperms)Seed;"
t = phylo.tree(ax, NEWICK, origin=(23.2, 3.0), width=4.0, height=8.4, direction="right", root_edge=0.3, label_size="small",
               icons={"Cycads": "phylopic/cycad", "Ginkgo": "phylopic/ginkgo", "Gnetophytes": "phylopic/ephedra",
                      "Pinaceae": "phylopic/pine", "Cupressophytes": "phylopic/conifer"},
               icon_size=0.7, icon_color="plant",
               clades=[dict(node="Gymnosperms", token="ovule", style="bar", label="Living gymnosperms")])
bio.label(ax, (26.0, 12.4), "Living seed plants", size="normal", bold=True)
