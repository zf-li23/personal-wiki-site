"""Reactions in compartments. A bimolecular reaction A + B -> C runs in a cell in which a compartment
(a condensate or organelle) occupies the volume fraction phi and concentrates both reactants by the
partition coefficient K, with the total amounts fixed. A: rate relative to the well-mixed cell,
r/r0 = [(1 - phi) + phi K^2] / (1 - phi + phi K)^2, against phi for K = 10, 100 and 1000: the
enhancement peaks near phi = 1/K at about K/4. B: when only A is concentrated (K_A = 100) the rate
does not change at all for K_B = 1; it rises with the partitioning of the second reactant and falls
below 1 if B is excluded (K_B < 1)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(7.6, 3.1))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.98, bottom=0.17, top=0.87)

phi = np.logspace(-5, 0, 400)
ax = axs[0]
for K, tok in [(10, "dna"), (100, "bacterium"), (1000, "blood")]:
    r = ((1 - phi) + phi * K ** 2) / (1 - phi + phi * K) ** 2
    ax.loglog(phi, r, color=charts.line(tok), lw=1.6, label=f"K = {K}")
    ax.plot([1 / K], [((1 - 1 / K) + K) / (2 - 1 / K) ** 2], "o", ms=3.5, color=charts.line(tok))
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"compartment volume fraction $\phi$", r"rate enhancement $r/r_0$")
charts.title(ax, "A  Both reactants concentrated")

ax = axs[1]
KA = 100
for KB, tok in [(0.1, "neutral"), (1, "dna"), (10, "bacterium"), (100, "blood")]:
    r = (1 - phi + phi * KA * KB) / ((1 - phi + phi * KA) * (1 - phi + phi * KB))
    ax.loglog(phi, r, color=charts.line(tok), lw=1.6, label=rf"$K_B = {KB:g}$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"compartment volume fraction $\phi$", r"$r/r_0$")
charts.title(ax, r"B  $K_A = 100$")
