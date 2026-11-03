"""Why species are not independent data (after Felsenstein 1985). Two traits X and Y evolve by
independent Brownian motions on a tree of 20 species made of two clades of 10 that split near the
root (root age 1; the clades radiate in the last 0.2 time units). A: one simulated data set; within
each clade there is no association, but because the two clades drifted apart early, ordinary
regression across species finds a strong correlation. B: over 2000 simulated data sets with no
correlation between X and Y, the proportion of tests rejecting zero slope at the 5 % level: ordinary
least squares on tip values, phylogenetically independent contrasts (regression through the origin
of the 19 standardized contrasts) and phylogenetic generalized least squares with the Brownian
covariance matrix. The last two give identical slopes and hold the nominal rate."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(1)


def clade(tips, t0):
    """Random ultrametric clade on the given tip labels starting at time t0 (tips at time 1)."""
    if len(tips) == 1:
        return tips[0]
    k = rng.integers(1, len(tips))
    t = t0 + rng.uniform(0.02, 0.6) * (1 - t0)
    return (clade(tips[:k], t), clade(tips[k:], t), t)


# nested (left, right, time); root at time 0, the two clades radiate after time 0.8
T = (clade(list(range(10)), 0.8), clade(list(range(10, 20)), 0.8), 0.0)
n = 20


def tips_of(nd):
    return [nd] if not isinstance(nd, tuple) else tips_of(nd[0]) + tips_of(nd[1])


def node_time(nd):
    return 1.0 if not isinstance(nd, tuple) else nd[2]


C = np.zeros((n, n))


def fill(nd):
    if not isinstance(nd, tuple):
        C[nd, nd] = 1.0
        return
    l, r = tips_of(nd[0]), tips_of(nd[1])
    for i in l:
        for j in r:
            C[i, j] = C[j, i] = nd[2]
    fill(nd[0])
    fill(nd[1])


fill(T)


def pic(nd, x, parent_time):
    """Felsenstein's contrasts: returns (value, extra branch length, list of standardized contrasts)."""
    if not isinstance(nd, tuple):
        return x[nd], 1.0 - parent_time, []
    xl, vl, cl = pic(nd[0], x, nd[2])
    xr, vr, cr = pic(nd[1], x, nd[2])
    u = (xl - xr) / np.sqrt(vl + vr)
    val = (xl / vl + xr / vr) / (1 / vl + 1 / vr)
    extra = vl * vr / (vl + vr)
    return val, nd[2] - parent_time + extra, cl + cr + [u]


L = np.linalg.cholesky(C)
Ci = np.linalg.inv(C)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8), gridspec_kw=dict(width_ratios=[1.2, 1]))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.3)
x, y = L @ rng.normal(size=n), L @ rng.normal(size=n)
grp = np.array([0] * 10 + [1] * 10)
for g, tok in ((0, "dna"), (1, "rna")):
    a.scatter(x[grp == g], y[grp == g], s=20, color=charts.line(tok), zorder=4, label=f"clade {g + 1}")
sl, ic, r, p, _ = stats.linregress(x, y)
xx = np.linspace(x.min(), x.max(), 10)
a.plot(xx, ic + sl * xx, color=P.ink(), lw=1)
a.text(0.03, 0.95, f"OLS across species: r = {r:.2f}, p = {p:.3g}", transform=a.transAxes,
       fontsize=FT["tiny"], color=P.ink(), va="top")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(a, "trait $X$", "trait $Y$")
charts.title(a, "A  A spurious correlation")
rej = np.zeros(3)
reps = 2000
X1 = np.column_stack([np.ones(n), np.zeros(n)])
maxdiff = 0.0
for _ in range(reps):
    x, y = L @ rng.normal(size=n), L @ rng.normal(size=n)
    rej[0] += stats.linregress(x, y).pvalue < 0.05
    _, _, ux = pic(T, x, 0.0)
    _, _, uy = pic(T, y, 0.0)
    ux, uy = np.array(ux), np.array(uy)
    bpic = (ux @ uy) / (ux @ ux)
    res = uy - bpic * ux
    se = np.sqrt(res @ res / (len(ux) - 1) / (ux @ ux))
    rej[1] += 2 * stats.t.sf(abs(bpic / se), len(ux) - 1) < 0.05
    X1[:, 1] = x
    A = X1.T @ Ci @ X1
    beta = np.linalg.solve(A, X1.T @ Ci @ y)
    e = y - X1 @ beta
    s2 = e @ Ci @ e / (n - 2)
    seg = np.sqrt(s2 * np.linalg.inv(A)[1, 1])
    rej[2] += 2 * stats.t.sf(abs(beta[1] / seg), n - 2) < 0.05
    maxdiff = max(maxdiff, abs(beta[1] - bpic))
labels = ["OLS on species", "independent\ncontrasts", "PGLS"]
b.bar(range(3), rej / reps, color=[P.fill("negative"), P.fill("dna"), P.fill("dna")],
      edgecolor=[P.edge("negative"), P.edge("dna"), P.edge("dna")], width=0.6)
b.axhline(0.05, color=P.ink(), lw=0.8, ls="--")
for k, v in enumerate(rej / reps):
    b.text(k, v + 0.01, f"{v:.3f}", ha="center", fontsize=FT["tiny"], color=P.ink())
b.set_xticks(range(3))
b.set_xticklabels(labels)
b.text(1.5, 0.3, f"largest |PGLS slope - PIC slope|\nover all data sets: {maxdiff:.1e}", ha="center",
       fontsize=FT["tiny"], color=P.muted())
charts.style_axes(b, None, "false positive rate")
charts.title(b, "B  Type I error at nominal 5 %")
