"""Equilibrium biomass along a productivity gradient in a Lotka-Volterra food chain
(the exploitation ecosystems hypothesis of Oksanen et al. 1981).

dX1/dt = X1 [r (1 - X1/K) - a X2]
dXi/dt = Xi [e a X(i-1) - m - a X(i+1)],  i = 2, 3, 4  (X5 = 0)
with r = 1, a = 1, e = 0.5, m = 0.1. For each carrying capacity K the system is integrated from small
positive initial values to its (globally stable) equilibrium. A new level can persist once the level
below it can feed it: thresholds K = 0.2 (herbivores), 0.25 (carnivores), 0.75 (top carnivores).
A: equilibrium biomass of each level against K. In a chain of n levels the top level and every second
level below it increase with K, while the other levels stay constant: plants increase with
productivity in odd-numbered chains and are held fixed by herbivores in even-numbered ones.
B: a trophic cascade at K = 2: a three-level chain at equilibrium is invaded by a top carnivore at
t = 100, and the abundances of the levels below change in alternation.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)

r, a, e, m = 1.0, 1.0, 0.5, 0.1


def rhs(t, X, K):
    X = np.maximum(X, 0)
    d = np.zeros(4)
    d[0] = X[0] * (r * (1 - X[0] / K) - a * X[1])
    for i in (1, 2, 3):
        up = X[i + 1] if i < 3 else 0.0
        d[i] = X[i] * (e * a * X[i - 1] - m - a * up)
    return d


Ks = np.logspace(np.log10(0.1), np.log10(5), 70)
eq = []
for K in Ks:
    s = solve_ivp(rhs, (0, 4000), [K / 2, 0.01, 0.01, 0.01], args=(K,), rtol=1e-8, atol=1e-12, method="LSODA")
    eq.append(np.where(s.y[:, -1] > 1e-6, s.y[:, -1], 0.0))
eq = np.array(eq)
names = ["plants", "herbivores", "carnivores", "top carnivores"]
toks = ["plant", "dna", "rna", "negative"]
pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
for i in range(4):
    pa.semilogx(Ks, eq[:, i], color=Q.line_color(toks[i]), lw=1.8, label=names[i])
for kth, lab in [(0.2, "2 levels"), (0.25, "3"), (0.75, "4 levels")]:
    pa.axvline(kth, color=P.muted(), lw=0.7, ls=":")
pa.text(0.105, 1.9, "1", fontsize=FS["tiny"], color=P.ink())
pa.text(0.4, 1.9, "3 levels", fontsize=FS["tiny"], color=P.ink())
pa.text(1.6, 1.9, "4 levels", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0.1, 5)
pa.set_ylim(0, 2.0)
C.style_axes(pa, "carrying capacity of plants K (productivity)", "equilibrium biomass")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center left", bbox_to_anchor=(0, 0.6))
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Biomass staircases along a productivity gradient", size="small", bold=True, ha="left")

K = 2.0
s1 = solve_ivp(rhs, (0, 100), [1.0, 0.1, 0.1, 0.0], args=(K,), rtol=1e-8, atol=1e-12, t_eval=np.linspace(0, 100, 400))
x = s1.y[:, -1].copy()
x[3] = 0.01
s2 = solve_ivp(rhs, (100, 400), x, args=(K,), rtol=1e-8, atol=1e-12, t_eval=np.linspace(100, 400, 1200))
t = np.concatenate([s1.t, s2.t])
Y = np.concatenate([s1.y, s2.y], axis=1)
pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
for i in range(4):
    pb.plot(t, Y[i], color=Q.line_color(toks[i]), lw=1.6, label=names[i])
pb.axvline(100, color=P.muted(), lw=0.8, ls="--")
pb.text(103, 1.85, "top carnivore introduced", fontsize=FS["tiny"], color=P.ink())
pb.set_xlim(0, 400)
pb.set_ylim(0, 2.0)
C.style_axes(pb, "time", "biomass")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1, 0.9))
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), "A trophic cascade (K = 2)", size="small", bold=True, ha="left")
