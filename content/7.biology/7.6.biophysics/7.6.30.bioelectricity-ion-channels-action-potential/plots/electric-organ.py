"""Electric organs as batteries of electrocytes. A: a column of electrocytes, each a flat cell
innervated on one face only: at rest both faces are at the resting potential and their potentials
cancel; when the innervated face fires an action potential, the cell becomes a battery of about
0.15 V, and cells stacked in series add their voltages. B: power delivered to the water by an organ of
N_tot = 2 x 10^5 electrocytes (emf 0.15 V and internal resistance 5 Ohm each) arranged as N in series
and N_tot/N columns in parallel, for a fresh-water load (1 kOhm, high resistance) and a sea-water load
(2 Ohm): the power is maximal when the internal resistance of the organ matches the load,
N* = (N_tot R_L / r)^(1/2): about 6000 cells in series (as in the electric eel Electrophorus) for fresh
water, a few hundred (as in the marine ray Torpedo) for sea water. Illustrative parameters."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.3), gridspec_kw=dict(width_ratios=[1.0, 1.1]))
fig.subplots_adjust(wspace=0.3, left=0.02, right=0.98, bottom=0.17, top=0.87)

ax = axs[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect("equal")
ax.axis("off")
for k in range(4):
    x0 = 1.0 + 2.0 * k
    ax.add_patch(FancyBboxPatch((x0, 1.6), 0.9, 2.8, boxstyle="round,pad=0.05", facecolor=P.fill("muscle"),
                                edgecolor=P.edge("muscle"), lw=1))
    ax.plot([x0 + 0.95, x0 + 1.4], [3.0, 3.0], color=P.edge("neuron"), lw=1.3)
    ax.plot([x0 + 1.4, x0 + 1.4], [3.0, 5.0], color=P.edge("neuron"), lw=1.3)
    ax.text(x0 + 0.05, 1.25, "+", fontsize=FT["small"], color=P.ink(), ha="center")
    ax.text(x0 + 0.85, 1.25, "−", fontsize=FT["small"], color=P.ink(), ha="center")
ax.plot([2.4, 8.4], [5.0, 5.0], color=P.edge("neuron"), lw=1.3)
ax.text(5.4, 5.3, "nerve (innervated posterior faces)", fontsize=FT["tiny"], color=P.ink(), ha="center")
ax.annotate("", (9.6, 0.6), (0.4, 0.6), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1))
ax.text(5.0, 0.15, r"discharge: $V = N\varepsilon \approx N \times 0.15$ V", fontsize=FT["tiny"], color=P.ink(),
        ha="center")
charts.title(ax, "A  Electrocytes in series")

ax = axs[1]
Ntot, eps, r = 2e5, 0.15, 5.0
N = np.logspace(1, 5, 400)
for RL, tok, lab in [(1000.0, "dna", r"fresh water, $R_L = 1$ k$\Omega$"), (2.0, "blood", r"sea water, $R_L = 2\,\Omega$")]:
    Rint = N * r / (Ntot / N)
    Pw = (N * eps) ** 2 * RL / (RL + Rint) ** 2
    ax.loglog(N, Pw, color=charts.line(tok), lw=1.7, label=lab)
    Ns = np.sqrt(Ntot * RL / r)
    ax.plot([Ns], [(Ns * eps) ** 2 / (4 * RL)], "o", ms=5, color=charts.line(tok))
    ax.annotate(f"N* = {Ns:.0f}", (Ns, (Ns * eps) ** 2 / (4 * RL)), xytext=(6, 4), textcoords="offset points",
                fontsize=FT["tiny"], color=P.ink())
ax.set_ylim(1, 3e4)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower center")
charts.style_axes(ax, "cells in series $N$", "power into the load / W")
charts.title(ax, "B  Impedance matching")
