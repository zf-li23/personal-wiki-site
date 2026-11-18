"""A closed nutrient cycle: dissolved nutrient N, producers P and detritus with decomposers D.

dN/dt = d D - mu N P / (k + N),  dP/dt = mu N P / (k + N) - m P,  dD/dt = m P - d D,
mu = 1, k = 0.5, m = 0.2 (producer mortality), d = 0.1 (decomposition rate), all per unit time;
the total nutrient T = N + P + D is conserved. Equilibrium: N* = k m / (mu - m), D* = m P*/d,
P* = (T - N*) / (1 + m/d).
A: with T = 10, a disturbance at t = 100 converts 80 % of producer biomass into dissolved nutrient
(a fire releasing nutrients in ash); producers regrow on the released nutrient, detritus first falls
and then recovers, and the system returns to the same equilibrium (negative feedback through nutrient
limitation of producers). B: equilibrium partition of the nutrient capital against the total T: the
dissolved pool is fixed by the producers' requirement N*, and all additional nutrient is held in
living and dead biomass.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)

mu, k, m, d = 1.0, 0.5, 0.2, 0.1


def rhs(t, y):
    N, Pp, D = y
    up = mu * N * Pp / (k + N)
    return [d * D - up, up - m * Pp, m * Pp - d * D]


T = 10.0
Ns = k * m / (mu - m)
Ps = (T - Ns) / (1 + m / d)
y0 = [Ns, Ps, m * Ps / d]
s1 = solve_ivp(rhs, (0, 100), y0, t_eval=np.linspace(0, 100, 101), rtol=1e-9)
y = s1.y[:, -1].copy()
y[0] += 0.8 * y[1]
y[1] *= 0.2
s2 = solve_ivp(rhs, (100, 300), y, t_eval=np.linspace(100, 300, 801), rtol=1e-9)
t = np.concatenate([s1.t, s2.t])
Y = np.concatenate([s1.y, s2.y], axis=1)
pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
for i, (lab, tok) in enumerate([("dissolved nutrient N", "metabolite"), ("producers P", "plant"),
                                 ("detritus and decomposers D", "rna")]):
    pa.plot(t, Y[i], color=Q.line_color(tok), lw=1.8, label=lab)
pa.plot(t, Y.sum(0), color=P.muted(), lw=1.0, ls="--", label="total (conserved)")
pa.axvline(100, color=P.muted(), lw=0.8, ls=":")
pa.text(102, 9.3, "fire: 80 % of P to N", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, 300)
pa.set_ylim(0, 10.8)
C.style_axes(pa, "time", "nutrient content")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Return to equilibrium after a disturbance", size="small", bold=True, ha="left")

Tg = np.linspace(0.2, 20, 100)
Pg = np.maximum(Tg - Ns, 0) / (1 + m / d)
pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
pb.plot(Tg, np.minimum(Tg, Ns), color=Q.line_color("metabolite"), lw=1.8, label="N*")
pb.plot(Tg, Pg, color=Q.line_color("plant"), lw=1.8, label="P*")
pb.plot(Tg, m * Pg / d, color=Q.line_color("rna"), lw=1.8, label="D*")
pb.set_xlim(0, 20)
pb.set_ylim(0, 14)
C.style_axes(pb, "total nutrient in the system T", "equilibrium content")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), "Where the nutrient capital is held", size="small", bold=True, ha="left")
