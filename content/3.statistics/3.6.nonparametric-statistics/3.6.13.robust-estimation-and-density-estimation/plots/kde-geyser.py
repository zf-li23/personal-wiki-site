"""Density estimates for bimodal waiting times: kernel estimates with three bandwidths (A) and a
comparison of the kernel, local linear and k-nearest-neighbor estimators (B). The sample (n = 272)
is simulated from a two-component normal mixture close to the one fitted to the Old Faithful
waiting times; the R companion uses the real data set faithful$waiting."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 272
first = rng.random(n) < 0.361
x = np.where(first, rng.normal(54.6, 5.87, n), rng.normal(80.1, 5.87, n))
grid = np.linspace(30, 110, 400)


def kde(t, data, h):
    u = (t[:, None] - data[None, :]) / h
    return np.exp(-u**2 / 2).sum(axis=1) / (len(data) * h * np.sqrt(2 * np.pi))


def local_linear_density(t, data, h, delta=0.5):
    # Bin the data finely, then fit a kernel-weighted local line to the bin heights.
    edges = np.arange(data.min() - delta, data.max() + 2 * delta, delta)
    counts, _ = np.histogram(data, bins=edges)
    centers = (edges[:-1] + edges[1:]) / 2
    heights = counts / (len(data) * delta)
    out = np.empty_like(t)
    for j, t0 in enumerate(t):
        d = centers - t0
        w = np.exp(-(d / h) ** 2 / 2)
        s0, s1, s2 = w.sum(), (w * d).sum(), (w * d * d).sum()
        out[j] = ((s2 * w - s1 * w * d) * heights).sum() / (s0 * s2 - s1**2)
    return out


def knn_density(t, data, k):
    dk = np.sort(np.abs(t[:, None] - data[None, :]), axis=1)[:, k - 1]
    return k / (2 * len(data) * dk)


s = x.std(ddof=1)
iqr = np.subtract(*np.percentile(x, [75, 25]))
h0 = 0.9 * min(s, iqr / 1.34) * n ** (-0.2)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
ax = axes[0]
ax.hist(x, bins=np.arange(40, 101, 4), density=True, color="0.8", edgecolor="0.6")
for h, color, label in [(1.0, "C1", "h = 1 (undersmoothed)"),
                        (h0, "C0", f"h = {h0:.1f} (rule of thumb)"),
                        (10.0, "C2", "h = 10 (oversmoothed)")]:
    ax.plot(grid, kde(grid, x, h), color=color, lw=1.7, label=label)
ax.set_title("A. Gaussian kernel, three bandwidths", fontsize=10)
ax.legend(fontsize=8, loc="upper left")

ax = axes[1]
ax.plot(grid, kde(grid, x, h0), color="C0", lw=1.8, label="kernel estimate")
ax.plot(grid, local_linear_density(grid, x, h0), color="C3", lw=1.6, ls="--",
        label="local linear estimate")
ax.plot(grid, knn_density(grid, x, 50), color="C2", lw=1.4, ls=":", label="k-NN estimate, k = 50")
ax.axhline(0, color="0.4", lw=0.8)
ax.set_title("B. three estimators", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
for ax in axes:
    ax.plot(x, np.full_like(x, -0.002), "|", color="0.4", ms=5, alpha=0.5)
    ax.set_xlim(30, 110)
    ax.set_ylim(-0.006, 0.075)
    ax.set_xlabel("waiting time / min")
    ax.set_ylabel("density")
    ax.grid(alpha=0.3)
fig.tight_layout()
