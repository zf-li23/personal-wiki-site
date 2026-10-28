# Mitotic recombination in a y sn+ / y+ sn cell: twin spots and single spots
import numpy as np
from matplotlib.patches import RegularPolygon

import wikibio as bio
from wikibio import transmission as T

P = bio.P
fig, ax = bio.canvas(28, 13)
loci = [(0.6, ("sn+", "sn")), (0.9, ("y", "y+"))]


def cell_with(ax, c, segs, genos, title, token="cytoplasm"):
    bio.shape(ax, bio.blob(c, 2.3, 1.45, wobble=0.04, seed=3), token=token, zorder=2)
    for k, (sg, g) in enumerate(zip(segs, genos)):
        y = c[1] + 0.35 - 0.7 * k
        T.chromatid_bar(ax, c[0] - 1.6, c[0] + 1.6, y, sg, height=0.22, loci=[(0.6, ""), (0.9, "")], label_pos=None,
                        centromere=0.03)
        bio.label(ax, (c[0] + 1.75, y), T.allele(g), size="tiny", ha="left")
    bio.label(ax, (c[0], c[1] - 1.85), title, size="small")


# A: G2 cell with a crossover between centromere and sn
bio.panel(ax, "A", (0.2, 12.8))
pr = T.four_chromatids(ax, 0.9, 6.4, 9.6, crossovers=[(0.35, 1, 2)], loci=loci)
bio.label(ax, (3.6, 11.7), r"G2: crossover between centromere and $\it{sn}$", size="small", bold=True)
segs, geno = pr["segments"], [" ".join(g) for g in pr["genotypes"]]

# B: x segregation -> two homozygous daughters
bio.panel(ax, "B", (8.6, 12.8))
bio.arrow(ax, (6.9, 10.2), (9.4, 11.0), kind="process")
bio.arrow(ax, (6.9, 9.0), (9.4, 8.2), kind="process")
bio.label(ax, (8.1, 9.6), "x segregation", size="tiny", color=P.muted())
cell_with(ax, (12.0, 11.0), [segs[0], segs[2]], [geno[0], geno[2]], r"homozygous $\it{y}$: yellow")
cell_with(ax, (12.0, 7.0), [segs[1], segs[3]], [geno[1], geno[3]], r"homozygous $\it{sn}$: singed")

# C: tissue with a twin spot
bio.panel(ax, "C", (17.6, 12.8))
rng = np.random.default_rng(1)
cx0, cy0 = 18.6, 6.3
yellow = [(5, 4), (6, 4), (5, 5), (6, 5), (7, 5), (6, 6), (5, 3)]
singed = [(8, 4), (8, 5), (9, 4), (9, 5), (8, 3), (9, 3)]
for i in range(14):
    for j in range(10):
        x = cx0 + i * 0.62 + (0.31 if j % 2 else 0)
        y = cy0 + j * 0.54
        tok = "highlight" if (i, j) in yellow else "negative" if (i, j) in singed else "neutral"
        ax.add_patch(RegularPolygon((x, y), 6, radius=0.34, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.5))
bio.label(ax, (22.6, 12.0), "Twin spot in heterozygous tissue", size="small", bold=True)
bio.callout(ax, (cx0 + 5.5 * 0.62, cy0 + 4.5 * 0.54), (cx0 + 2.0, cy0 - 0.7), r"yellow clone ($\it{y/y}$)", size="tiny")
bio.callout(ax, (cx0 + 8.6 * 0.62, cy0 + 4 * 0.54), (cx0 + 6.8, cy0 - 0.7), r"singed clone ($\it{sn/sn}$)", size="tiny")

# D: crossover between sn and y -> single yellow spot
bio.panel(ax, "D", (0.2, 5.0))
pr2 = T.four_chromatids(ax, 0.9, 6.4, 2.6, crossovers=[(0.75, 1, 2)], loci=loci)
bio.label(ax, (3.6, 4.6), r"crossover between $\it{sn}$ and $\it{y}$", size="small", bold=True)
s2, g2 = pr2["segments"], [" ".join(g) for g in pr2["genotypes"]]
bio.arrow(ax, (6.9, 2.6), (8.9, 2.6), kind="process")
bio.label(ax, (7.9, 3.0), "x segregation", size="tiny", color=P.muted())
T.chromatid_bar(ax, 9.3, 12.5, 3.0, s2[0], height=0.22, loci=[(0.6, ""), (0.9, "")], label_pos=None, centromere=0.03)
T.chromatid_bar(ax, 9.3, 12.5, 2.3, s2[2], height=0.22, loci=[(0.6, ""), (0.9, "")], label_pos=None, centromere=0.03)
bio.label(ax, (12.7, 3.0), T.allele(g2[0]), size="tiny", ha="left")
bio.label(ax, (12.7, 2.3), T.allele(g2[2]), size="tiny", ha="left")
bio.label(ax, (14.6, 2.65), r"$\it{y/y}$, $\it{sn}^{+}/\it{sn}$: single yellow spot" + "\n(sister cell: wild type)", size="small", ha="left")
