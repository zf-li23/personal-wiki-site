"""Lotka-Volterra competition among more than two species.

A: six species on a resource axis with Gaussian utilization curves of equal width w, peaks d = 2 w
apart, so that the competition coefficients are a_ij = exp(-(i - j)^2 d^2 / (4 w^2)) (MacArthur and
Levins 1967; see 7.19.23), and carrying capacities 100, 90, 110, 95, 105 and 100; r = 1 for all.
The matrix is symmetric and positive definite, and with this spacing the equilibrium
(88.9, 26.1, 82.8, 40.5, 60.2, 77.1) is feasible, hence globally stable: from unequal starts all six
species converge to it. (With d = 1.2 w the same carrying capacities give no feasible six-species
equilibrium, and species 2 and 4 are excluded.) B: three species with cyclic, non-transitive
competition (May and Leonard 1975): a_12 = a_23 = a_31 = 0.8 and a_13 = a_21 = a_32 = 1.3, r = 1, K = 1.
Since 0.8 + 1.3 > 2 the interior equilibrium is unstable and the system approaches a heteroclinic cycle:
each species in turn nearly takes over, and the dominance periods lengthen (log scale).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)
toks = ["dna", "rna", "positive", "enzyme", "protein", "negative"]

n = 6
i = np.arange(n)
A = np.exp(-((i[:, None] - i[None, :]) ** 2) * 2.0 ** 2 / 4)
K = np.array([100, 90, 110, 95, 105, 100], float)
f = lambda t, N: N * (K - A @ N) / K
s = solve_ivp(f, (0, 300), [20, 1, 5, 40, 2, 10], t_eval=np.linspace(0, 300, 600), rtol=1e-8)
pa = C.axes_at(ax, (2.4, 1.8, 11.5, 8.6))
for k in range(n):
    pa.plot(s.t, s.y[k], color=Q.line_color(toks[k]), lw=1.5, label=f"species {k + 1}")
pa.set_xlim(0, 300)
pa.set_ylim(0, 130)
C.style_axes(pa, "time", "density")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", ncol=3)
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Six species on a resource axis (d/w = 2)", size="small", bold=True, ha="left")

al, be = 0.8, 1.3
M = np.array([[1, al, be], [be, 1, al], [al, be, 1]])
g = lambda t, N: N * (1 - M @ N)
s = solve_ivp(g, (0, 1500), [0.5, 0.3, 0.2], t_eval=np.linspace(0, 1500, 6000), rtol=1e-11, atol=1e-14,
              method="LSODA")
pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
for k in range(3):
    pb.plot(s.t, np.log10(np.maximum(s.y[k], 1e-30)), color=Q.line_color(toks[k]), lw=1.3, label=f"species {k + 1}")
pb.set_xlim(0, 1500)
pb.set_ylim(-12, 0.5)
C.style_axes(pb, "time", "log10 density")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left", ncol=3)
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), "Non-transitive competition: May-Leonard cycle", size="small", bold=True, ha="left")
