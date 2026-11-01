# Ancestry proportions estimated by maximum likelihood (the ADMIXTURE model) on the simulated genotypes of the
# PCA figure (three Balding-Nichols populations of 100 and 40 individuals admixed between populations 1 and 2).
# g_ij ~ Bin(2, sum_k q_ik f_kj); Q and F are fitted on the first 2000 SNPs by the EM algorithm (each allele copy
# has a latent ancestral population), accelerated by SQUAREM and started from k-means on the leading PCs.
# Each bar is one individual, divided into its estimated ancestry proportions; individuals are ordered by
# population and, within the admixed group, by their true proportion from population 1. A: with K = 2,
# populations 1 and 2 share a component and population 1 appears as a 70:30 mixture of the two components, an
# artifact of too small a K. B: K = 3 recovers the three sources; the admixed individuals are mixtures of the first two. The
# text gives the correlation between true and estimated proportions of the admixed individuals.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
m, npop = 5000, 100
p0 = rng.uniform(0.05, 0.95, m)
F = [0.05, 0.08, 0.12]
freqs = [rng.beta(p0 * (1 - f) / f, (1 - p0) * (1 - f) / f) for f in F]
G = [rng.binomial(2, freqs[k], (npop, m)) for k in range(3)]
q = rng.uniform(0, 1, 40)
G.append(rng.binomial(2, q[:, None] * freqs[0] + (1 - q[:, None]) * freqs[1]))
G = np.vstack(G).astype(float)
n = G.shape[0]
order = np.r_[np.arange(300), 300 + np.argsort(q)]


G = G[:, :2000]                                         # the first 2000 SNPs keep the script fast


def step(Q, Fm):
    """One EM step: each allele copy has a latent ancestral component."""
    pa = np.einsum("ik,kj->ij", Q, Fm)                  # einsum: plain loops, no BLAS threads
    a = G / np.clip(pa, 1e-9, None)
    b = (2 - G) / np.clip(1 - pa, 1e-9, None)
    qa = Q * np.einsum("ij,kj->ik", a, Fm)              # expected copies from each component
    qb = Q * np.einsum("ij,kj->ik", b, 1 - Fm)
    fa, fb = Fm * np.einsum("ik,ij->kj", Q, a), (1 - Fm) * np.einsum("ik,ij->kj", Q, b)
    return (qa + qb) / (2 * G.shape[1]), np.clip(fa / (fa + fb), 1e-6, 1 - 1e-6)


def loglik(Q, Fm):
    pa = np.clip(np.einsum("ik,kj->ij", Q, Fm), 1e-9, 1 - 1e-9)
    return np.sum(G * np.log(pa) + (2 - G) * np.log(1 - pa))


def kmeans(X, K, r):
    cen = X[r.choice(len(X), K, replace=False)]
    for _ in range(50):
        lab = ((X[:, None] - cen[None]) ** 2).sum(2).argmin(1)
        cen = np.array([X[lab == k].mean(0) for k in range(K)])
    return lab


ph = G.mean(0) / 2
kp = (ph > 0) & (ph < 1)
U, s, _ = np.linalg.svd((G[:, kp] - 2 * ph[kp]) / np.sqrt(2 * ph[kp] * (1 - ph[kp])), full_matrices=False)


def fit(K, iters=60):
    """EM accelerated by SQUAREM, started from k-means on the top K - 1 principal components."""
    lab = kmeans(U[:, :K - 1] * s[:K - 1], K, np.random.default_rng(1))
    Q = np.full((n, K), 0.1 / (K - 1))
    Q[np.arange(n), lab] = 0.9
    Fm = np.array([G[lab == k].mean(0) / 2 for k in range(K)]).clip(0.01, 0.99)
    for _ in range(iters):
        Q1, F1 = step(Q, Fm)
        Q2, F2 = step(Q1, F1)
        rq, rf, vq, vf = Q1 - Q, F1 - Fm, Q2 - 2 * Q1 + Q, F2 - 2 * F1 + Fm
        al = min(-np.sqrt((rq ** 2).sum() + (rf ** 2).sum()) / np.sqrt((vq ** 2).sum() + (vf ** 2).sum()), -1.0)
        Qn = np.clip(Q - 2 * al * rq + al * al * vq, 1e-6, None)
        Qn, Fn = step(Qn / Qn.sum(1, keepdims=True), np.clip(Fm - 2 * al * rf + al * al * vf, 1e-6, 1 - 1e-6))
        Q, Fm = (Qn, Fn) if loglik(Qn, Fn) >= loglik(Q2, F2) else (Q2, F2)
    return Q


fig, ax = bio.canvas(28.0, 11.0)
toks = ["dna", "rna", "enzyme"]
for row, K in enumerate((2, 3)):
    Q = fit(K)
    # name components by the population where they dominate
    comp = [int(np.argmax([Q[k * 100:(k + 1) * 100, c].mean() for k in range(3)])) for c in range(K)]
    perm = np.argsort(comp)
    Q = Q[:, perm]
    y0 = 6.2 - 5.0 * row
    a = C.axes_at(ax, (2.0, y0, 25.0, 3.6))
    bottom = np.zeros(n)
    for c in range(K):
        a.bar(np.arange(n), Q[order, c], bottom=bottom, width=1.0, color=P.fill(toks[sorted(comp)[c]]),
              edgecolor="none")
        bottom += Q[order, c]
    for x in (99.5, 199.5, 299.5):
        a.axvline(x, color=P.ink(), lw=0.8)
    a.set_xlim(-0.5, n - 0.5)
    a.set_ylim(0, 1)
    a.set_xticks([50, 150, 250, 320])
    a.set_xticklabels(["population 1", "population 2", "population 3", "admixed 1 x 2"])
    C.style_axes(a, None, f"K = {K}", box=True)
    if K == 3:
        est = Q[300:, 0]
        r = np.corrcoef(est, q)[0, 1]
        a.text(n + 2, 0.5, f"admixed: r(true, estimated)\n= {r:.3f}", fontsize=bio.core.FONT["tiny"],
               color=P.ink(), va="center")
bio.panel(ax, "A", (0.3, 10.4))
bio.panel(ax, "B", (0.3, 5.4))
