"""The star tree paradox. Binary characters evolve under a molecular clock on a star tree of three
species (branch length 0.2), and the three rooted binary trees are compared by Bayesian inference with
exponential priors (mean 0.1) on their two branch lengths, the marginal likelihoods computed by
two-dimensional numerical integration. A: posterior probabilities of the three binary trees for 300 data
sets of n = 3000 sites, on the triangle whose corners are probability 1 for one tree. They do not
converge to (1/3, 1/3, 1/3): many data sets give one tree a high probability. B: the distribution of the
largest of the three posterior probabilities in the simulated data sets (histogram) and in the limiting
distribution for n -> infinity (line) of Susko (2008), P_i proportional to exp(z_i^2/2) Phi(z_i) with
correlated normal z_i."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(11)


def pdiff(t):
    return 0.5 - 0.5 * np.exp(-2 * t)


def pattern_probs(t1, t0):
    """Rooted tree ((1,2),3): 1 and 2 join at height t1, the root at t1 + t0.
    Returns probabilities of xxx, xxy (3 differs), yxx (1 differs), xyx (2 differs)."""
    a, b, c = pdiff(t0), pdiff(t1), pdiff(t0 + t1)
    # root state 0 by symmetry; u = state of the ancestor of 1 and 2
    out = []
    for x1, x2, x3 in ((0, 0, 0), (0, 0, 1), (1, 0, 0), (0, 1, 0)):
        tot = 0.0
        for r in (0, 1):
            for u in (0, 1):
                pu = (a if u != r else 1 - a)
                p1 = b if x1 != u else 1 - b
                p2 = b if x2 != u else 1 - b
                p3 = c if x3 != r else 1 - c
                tot = tot + 0.5 * pu * p1 * p2 * p3
        out.append(2 * tot)                    # patterns and their complements
    return np.array(out)


# quadrature grid on log scale for (t1, t0)
g = np.logspace(-5, 0.5, 90)
w = np.gradient(g)
T1, T0 = np.meshgrid(g, g, indexing="ij")
W = np.outer(w, w) * (np.exp(-T1 / 0.1) / 0.1) * (np.exp(-T0 / 0.1) / 0.1)
PP = np.log(pattern_probs(T1, T0))           # 4 x grid
true = pattern_probs(np.array(0.2), np.array(0.0))
n, reps = 3000, 300
post = np.zeros((reps, 3))
for r in range(reps):
    c = rng.multinomial(n, true)
    lm = []
    for k in range(3):
        # tree k is supported by pattern k + 1; rotate the three variable patterns
        cc = np.array([c[0], c[1 + k], c[1 + (k + 1) % 3], c[1 + (k + 2) % 3]])
        ll = np.tensordot(cc, PP, axes=1)
        m = ll.max()
        lm.append(m + np.log((W * np.exp(ll - m)).sum()))
    lm = np.array(lm)
    post[r] = np.exp(lm - lm.max()) / np.exp(lm - lm.max()).sum()

S = np.array([[1, -0.5, -0.5], [-0.5, 1, -0.5], [-0.5, -0.5, 1]])
z = rng.multivariate_normal(np.zeros(3), S, size=200000)
lim = np.exp(z ** 2 / 2) * norm.cdf(z)
lim /= lim.sum(1, keepdims=True)

fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4.2))
fig.subplots_adjust(left=0.04, right=0.98, bottom=0.15, top=0.9, wspace=0.2)
corners = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])
a.plot(*np.vstack([corners, corners[:1]]).T, color=P.muted(), lw=0.8)
xy = post @ corners
a.plot(xy[:, 0], xy[:, 1], "o", ms=2.6, color=charts.line("dna"), alpha=0.7)
a.plot(*(np.full(3, 1 / 3) @ corners), "+", ms=9, color=charts.line("negative"), mew=1.5)
for k, lab in enumerate(("$\\tau_1$ ((1,2),3)", "$\\tau_2$ ((2,3),1)", "$\\tau_3$ ((1,3),2)")):
    off = np.array([[-0.05, -0.06], [0.05, -0.06], [0, 0.04]])[k]
    a.text(*(corners[k] + off), lab, ha="center", fontsize=FT["tiny"], color=P.ink())
a.set_aspect("equal")
a.set_xlim(-0.15, 1.15)
a.set_ylim(-0.12, 0.95)
a.axis("off")
charts.title(a, f"A  Posterior tree probabilities, $n = {n}$")

bins = np.linspace(1 / 3, 1, 34)
b.hist(post.max(1), bins=bins, density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.5,
       label="simulated data sets")
h, e = np.histogram(lim.max(1), bins=bins, density=True)
b.plot(0.5 * (e[1:] + e[:-1]), h, color=charts.line("negative"), lw=1.5, label="limit $n \\to \\infty$")
f95 = (lim.max(1) > 0.95).mean()
b.text(0.62, 0.8 * b.get_ylim()[1], f"limit: P(max > 0.95) = {f95:.3f}\nsimulated: {(post.max(1) > 0.95).mean():.3f}",
       fontsize=FT["tiny"], color=P.ink(),
       bbox=dict(boxstyle="round,pad=0.3", fc=P.surface(), ec=P.muted(), lw=0.5))
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "largest posterior tree probability", "density")
charts.title(b, "B  No convergence to 1/3")
