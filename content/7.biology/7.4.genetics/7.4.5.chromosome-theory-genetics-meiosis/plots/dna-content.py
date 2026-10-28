"""DNA content per nucleus (in C, the DNA content of one haploid set) and chromosome number (in n, counting
centromeres) through a mitotic cycle (A) and through meiosis followed by fertilization (B). Replication in
S phase raises the DNA content gradually; each nuclear division halves it at once."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.6))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.12, top=0.86, wspace=0.22)


def draw(ax, bounds, names, c, n, title):
    # bounds: stage boundaries; c, n: (value at start, value at end) of each stage
    xs_c, ys_c, xs_n, ys_n = [], [], [], []
    for (a, b), (c0, c1), (n0, n1) in zip(zip(bounds, bounds[1:]), c, n):
        xs_c += [a, b]
        ys_c += [c0, c1]
        xs_n += [a, b]
        ys_n += [n0, n1]
    ax.plot(xs_c, ys_c, color=charts.line("dna"), lw=2.0, label="DNA content (C)")
    ax.plot(xs_n, [v - 0.04 for v in ys_n], color=charts.line("receptor"), lw=2.0, ls="--", label="chromosome number (n)")
    for x in bounds:
        ax.axvline(x, color=P.muted(), lw=0.6, ls=":")
    for a, b, s in zip(bounds, bounds[1:], names):
        ax.text((a + b) / 2, 4.45, s, ha="center", fontsize=FT["tiny"], color=P.muted())
    ax.set_ylim(0, 4.8)
    ax.set_xlim(bounds[0], bounds[-1])
    ax.set_yticks([1, 2, 3, 4])
    ax.set_xticks([])
    charts.style_axes(ax, None, "C or n")
    charts.title(ax, title)
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")


draw(axs[0], [0, 2, 3.5, 5, 6, 8], ["G1", "S", "G2", "M", "G1"],
     [(2, 2), (2, 4), (4, 4), (4, 4), (2, 2)], [(2, 2)] * 5, "A  Mitotic cell cycle")
draw(axs[1], [0, 1.5, 3, 4.5, 5.5, 6.5, 8, 9.5],
     ["G1", "S", "prophase I", "MI", "MII", "gamete", "zygote"],
     [(2, 2), (2, 4), (4, 4), (4, 4), (2, 2), (1, 1), (2, 2)],
     [(2, 2), (2, 2), (2, 2), (2, 2), (1, 1), (1, 1), (2, 2)], "B  Meiosis and fertilization")
