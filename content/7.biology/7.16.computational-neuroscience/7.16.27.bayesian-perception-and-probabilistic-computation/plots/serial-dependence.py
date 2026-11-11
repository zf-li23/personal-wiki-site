"""Serial dependence as inference with a prior on the continuity of the world.

Orientation task: the stimulus s and the previous stimulus s_prev = s + delta; the observer measures
x = s + noise (s.d. sigma) and uses the prior (1 - q) N(0, 200^2) + q N(s_prev, tau^2) with q = 0.3,
tau = 10 deg: with probability q the previous stimulus is informative about the present one.
The estimate is the posterior mean. A: errors of 3000 simulated trials against delta (sigma = 8 deg),
with the binned mean. B: mean error against delta for sigma = 4, 8 and 16 deg: the bias is attractive
for small differences, peaks at a difference of 15-30 degrees and vanishes for large differences, with a
derivative-of-Gaussian shape; it is stronger for noisier observations.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
q, tau, s0 = 0.3, 10.0, 200.0


def gauss(x, m, v):
    return np.exp(-(x - m) ** 2 / (2 * v)) / np.sqrt(2 * np.pi * v)


def estimate(x, sp, sigma):
    w1 = q * gauss(x, sp, sigma ** 2 + tau ** 2)
    w0 = (1 - q) * gauss(x, 0.0, sigma ** 2 + s0 ** 2)
    m1 = (x / sigma ** 2 + sp / tau ** 2) / (1 / sigma ** 2 + 1 / tau ** 2)
    m0 = x / (1 + sigma ** 2 / s0 ** 2)
    return (w1 * m1 + w0 * m0) / (w1 + w0)


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.1))
ax = axs[0]
n = 3000
dl = rng.uniform(-60, 60, n)
s = rng.uniform(-60, 60, n)
x = s + rng.normal(0, 8, n)
err = estimate(x, s + dl, 8.0) - s
ax.plot(dl, err, ".", color=P.fill("dna"), ms=2.5)
edges = np.linspace(-60, 60, 25)
c = 0.5 * (edges[1:] + edges[:-1])
bm = [err[(dl >= a) & (dl < b)].mean() for a, b in zip(edges[:-1], edges[1:])]
ax.plot(c, bm, "o-", color=P.edge("rna"), lw=2, ms=4, label="binned mean")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlabel("Previous minus current orientation / deg")
ax.set_ylabel("Error (estimate - stimulus) / deg")
ax.set_ylim(-25, 25)
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Single trials (sigma = 8 deg)", loc="left", fontsize=10)

ax = axs[1]
dd = np.linspace(-60, 60, 49)
for sg, col in ((4, P.edge("dna")), (8, P.edge("protein")), (16, P.edge("rna"))):
    b = []
    for d in dd:
        s = rng.uniform(-30, 30, 6000)
        x = s + rng.normal(0, sg, 6000)
        b.append((estimate(x, s + d, sg) - s).mean())
    ax.plot(dd, b, color=col, lw=2, label=f"sigma = {sg} deg")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlabel("Previous minus current orientation / deg")
ax.set_ylabel("Mean error / deg")
ax.legend(frameon=False, fontsize=8)
ax.set_title("B  Bias against previous stimulus", loc="left", fontsize=10)
fig.tight_layout()
