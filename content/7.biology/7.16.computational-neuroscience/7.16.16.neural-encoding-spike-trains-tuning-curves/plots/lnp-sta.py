"""Recovering the filter and nonlinearity of a linear-nonlinear-Poisson (LNP) neuron by reverse correlation.

Stimulus: Gaussian white noise s(t) with 2 ms time steps, variance 1 per step.
Filter D(tau): biphasic, D(tau) = tau/a^2 exp(-tau/a) - 0.5 tau/b^2 exp(-tau/b), a = 15 ms, b = 30 ms.
Nonlinearity F(x) = 60 / (1 + exp(-(x - 1)/0.4)) Hz (sigmoid); spikes Poisson with rate F(D * s).
A: spike-triggered average (STA) from 200 s of data, rescaled, against the true filter (time reversed:
the STA at lag tau is the mean stimulus tau before a spike). B: the nonlinearity estimated as
P(spike | x) / dt from histograms of the filtered stimulus x, compared with the true F.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(3)
dt, Tdur = 0.002, 200.0
n = int(Tdur / dt)
s = rng.normal(0, 1, n)
lags = np.arange(0, 0.2, dt)
a, b = 0.015, 0.030
D = lags / a**2 * np.exp(-lags / a) - 0.5 * lags / b**2 * np.exp(-lags / b)
D /= np.linalg.norm(D)
x = np.convolve(s, D, mode="full")[:n]
F = lambda u: 60 / (1 + np.exp(-(u - 1) / 0.4))
spikes = rng.poisson(F(x) * dt)
idx = np.nonzero(spikes)[0]
idx = idx[idx >= len(lags)]
w = spikes[idx]
sta = np.array([(s[idx - k] * w).sum() / w.sum() for k in range(len(lags))])

fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axs[0]
scale = (sta @ D) / (D @ D)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.plot(lags * 1000, D * scale, color=P.muted(), lw=2.2, ls="--", label="true filter D(tau) (scaled)")
ax.plot(lags * 1000, sta, color=P.edge("dna"), lw=1.5,
        label=f"STA from {w.sum()} spikes")
ax.set_xlabel("Time before spike tau / ms")
ax.set_ylabel("Mean stimulus")
ax.legend(frameon=False, fontsize=8)
ax.set_title("A  The STA recovers the linear filter", loc="left", fontsize=10)

bx = axs[1]
xe = np.convolve(s, sta / np.linalg.norm(sta), mode="full")[:n]
edges = np.linspace(-3, 3.5, 30)
h_all, _ = np.histogram(xe, edges)
h_sp, _ = np.histogram(xe, edges, weights=spikes)
mid = 0.5 * (edges[1:] + edges[:-1])
ok = h_all > 400
bx.plot(mid[ok], h_sp[ok] / h_all[ok] / dt, "o", color=P.edge("rna"), ms=4,
        label="estimate: spikes per bin / time in bin")
uu = np.linspace(-3, 3.5, 200)
bx.plot(uu, F(uu), color=P.muted(), lw=2, ls="--", label="true nonlinearity F")
bx.set_xlabel("Filtered stimulus x = (D * s)(t)  (units of its SD)")
bx.set_ylabel("Firing rate / Hz")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  The static nonlinearity", loc="left", fontsize=10)
fig.tight_layout()
