"""Habitat destruction and the extinction debt in a competition-colonization hierarchy (Tilman et al. 1994).

Ten species ranked by competitive ability (species 1 best). Species i occupies a fraction p_i of all sites
and obeys dp_i/dt = c_i p_i (1 - D - p_1 - ... - p_i) - m p_i - p_i (c_1 p_1 + ... + c_{i-1} p_{i-1}):
it colonizes sites that are neither destroyed nor held by a better competitor, is displaced by better
competitors, and dies at rate m = 0.05 per year. Colonization rates c_i = m / (1 - q)^(2i - 1) with q = 0.2
give the geometric equilibrium abundances p_i* = q (1 - q)^(i - 1) before destruction: the best competitor
is the most abundant but the poorest colonizer. A: abundances after a fraction D = 0.25 of the sites is
destroyed at t = 0 (integrated with scipy solve_ivp); species 1, the dominant competitor, declines slowly
to extinction over centuries (the extinction debt) although it was the most abundant species, and
species 2 benefits. B: number of species eventually lost and the time species 1 needs to fall below 1 %
of its initial abundance, against D.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
n, q, m = 10, 0.2, 0.05
i = np.arange(1, n + 1)
c = m / (1 - q) ** (2 * i - 1)
p0 = q * (1 - q) ** (i - 1)


def f(t, p, D):
    p = np.clip(p, 0, None)
    cum = np.cumsum(p)
    pref = np.r_[0, np.cumsum(c * p)[:-1]]
    return c * p * (1 - D - cum) - m * p - pref * p


fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.0, 1.6, 14.0, 6.8))
sol = solve_ivp(f, (0, 1500), p0, args=(0.25,), rtol=1e-8, atol=1e-14, dense_output=True)
t = np.linspace(0, 1500, 800)
y = sol.sol(t)
toks = ["negative", "dna", "enzyme", "protein", "atp", "rna", "k", "carbohydrate", "receptor", "neutral"]
for k in range(n):
    pa.plot(t, np.clip(y[k], 1e-6, None), color=Q.line_color(toks[k]), lw=1.9 if k == 0 else 1.0,
            label=f"species {k + 1}" if k < 4 else None)
pa.set_yscale("log")
pa.set_ylim(1e-4, 0.5)
pa.set_xlim(0, 1500)
C.style_axes(pa, "years after destruction of 25 % of the sites", "fraction of sites occupied")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left", ncol=2)
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "The best competitor pays the extinction debt", size="small", bold=True, ha="left")

Ds = np.linspace(0.0, 0.6, 31)
lost, t1 = [], []
for D in Ds:
    s = solve_ivp(f, (0, 20000), p0, args=(D,), rtol=1e-8, atol=1e-14, dense_output=True)
    lost.append(int((s.y[:, -1] < 1e-5).sum()))
    tt = np.linspace(0, 20000, 4000)
    yy = s.sol(tt)[0]
    below = np.where(yy < 0.01 * p0[0])[0]
    t1.append(tt[below[0]] if len(below) else np.nan)
pb = C.axes_at(ax, (20.5, 1.6, 8.5, 6.8))
pb.step(Ds, lost, where="mid", color=Q.line_color("negative"), lw=1.6, label="species lost")
pb.set_ylim(0, 10)
C.style_axes(pb, "fraction of sites destroyed D", "species eventually lost")
pb2 = pb.twinx()
pb2.plot(Ds, t1, "o", ms=3, color=Q.line_color("dna"), label="years until species 1 < 1 %")
pb2.set_yscale("log")
C.style_axes(pb2, None, "years until species 1 < 1 % (points)", box=True)
pb2.spines["left"].set_visible(False)
pb.spines["right"].set_visible(False)
bio.panel(ax, "B", (19.0, 9.6))
bio.label(ax, (20.5, 9.2), "Losses and their delay", size="small", bold=True, ha="left")
