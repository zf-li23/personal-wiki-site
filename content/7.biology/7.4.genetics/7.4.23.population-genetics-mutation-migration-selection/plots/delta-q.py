"""Change in allele frequency per generation, Delta p, as a function of p, with the phase lines below
(arrows: direction of change; filled dots: stable equilibria; open dots: unstable). A: directional selection
(additive, s = 0.05): p increases at every frequency, fastest at p = 1/2. B: heterozygote advantage with the
fitnesses estimated for the sickle-cell locus in West Africa (w_AA = 0.88, w_AS = 1, w_SS = 0.14): a stable
interior equilibrium at q = s1/(s1 + s2) = 0.122 (only q < 0.3 shown; Delta q is negative beyond). C: heterozygote disadvantage (w = 1, 0.8, 1): an unstable
equilibrium at 1/2 separates two domains of attraction, and the allele that is initially more common goes to
fixation."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def dp(p, w11, w12, w22):
    q = 1 - p
    wb = p * p * w11 + 2 * p * q * w12 + q * q * w22
    return p * q * (p * (w11 - w12) + q * (w12 - w22)) / wb


cases = [("A  Directional (additive)", (1.05, 1.025, 1.0), [(0, False), (1, True)], "frequency $p$ of $A$"),
         ("B  Heterozygote advantage (HbS)", (0.14, 1.0, 0.88), [(0, False), (0.1224, True), (0.3, None)],
          "frequency $q$ of $S$ (axis to 0.3)"),
         ("C  Heterozygote disadvantage", (1.0, 0.8, 1.0), [(0, True), (0.5, False), (1, True)], "frequency $p$ of $A$")]
fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.9))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.2, top=0.88, wspace=0.32)
for ax, (title, w, eq, xl) in zip(axs, cases):
    xmax = eq[-1][0]
    p = np.linspace(0, xmax, 400)
    y = dp(p, *w)
    ax.plot(p, y, color=charts.line("dna"), lw=2)
    ax.axhline(0, color=P.muted(), lw=0.8)
    lo = y.min() if y.min() < 0 else -0.25 * y.max()
    hi = y.max() if y.max() > 0 else -0.25 * y.min()
    span = hi - lo
    yl = lo - 0.18 * span
    ax.set_ylim(yl - 0.06 * span, hi + 0.08 * span)
    ax.plot([0, xmax], [yl, yl], color=P.muted(), lw=0.8)
    pts = [e for e, _ in eq]
    for x0, x1 in zip(pts[:-1], pts[1:]):
        mid = (x0 + x1) / 2
        d = np.sign(dp(np.array([mid]), *w))[0]
        a0, a1 = (mid - 0.06 * xmax * d, mid + 0.06 * xmax * d)
        ax.annotate("", xy=(a1, yl), xytext=(a0, yl), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.0))
    for x0, stable in eq:
        if stable is None:
            continue
        ax.scatter([x0], [yl], s=36, zorder=4, facecolor=P.ink() if stable else P.surface(), edgecolor=P.ink(), lw=1.0)
    ax.set_xlim(-0.03 * xmax, 1.03 * xmax)
    charts.style_axes(ax, xl, "change per generation" if ax is axs[0] else None)
    charts.title(ax, title)
axs[1].text(0.128, axs[1].get_ylim()[0] + 0.02 * (axs[1].get_ylim()[1] - axs[1].get_ylim()[0]), "$\\hat q = 0.122$",
            fontsize=FT["tiny"], color=P.ink())
