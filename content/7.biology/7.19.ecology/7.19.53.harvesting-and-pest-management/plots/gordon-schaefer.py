"""Bioeconomics of a logistic fishery (Section 53.2), dimensionless.

Stock x = N/K, effort e = qE/r, money in units of p r K. Sustainable revenue e(1 - e), cost x_inf e,
where x_inf = c/(p q K) is the stock at which a unit of effort just pays for itself.
A: revenue and cost against effort, x_inf = 0.3: MEY at e = (1 - x_inf)/2 = 0.35, MSY at 0.5,
open-access equilibrium at e = 1 - x_inf = 0.7 (twice the MEY effort).
B, C: the open-access (Smith) dynamics dx/dtau = x(1 - x) - e x, de/dtau = kappa e (x - x_inf),
kappa = 1.5, started from an unexploited stock with little effort: damped boom-and-bust oscillations.
D: optimal steady stock under discounting at rate delta (modified golden rule, Theorem 53.2.1):
(1 - 2x) + x_inf (1 - x)/(x - x_inf) = delta / r, solved for x in (x_inf, 1).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
cr, cc, cf, ce = C.line("positive"), C.line("negative"), C.line("plant"), C.line("dna")
xi = 0.3

fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.6))

ax = axes[0, 0]
e = np.linspace(0, 1, 400)
ax.plot(e, e * (1 - e), color=cr, lw=2.2, label="sustainable revenue")
ax.plot(e, xi * e, color=cc, lw=2, label="total cost (x∞ = 0.3)")
ax.fill_between(e, xi * e, e * (1 - e), where=e * (1 - e) > xi * e, color=P.mix(cr, P.surface(), 0.8))
for ev, lab, col in (((1 - xi) / 2, "MEY", cr), (0.5, "MSY", cf), (1 - xi, "open\naccess", cc)):
    ax.axvline(ev, color=col, lw=0.8, ls=(0, (3, 2)))
    ax.text(ev + 0.01, 0.295, lab, color=col, fontsize=FS["tiny"], va="top")
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.30)
C.style_axes(ax, "effort e = qE / r", "money (units of prK)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "A  Gordon–Schaefer: rent, MEY and open access")

kap = 1.5
rhs = lambda t, y: [y[0] * (1 - y[0]) - y[1] * y[0], kap * y[1] * (y[0] - xi)]
sol = solve_ivp(rhs, (0, 120), [1.0, 0.02], max_step=0.05)

ax = axes[0, 1]
xx = np.linspace(0, 1, 200)
ax.plot(xx, 1 - xx, color=cf, lw=1.2, ls=(0, (3, 2)), label="stock nullcline e = 1 − x")
ax.axvline(xi, color=ce, lw=1.2, ls=(0, (3, 2)), label="effort nullcline x = x∞")
ax.plot(sol.y[0], sol.y[1], color=P.ink(), lw=1.3)
ax.plot([xi], [1 - xi], "o", color=cc, ms=7, zorder=5)
ax.plot([1.0], [0.02], "s", color=P.muted(), ms=5)
ax.set_xlim(0, 1.02)
ax.set_ylim(0, 1.3)
C.style_axes(ax, "stock x", "effort e")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "B  Open access: phase plane")

ax = axes[1, 0]
ax.plot(sol.t, sol.y[0], color=cf, lw=2, label="stock x")
ax.plot(sol.t, sol.y[1], color=ce, lw=2, label="effort e")
ax.plot(sol.t, sol.y[0] * sol.y[1] / 0.25, color=cr, lw=1.2, label="catch / MSY")
ax.set_xlim(0, 120)
C.style_axes(ax, "time τ = rt", "")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", ncol=3)
C.title(ax, "C  Boom and bust of an open-access fishery")

ax = axes[1, 1]
d = np.linspace(0, 3, 300)
for xinf, col in ((0.0, cc), (0.1, C.line("rna")), (0.3, ce), (0.5, C.line("protein"))):
    xs = []
    for dd in d:
        if xinf == 0:
            xs.append(max((1 - dd) / 2, 0))
            continue
        g = lambda x: (1 - 2 * x) + xinf * (1 - x) / (x - xinf) - dd
        xs.append(brentq(g, xinf + 1e-9, 1 - 1e-12))
    ax.plot(d, xs, color=col, lw=2, label=f"x∞ = {xinf:g}")
    ax.axhline(xinf, color=col, lw=0.6, ls=":")
ax.set_xlim(0, 3)
ax.set_ylim(0, 0.8)
C.style_axes(ax, "discount rate relative to growth rate, δ / r", "optimal stock x* = N* / K")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "D  Discounting lowers the optimal stock")
fig.tight_layout()
