# Beta diversity of two groups of simulated gut samples. 20 samples per group, 60 taxa; each sample's
# composition is drawn from a Dirichlet distribution around its group's mean (concentration 60), and 10 000
# reads are drawn from it. In group 2 six abundant taxa are twice as abundant and six others half as abundant
# as in group 1. A: principal coordinates analysis (classical multidimensional scaling) of the Bray-Curtis
# dissimilarities of the relative abundances; the axis labels give each coordinate's share of the positive
# eigenvalues (Bray-Curtis is not Euclidean, so some eigenvalues are negative). B: PERMANOVA: the observed
# pseudo-F against its distribution under 999 random permutations of the group labels.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
T, n = 60, 20
base = np.exp(rng.normal(0, 1.5, T))
base /= base.sum()
order = np.argsort(base)[::-1]
g2 = base.copy()
g2[order[2:8]] *= 2
g2[order[8:14]] /= 2
g2 /= g2.sum()
X = []
for mean in (base, g2):
    for _ in range(n):
        X.append(rng.multinomial(10000, rng.dirichlet(60 * mean)) / 10000)
X = np.array(X)
lab = np.r_[np.zeros(n, int), np.ones(n, int)]
Nn = len(X)
D = np.array([[1 - 2 * np.minimum(x, y).sum() / (x.sum() + y.sum()) for y in X] for x in X])
A = -0.5 * D ** 2
J = np.eye(Nn) - 1 / Nn
B = J @ A @ J
ev, V = np.linalg.eigh(B)
ev, V = ev[::-1], V[:, ::-1]
coords = V[:, :2] * np.sqrt(ev[:2])
share = ev[:2] / ev[ev > 0].sum()


def pseudo_f(lab):
    sst = (D[np.triu_indices(Nn, 1)] ** 2).sum() / Nn
    ssw = 0.0
    for g in (0, 1):
        idx = np.where(lab == g)[0]
        sub = D[np.ix_(idx, idx)]
        ssw += (sub[np.triu_indices(len(idx), 1)] ** 2).sum() / len(idx)
    return ((sst - ssw) / 1) / (ssw / (Nn - 2))


F_obs = pseudo_f(lab)
perm = np.array([pseudo_f(rng.permutation(lab)) for _ in range(999)])
pval = (1 + np.sum(perm >= F_obs)) / 1000

fig, ax = bio.canvas(28.0, 10.6)
a = C.axes_at(ax, (2.2, 1.6, 10.8, 7.8))
for g, tok, name in [(0, "dna", "group 1"), (1, "rna", "group 2")]:
    s = lab == g
    a.scatter(coords[s, 0], coords[s, 1], s=22, color=C.line(tok), lw=0, alpha=0.85, label=name)
C.style_axes(a, f"PCoA 1 ({100 * share[0]:.0f} %)", f"PCoA 2 ({100 * share[1]:.0f} %)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="best")
a.text(0.02, 0.02, f"{np.sum(ev < -1e-10)} of {Nn} eigenvalues negative", transform=a.transAxes,
       fontsize=bio.core.FONT["tiny"], color=P.ink())
b = C.axes_at(ax, (16.6, 1.6, 10.6, 7.8))
b.hist(perm, bins=40, color=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.4)
b.axvline(F_obs, color=C.line("negative"), lw=1.4)
b.text(F_obs * 0.97, b.get_ylim()[1] * 0.85, f"observed F = {F_obs:.1f}\np = {pval:.3f}", ha="right",
       fontsize=bio.core.FONT["tiny"], color=P.ink())
C.style_axes(b, "pseudo-F (999 label permutations)", "permutations")
bio.panel(ax, "A", (0.3, 10.2))
bio.panel(ax, "B", (14.8, 10.2))
