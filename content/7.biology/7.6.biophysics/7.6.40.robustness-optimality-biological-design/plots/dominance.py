# Robustness of flux to enzyme levels in a linear pathway (Kacser and Burns 1973, 1981).
# A linear chain S0 -> X1 -> ... -> Xn-1 -> Sn of n reversible first-order steps with fixed end
# concentrations has a steady flux of the form J = Delta / sum_i r_i, where Delta is the thermodynamic
# driving force and the "resistance" r_i of step i is proportional to 1/e_i (enzyme amount e_i) times
# the product of the equilibrium constants before it; hence C_i = r_i / sum_j r_j.
# A: flux against the activity of one enzyme (relative to wild type) when it carries a fraction c of the
# total resistance: J/J_wt = 1/(1 + c (1/f - 1)). With many enzymes each has small control, and halving
# one (a heterozygote for a null allele) barely changes the flux: dominance of the wild type.
# B: flux control coefficients C_i = d ln J / d ln e_i of random pathways with 5, 10 and 20 enzymes (bars,
# one pathway each, rates log-uniform over two decades): positive, summing to 1 (summation theorem), so
# that on average each is 1/n.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axs[0]
f = np.linspace(0.01, 2, 300)
for c, tok in ((1.0, "negative"), (0.3, "atp"), (0.1, "enzyme"), (0.03, "dna")):
    ax.plot(f, 1 / (1 + c * (1 / f - 1)), color=charts.line(tok), lw=1.8, label=f"control coefficient {c}")
ax.axvline(0.5, color=P.muted(), lw=0.7, ls=":")
ax.axvline(1.0, color=P.muted(), lw=0.7, ls=":")
ax.text(0.52, 0.05, "heterozygote\n(half activity)", fontsize=7.5, color=P.ink())
ax.set_ylim(0, 1.3)
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "activity of one enzyme / wild type", "pathway flux / wild type")
charts.title(ax, "A   Flux is insensitive to most enzymes")

ax = axs[1]
x0 = 0
for n, tok in ((5, "rna"), (10, "enzyme"), (20, "dna")):
    k = 10 ** rng.uniform(-1, 1, n)
    K = 10 ** rng.uniform(-0.5, 0.5, n)
    # resistance of step i: 1/(e_i k_i) times the product of equilibrium constants before it
    r = 1 / k * np.cumprod(np.r_[1.0, 1 / K[:-1]])
    C = r / r.sum()  # C_i = r_i / sum r for this chain
    ax.bar(x0 + np.arange(n), C, color=P.fill(tok), edgecolor=P.edge(tok), width=0.8,
           label=f"$n$ = {n}: sum = {C.sum():.2f}, largest {C.max():.2f}")
    x0 += n + 3
ax.legend(fontsize=7.5, frameon=False)
ax.set_xticks([])
charts.style_axes(ax, "enzymes of three random pathways", "flux control coefficient")
charts.title(ax, "B   The summation theorem")
fig.tight_layout()
