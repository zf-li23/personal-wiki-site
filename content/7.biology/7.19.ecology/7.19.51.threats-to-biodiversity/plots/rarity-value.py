"""Open-access exploitation when price rises with rarity (an anthropogenic Allee effect).

Dimensionless model: stock n = N / K with logistic growth and harvest proportional to effort e,
    dn/dt = n (1 - n) - e n,
effort grows when harvesting is profitable (open access, Gordon-Schaefer dynamics):
    de/dt = eta e (pi n^(1 - b) - gamma),
where revenue per unit effort is price x catch per effort, with price p(n) proportional to n^-b (b = 0: price
independent of abundance; b > 0: rarer goods fetch higher prices). gamma = cost per unit effort relative to
the maximal revenue, here 0.3; pi = 1; eta = 0.5.
A: stock against time from n = 1, e = 0.05 for b = 0 (bionomic equilibrium n* = gamma = 0.3), b = 0.6
(n* = gamma^(1/(1 - b)) = 0.05) and b = 1 (revenue per effort pi independent of n; if pi > gamma effort grows
without limit and the stock is driven to extinction).
B: the same trajectories in the (n, e) plane, with the nullclines of n (e = 1 - n, gray).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
gamma, eta = 0.3, 0.5


def rhs(b):
    def f(t, y):
        n, e = np.maximum(y, 1e-12)
        return [n * (1 - n) - e * n, eta * e * (n ** (1 - b) - gamma)]
    return f


fig, ax = bio.canvas(30.0, 10.5)
pa = C.axes_at(ax, (2.4, 1.6, 11.6, 7.2))
pb = C.axes_at(ax, (18.4, 1.6, 10.0, 7.2))
for b, tok in ((0.0, "dna"), (0.6, "enzyme"), (1.0, "negative")):
    sol = solve_ivp(rhs(b), (0, 150), [1.0, 0.05], max_step=0.1, rtol=1e-8, atol=1e-12)
    pa.plot(sol.t, sol.y[0], color=Q.line_color(tok), lw=1.6, label=f"price exponent b = {b}")
    pb.plot(sol.y[0], sol.y[1], color=Q.line_color(tok), lw=1.4)
pa.set_yscale("log")
pa.set_ylim(1e-4, 1.5)
pa.set_xlim(0, 150)
C.style_axes(pa, "time (units of 1/r)", "stock n = N / K (log scale)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.6, 10.1))
bio.label(ax, (2.4, 9.7), "Rarity value removes the economic brake", size="small", bold=True, ha="left")
nn = np.linspace(0, 1, 100)
pb.plot(nn, 1 - nn, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
pb.text(0.70, 0.12, "dn/dt = 0", fontsize=FS["tiny"], color=P.muted())
pb.set_xlim(0, 1.02)
pb.set_ylim(0, 1.6)
C.style_axes(pb, "stock n", "effort e")
bio.panel(ax, "B", (16.8, 10.1))
bio.label(ax, (18.4, 9.7), "Stock and effort", size="small", bold=True, ha="left")
