"""Expansion recoding by cerebellar granule cells and the linear separability of patterns.

A: Cover's function counting theorem: fraction of the 2^P dichotomies of P points in general position
in R^N (with a bias weight, N + 1 parameters) that are linearly separable, against P/N, for
N = 5, 25 and 125: the transition at P = 2N sharpens as N grows.
B: simulation. P random patterns of N = 10 mossy fiber rates (independent Gaussians) receive random
labels +-1; the patterns are classified by a perceptron reading either the mossy fibers directly or
M = 50 or 200 granule cells, each summing K = 4 randomly chosen mossy fibers with random positive
weights, minus a Golgi-cell inhibition proportional to the mean mossy fiber input, and thresholded
(rectified) so that a fraction f = 0.2 of the granule cells is active on
average. Separability is decided exactly by linear programming (a feasible w, b with
y (w . x + b) >= 1). 16 random labelings per point.
C: fraction separable at P = 300, M = 200, against the coding level f set by the threshold: very
sparse codes (few active cells) and dense, almost linear codes are both poor; intermediate coding
levels are best.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog
from scipy.special import comb

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)


def cover_fraction(p, n):
    k = np.arange(n)
    return min(1.0, 2 * comb(p - 1, k).sum() / 2.0 ** p) if p > n else 1.0


def separable(X, y):
    n, d = X.shape
    A = -y[:, None] * np.c_[X, np.ones(n)]
    res = linprog(np.zeros(d + 1), A_ub=A, b_ub=-np.ones(n), bounds=[(None, None)] * (d + 1),
                  method="highs")
    return res.status == 0


Nmf, K = 10, 4


def granule(X, M, f):
    idx = np.array([rng.choice(Nmf, K, replace=False) for _ in range(M)])
    W = np.zeros((M, Nmf))
    for j in range(M):
        W[j, idx[j]] = rng.uniform(0.5, 1.5, K)
    H = (X - X.mean(1, keepdims=True)) @ W.T              # Golgi inhibition removes the mean drive
    theta = np.quantile(H, 1 - f, axis=0)                 # per-cell threshold sets coding level
    return np.maximum(H - theta, 0)


def frac(rep, Pn, reps=16):
    ok = 0
    for _ in range(reps):
        X = rng.normal(size=(Pn, Nmf))
        y = rng.choice([-1.0, 1.0], Pn)
        Z = X if rep is None else granule(X, *rep)
        ok += separable(Z, y)
    return ok / reps


fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.8))
ax = axs[0]
x = np.linspace(0.2, 4, 80)
for n, tok in ((5, "neutral"), (25, "dna"), (125, "negative")):
    ax.plot(x, [cover_fraction(int(round(xx * n)), n + 1) for xx in x], color=P.edge(tok), lw=1.8,
            label=f"$N = {n}$")
ax.axvline(2, color=P.muted(), lw=0.8, ls=":")
ax.set_xlabel("Patterns per input dimension $P/N$")
ax.set_ylabel("Fraction linearly separable")
ax.set_title("A  Cover's theorem", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

ax = axs[1]
Ps = [10, 20, 30, 40, 60, 80, 120, 160, 240, 320, 400, 500]
for rep, lab, tok in ((None, "10 mossy fibers", "neutral"), ((50, 0.2), "50 granule cells", "dna"),
                      ((200, 0.2), "200 granule cells", "negative")):
    ax.plot(Ps, [frac(rep, p) for p in Ps], "o-", color=P.edge(tok), lw=1.6, ms=3.5, label=lab)
ax.set_xscale("log")
ax.set_xlabel("Number of patterns $P$")
ax.set_ylabel("Fraction separable")
ax.set_title("B  Expansion ($K = 4$, $f = 0.2$)", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

ax = axs[2]
fs = [0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.85, 0.95, 1.0]
ax.plot(fs, [frac((200, f), 300) for f in fs], "o-", color=P.edge("negative"), lw=1.6, ms=3.5)
ax.set_xlabel("Coding level $f$ (fraction of active granule cells)")
ax.set_ylabel("Fraction separable ($P = 300$)")
ax.set_title("C  Coding level", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
    a.set_ylim(-0.03, 1.03)
fig.tight_layout()
