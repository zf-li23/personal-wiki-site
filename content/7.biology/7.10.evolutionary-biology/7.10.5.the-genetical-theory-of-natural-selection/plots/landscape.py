"""Wright's adaptive landscape. Top row: genotype fitnesses w11, w12, w22 (A1A1, A1A2, A2A2) for directional
selection (1, 1.05, 1.1), overdominance (0.9, 1, 0.8) and underdominance (1.1, 1, 1.2). Middle row: mean
fitness against the frequency p of A2, with arrows for the direction of change under selection; filled dots:
stable equilibria (peaks), open dot: unstable equilibrium (valley). Right: a two-locus landscape for a haploid
population, fitnesses AB 1.1, ab 1.05, Ab and aB 1.0 (epistasis), mean fitness under linkage equilibrium as
contours over the two allele frequencies, and trajectories of the gradient dynamics
Delta p = p (1 - p) d ln(w_bar)/dp for each locus, which reach one of the two peaks according to the start."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig = plt.figure(figsize=(12.0, 4.8))
gs = fig.add_gridspec(2, 4, height_ratios=[0.55, 1], width_ratios=[1, 1, 1, 1.45], left=0.05, right=0.98,
                      bottom=0.12, top=0.92, wspace=0.35, hspace=0.45)
cases = (("Directional", (1.0, 1.05, 1.1)), ("Overdominance", (0.9, 1.0, 0.8)), ("Underdominance", (1.1, 1.0, 1.2)))
p = np.linspace(0, 1, 300)
for k, (name, w) in enumerate(cases):
    top = fig.add_subplot(gs[0, k])
    top.bar([0, 1, 2], w, color=[P.fill("dna"), P.fill("enzyme"), P.fill("rna")],
            edgecolor=[P.edge("dna"), P.edge("enzyme"), P.edge("rna")], width=0.6)
    top.set_xticks([0, 1, 2], ["$A_1A_1$", "$A_1A_2$", "$A_2A_2$"])
    top.set_ylim(0.7, 1.25)
    charts.style_axes(top, None, "$w$" if k == 0 else None)
    charts.title(top, f"{'ABC'[k]}  {name}")
    ax = fig.add_subplot(gs[1, k])
    wb = (1 - p) ** 2 * w[0] + 2 * p * (1 - p) * w[1] + p ** 2 * w[2]
    ax.plot(p, wb, color=P.ink(), lw=1.8)
    alpha = p * w[2] + (1 - p) * w[1] - (p * w[1] + (1 - p) * w[0])
    for x in (0.12, 0.3, 0.5, 0.7, 0.88):
        a_ = x * w[2] + (1 - x) * w[1] - (x * w[1] + (1 - x) * w[0])
        y = (1 - x) ** 2 * w[0] + 2 * x * (1 - x) * w[1] + x ** 2 * w[2]
        d = 0.06 * np.sign(a_)
        if abs(a_) > 1e-3:
            ax.annotate("", xy=(x + d, y + d * 2 * a_), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->", color=charts.line("rna"), lw=1.1))
    lo, hi = wb.min(), wb.max()
    ax.set_ylim(lo - 0.12 * (hi - lo) - 0.005, hi + 0.15 * (hi - lo) + 0.005)
    if k == 0:
        ax.scatter([1], [1.1], s=34, color=P.ink(), zorder=5)
    if k == 1:
        ph = 0.1 / 0.3
        ph = (1 - 0.9) / (2 - 0.9 - 0.8)
        ax.scatter([ph], [(1 - ph) ** 2 * 0.9 + 2 * ph * (1 - ph) + ph ** 2 * 0.8], s=34, color=P.ink(), zorder=5)
        ax.axvline(ph, color=P.muted(), lw=0.7, ls=":")
    if k == 2:
        ph = (1 - 1.1) / (2 - 1.1 - 1.2)
        ax.scatter([0, 1], [1.1, 1.2], s=34, color=P.ink(), zorder=5, clip_on=False)
        ax.scatter([ph], [(1 - ph) ** 2 * 1.1 + 2 * ph * (1 - ph) + ph ** 2 * 1.2], s=40, facecolor=P.surface(),
                   edgecolor=P.ink(), zorder=5)
        ax.axvline(ph, color=P.muted(), lw=0.7, ls=":")
    ax.set_xlim(0, 1)
    charts.style_axes(ax, "frequency $p$ of $A_2$", "mean fitness $\\bar w$" if k == 0 else None)

ax = fig.add_subplot(gs[:, 3])
g = np.linspace(0.001, 0.999, 200)
PA, PB = np.meshgrid(g, g)
W = {"AB": 1.1, "Ab": 1.0, "aB": 1.0, "ab": 1.05}


def wbar(pa, pb):
    return pa * pb * W["AB"] + pa * (1 - pb) * W["Ab"] + (1 - pa) * pb * W["aB"] + (1 - pa) * (1 - pb) * W["ab"]


cs = ax.contourf(PA, PB, wbar(PA, PB), levels=12, cmap="Greys", alpha=0.45)
ax.contour(PA, PB, wbar(PA, PB), levels=12, colors=[P.muted()], linewidths=0.5)
starts = [(0.2, 0.9), (0.5, 0.75), (0.65, 0.6), (0.3, 0.55), (0.55, 0.3), (0.9, 0.2), (0.4, 0.15), (0.15, 0.4)]
for pa, pb in starts:
    xs, ys = [pa], [pb]
    for t in range(4000):
        w0 = wbar(pa, pb)
        ga = (pb * W["AB"] + (1 - pb) * W["Ab"] - pb * W["aB"] - (1 - pb) * W["ab"]) / w0
        gb = (pa * W["AB"] + (1 - pa) * W["aB"] - pa * W["Ab"] - (1 - pa) * W["ab"]) / w0
        pa, pb = pa + pa * (1 - pa) * ga, pb + pb * (1 - pb) * gb
        xs.append(pa)
        ys.append(pb)
    ax.plot(xs, ys, color=charts.line("rna"), lw=1.2)
    ax.scatter([xs[0]], [ys[0]], s=10, color=charts.line("rna"), zorder=4)
ax.scatter([1, 0], [1, 0], s=40, color=P.ink(), zorder=5, clip_on=False)
ax.text(0.97, 0.93, "AB peak", ha="right", fontsize=FT["tiny"], color=P.ink())
ax.text(0.03, 0.05, "ab peak", fontsize=FT["tiny"], color=P.ink())
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
charts.style_axes(ax, "frequency of $A$", "frequency of $B$", box=True)
charts.title(ax, "D  Two loci with epistasis")
