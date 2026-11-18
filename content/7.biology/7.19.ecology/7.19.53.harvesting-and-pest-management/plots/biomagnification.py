"""Biomagnification of persistent chemicals (Section 53.3.4).

A: DDT residues (DDT + DDD + DDE, ppm wet weight, whole organism) in a Long Island estuary,
data of Woodwell, Wurster and Isaacson (1967) as tabulated by Odum and Barrett (2005), Table 5-3.
B: steady states of the food-chain model dC_i/dt = alpha I C_{i-1} - (k_e + g) C_i with growth
g = eps I (gross growth efficiency eps = 0.1), so that BMF = alpha / (eps + k_e / I)
(Proposition 53.3.3); level 1 is set by bioconcentration from water, C_1 = 1 (relative units).
Three chemicals: persistent and lipophilic (alpha = 0.8, k_e/I = 0.01), partly metabolized
(alpha = 0.5, k_e/I = 0.2) and rapidly excreted (alpha = 0.3, k_e/I = 0.8).
C: dynamics of a four-level chain for the persistent chemical: uptake from water from year 0,
a ban in year 15 after which the water concentration declines with a half-life of 3 years;
rate constants k_e + g fall with body size up the chain (4, 2, 0.8, 0.25 per year).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT

data = [("water", 0.00005), ("plankton", 0.04), ("silverside minnow", 0.23),
        ("sheepshead minnow", 0.94), ("pickerel", 1.33), ("needlefish", 2.07),
        ("heron", 3.57), ("tern", 3.91), ("herring gull", 6.00), ("osprey (egg)", 13.8),
        ("merganser", 22.8), ("cormorant", 26.4)]

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2), gridspec_kw={"width_ratios": [1.15, 1, 1.1]})
ax = axes[0]
names = [d[0] for d in data]
vals = [d[1] for d in data]
groups = [C.line("neutral")] + [C.line("plant")] + [C.line("channel")] * 4 + [C.line("rna")] * 6
y = np.arange(len(data))
ax.barh(y, vals, color=[P.mix(g, P.surface(), 0.35) for g in groups], edgecolor=groups, height=0.7)
ax.set_xscale("log")
ax.set_yticks(y, names)
ax.invert_yaxis()
ax.set_xlim(1e-5, 100)
for yi, v in zip(y, vals):
    ax.text(v * 1.3, yi, f"{v:.5f}" if v < 0.001 else f"{v:g}", va="center", fontsize=FS["tiny"], color=P.ink())
C.style_axes(ax, "DDT residues (ppm)", None)
C.title(ax, "A  DDT in an estuarine food web (1967)")

ax = axes[1]
lev = np.arange(1, 6)
for alpha, ki, col, lab in ((0.8, 0.01, C.line("negative"), "persistent, lipophilic"),
                            (0.5, 0.2, C.line("rna"), "partly metabolized"),
                            (0.3, 0.8, C.line("dna"), "rapidly excreted")):
    bmf = alpha / (0.1 + ki)
    ax.plot(lev, bmf ** (lev - 1), "o-", color=col, lw=2, ms=5, label=f"{lab} (BMF = {bmf:.2g})")
ax.set_yscale("log")
ax.set_xticks(lev)
C.style_axes(ax, "trophic level", "concentration relative to level 1")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "B  Steady states of the chain model")

ax = axes[2]
kk = np.array([4.0, 2.0, 0.8, 0.25])
alpha, eps, kI = 0.8, 0.1, 0.01
Ifeed = kk / (eps + kI)
lam = np.log(2) / 3


def cw(t):
    return 1.0 if t < 15 else np.exp(-lam * (t - 15))


def rhs(t, c):
    up = np.concatenate(([kk[0] * cw(t)], alpha * Ifeed[1:] * c[:-1]))
    return up - kk * c


sol = solve_ivp(rhs, (0, 45), np.zeros(4), max_step=0.02)
cols = [C.line("plant"), C.line("channel"), C.line("enzyme"), C.line("rna")]
labs = ["level 1 (plankton)", "level 2", "level 3", "level 4 (top predator)"]
for i in range(4):
    ax.plot(sol.t, sol.y[i], color=cols[i], lw=2, label=labs[i])
ax.axvline(15, color=P.muted(), lw=0.7, ls=":")
ax.text(15.5, 600, "ban", color=P.muted(), fontsize=FS["tiny"])
ax.set_yscale("log")
ax.set_ylim(0.5, 1000)
ax.set_xlim(0, 45)
C.style_axes(ax, "year", "concentration (relative)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "C  Slow rise and slow recovery at the top")
fig.tight_layout()
