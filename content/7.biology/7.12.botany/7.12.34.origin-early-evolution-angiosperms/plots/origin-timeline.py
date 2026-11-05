# The age of the angiosperms: fossil record versus molecular-clock estimates of the crown group.
# Fossils: earliest accepted angiosperm pollen (Valanginian-Hauterivian, c. 136-130 Ma), tricolpate pollen
# (c. 125 Ma), Montsechia (Barremian, c. 130 Ma), Archaefructus (Yixian Formation, c. 125 Ma), Cretaceous
# mesofossil flowers (c. 130-100 Ma); disputed Jurassic records (Schmeissneria, Nanjinganthus: open
# symbols). Clock estimates of crown angiosperms: Sanderson & Doyle 2001 (most likely 190-140), Wikstrom et
# al. 2001 (179-158), Bell et al. 2010 (199-167), Smith et al. 2010 (228-217), Magallon et al. 2015 (c. 140),
# Barba-Montoya et al. 2018 (256-149).
import wikibio as bio
from wikibio import phylo

P = bio.P
OLD, YOUNG = 280.0, 90.0
X0, X1 = 6.0, 27.0


def x(a):
    return X0 + (OLD - a) / (OLD - YOUNG) * (X1 - X0)


fig, ax = bio.canvas(28.5, 14.2)
phylo.geo_scale(ax, (X0, X1), (OLD, YOUNG), 13.6, ranks=("era", "period"), height=0.5, size="tiny")
for a in range(100, 281, 20):
    ax.plot([x(a), x(a)], [0.9, 12.0], color=P.muted(), lw=0.5, ls=(0, (2, 3)), alpha=0.6, zorder=1)
    bio.label(ax, (x(a), 0.55), f"{a}", size="tiny", color=P.muted())
bio.label(ax, (X1 + 0.5, 0.55), "Ma", size="tiny", color=P.muted(), ha="left")

bio.label(ax, (0.2, 11.6), "Fossils", size="normal", bold=True, ha="left")
FOSSILS = [  # label, from, to, accepted
    ("Earliest angiosperm pollen", 136, 130, True), ("Montsechia", 131, 129, True),
    ("Archaefructus", 126, 124, True), ("Tricolpate pollen (eudicots)", 126, 124, True),
    ("Mesofossil flowers (Portugal, N America)", 130, 100, True),
    ("Schmeissneria", 190, 180, False), ("Nanjinganthus", 178, 174, False),
]
y = 11.0
for name, a0, a1, ok in FOSSILS:
    tok = "plant" if ok else "neutral"
    if a0 - a1 > 3:
        bio.box(ax, ((x(a0) + x(a1)) / 2, y), x(a1) - x(a0), 0.36, token=tok, radius=0.1)
    else:
        mid = (a0 + a1) / 2
        ax.scatter([x(mid)], [y], s=55, facecolor=P.fill(tok) if ok else "none", edgecolor=P.edge(tok), lw=1.4,
                   zorder=8)
    genus = " " not in name
    bio.label(ax, (x(a0) - 0.25, y), name, size="small", ha="right", italic=genus,
              color=None if ok else P.muted())
    y -= 0.72
bio.label(ax, (0.2, 5.4), "Molecular clock: crown angiosperms", size="normal", bold=True, ha="left")
CLOCKS = [("Sanderson & Doyle 2001", 190, 140, None), ("Wikstrom et al. 2001", 179, 158, None),
          ("Bell et al. 2010", 199, 167, None), ("Smith et al. 2010", 228, 217, None),
          ("Magallon et al. 2015", 141, 137, 139), ("Barba-Montoya et al. 2018", 256, 149, None)]
y = 4.8
for name, a0, a1, point in CLOCKS:
    bio.box(ax, ((x(a0) + x(a1)) / 2, y), max(x(a1) - x(a0), 0.15), 0.36, token="dna", radius=0.1)
    if point:
        ax.scatter([x(point)], [y], s=30, color=P.edge("dna"), zorder=9)
    bio.label(ax, (x(a0) - 0.25, y), name, size="small", ha="right")
    y -= 0.62
ax.annotate("", xy=(x(136), 5.75), xytext=(x(190), 5.75),
            arrowprops=dict(arrowstyle="<->", color=P.edge("highlight"), lw=1.3))
bio.label(ax, (x(134), 5.75), "Gap: oldest fossils vs most clock estimates", size="small", ha="left",
          color=P.edge("highlight"))
bio.label(ax, (x(230), 7.4), "Grey: disputed records", size="tiny", color=P.muted())
