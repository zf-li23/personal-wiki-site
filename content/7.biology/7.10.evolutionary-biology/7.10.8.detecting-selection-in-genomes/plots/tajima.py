"""Tajima's D under three histories: coalescent simulations of n = 20 sequences, theta = 10 per locus under
the infinite-sites model, 5000 independent loci per history, with time-varying population size handled by
rescaling the coalescent intensity (time in units of 2N0 generations, N0 the present size). Histories:
constant; exponential growth backward, N(t) = N0 exp(-10 t) floored at 0.001 N0; decline, N(t) = 10 N0 for
t > 0.1. D from Eq. (8.2); the vertical line marks 0."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
n, theta, R = 20, 10.0, 5000
grid = np.linspace(0, 40, 400001)
dtg = grid[1] - grid[0]
hist = {"constant size": lambda t: np.ones_like(t),
        "exponential growth": lambda t: np.maximum(np.exp(-10 * t), 1e-3),
        "recent decline": lambda t: np.where(t > 0.1, 10.0, 1.0)}
i = np.arange(1, n)
a1, a2 = np.sum(1 / i), np.sum(1 / i ** 2)
b1, b2 = (n + 1) / (3 * (n - 1)), 2 * (n * n + n + 3) / (9 * n * (n - 1))
c1, c2 = b1 - 1 / a1, b2 - (n + 2) / (a1 * n) + a2 / a1 ** 2
e1, e2 = c1 / a1, c2 / (a1 ** 2 + a2)
rng = np.random.default_rng(21)
fig, ax = plt.subplots(figsize=(7.2, 3.9))
fig.subplots_adjust(left=0.1, right=0.97, bottom=0.15, top=0.9)
for (name, rel), tok in zip(hist.items(), ("neutral", "rna", "dna")):
    inten = np.concatenate([[0], np.cumsum(1 / rel(grid[:-1]) * dtg)])
    D = []
    for r in range(R):
        sizes = [1] * n
        xi = np.zeros(n)
        w = tprev = 0.0
        while len(sizes) > 1:
            k = len(sizes)
            w += rng.exponential(2 / (k * (k - 1)))
            t = float(np.interp(w, inten, grid))
            for s in sizes:
                xi[s] += rng.poisson(theta * (t - tprev) / 2)
            tprev = t
            a, b = sorted(rng.choice(k, 2, replace=False))
            sizes[a] += sizes[b]
            sizes.pop(b)
        x = xi[1:]
        S = x.sum()
        if S < 2:
            continue
        pi = (x * i * (n - i)).sum() / (n * (n - 1) / 2)
        D.append((pi - S / a1) / np.sqrt(e1 * S + e2 * S * (S - 1)))
    ax.hist(D, bins=np.linspace(-3, 3.5, 66), density=True, histtype="stepfilled", alpha=0.55,
            color=P.fill(tok), edgecolor=P.edge(tok), lw=1.2, label=f"{name} (mean {np.mean(D):.2f})")
ax.axvline(0, color=P.ink(), lw=0.8)
ax.set_xlim(-3, 3.5)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "Tajima's $D$", "density")
charts.title(ax, "Demography shifts the distribution of $D$")
