# Dwell times and the randomness parameter. A: dwell-time densities for cycles of n sequential irreversible
# steps of equal rate (gamma distributions) with the same mean dwell, 10 ms; the more hidden steps, the narrower
# and the more peaked the distribution (histogram: 3000 simulated dwells of the n = 2 cycle).
# B: randomness r = lim 2D/(Va) of the three-state kinesin model of Formula 27.3.4 against [ATP] at two loads,
# from the exact large-time cumulants of the master equation (lines) and from 3000 simulated runs of 200 cycles
# each (points). At low ATP one step (ATP binding) limits, r -> 1; at saturating ATP two comparable steps
# remain, r -> 1/2; near stall backward steps make r > 1.
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
kT, a = 4.1, 8.2
kon, koff, k10, k2 = 1.5, 10.0, 200.0, 200.0
kb0, d0, d1, db = k10 / 800, 0.8, 1.2, 2.6

fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axs[0]
t = np.linspace(0, 40, 400)
mean = 10.0
dw = rng.exponential(mean / 2, 3000) + rng.exponential(mean / 2, 3000)
ax.hist(dw, bins=np.linspace(0, 40, 41), density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.4, alpha=0.8)
for n, tok in ((1, "neutral"), (2, "dna"), (4, "enzyme"), (10, "rna")):
    ax.plot(t, gamma.pdf(t, n, scale=mean / n), color=charts.line(tok), lw=1.8, label=f"n = {n}, r = 1/{n}" if n > 1 else "n = 1, r = 1")
ax.legend(fontsize=7.5, frameon=False)
ax.set_xlim(0, 40)
charts.style_axes(ax, "dwell time / ms", "probability density / ms$^{-1}$")
charts.title(ax, "A   Hidden steps sharpen the dwell-time distribution")


def generator(F, atp, s):
    u0, k1, kb = kon * atp * np.exp(-d0 * F / kT), k10 * np.exp(-d1 * F / kT), kb0 * np.exp(db * F / kT)
    return np.array([[-u0, koff, k2], [u0, -(koff + k1 + kb), 0.0], [0.0, k1 * np.exp(s) + kb * np.exp(-s), -k2]])


def randomness(F, atp, h=1e-4):
    lam = [np.max(np.linalg.eigvals(generator(F, atp, s)).real) for s in (-h, 0.0, h)]
    v = (lam[2] - lam[0]) / (2 * h)
    d2 = (lam[2] - 2 * lam[1] + lam[0]) / h**2
    return d2 / v


def simulate(F, atp, runs=3000, steps=200):
    u0, k1, kb = kon * atp * np.exp(-d0 * F / kT), k10 * np.exp(-d1 * F / kT), kb0 * np.exp(db * F / kT)
    T = np.zeros(runs)
    X = np.zeros(runs)
    for _ in range(steps):
        # state 0 -> 1 (with possible returns by unbinding), then 1 -> 2 forward or backward, then 2 -> 0
        alive = np.ones(runs, bool)
        while alive.any():
            T[alive] += rng.exponential(1 / u0, alive.sum())
            tot = koff + k1 + kb
            T[alive] += rng.exponential(1 / tot, alive.sum())
            r = rng.random(alive.sum()) * tot
            idx = np.flatnonzero(alive)
            stepped = r >= koff
            X[idx[stepped]] += np.where(r[stepped] < koff + k1, a, -a)
            alive[idx[stepped]] = False
        T += rng.exponential(1 / k2, runs)
    # displacement statistics at a common time: use the per-run velocity and the renewal estimate
    tbar = T.mean()
    v = X.mean() / tbar
    varx = np.var(X - v * T)  # fluctuation of position about the drift at fixed step count
    return varx / (a * X.mean())


A = np.logspace(0, 4, 120)
for Fl, tok in ((1.05, "enzyme"), (5.63, "rna")):
    ax = axs[1]
    ax.semilogx(A, [randomness(Fl, x) for x in A], color=charts.line(tok), lw=1.8, label=f"{Fl} pN")
    As = np.array([2, 20, 200, 2000])
    ax.semilogx(As, [simulate(Fl, x) for x in As], "o", color=charts.line(tok), ms=5)
ax = axs[1]
for r0, lab in ((1, "r = 1: one rate-limiting step"), (0.5, "r = 1/2: two equal steps")):
    ax.axhline(r0, color=P.muted(), lw=0.8, ls="--")
    ax.text(1.1, r0 + 0.03, lab, fontsize=7.5, color=P.muted())
ax.set_ylim(0, 1.9)
ax.legend(fontsize=7.5, frameon=False, loc="upper right", title="load", title_fontsize=7.5)
charts.style_axes(ax, "[ATP] / µM", "randomness $r$")
charts.title(ax, "B   Counting rate-limiting steps in the kinesin cycle")
fig.tight_layout()
