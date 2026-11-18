"""Land equivalent ratio (LER) of intercrops from competition models (Section 54.1.4).

A: LER of the Lotka-Volterra competition equilibrium with equal carrying capacities (kappa = K2/K1 = 1):
LER = N1*/K1 + N2*/K2 = 1 + (1 - a12)(1 - a21)/(1 - a12 a21) where both species coexist stably
(a12, a21 < 1, Proposition 54.1.1), and 1 where one species excludes the other.
Negative coefficients represent facilitation (for example nitrogen transfer from a legume).
B: replacement series (de Wit) with hyperbolic yield-density responses,
Y_i = w N_i / (1 + b (N_i + a N_j)), total density D = 100, b = 0.05, sown proportion p of crop 1;
relative yields RY_i = Y_i(p) / Y_i(monoculture) and their sum (the LER at that proportion),
for a = 0.4 (partial niche separation) and a = 1 (identical resource use).
C: symmetric case of A, LER = 2 / (1 + a), against the competition coefficient.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT

fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.0), gridspec_kw={"width_ratios": [1.15, 1, 1]})

ax = axes[0]
a = np.linspace(-0.4, 1.5, 381)
A12, A21 = np.meshgrid(a, a)
coex = (A12 < 1) & (A21 < 1)
den = np.where(coex, 1 - A12 * A21, 1.0)
L = np.where(coex, 1 + (1 - A12) * (1 - A21) / den, 1.0)
cf = ax.contourf(A12, A21, L, levels=np.linspace(1, 3.4, 13), cmap=LinearSegmentedColormap.from_list("ler", [P.surface(), P.fill("plant"), P.edge("plant")]))
cs = ax.contour(A12, A21, L, levels=[1.1, 1.2, 1.4, 1.6, 2.0], colors=[P.ink()], linewidths=0.6)
ax.clabel(cs, fmt="%.1f", fontsize=FS["tiny"])
ax.plot([1, 1], [-0.4, 1], color=P.ink(), lw=1)
ax.plot([-0.4, 1], [1, 1], color=P.ink(), lw=1)
ax.axhline(0, color=P.muted(), lw=0.5, ls=":")
ax.axvline(0, color=P.muted(), lw=0.5, ls=":")
ax.text(0.25, 0.55, "stable\ncoexistence:\nLER > 1", fontsize=FS["tiny"], color=P.ink(), ha="center")
ax.text(1.25, 1.25, "one species\nexcluded:\nLER = 1", fontsize=FS["tiny"], color=P.ink(), ha="center")
ax.text(-0.35, -0.33, "facilitation", fontsize=FS["tiny"], color=P.ink())
cb = fig.colorbar(cf, ax=ax, fraction=0.05, pad=0.03)
cb.ax.tick_params(labelsize=FS["tiny"], colors=P.muted(), labelcolor=P.ink())
cb.set_label("LER", fontsize=FS["small"], color=P.ink())
C.style_axes(ax, "effect of crop 2 on crop 1, α12", "effect of crop 1 on crop 2, α21", box=True)
C.title(ax, "A  LER of the competition equilibrium")

ax = axes[1]
D, b, w = 100.0, 0.05, 1.0
p = np.linspace(0, 1, 201)
for alpha, ls in ((0.4, "-"), (1.0, (0, (4, 2)))):
    n1, n2 = p * D, (1 - p) * D
    mono = w * D / (1 + b * D)
    ry1 = w * n1 / (1 + b * (n1 + alpha * n2)) / mono
    ry2 = w * n2 / (1 + b * (n2 + alpha * n1)) / mono
    ax.plot(p, ry1, color=C.line("plant"), lw=1.6, ls=ls)
    ax.plot(p, ry2, color=C.line("lipid_head"), lw=1.6, ls=ls)
    ax.plot(p, ry1 + ry2, color=P.ink(), lw=2, ls=ls, label=f"α = {alpha:g}: total (LER)")
ax.text(0.97, 0.80, "crop 1", color=C.line("plant"), fontsize=FS["tiny"], ha="right")
ax.text(0.03, 0.80, "crop 2", color=C.line("lipid_head"), fontsize=FS["tiny"])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.5)
C.style_axes(ax, "proportion of crop 1 sown, p", "relative yield")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper center")
C.title(ax, "B  Replacement series")

ax = axes[2]
aa = np.linspace(-0.4, 1, 200)
ax.plot(aa, 2 / (1 + aa), color=C.line("plant"), lw=2.2)
ax.axhline(1, color=P.muted(), lw=0.7, ls=":")
ax.axhspan(1.1, 1.3, color=P.mix(C.line("highlight"), P.surface(), 0.7))
ax.text(0.98, 1.31, "typical field LER", fontsize=FS["tiny"], color=P.ink(), ha="right", va="bottom")
ax.set_xlim(-0.4, 1)
ax.set_ylim(0.8, 3.4)
C.style_axes(ax, "competition coefficient α (symmetric)", "LER = 2 / (1 + α)")
C.title(ax, "C  Overyielding needs α < 1")
fig.tight_layout()
