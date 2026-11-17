"""Aggregation of parasitoid attacks and May's negative binomial model (Section 27.3.2).

A: the fraction of hosts escaping parasitism as a function of the mean number of attacks per host,
aP: exp(-aP) for random (Poisson) search and (1 + aP/k)^(-k) for negative binomial attacks with
k = 2, 1 and 0.5; strong clumping (small k) leaves many hosts unattacked even at high parasitoid density.
B: May's model with lam = 2, a = 0.05, c = 1, started at twice the host and half the parasitoid
equilibrium: k = 0.5 (damped, stable) and k = 2 (diverging).
C: det J of the linearization (Theorem 27.3.1) against lam for k = 0.25, 0.5, 1, 2 and the
Nicholson-Bailey limit k -> infinity; the equilibrium is stable where det J < 1, i.e. iff k < 1.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
lam, a, c = 2.0, 0.05, 1.0
host, para = C.line("positive"), C.line("negative")
cols = [C.line("dna"), C.line("positive"), C.line("highlight"), C.line("negative"), P.ink()]

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3))
ax = axes[0]
m = np.linspace(0, 6, 300)
ax.plot(m, np.exp(-m), color=P.ink(), lw=1.4, label="random search (Poisson)")
for k, col in zip([2, 1, 0.5], cols):
    ax.plot(m, (1 + m / k) ** (-k), color=col, lw=1.4, label=f"negative binomial, k = {k:g}")
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
C.style_axes(ax, "Mean attacks per host, aP", "Fraction of hosts escaping")
C.title(ax, "A  Clumped attacks create a partial refuge")

ax = axes[1]
for k, ls in [(0.5, "-"), (2.0, (0, (3, 1.5)))]:
    Ps = k * (lam ** (1 / k) - 1) / a
    Hs = lam * Ps / ((lam - 1) * c)
    H, Q = [2 * Hs], [0.5 * Ps]
    for _ in range(40):
        e = (1 + a * Q[-1] / k) ** (-k)
        H.append(lam * H[-1] * e)
        Q.append(c * H[-2] * (1 - e))
    ax.semilogy(H, color=host, ls=ls, lw=1.3, label=f"hosts, k = {k:g}")
    ax.semilogy(Q, color=para, ls=ls, lw=1.3, label=f"parasitoids, k = {k:g}")
ax.set_ylim(1, 5e3)
ax.legend(fontsize=FS["tiny"], frameon=False, ncol=2, loc="upper left")
C.style_axes(ax, "Generation t", "Number (log scale)")
C.title(ax, "B  k = 0.5 stable, k = 2 unstable")

ax = axes[2]
L = np.linspace(1.01, 10, 300)
for k, col in zip([0.25, 0.5, 1, 2], cols):
    ax.plot(L, k * L * (1 - L ** (-1 / k)) / (L - 1), color=col, lw=1.4, label=f"k = {k:g}")
ax.plot(L, L * np.log(L) / (L - 1), color=P.ink(), lw=1.4, ls=(0, (4, 2)), label="k → ∞ (Nicholson–Bailey)")
ax.axhline(1, color=P.muted(), lw=0.8)
ax.text(9.8, 0.93, "stable below", ha="right", va="top", fontsize=FS["tiny"], color=P.muted())
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper left")
ax.set_ylim(0, 2.8)
C.style_axes(ax, "Host rate of increase λ", "det J at equilibrium")
C.title(ax, "C  Stability criterion k < 1")
fig.tight_layout()
