"""Deletion mapping of rII point mutations of phage T4 (schematic, after the logic of Benzer's method).
The rII region (rIIA and rIIB cistrons) is divided into seven intervals 1-7 by the end points of a set of
overlapping deletions (bars; the gap in each bar is the deleted segment). A point mutant is crossed with each
deletion mutant in E. coli B and the progeny are plated on E. coli K(lambda): wild-type recombinants (+) can arise
only if the point mutation lies outside the deleted segment. The pattern of + and - across the deletions places
the mutation in one interval (here interval 4), after which it is mapped finely by two-point crosses with the
other mutations in that interval only."""

from matplotlib.patches import Rectangle

import wikibio as bio

P = bio.P

fig, ax = bio.canvas(18.0, 9.0)
x0, L = 3.0, 12.0
cuts = [0, 1.6, 3.4, 5.0, 6.4, 8.2, 10.0, 12.0]
y_top = 7.8
ax.add_patch(Rectangle((x0, y_top - 0.2), 6.6, 0.4, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.9))
ax.add_patch(Rectangle((x0 + 6.6, y_top - 0.2), L - 6.6, 0.4, facecolor=P.fill("dna2"), edgecolor=P.edge("dna2"),
                       lw=0.9))
bio.label(ax, (x0 + 3.3, y_top + 0.55), "rIIA", size="small", italic=True)
bio.label(ax, (x0 + 9.3, y_top + 0.55), "rIIB", size="small", italic=True)
for k in range(7):
    xm = x0 + (cuts[k] + cuts[k + 1]) / 2
    bio.label(ax, (xm, y_top - 0.55), str(k + 1), size="tiny", color=P.muted())
    ax.plot([x0 + cuts[k + 1]] * 2, [1.3, y_top - 0.25], color=P.muted(), lw=0.4, ls=":")

dels = [("Df1", 0, 12.0), ("Df2", 1.6, 12.0), ("Df3", 3.4, 12.0), ("Df4", 5.0, 12.0), ("Df5", 0, 6.4),
        ("Df6", 8.2, 12.0), ("Df7", 10.0, 12.0)]
mut = x0 + 5.7  # interval 4
for r, (name, a, b) in enumerate(dels):
    y = 6.6 - r * 0.72
    bio.label(ax, (x0 - 0.2, y), name, size="tiny", ha="right")
    if a > 0:
        ax.plot([x0, x0 + a], [y, y], color=P.ink(), lw=2.4, solid_capstyle="butt")
    if b < L:
        ax.plot([x0 + b, x0 + L], [y, y], color=P.ink(), lw=2.4, solid_capstyle="butt")
    ax.add_patch(Rectangle((x0 + a, y - 0.16), b - a, 0.32, facecolor=P.light("negative"), edgecolor=P.edge("negative"),
                           lw=0.6, ls="--"))
    covered = x0 + a <= mut <= x0 + b
    bio.label(ax, (x0 + L + 0.6, y), "-" if covered else "+", size="normal",
              color=P.edge("negative") if covered else P.edge("positive"))
bio.label(ax, (x0 + L + 0.6, 7.25), "rII+\nprogeny", size="tiny")
ax.plot([mut, mut], [1.3, y_top + 0.25], color=P.edge("highlight"), lw=1.4)
ax.plot([mut], [y_top], "v", color=P.edge("highlight"), ms=8)
bio.label(ax, (mut, 0.95), "point mutation: covered by deletions with -, so it lies in interval 4", size="small")
bio.label(ax, (x0 - 0.2, 7.8), "rII region", size="tiny", ha="right")
