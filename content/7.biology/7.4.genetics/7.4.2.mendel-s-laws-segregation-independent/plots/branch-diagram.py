"""Branch (forked-line) diagrams for RrYy x RrYy. A: phenotypes, two outcomes per gene (3/4, 1/4).
B: genotypes, three outcomes per gene (1/4, 1/2, 1/4). The probability of a path is the product along it."""
from fractions import Fraction as F

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 12.0)


def fork(x0, y0, x1, ys, texts, probs):
    for y, t, p in zip(ys, texts, probs):
        ax.plot([x0 + 0.1, x1 - 0.15], [y0, y], color=P.muted(), lw=1.0, zorder=5)
        bio.label(ax, ((x0 + x1) / 2, (y0 + y) / 2 + 0.22), str(p), size="tiny", color=P.edge("dna"))
        bio.label(ax, (x1, y), t, size="small", ha="left", italic=True)


# A: phenotypes
bio.panel(ax, "A", (0.2, 11.8))
bio.label(ax, (1.0, 11.0), "Seed shape", size="small", bold=True, ha="left")
bio.label(ax, (4.2, 11.0), "Seed color", size="small", bold=True, ha="left")
bio.label(ax, (7.6, 11.0), "Phenotype", size="small", bold=True, ha="left")
bio.label(ax, (10.6, 11.0), "Probability", size="small", bold=True, ha="left")
top = [(8.0, "R_", F(3, 4)), (3.6, "rr", F(1, 4))]
fork(0.2, 5.8, 1.4, [t[0] for t in top], [t[1] for t in top], [t[2] for t in top])
bio.label(ax, (0.1, 5.8), "", size="small")
for y, g, pr in top:
    sub = [(y + 1.2, "Y_", F(3, 4)), (y - 1.2, "yy", F(1, 4))]
    fork(2.2, y, 4.6, [s[0] for s in sub], [s[1] for s in sub], [s[2] for s in sub])
    for yy, g2, p2 in sub:
        name = ("round" if g == "R_" else "wrinkled") + ", " + ("yellow" if g2 == "Y_" else "green")
        bio.label(ax, (7.6, yy), name, size="small", ha="left")
        bio.label(ax, (10.6, yy), f"{pr} × {p2} = {pr * p2}", size="small", ha="left")

# B: genotypes
bio.panel(ax, "B", (14.0, 11.8))
bio.label(ax, (14.8, 11.0), "R gene", size="small", bold=True, ha="left")
bio.label(ax, (17.8, 11.0), "Y gene", size="small", bold=True, ha="left")
bio.label(ax, (21.0, 11.0), "Genotype", size="small", bold=True, ha="left")
bio.label(ax, (23.6, 11.0), "Probability", size="small", bold=True, ha="left")
g1 = [(8.9, "RR", F(1, 4)), (5.8, "Rr", F(1, 2)), (2.7, "rr", F(1, 4))]
fork(14.0, 5.8, 15.2, [t[0] for t in g1], [t[1] for t in g1], [t[2] for t in g1])
for y, g, pr in g1:
    sub = [(y + 1.0, "YY", F(1, 4)), (y, "Yy", F(1, 2)), (y - 1.0, "yy", F(1, 4))]
    fork(16.2, y, 18.4, [s[0] for s in sub], [s[1] for s in sub], [s[2] for s in sub])
    for yy, g2, p2 in sub:
        bio.label(ax, (21.0, yy), g + g2, size="small", ha="left", italic=True)
        bio.label(ax, (23.6, yy), str(pr * p2), size="small", ha="left")
