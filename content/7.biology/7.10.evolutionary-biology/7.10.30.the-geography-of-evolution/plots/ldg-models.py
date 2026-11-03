"""Three models of species accumulation that could produce the latitudinal diversity gradient
(Section 30.7.1), after the scheme of Futuyma and Kirkpatrick (2017), Fig. 18.19. Each region starts with
one lineage and grows logistically, dN/dt = D N (1 - N/K), D the net diversification rate and K the
number of species the region can hold. A: the tropics hold more species (K = 400 vs 120) with the same
D = 0.15 per Myr. B: the tropics diversify faster (D = 0.12 vs 0.06 per Myr) and neither region has
reached its limit (K = 2000). C: the same D = 0.08 per Myr and no limit, but diversification began
60 Myr ago in the tropics and only 25 Myr ago in the temperate zone (time and area). The dotted line
marks the present."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
t = np.linspace(0, 70, 701)


def logistic(D, K, t0):
    out = np.zeros_like(t)
    m = t >= t0
    tt = t[m] - t0
    out[m] = K / (1 + (K - 1) * np.exp(-D * tt))
    return out


cases = [("A  Different limits K", (0.15, 400, 0), (0.15, 120, 0)),
         ("B  Different rates D", (0.12, 2000, 0), (0.06, 2000, 0)),
         ("C  Different start times", (0.08, 1e7, 10), (0.08, 1e7, 45))]
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.2))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.18, top=0.86, wspace=0.32)
for ax, (title, trop, temp) in zip(axes, cases):
    ax.plot(t, logistic(*trop), color=charts.line("plant"), lw=2, label="tropical")
    ax.plot(t, logistic(*temp), color=charts.line("dna"), lw=2, label="temperate")
    ax.axvline(70, color=P.muted(), lw=0.8, ls=":")
    ax.set_xticks([0, 20, 40, 60])
    ax.set_xticklabels(["70", "50", "30", "10"])
    charts.style_axes(ax, "time (Myr ago)", "species richness" if ax is axes[0] else None)
    charts.title(ax, title)
axes[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
