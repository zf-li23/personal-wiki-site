"""Conjugation in a ciliate (Tetrahymena-like, one micronucleus per cell; schematic). 1: cells of different
mating types pair. 2: the diploid micronucleus undergoes meiosis; three of the four haploid products degenerate.
3: the survivor divides by mitosis into a stationary and a migratory pronucleus; the migratory pronuclei are
exchanged. 4: the pronuclei fuse into a diploid zygotic nucleus; the old macronucleus begins to degrade.
5: the zygotic nucleus divides; some products become new micronuclei, others develop into new macronuclei
(DNA elimination, chromosome fragmentation and amplification), and the exconjugants separate."""
import numpy as np
from matplotlib.patches import Ellipse, Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 8.2)


def cellpair(cx, cy, sep=1.05, apart=False):
    out = []
    for side, tok in ((-1, "cytoplasm"), (1, "cytoplasm")):
        x = cx + side * (sep + (0.25 if apart else 0))
        ax.add_patch(Ellipse((x, cy), 2.0, 3.6, facecolor=P.fill(tok), edgecolor=P.edge("protein"), lw=1.2, zorder=4))
        for th in np.linspace(0, 2 * np.pi, 40, endpoint=False):
            px, py = x + 1.0 * np.cos(th), cy + 1.8 * np.sin(th)
            ax.plot([px, px + 0.16 * np.cos(th)], [py, py + 0.16 * np.sin(th)], color=P.edge("protein"), lw=0.6, zorder=3)
        out.append(x)
    return out


def mac(x, y, r=0.55, old=False):
    tok = "neutral" if old else "nucleus"
    ax.add_patch(Ellipse((x, y), 1.2 * r * 1.6, 1.2 * r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0,
                         zorder=6, linestyle="--" if old else "-"))


def mic(x, y, r=0.16, tok="dna", hollow=False):
    ax.add_patch(Circle((x, y), r, facecolor="none" if hollow else P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=7))


titles = ["1  pairing", "2  meiosis", "3  exchange", "4  fusion", "5  new nuclei"]
xs = [2.8, 8.0, 13.2, 18.4, 23.6]
cy = 4.2
for k, (x0, t) in enumerate(zip(xs, titles)):
    bio.label(ax, (x0, 7.6), t, size="small", bold=True)
    a, b = cellpair(x0, cy, apart=(k == 4))
    for xc, tokA, tokB in ((a, "dna", "rna"), (b, "rna", "dna")):
        mine = tokA
        if k == 0:
            mac(xc, cy - 0.6); mic(xc, cy + 0.8, 0.2, mine)
        elif k == 1:
            mac(xc, cy - 0.8)
            for j, (dx, dy) in enumerate(((-0.4, 1.2), (0.4, 1.2), (-0.4, 0.5), (0.4, 0.5))):
                mic(xc + dx, cy + dy, 0.13, mine, hollow=(j > 0))
        elif k == 2:
            mac(xc, cy - 0.8)
            mic(xc + (-0.3 if xc < x0 else 0.3), cy + 0.6, 0.13, mine)
            mic(xc + (0.55 if xc < x0 else -0.55), cy + (0.95 if xc < x0 else 0.25), 0.13, mine)
        elif k == 3:
            mac(xc, cy - 1.0, r=0.4, old=True)
            ax.add_patch(Circle((xc + (0.45 if xc < x0 else -0.45), cy + 0.6), 0.2, facecolor=P.fill("dna"),
                                edgecolor=P.edge("rna"), lw=1.6, zorder=7))
        else:
            mac(xc, cy - 0.3, r=0.42); mac(xc, cy - 1.2, r=0.42)
            ax.add_patch(Circle((xc, cy + 1.0), 0.17, facecolor=P.fill("dna"), edgecolor=P.edge("rna"), lw=1.6, zorder=7))
            ax.add_patch(Circle((xc + 0.55, cy - 0.75), 0.1, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6, zorder=6))
    if k == 2:
        bio.arrow(ax, (a + 0.72, cy + 0.95), (b - 0.1, cy + 0.95), kind="process", head=0.14)
        bio.arrow(ax, (b - 0.72, cy + 0.25), (a + 0.1, cy + 0.25), kind="process", head=0.14)
    if k < 4:
        bio.arrow(ax, (x0 + 2.25, cy), (xs[k + 1] - 2.25, cy), kind="process", head=0.2)
bio.callout(ax, (xs[0] - 1.05, cy - 0.6), (0.6, 1.0), "macronucleus")
bio.callout(ax, (xs[0] - 1.05, cy + 0.8), (0.6, 6.8), "micronucleus (2n)")
bio.label(ax, (xs[1], 1.2), "3 of 4 haploid\nproducts degenerate", size="tiny", color=P.muted())
bio.label(ax, (xs[2], 1.2), "stationary + migratory\npronuclei", size="tiny", color=P.muted())
bio.label(ax, (xs[3], 1.2), "zygotic nucleus (2n);\nold macronucleus degrades", size="tiny", color=P.muted())
bio.label(ax, (xs[4], 1.2), "new micronucleus (2n) and\ndeveloping macronuclei", size="tiny", color=P.muted())
