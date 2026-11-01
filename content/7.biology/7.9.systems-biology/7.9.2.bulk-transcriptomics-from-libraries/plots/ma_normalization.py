"""Normalization of microarray intensities (simulated two-colour array, 5000 genes, 3% of them truly
changed by a factor of 4 in either direction). A: the M-A plot before normalization, M = log2(R/G),
A = (log2 R + log2 G)/2; an intensity-dependent dye bias bends the cloud, and the LOWESS curve
(locally weighted linear regression, span 0.3) estimates it. B: after subtracting the LOWESS curve the
unchanged genes are centred on M = 0 at every intensity. C, D: quantile normalization of four
single-channel arrays. When the arrays differ only technically (C, densities of log2 intensities
before, thin, and after, thick), it makes the distributions identical; when 30% of the genes truly
rise twofold in arrays 3 and 4 (D), forcing identical distributions moves the reference: the changed
genes (log2 fold change 1, dashed) appear to rise less and the unchanged genes appear to fall
(medians after normalization shown)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)


def lowess(x, y, span=0.3, grid=60):
    # locally weighted linear regression with tricube weights, evaluated on a grid then interpolated
    g = np.quantile(x, np.linspace(0.01, 0.99, grid))
    k = int(span * len(x))
    fit = []
    for g0 in g:
        d = np.abs(x - g0)
        h = np.partition(d, k)[k]
        w = np.clip(1 - (d / h) ** 3, 0, None) ** 3
        W = w.sum()
        mx, my = (w * x).sum() / W, (w * y).sum() / W
        b = (w * (x - mx) * (y - my)).sum() / (w * (x - mx) ** 2).sum()
        fit.append(my + b * (g0 - mx))
    return np.interp(x, g, fit), g, np.array(fit)


n = 5000
true = rng.normal(8, 1.8, n)
fc = np.zeros(n)
ch = rng.choice(n, 150, replace=False)
fc[ch] = rng.choice([-2, 2], 150)
lr = true + fc / 2 + rng.normal(0, 0.25, n)
lg = true - fc / 2 + rng.normal(0, 0.25, n)
lr = lr + 0.6 - 0.12 * (lr - 8) + 0.03 * (lr - 8) ** 2  # dye bias in the red channel
M, A = lr - lg, (lr + lg) / 2
fit, g, f = lowess(A, M)

fig, axs = plt.subplots(1, 4, figsize=(13, 3.4))
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.17, top=0.87, wspace=0.32)
isch = np.zeros(n, bool)
isch[ch] = True
for ax, MM, ttl in [(axs[0], M, "A  Before: M-A plot"), (axs[1], M - fit, "B  After LOWESS")]:
    ax.scatter(A[~isch], MM[~isch], s=2, color=P.fill("neutral"), lw=0)
    ax.scatter(A[isch], MM[isch], s=4, color=charts.line("rna"), lw=0)
    ax.axhline(0, color=P.muted(), lw=0.7)
    if MM is M:
        ax.plot(g, f, color=charts.line("dna"), lw=1.8)
    ax.set_ylim(-4, 4)
    charts.style_axes(ax, "A (mean log2 intensity)", "M (log2 ratio)")
    charts.title(ax, ttl)


def qnorm(Xa):
    order = np.argsort(Xa, axis=0)
    ref = np.sort(Xa, axis=0).mean(1)
    out = np.empty_like(Xa)
    for j in range(Xa.shape[1]):
        out[order[:, j], j] = ref
    return out


base = rng.normal(8, 1.8, n)
Xs = np.column_stack([base * s + o + rng.normal(0, 0.3, n) for s, o in [(1, 0), (1.1, -0.5), (0.9, 0.8), (1.05, 0.3)]])
Q = qnorm(Xs)
xx = np.linspace(0, 16, 300)
toks = ["dna", "rna", "enzyme", "protein"]
ax = axs[2]
for j in range(4):
    ax.plot(xx, stats.gaussian_kde(Xs[:, j])(xx), color=charts.line(toks[j]), lw=0.8)
ax.plot(xx, stats.gaussian_kde(Q[:, 0])(xx), color=P.ink(), lw=2.0)
charts.style_axes(ax, "log2 intensity", "density")
charts.title(ax, "C  Quantile normalization")

up = rng.random(n) < 0.3
Xg = np.column_stack([base + rng.normal(0, 0.3, n) for _ in range(4)])
Xg[up, 2:] += 1.0
Qg = qnorm(Xg)
lf_raw = Xg[:, 2:].mean(1) - Xg[:, :2].mean(1)
lf_q = Qg[:, 2:].mean(1) - Qg[:, :2].mean(1)
ax = axs[3]
bins = np.linspace(-1, 1.8, 57)
ax.hist(lf_raw[up], bins, color=P.fill("rna"), alpha=0.6, label="before")
ax.hist(lf_q[up], bins, color=P.fill("dna"), alpha=0.6, label="after")
ax.axvline(1, color=charts.line("rna"), lw=1, ls="--")
ax.text(0.03, 0.9, f"median after: {np.median(lf_q[up]):.2f}\nunchanged: {np.median(lf_q[~up]):.2f}",
        transform=ax.transAxes, fontsize=7.5, color=P.ink())
ax.legend(frameon=False, fontsize=7, loc="upper right")
ax.set_ylim(0, ax.get_ylim()[1] * 1.35)
charts.style_axes(ax, "log2 fold change (truly changed genes)", "number of genes")
charts.title(ax, "D  When many genes shift")
