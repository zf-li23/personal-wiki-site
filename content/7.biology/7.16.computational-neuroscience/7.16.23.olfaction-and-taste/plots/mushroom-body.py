"""Random expansion and sparse coding in the mushroom body, and the fly hashing algorithm.

Model: 50 PN types project to 2000 Kenyon cells (KCs); each KC sums 6 randomly chosen PNs with unit
weights. With APL feedback inhibition, only the 5 % most strongly driven KCs fire (k-winners-take-all);
without APL, KCs fire above a fixed threshold set so that 5 % fire at the reference concentration.
A: overlap (Jaccard index) of the KC codes of two odours against the correlation of their PN inputs
(PN vectors: rectified Gaussian, mean-centred and rescaled after Dasgupta et al. 2017).
B: fraction of active KCs as the PN input is scaled (concentration): APL keeps it constant.
C: nearest-neighbour search on 600 synthetic 50-dimensional odours (20 clusters). For each query the
20 true nearest neighbours (Euclidean) are compared with the 20 nearest by the hash: the fly hash
(2000 sparse projections, k winners kept, Hamming distance) and a classical LSH with k dense Gaussian
projections (Euclidean distance among projections). Mean precision over 100 queries.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
nPN, nKC, fan, frac = 50, 2000, 6, 0.05

W = np.zeros((nKC, nPN))
for i in range(nKC):
    W[i, rng.choice(nPN, fan, replace=False)] = 1.0


def kwta(h, k):
    """Binary code with the k largest entries of each row set to 1."""
    out = np.zeros_like(h)
    idx = np.argpartition(-h, k, axis=-1)[..., :k]
    np.put_along_axis(out, idx, 1.0, axis=-1)
    return out


def odour_pair(rho):
    a = rng.normal(size=nPN)
    b = rho * a + np.sqrt(1 - rho**2) * rng.normal(size=nPN)
    return np.clip(a, 0, None) + 0.2, np.clip(b, 0, None) + 0.2


def centre(x):
    return (x - x.mean(axis=-1, keepdims=True)) / x.std(axis=-1, keepdims=True)


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
ax = axs[0]
rhos = np.linspace(0, 0.99, 12)
k = int(frac * nKC)
for kk, c, lab in ((k, P.edge("rna"), "5 % active"), (4 * k, P.edge("dna"), "20 % active")):
    jac, inp = [], []
    for r in rhos:
        js, cs = [], []
        for _ in range(30):
            a, b = odour_pair(r)
            ca, cb = kwta(W @ centre(a), kk), kwta(W @ centre(b), kk)
            js.append((ca * cb).sum() / np.clip(ca + cb, 0, 1).sum())
            cs.append(np.corrcoef(a, b)[0, 1])
        jac.append(np.mean(js))
        inp.append(np.mean(cs))
    ax.plot(inp, jac, "o-", color=c, ms=3.5, lw=1.6, label=lab)
ax.plot([0, 1], [0, 1], color=P.muted(), lw=0.8, ls=":")
ax.set_xlabel("Correlation of PN inputs")
ax.set_ylabel("Overlap of KC codes (Jaccard)")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Similar odours, separated codes", loc="left", fontsize=10)

ax = axs[1]
odours = np.clip(rng.normal(size=(200, nPN)), 0, None)
h = odours @ W.T
theta = np.quantile(h, 1 - frac)
scales = np.logspace(-0.5, 0.5, 15)
act_fixed = [(h * s > theta).mean() for s in scales]
ax.plot(scales, act_fixed, "o-", color=P.edge("negative"), ms=3.5, lw=1.6, label="fixed threshold (no APL)")
ax.plot(scales, np.full_like(scales, frac), "o-", color=P.edge("positive"), ms=3.5, lw=1.6,
        label="APL feedback (k winners)")
ax.set_xscale("log")
ax.set_xlabel("PN input scale (concentration)")
ax.set_ylabel("Fraction of KCs active")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("B  Sparseness held by inhibition", loc="left", fontsize=10)

ax = axs[2]
centres = rng.normal(size=(20, nPN)) * 2
X = np.repeat(centres, 30, axis=0) + rng.normal(size=(600, nPN))
X = np.clip(X, 0, None)
Xc = X - X.mean(axis=1, keepdims=True)
D = ((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)
queries = rng.choice(600, 100, replace=False)
nn = 20


def precision(dist):
    out = []
    for q in queries:
        true = np.argsort(D[q])[1: nn + 1]
        d = dist[q].copy()
        d[q] = np.inf
        got = np.argsort(d + 1e-9 * rng.random(600))[:nn]
        out.append(len(np.intersect1d(true, got)) / nn)
    return np.mean(out)


ks = [4, 8, 16, 32, 64]
fly, lsh = [], []
for kk in ks:
    H = kwta(Xc @ W.T, kk)
    fly.append(precision(-(H @ H.T)))
    G = rng.normal(size=(nPN, kk))
    Y = Xc @ G
    lsh.append(precision(((Y[:, None, :] - Y[None, :, :]) ** 2).sum(-1)))
ax.plot(ks, fly, "o-", color=P.edge("rna"), lw=1.8, ms=4, label="fly hash (expand, k winners)")
ax.plot(ks, lsh, "s-", color=P.edge("dna"), lw=1.8, ms=4, label="dense LSH (k projections)")
ax.set_xscale("log", base=2)
ax.set_xlabel("Hash length k")
ax.set_ylabel("Precision of 20 nearest neighbours")
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("C  Similarity search", loc="left", fontsize=10)
fig.tight_layout()
