"""Predator interference and ratio dependence (Section 25.5).

Logistic prey (r = 1, K = 100 in A and B) and a predator with attack rate a = 0.1, handling time h = 0.2,
conversion c = 0.5 and death rate m = 0.5. Beddington-DeAngelis response f = aN / (1 + ahN + qP).
A: no interference (q = 0): vertical predator isocline left of the hump of the prey isocline,
trajectory approaches a limit cycle. B: interference q = 0.3: the predator isocline tilts and the
equilibrium becomes stable. C: equilibrium prey density against K: constant for
prey-dependent predation (q = 0), rising with K under interference and proportional to K for the
ratio-dependent response f = alpha (N/P) / (1 + alpha h N/P) with alpha = 0.6.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
r, a, h, c, m = 1.0, 0.1, 0.2, 0.5, 0.5
prey, pred = C.line("dna"), C.line("negative")


def rhs(t, z, K, q):
    N, Q = z
    f = a * N / (1 + a * h * N + q * Q)
    return [r * N * (1 - N / K) - f * Q, Q * (c * f - m)]


fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3))
K = 100.0
n, qq = np.meshgrid(np.linspace(0.5, 110, 400), np.linspace(0.01, 40, 400))
for ax, q, lab in [(axes[0], 0.0, "A  No interference (q = 0)"), (axes[1], 0.3, "B  Interference (q = 0.3)")]:
    dN, dP = rhs(0, (n, qq), K, q)
    ax.contour(n, qq, dN / n, levels=[0], colors=[prey], linewidths=1.2, linestyles="dashed")
    ax.contour(n, qq, dP / qq, levels=[0], colors=[pred], linewidths=1.2, linestyles="dashed")
    s = solve_ivp(rhs, [0, 400], [100, 5], args=(K, q), max_step=0.1, rtol=1e-8)
    ax.plot(s.y[0], s.y[1], color=P.ink(), lw=0.8)
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 40)
    C.style_axes(ax, "Prey N", "Predator P")
    C.title(ax, lab)
axes[0].text(82, 6, "prey isocline", color=prey, fontsize=FS["tiny"])
axes[0].text(14, 37, "predator isocline", color=pred, fontsize=FS["tiny"])

ax = axes[2]
Ks = np.linspace(20, 300, 120)
for q, col, lab in [(0.0, C.line("neutral"), "prey dependent (q = 0)"), (0.3, C.line("dna"), "Beddington-DeAngelis (q = 0.3)")]:
    Nstar = []
    for Kk in Ks:
        # predator isocline P(N) = (caN - m(1 + ahN)) / (m q); substitute into the prey isocline
        if q == 0:
            Nstar.append(m / (a * (c - m * h)))
            continue
        Pn = lambda N: (c * a * N - m * (1 + a * h * N)) / (m * q)
        g = lambda N: r * (1 - N / Kk) - a * Pn(N) / (1 + a * h * N + q * Pn(N))
        lo = m / (a * (c - m * h)) + 1e-9
        Nstar.append(brentq(g, lo, Kk) if g(lo) > 0 else np.nan)
    ax.plot(Ks, Nstar, color=col, lw=1.4, label=lab)
al = 0.6
gam = al * (c - m * h) / m
ax.plot(Ks, Ks * (1 - al * gam / (r * (gam + al * h))), color=C.line("negative"), lw=1.4, label="ratio dependent")
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper left")
C.style_axes(ax, "Prey carrying capacity K", "Equilibrium prey density N*")
C.title(ax, "C  Does enrichment raise prey density?")
fig.tight_layout()
