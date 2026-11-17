"""The Rosenzweig-MacArthur model in dimensionless form (Section 26.1):
x' = x (1 - x/kappa) - x y / (1 + x),  y' = y (gamma x / (1 + x) - delta),
with gamma = 2, delta = 1, so the predator isocline is x* = delta / (gamma - delta) = 1 and the Hopf
point is kappa_H = 1 + 2 x* = 3.
A: kappa = 2.5: the predator isocline meets the descending limb of the humped prey isocline;
trajectories spiral into a stable focus. B: kappa = 5: it meets the rising limb; the equilibrium is
an unstable focus and trajectories from inside and outside approach a stable limit cycle.
C: a sigmoid (type III) functional response x^2 / (1 + x^2) instead: the prey isocline rises
steeply toward low prey density (rare prey escape predation), and an efficient predator (x* = 0.5) is held at a stable low equilibrium
even at kappa = 8.
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


def rhs(t, z, kap, q=1):
    x, y = z
    f = x**q / (1 + x**q)
    return [x * (1 - x / kap) - f * y, y * (g * f - d)]


fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.4))
for ax, kap, starts, lab in [(axes[0], 2.5, [(2.0, 0.2)], "A  κ = 2.5 < κ_H: stable focus"),
                             (axes[1], 5.0, [(1.1, 0.9), (4.5, 0.2)], "B  κ = 5 > κ_H: limit cycle")]:
    xx = np.linspace(0.001, kap, 300)
    ax.plot(xx, (1 + xx) * (1 - xx / kap), color=prey, ls=(0, (4, 2)), lw=1.2)
    ax.axvline(1.0, color=pred, ls=(0, (4, 2)), lw=1.2)
    ax.plot((kap - 1) / 2, (1 + (kap - 1) / 2) ** 2 / kap, "^", color=prey, ms=5)
    for k, z0 in enumerate(starts):
        s = solve_ivp(rhs, [0, 300], z0, args=(kap,), max_step=0.05, rtol=1e-9, atol=1e-11)
        ax.plot(s.y[0], s.y[1], color=P.ink() if k == 0 else P.muted(), lw=0.8)
    ystar = 2 * (1 - 1 / kap)
    ax.plot(1, ystar, "o", ms=6, mfc=P.ink() if kap < 3 else P.surface(), mec=P.ink())
    ax.set_xlim(0, kap * 1.02)
    ax.set_ylim(0, 2.6 if kap < 3 else 3.4)
    C.style_axes(ax, "Prey x", "Predator y")
    C.title(ax, lab)
axes[0].text(1.05, 2.45, "predator isocline", color=pred, fontsize=FS["tiny"])
axes[0].text(1.6, 0.75, "prey isocline\n(▲ = hump)", color=prey, fontsize=FS["tiny"])

ax = axes[2]
kap, gg, dd = 8.0, 3.0, 0.6
xs = np.sqrt(dd / (gg - dd))
xx = np.linspace(0.001, kap, 400)
ax.plot(xx, (1 + xx**2) / xx * (1 - xx / kap), color=prey, ls=(0, (4, 2)), lw=1.2)
ax.axvline(xs, color=pred, ls=(0, (4, 2)), lw=1.2)


def rhs3(t, z):
    x, y = z
    f = x**2 / (1 + x**2)
    return [x * (1 - x / kap) - f * y, y * (gg * f - dd)]


s = solve_ivp(rhs3, [0, 300], [6, 0.3], max_step=0.05, rtol=1e-9)
ax.plot(s.y[0], s.y[1], color=P.ink(), lw=0.8)
ax.plot(xs, (1 + xs**2) / xs * (1 - xs / kap), "o", ms=6, color=P.ink())
ax.set_ylim(0, 5)
ax.set_xlim(0, kap)
C.style_axes(ax, "Prey x", "Predator y")
C.title(ax, "C  Type III response, κ = 8: stable")
fig.tight_layout()
