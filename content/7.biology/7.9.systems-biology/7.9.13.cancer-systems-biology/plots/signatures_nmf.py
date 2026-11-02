"""Recovering mutational signatures by non-negative matrix factorization (simulation). Four
illustrative signatures over the 96 substitution classes (6 base changes of the pyrimidine of the
mutated pair, each in 16 contexts of the 5' and 3' neighbors) are mixed in 100 tumors with sparse
gamma-distributed exposures (44 to 5949 mutations per tumor, median 1332), and counts are drawn from
the Poisson distribution. A: the true signatures (black outline) and the signatures recovered by NMF
with rank 4 (bars, colored by base change), with their cosine similarities. B: true and estimated
numbers of mutations attributed to each signature in each tumor (logarithmic axes). C: choice of the
rank: the Poisson deviance of the best of 10 factorizations against the rank k (it drops until k = 4
and then barely changes)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
classes = ["C>A", "C>G", "C>T", "T>A", "T>C", "T>G"]
bases = "ACGT"
ctx = [(c, a + ("C" if c[0] == "C" else "T") + b) for c in classes for a in bases for b in bases]
n_feat = len(ctx)


def signature(weights):
    w = np.array([weights(c, x) for c, x in ctx], float) + 0.02
    return w / w.sum()


true = np.array([
    signature(lambda c, x: 6.0 if c == "C>T" and x[2] == "G" else 0.3 * (c == "C>T")),           # clock-like CpG
    signature(lambda c, x: 3.0 if c == "C>A" else (0.6 if c in ("C>T", "T>A") else 0.2)),        # tobacco-like
    signature(lambda c, x: 5.0 if c == "C>T" and x[0] in "CT" else (0.8 if c == "C>T" else 0.1)),  # UV-like
    signature(lambda c, x: 5.0 if c in ("C>T", "C>G") and x[0] == "T" and x[2] in "AT" else 0.15),  # APOBEC-like
]).T
names = ["clock-like (C>T at CpG)", "tobacco-like (C>A)", "UV-like (C>T at dipyrimidines)",
         "APOBEC-like (TCW)"]
n_tum, K = 100, 4
H_true = rng.gamma(1.0, 600, (K, n_tum)) * (rng.random((K, n_tum)) < 0.5)
H_true[0] += rng.gamma(2.0, 100, n_tum)            # every tumor carries the clock-like process
M = rng.poisson(true @ H_true)


def nmf(M, k, iters=600, seed=0):
    """Lee-Seung multiplicative updates for the Kullback-Leibler (Poisson) objective."""
    r = np.random.default_rng(seed)
    W = r.random((M.shape[0], k)) + 0.1
    H = r.random((k, M.shape[1])) * M.sum(0) / k
    for _ in range(iters):
        WH = W @ H + 1e-12
        H *= (W.T @ (M / WH)) / W.sum(0)[:, None]
        WH = W @ H + 1e-12
        W *= ((M / WH) @ H.T) / H.sum(1)[None, :]
        s = W.sum(0)
        W /= s
        H *= s[:, None]
    WH = W @ H + 1e-12
    dev = 2 * np.sum(np.where(M > 0, M * np.log(np.maximum(M, 1) / WH), 0) - M + WH)
    return W, H, dev


ranks = range(1, 8)
fits = {k: min((nmf(M, k, seed=s) for s in range(10)), key=lambda f: f[2]) for k in ranks}
W, H, _ = fits[K]
cos = (true / np.linalg.norm(true, axis=0)).T @ (W / np.linalg.norm(W, axis=0))
row, col = linear_sum_assignment(-cos)
W, H = W[:, col], H[col]
sims = cos[row, col]

cols = [charts.line(t) for t in ("dna", "neutral", "negative", "highlight", "positive", "rna")]
bar_col = [cols[i // 16] for i in range(n_feat)]
fig = plt.figure(figsize=(11, 5.6))
gs = fig.add_gridspec(4, 2, width_ratios=[2.3, 1], left=0.05, right=0.98, bottom=0.1, top=0.93,
                      hspace=0.45, wspace=0.18)
for j in range(K):
    ax = fig.add_subplot(gs[j, 0])
    ax.bar(np.arange(n_feat), W[:, j], color=bar_col, width=0.8)
    ax.step(np.arange(n_feat + 1) - 0.5, np.r_[true[:, j], true[-1, j]], where="post", color=P.ink(), lw=0.7)
    ax.set_xlim(-0.5, n_feat - 0.5)
    ax.set_xticks([])
    charts.style_axes(ax, None, "fraction" if j == 0 else None)
    ax.text(0.99, 0.82, f"{names[j]}; cosine {sims[j]:.3f}", transform=ax.transAxes, ha="right",
            fontsize=7, color=P.ink())
    if j == 0:
        charts.title(ax, "A  True (outline) and recovered (bars) signatures")
    if j == K - 1:
        for i, c in enumerate(classes):
            ax.text(16 * i + 7.5, -0.18 * ax.get_ylim()[1], c, ha="center", va="top", fontsize=7, color=cols[i])
axB = fig.add_axes([0.73, 0.58, 0.25, 0.35])
for j in range(K):
    keep = H_true[j] > 0
    axB.loglog(H_true[j][keep], H[j][keep], "o", ms=2.5, color=cols[[2, 0, 4, 3][j]], alpha=0.8,
               label=names[j].split(" (")[0])
axB.legend(fontsize=6, frameon=False, loc="upper left", markerscale=1.5)
lim = [20, 2e4]
axB.plot(lim, lim, color=P.muted(), lw=0.8, ls="--")
axB.set_xlim(lim)
axB.set_ylim(lim)
charts.style_axes(axB, "true exposure", "estimated exposure")
charts.title(axB, "B  Exposures per tumor")
axC = fig.add_axes([0.73, 0.1, 0.25, 0.3])
devs = [fits[k][2] for k in ranks]
axC.semilogy(list(ranks), devs, "o-", color=P.ink(), ms=3.5, lw=1.2)
axC.axvline(K, color=P.muted(), ls=":", lw=0.8)
charts.style_axes(axC, "rank k", "Poisson deviance")
charts.title(axC, "C  Choosing the rank")
