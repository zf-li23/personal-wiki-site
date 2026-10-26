"""A minimal model of how the two allosteric sites of ribonucleotide reductase balance the four dNTP pools.
Specificity site: ATP (fixed, weight 1), dATP, dTTP and dGTP compete (dissociation constants 2, 5 and 2 uM);
ATP- or dATP-bound enzyme reduces CDP and UDP (shared 0.4 : 0.6, giving dCTP and dTTP), dTTP-bound enzyme
reduces GDP, dGTP-bound enzyme reduces ADP. Activity site: dATP inhibits, activity 1/(1 + ([dATP]/30 uM)^2).
Maximal flux 40 uM/min; DNA synthesis consumes dNTPs at 10 uM/min in proportions A : C : G : T = 0.3 : 0.2 :
0.2 : 0.3 (Michaelis constant 5 uM) plus a slow first-order loss 0.02/min. Illustrative parameters.
(A) From empty pools all four dNTPs reach a balanced steady state within about 20 minutes, with no pool running
away although the enzyme has a single active site. (B) Extra dATP from deoxyadenosine, as in adenosine deaminase deficiency: dATP rises, the
activity site shuts the enzyme down and the other three pools collapse (the cause of the T-cell death in
ADA-SCID). (C) Extra dTTP from thymidine: dTTP shifts the specificity toward GDP, and dCTP falls (the
"thymidine block" used to arrest cells in S phase)."""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

V, KA, KT, KG, KI = 40.0, 2.0, 5.0, 2.0, 30.0
D, KMD, KD = 10.0, 5.0, 0.02
COMP = np.array([0.3, 0.2, 0.2, 0.3])  # A, C, G, T


def rhs(t, y, ja=0.0, jt=0.0):
    a_, c_, g_, t_ = np.maximum(y, 0.0)
    w = np.array([1.0, a_ / KA, t_ / KT, g_ / KG])
    f = w / (1.0 + w.sum())
    act = 1.0 / (1.0 + (a_ / KI) ** 2)
    pyr = V * act * (f[0] + f[1])
    prod = np.array([V * act * f[3] + ja, 0.4 * pyr, V * act * f[2], 0.6 * pyr + jt])
    x = np.array([a_, c_, g_, t_])
    return prod - D * COMP * x / (KMD + x) - KD * x


def steady(ja=0.0, jt=0.0):
    s = solve_ivp(rhs, (0, 4000), [40, 30, 30, 40], args=(ja, jt), rtol=1e-8, atol=1e-8, method="LSODA")
    return s.y[:, -1]


names = ["dATP", "dCTP", "dGTP", "dTTP"]
toks = ["positive", "dna", "rna", "negative"]
fig, ax = bio.canvas(21.0, 7.6)

a = charts.axes_at(ax, (1.6, 1.3, 5.4, 5.6))
t = np.linspace(0, 120, 600)
s = solve_ivp(rhs, (0, t[-1]), [0, 0, 0, 0], t_eval=t, rtol=1e-8, method="LSODA")
for y, n, k in zip(s.y, names, toks):
    a.plot(t, y, color=charts.line(k), lw=2.0, label=n)
a.set_xlim(0, 120)
a.set_ylim(0, 70)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=bio.P.ink(), loc="lower right")
charts.style_axes(a, "t / min", "[dNTP] / µM")
charts.title(a, "A  Filling the pools")

b = charts.axes_at(ax, (8.6, 1.3, 5.4, 5.6))
ja = np.linspace(0, 8, 41)
ss = np.array([steady(ja=j) for j in ja])
for i, (n, k) in enumerate(zip(names, toks)):
    b.plot(ja, ss[:, i], color=charts.line(k), lw=2.0, label=n)
b.set_yscale("log")
b.set_ylim(0.1, 400)
b.set_xlim(0, 8)
charts.style_axes(b, "dATP from deoxyadenosine / (µM min⁻¹)", "steady [dNTP] / µM")
charts.title(b, "B  ADA deficiency")

c = charts.axes_at(ax, (15.6, 1.3, 5.4, 5.6))
jt = np.linspace(0, 8, 41)
ss = np.array([steady(jt=j) for j in jt])
for i, (n, k) in enumerate(zip(names, toks)):
    c.plot(jt, ss[:, i], color=charts.line(k), lw=2.0, label=n)
c.set_yscale("log")
c.set_ylim(0.1, 400)
c.set_xlim(0, 8)
charts.style_axes(c, "dTTP from thymidine / (µM min⁻¹)", "steady [dNTP] / µM")
charts.title(c, "C  Excess thymidine")
