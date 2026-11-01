"""Two 2 x 2 tables from birthwt (189 births, Baystate Medical Center 1986; Hosmer and Lemeshow). Mosaic
plots: column width is proportional to the number of mothers in each exposure group, the shaded height to
the proportion of low-birth-weight infants (< 2500 g). A: maternal smoking (74 smokers, 30 low; 115
non-smokers, 29 low). B: history of hypertension (12 mothers, 7 low; 177 without, 52 low): a striking
difference in proportions but a tiny exposed group. The dashed line is the overall proportion 59/189.
"""
import matplotlib.pyplot as plt
import wikibio as bio
from matplotlib.patches import Rectangle
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.25)
tables = [("A  Smoking x low birth weight", [("non-smoker", 29, 115), ("smoker", 30, 74)]),
          ("B  Hypertension x low birth weight", [("no hypertension", 52, 177), ("hypertension", 7, 12)])]
for ax, (title, cols) in zip(axs, tables):
    N = sum(c[2] for c in cols)
    x0 = 0.0
    gap = 0.02
    for k, (lab, low, n) in enumerate(cols):
        w = n / N - gap / 2
        tok = "dna" if k == 0 else "rna"
        ax.add_patch(Rectangle((x0, 0), w, low / n, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8))
        ax.add_patch(Rectangle((x0, low / n), w, 1 - low / n, facecolor=P.surface(), edgecolor=P.edge(tok), lw=0.8))
        ax.text(x0 + w / 2, low / n / 2, f"low\n{low}/{n}\n{low / n:.0%}", ha="center", va="center",
                fontsize=FT["tiny"], color=P.ink())
        ax.text(x0 + w / 2, -0.06, f"{lab}\n(n = {n})", ha="center", va="top", fontsize=FT["tiny"], color=P.ink())
        x0 += w + gap
    ax.axhline(59 / 189, color=P.ink(), lw=0.8, ls="--")
    ax.set_xlim(0, 1.0 + gap)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    charts.style_axes(ax, None, "proportion of births")
    charts.title(ax, title)
