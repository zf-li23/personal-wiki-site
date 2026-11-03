"""Measuring phylogenetic signal. Traits were simulated on a random ultrametric tree of 50 species
(height 1) under Pagel's lambda model, Eq. (26.3): multivariate normal with covariance sigma^2 C(lambda),
whose off-diagonal elements are lambda times those of the Brownian matrix C. A: profile log
likelihood of lambda (sigma^2 and the root state maximized analytically) for one data set
simulated with each of lambda = 0, 0.5 and 1 (true values dotted). B: Blomberg's K, Eq. (26.4),
for 500 data sets simulated under each lambda; K is near 1 under Brownian motion (lambda = 1) and much
smaller when the tips are nearly independent (lambda = 0)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(9)
n = 50


def random_tree(labels, t0):
    if len(labels) == 1:
        return labels[0]
    k = rng.integers(1, len(labels))
    t = t0 + rng.beta(1, 2.5) * (1 - t0)
    return (random_tree(labels[:k], t), random_tree(labels[k:], t), t)


def tips(nd):
    return [nd] if not isinstance(nd, tuple) else tips(nd[0]) + tips(nd[1])


C = np.zeros((n, n))


def fill(nd):
    if not isinstance(nd, tuple):
        C[nd, nd] = 1.0
        return
    for i in tips(nd[0]):
        for j in tips(nd[1]):
            C[i, j] = C[j, i] = nd[2]
    fill(nd[0])
    fill(nd[1])


fill(random_tree(list(range(n)), 0.0))
one = np.ones(n)


def Clam(lam):
    M = C * lam
    np.fill_diagonal(M, np.diag(C))
    return M


def profile(x, lam):
    V = Clam(lam)
    Vi = np.linalg.inv(V)
    a = (one @ Vi @ x) / (one @ Vi @ one)
    r = x - a
    s2 = r @ Vi @ r / n
    _, ld = np.linalg.slogdet(V)
    return -0.5 * (n * np.log(2 * np.pi * s2) + ld + n)


Ci = np.linalg.inv(C)
expected = (np.trace(C) - n / (one @ Ci @ one)) / (n - 1)


def blomberg(x):
    a = (one @ Ci @ x) / (one @ Ci @ one)
    r = x - a
    return ((r @ r) / (r @ Ci @ r)) / expected


fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
lams = np.linspace(0, 1, 51)
toks = {0.0: "rna", 0.5: "positive", 1.0: "dna"}
for lam, tok in toks.items():
    L = np.linalg.cholesky(Clam(lam))
    x = L @ rng.normal(size=n)
    pl = np.array([profile(x, l) for l in lams])
    a.plot(lams, pl - pl.max(), color=charts.line(tok), lw=1.6, label=f"simulated $\\lambda = {lam:g}$")
    a.axvline(lam, color=charts.line(tok), lw=0.7, ls=":")
a.axhline(-1.92, color=P.muted(), lw=0.8, ls="--")
a.set_ylim(-12, 0.5)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower center")
charts.style_axes(a, "$\\lambda$", "profile log likelihood $-\\,\\ell_{\\max}$")
charts.title(a, "A  Estimating Pagel's $\\lambda$")
data = []
for lam in toks:
    L = np.linalg.cholesky(Clam(lam))
    data.append([blomberg(L @ rng.normal(size=n)) for _ in range(500)])
parts = b.boxplot(data, positions=[0, 1, 2], widths=0.5, patch_artist=True, showfliers=False)
for patch, tok in zip(parts["boxes"], toks.values()):
    patch.set_facecolor(P.fill(tok))
    patch.set_edgecolor(P.edge(tok))
for key in ("whiskers", "caps", "medians"):
    for ln in parts[key]:
        ln.set_color(P.ink())
b.axhline(1, color=P.muted(), lw=0.8, ls="--")
b.set_xticks([0, 1, 2])
b.set_xticklabels([f"$\\lambda = {l:g}$" for l in toks])
charts.style_axes(b, "simulation model", "Blomberg's $K$")
charts.title(b, "B  Blomberg's $K$")
