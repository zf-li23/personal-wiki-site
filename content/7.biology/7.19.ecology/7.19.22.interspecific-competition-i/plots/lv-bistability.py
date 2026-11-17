"""Time courses of Lotka-Volterra competition, and the probabilistic outcome of mutual antagonism.

A: N1 and N2 against time (r1 = 1, r2 = 0.8, K1 = K2 = 100, both starting at 5) for stable
coexistence (a12 = 0.5, a21 = 0.6; solid), which settles at N1* = 71.4, N2* = 57.1, and exclusion of
species 2 (a12 = 0.6, a21 = 1.4; dashed), which is slow while N2 is still large. B: the bistable case
(a12 = 1.5, a21 = 1.3) as a stochastic birth-death process with K1 = K2 = 60 individuals: per capita
birth rate 1, per capita death rate 0.2 + 0.8 (Ni + aij Nj)/Ki (so that the mean dynamics are the
Lotka-Volterra equations with r = 0.8), simulated by tau-leaping (step 0.02) from 60 individuals in
total with a given initial share of species 1, 400 runs per point (seed 0). The deterministic model
predicts a sharp threshold at the separatrix (vertical step, at about 62 % species 1 for this total: species 1, which suffers more from its competitor, needs a head start); with
demographic stochasticity the winner is decided by chance near the threshold, as in Park's flour beetles.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)
c1, c2 = Q.line_color("dna"), Q.line_color("rna")


def lv(a12, a21, K1=100.0, K2=100.0, r1=1.0, r2=0.8):
    return lambda t, n: [r1 * n[0] * (K1 - n[0] - a12 * n[1]) / K1, r2 * n[1] * (K2 - n[1] - a21 * n[0]) / K2]


pa = C.axes_at(ax, (2.4, 1.8, 11.5, 8.6))
t = np.linspace(0, 40, 400)
for (a12, a21), ls in [((0.5, 0.6), "-"), ((0.6, 1.4), (0, (4, 2)))]:
    s = solve_ivp(lv(a12, a21), (0, 40), [5, 5], t_eval=t, rtol=1e-8)
    pa.plot(t, s.y[0], color=c1, lw=1.7, ls=ls)
    pa.plot(t, s.y[1], color=c2, lw=1.7, ls=ls)
pa.text(39, 74, "$N_1$, coexistence", ha="right", fontsize=FS["tiny"], color=c1)
pa.text(39, 50, "$N_2$, coexistence", ha="right", fontsize=FS["tiny"], color=c2)
pa.text(39, 103, "$N_1$, species 1 wins", ha="right", fontsize=FS["tiny"], color=c1)
pa.text(39, 6, "$N_2$, excluded", ha="right", fontsize=FS["tiny"], color=c2)
pa.set_xlim(0, 40)
pa.set_ylim(0, 110)
C.style_axes(pa, "time (units of 1/r1)", "density")
bio.panel(ax, "A", (0.4, 11.6))
bio.label(ax, (2.4, 11.2), "Coexistence and exclusion", size="small", bold=True, ha="left")

rng = np.random.default_rng(0)
K, a12, a21, b, d0 = 60.0, 1.5, 1.3, 1.0, 0.2
dt, runs, total = 0.02, 400, 60
shares = np.linspace(0.3, 0.75, 10)
wins = []
for sh in shares:
    n1 = np.full(runs, round(sh * total), dtype=float)
    n2 = total - n1
    for _ in range(6000):
        live = (n1 > 0) & (n2 > 0)
        if not live.any():
            break
        d1 = d0 + (b - d0) * (n1 + a12 * n2) / K
        d2 = d0 + (b - d0) * (n2 + a21 * n1) / K
        n1 = np.maximum(n1 + rng.poisson(b * n1 * dt) - rng.poisson(d1 * n1 * dt), 0)
        n2 = np.maximum(n2 + rng.poisson(b * n2 * dt) - rng.poisson(d2 * n2 * dt), 0)
    wins.append(np.mean(n1 > n2))
# Deterministic threshold: the point of the separatrix on the line N1 + N2 = total.
f = lv(a12, a21, K, K, 0.8, 0.8)
lo, hi = 0.3, 0.8
for _ in range(40):
    mid = (lo + hi) / 2
    s = solve_ivp(f, (0, 400), [mid * total, (1 - mid) * total], rtol=1e-9)
    lo, hi = (mid, hi) if s.y[0, -1] < s.y[1, -1] else (lo, mid)
pb = C.axes_at(ax, (17.0, 1.8, 11.5, 8.6))
pb.plot(shares * 100, wins, "o-", color=c1, lw=1.4, ms=4)
pb.step([30, mid * 100, mid * 100, 75], [0, 0, 1, 1], where="post", color=P.muted(), lw=1.0, ls=(0, (3, 2)))
pb.set_xlim(30, 75)
pb.set_ylim(-0.02, 1.02)
C.style_axes(pb, "initial share of species 1 (%)", "probability that species 1 wins")
pb.text(31, 0.9, "dashed: deterministic model", fontsize=FS["tiny"], color=P.muted())
bio.panel(ax, "B", (15.0, 11.6))
bio.label(ax, (17.0, 11.2), "Mutual antagonism with demographic noise", size="small", bold=True, ha="left")
