# The bacterial 16S rRNA gene and common amplicons. Positions in Escherichia coli numbering (about 1542 nt):
# the nine hypervariable regions V1-V9 (boundaries after Chakravorty and colleagues 2007) alternate with
# conserved regions where universal primers bind. Below: three common amplicons with their primers, the
# V4 region of the Earth Microbiome Project (515F-806R, read by 2 x 250 or 2 x 150 reads), V3-V4 (341F-805R,
# 2 x 300 reads that overlap in the middle) and the full-length gene (27F-1492R) for PacBio HiFi reads.
from matplotlib.patches import Rectangle
import wikibio as bio

P = bio.P
L = 1542
V = [(69, 99), (137, 242), (433, 497), (576, 682), (822, 879), (986, 1043), (1117, 1173), (1243, 1294), (1435, 1465)]
fig, ax = bio.canvas(30.0, 9.6)
x0, w = 1.5, 27.0


def X(p):
    return x0 + w * p / L


y = 7.0
ax.add_patch(Rectangle((X(0), y - 0.35), X(L) - X(0), 0.7, fc=P.fill("rrna"), ec=P.edge("rrna"), lw=1.0))
for i, (a, b) in enumerate(V):
    ax.add_patch(Rectangle((X(a), y - 0.35), X(b) - X(a), 0.7, fc=P.fill("highlight"), ec=P.edge("highlight"), lw=0.8))
    bio.label(ax, ((X(a) + X(b)) / 2, y + 0.75), f"V{i + 1}", size="small")
for p in (0, 250, 500, 750, 1000, 1250, 1500):
    ax.plot([X(p), X(p)], [y - 0.45, y - 0.65], color=P.muted(), lw=0.8)
    bio.label(ax, (X(p), y - 1.0), str(p), size="tiny", color=P.muted())
bio.label(ax, (X(0) - 0.6, y), "5′", size="tiny")
bio.label(ax, (X(L) + 0.6, y), "3′", size="tiny")
bio.label(ax, (X(L / 2), y + 1.7),
          "16S rRNA gene, E. coli numbering: conserved regions (red) and hypervariable regions V1-V9 (yellow)",
          size="small")
amps = [("V4: 515F-806R, ~290 bp", 515, 533, 787, 806, 4.5),
        ("V3-V4: 341F-805R, ~465 bp", 341, 357, 785, 805, 3.0),
        ("full length: 27F-1492R, ~1500 bp", 8, 27, 1492, 1510, 1.5)]
for name, f0, f1, r0, r1, yy in amps:
    ax.plot([X(f0), X(r1)], [yy, yy], color=P.ink(), lw=1.2)
    bio.arrow(ax, (X(f0), yy + 0.3), (X(f1) + 0.3, yy + 0.3), kind="process", color=P.edge("dna"))
    bio.arrow(ax, (X(r1), yy - 0.3), (X(r0) - 0.3, yy - 0.3), kind="process", color=P.edge("dna"))
    bio.label(ax, ((X(f0) + X(r1)) / 2, yy + 0.55), name, size="tiny")
    for p in (f0, r1):
        ax.plot([X(p), X(p)], [yy + 0.1, y - 0.35], color=P.muted(), lw=0.5, ls=(0, (2, 2)))
