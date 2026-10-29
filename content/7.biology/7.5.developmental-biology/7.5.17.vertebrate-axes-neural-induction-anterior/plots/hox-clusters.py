# The four Hox clusters of the mouse and their relation to the single Drosophila complex. Top: the eight Drosophila
# HOM-C genes aligned with the 13 vertebrate paralogous groups (lab with group 1, pb with 2, Dfd with 4, Scr with 5,
# Antp with 6-8, Ubx and abd-A with groups 6-8 as well, Abd-B with 9-13). Middle: HoxA-D (39 genes) with the genes
# each cluster has retained; 3' genes are expressed earlier and more anteriorly (spatial and temporal colinearity).
# Bottom: the vertebral column of the mouse, with the anterior limits of expression of representative paralogous
# groups in the paraxial mesoderm (schematic); Hox10 genes repress rib formation in the lumbar region and Hox11 genes
# specify the sacrum.
import wikibio as bio

fig, ax = bio.canvas(24.0, 12.0)
P = bio.P
groups = list(range(1, 14))
gx = {g: 3.2 + (g - 1) * 1.55 for g in groups}
present = {"A": [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13], "B": [1, 2, 3, 4, 5, 6, 7, 8, 9, 13],
           "C": [4, 5, 6, 8, 9, 10, 11, 12, 13], "D": [1, 3, 4, 8, 9, 10, 11, 12, 13]}
col = lambda g: ["channel", "dna2", "cl", "positive", "highlight", "lipid", "drug", "receptor", "k", "protein", "metabolite",
                 "neutral", "chromatin"][g - 1]
# Drosophila
fly = [("lab", [1]), ("pb", [2]), ("Dfd", [4]), ("Scr", [5]), ("Antp", [6, 7, 8]), ("Ubx", [6, 7, 8]), ("abd-A", [6, 7, 8]),
       ("Abd-B", [9, 10, 11, 12, 13])]
bio.label(ax, (0.4, 11.6), "Drosophila", size="small", bold=True, ha="left", italic=True)
bio.label(ax, (2.25, 11.6), "HOM-C", size="small", bold=True, ha="left")
xs = [3.2, 4.75, 7.85, 9.4, 11.4, 12.9, 14.4, 19.5]
for (g, grp), xx in zip(fly, xs):
    bio.box(ax, (xx, 10.8), 1.35, 0.6, token=col(grp[0]), text=g, size="tiny", italic=True)
for g in groups:
    bio.label(ax, (gx[g], 9.6), str(g), size="tiny", color=P.muted())
bio.label(ax, (0.4, 9.6), "paralogous group", size="tiny", color=P.muted(), ha="left")
for k, cl in enumerate("ABCD"):
    y = 8.6 - k * 1.0
    ax.plot([gx[1] - 0.8, gx[13] + 0.8], [y, y], color=P.edge("dna"), lw=2.0, zorder=5)
    bio.label(ax, (0.4, y), f"Hox{cl.lower()}" if False else f"Hox{cl}", size="small", bold=True, ha="left")
    for g in present[cl]:
        bio.box(ax, (gx[g], y), 1.2, 0.55, token=col(g), text=f"{cl.lower()}{g}", size="tiny", italic=True)
bio.arrow(ax, (gx[1] - 0.5, 4.6), (gx[13] + 0.5, 4.6), kind="process", color=P.muted())
bio.label(ax, ((gx[1] + gx[13]) / 2, 4.95), "3′ → 5′: later activation, more posterior anterior limit", size="tiny", color=P.muted())
# vertebral column
regions = [("C1-C7", 7, "channel"), ("T1-T13", 13, "highlight"), ("L1-L6", 6, "positive"), ("S1-S4", 4, "drug"), ("Ca", 6, "neutral")]
x = 2.2
w = 0.6
ystrip = 2.4
for name, n, tok in regions:
    for i in range(n):
        ax.add_patch(bio.core.FancyBboxPatch((x, ystrip - 0.3), w - 0.08, 0.6, boxstyle="round,pad=0,rounding_size=0.08",
                                             facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6))
        x += w
    bio.label(ax, (x - n * w / 2, ystrip - 0.75), name, size="tiny")
lim = [(4, 2.2 + 2 * w, "Hox4"), (6, 2.2 + 6.5 * w, "Hox6 (C7/T1)"), (9, 2.2 + 12 * w, "Hox9"), (10, 2.2 + 20 * w, "Hox10 (L1)"),
       (11, 2.2 + 26 * w, "Hox11 (S1)")]
for k, (g, xx, txt) in enumerate(lim):
    ax.plot([xx, xx], [ystrip + 0.35, ystrip + 0.95 + 0.0 * k], color=P.edge(col(g)), lw=1.5)
    ax.plot([xx, x], [ystrip + 0.95 - 0.0, ystrip + 0.95], color=P.light(col(g)), lw=0.0)
    bio.label(ax, (xx, ystrip + 1.2), txt, size="tiny", color=P.edge(col(g)))
bio.label(ax, (0.4, ystrip), "mouse\nvertebrae", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.4, ystrip + 1.2), "anterior limits:", size="tiny", color=P.muted(), ha="left")
