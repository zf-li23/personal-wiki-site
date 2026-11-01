"""The giant component of G(N, M) random graphs. A: fraction S of vertices in the largest component
against the mean degree c = 2M/N for three sizes (averages over realizations) and the solution of
S = 1 - exp(-cS). B: at c = 1, the probability that a random vertex lies in a component of s vertices,
with the Borel distribution exp(-s) s^(s-1)/s! and its tail s^(-3/2)/sqrt(2 pi)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from scipy.special import gammaln
import wikigraph as G

rng = np.random.default_rng(1)


def component_sizes(n, c):
    m = int(round(c * n / 2))
    e = rng.integers(0, n, (m, 2))
    a = coo_matrix((np.ones(m), (e[:, 0], e[:, 1])), shape=(n, n))
    _, lab = connected_components(a, directed=False)
    return np.bincount(lab)


def theory(c):
    return 0.0 if c <= 1 else brentq(lambda s: s - 1 + np.exp(-c * s), 1e-12, 1.0)


fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.0, 3.5))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.16, top=0.9)
cs = np.linspace(0.05, 4, 40)
for n, reps, col in ((100, 40, G.GREEN), (1000, 20, G.BLUE), (100000, 3, G.RED)):
    s = [np.mean([component_sizes(n, c).max() / n for _ in range(reps)]) for c in cs]
    ax.plot(cs, s, "o", ms=3, color=col, label=f"simulation, N = {n:,}")
cc = np.linspace(0.0, 4, 400)
ax.plot(cc, [theory(c) for c in cc], color="black", lw=1.2, label=r"$S = 1 - \mathrm{e}^{-cS}$")
ax.axvline(1, color=G.GREY, lw=0.8, ls=":")
ax.set_xlabel(r"mean degree $c$")
ax.set_ylabel(r"fraction in largest component $S$")
ax.set_title("A  emergence of the giant component", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")

n = 200000
counts = np.zeros(n + 1)
for _ in range(5):
    sizes = component_sizes(n, 1.0)
    counts += np.bincount(sizes, weights=sizes, minlength=n + 1)  # vertex-weighted
p = counts / counts.sum()
edges = np.unique(np.round(np.logspace(0, np.log10(p.nonzero()[0].max() + 1), 30)).astype(int))
mid, dens = [], []
for a, b in zip(edges[:-1], edges[1:]):
    mass = p[a:b].sum()
    if mass > 0:
        mid.append(np.sqrt(a * (b - 1)) if b - 1 > a else a)
        dens.append(mass / (b - a))
bx.loglog(mid, dens, "o", ms=3.5, color=G.BLUE, label="simulation, N = 200,000, c = 1")
s = np.arange(1, 3000)
bx.loglog(s, np.exp(-s + (s - 1) * np.log(s) - gammaln(s + 1)), color="black", lw=1.0, label="Borel distribution")
bx.loglog(s, s ** -1.5 / np.sqrt(2 * np.pi), color=G.RED, lw=1.0, ls="--", label=r"$s^{-3/2}/\sqrt{2\pi}$")
bx.set_xlabel(r"component size $s$")
bx.set_ylabel(r"$p_s$")
bx.set_title("B  component sizes at the critical point", loc="left", fontsize=10)
bx.legend(frameon=False, fontsize=8)
