"""The paradox of enrichment in the Rosenzweig-MacArthur model (Section 26.2), with gamma = 2,
delta = 1 (x* = 1, kappa_H = 3).
A: bifurcation diagram against the prey carrying capacity kappa: equilibrium prey density (constant)
and predator density (rising), stable (solid) or unstable (dashed); for kappa > 3 the maximum and
minimum prey densities on the limit cycle. B: the minimum densities of prey and predator on the
cycle, log scale: they fall roughly exponentially with kappa. C: time series for kappa = 2.5
(damped) and kappa = 8 (large cycles with long troughs near zero).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
g, d = 2.0, 1.0
prey, pred = C.line("dna"), C.line("negative")


def rhs(t, z, kap):
    x, y = z
    f = x / (1 + x)
    return [x * (1 - x / kap) - f * y, y * (g * f - d)]


kaps = np.linspace(1.2, 10, 60)
xmax, xmin, ymax, ymin = [], [], [], []
for kap in kaps:
    s = solve_ivp(rhs, [0, 600], [1.2, 0.8 * 2 * (1 - 1 / kap) + 0.05], args=(kap,), method="LSODA",
                  rtol=1e-9, atol=1e-14, dense_output=True)
    t = np.linspace(400, 600, 8000)
    x, y = s.sol(t)
    xmax.append(x.max()); xmin.append(x.min()); ymax.append(y.max()); ymin.append(y.min())

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3))
ax = axes[0]
st = kaps <= 3
ax.plot(kaps[st], np.ones(st.sum()), color=prey, lw=1.4, label="prey x*")
ax.plot(kaps[~st], np.ones((~st).sum()), color=prey, lw=1.0, ls=(0, (3, 2)))
ax.plot(kaps[st], 2 * (1 - 1 / kaps[st]), color=pred, lw=1.4, label="predator y*")
ax.plot(kaps[~st], 2 * (1 - 1 / kaps[~st]), color=pred, lw=1.0, ls=(0, (3, 2)))
ax.fill_between(kaps[~st], np.array(xmin)[~st], np.array(xmax)[~st], color=P.light("dna"), lw=0, label="prey range on cycle")
ax.axvline(3, color=P.muted(), lw=0.8)
ax.text(3.15, 6.0, "Hopf\nκ_H = 3", fontsize=FS["tiny"], color=P.muted())
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper left")
C.style_axes(ax, "Prey carrying capacity κ", "Density")
C.title(ax, "A  Bifurcation diagram")

ax = axes[1]
ax.semilogy(kaps[~st], np.array(xmin)[~st], color=prey, lw=1.4, label="prey minimum")
ax.semilogy(kaps[~st], np.array(ymin)[~st], color=pred, lw=1.4, label="predator minimum")
ax.legend(fontsize=FS["tiny"], frameon=False)
C.style_axes(ax, "Prey carrying capacity κ", "Minimum density on cycle")
C.title(ax, "B  Troughs deepen with enrichment")

ax = axes[2]
for kap, ls in [(2.5, (0, (2, 1.5))), (8.0, "-")]:
    s = solve_ivp(rhs, [0, 120], [1.5, 0.5], args=(kap,), method="LSODA", rtol=1e-9, atol=1e-14, dense_output=True)
    t = np.linspace(0, 120, 3000)
    x, y = s.sol(t)
    ax.plot(t, x, color=prey, ls=ls, lw=1.2, label=f"prey, κ = {kap:g}")
    ax.plot(t, y, color=pred, ls=ls, lw=1.2, label=f"predator, κ = {kap:g}")
ax.legend(fontsize=FS["tiny"], frameon=False, ncol=2, loc="upper right")
ax.set_ylim(0, 11.5)
C.style_axes(ax, "Dimensionless time", "Density")
C.title(ax, "C  Damped versus large cycles")
fig.tight_layout()
