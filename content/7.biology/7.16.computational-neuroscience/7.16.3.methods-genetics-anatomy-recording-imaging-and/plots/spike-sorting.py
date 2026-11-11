"""Spike sorting on a synthetic extracellular recording (Algorithm 3.3.1). Three neurons near a
tetrode-like probe with four channels fire as Poisson processes (8, 5 and 3 Hz, 2 ms refractory
period); each has its own spike waveform, with a different amplitude on each channel, and the
recording adds Gaussian noise (sd 20 uV). A: 300 ms of one channel with the detection threshold at
-4.5 times the robust noise estimate median(|x|)/0.6745. B: the detected waveforms projected on
their first two principal components, coloured by the cluster found by a Gaussian mixture model
fitted with EM (3 components). C: mean waveform of each cluster on the four channels. D:
autocorrelogram of the spike times of cluster 1: the empty bins at |lag| < 2 ms (refractoriness)
show that the cluster is a single unit."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(1)
fs = 20000.0
T = 80.0
n = int(T * fs)
tw = np.arange(-20, 40) / fs * 1000  # waveform time axis (ms), 3 ms window


def wave(depth, width):
    t = tw
    return -np.exp(-0.5 * (t / (0.12 * width)) ** 2) + 0.35 * np.exp(-0.5 * ((t - 0.5 * width) / (0.3 * width)) ** 2)


units = [  # rate, amplitudes on 4 channels (uV), width (ms)
    (8.0, np.array([160, 110, 60, 30]), 1.0),
    (5.0, np.array([60, 140, 150, 70]), 1.4),
    (3.0, np.array([40, 60, 110, 190]), 0.8),
]
x = rng.normal(0, 20, (4, n))
truth = []
for k, (rate, amp, width) in enumerate(units):
    times = []
    t = 0.0
    while True:
        t += 0.002 + rng.exponential(1 / rate)
        if t > T - 0.01:
            break
        times.append(t)
    times = np.array(times)
    truth.append(times)
    w = wave(0, width)
    for st in times:
        i = int(st * fs)
        x[:, i - 20:i + 40] += amp[:, None] * w[None, :]

sigma = np.median(np.abs(x[0])) / 0.6745
thr = -4.5 * sigma
# detect on the channel with the most negative value at each sample (min across channels)
xm = x.min(axis=0)
sig_all = np.median(np.abs(x), axis=1) / 0.6745
crossing = np.where((xm[1:] < -4.5 * sig_all.mean()) & (xm[:-1] >= -4.5 * sig_all.mean()))[0] + 1
peaks = []
last = -100
for c in crossing:
    if c - last < 30 or c < 30 or c > n - 50:
        continue
    p = c + np.argmin(xm[c:c + 15])
    peaks.append(p)
    last = p
peaks = np.array(peaks)
W = np.stack([x[:, p - 20:p + 40].ravel() for p in peaks])
Wc = W - W.mean(0)
U, S, Vt = np.linalg.svd(Wc, full_matrices=False)
F = Wc @ Vt[:2].T

# EM for a 3-component Gaussian mixture in the 2-D feature space
K = 3
mu = F[rng.choice(len(F), K, replace=False)]
from numpy.linalg import inv, det
cov = np.array([np.cov(F.T) for _ in range(K)])
pi = np.ones(K) / K
for it in range(200):
    L = np.zeros((len(F), K))
    for k in range(K):
        d = F - mu[k]
        L[:, k] = pi[k] * np.exp(-0.5 * np.einsum("ij,jk,ik->i", d, inv(cov[k]), d)) / np.sqrt(det(cov[k]))
    R = L / L.sum(1, keepdims=True)
    Nk = R.sum(0)
    pi = Nk / len(F)
    mu = (R.T @ F) / Nk[:, None]
    for k in range(K):
        d = F - mu[k]
        cov[k] = (R[:, k, None] * d).T @ d / Nk[k] + 1e-6 * np.eye(2)
lab = R.argmax(1)
order = np.argsort(-np.bincount(lab, minlength=K))
toks = ["neuron", "dna", "negative"]

fig = plt.figure(figsize=(10.4, 5.6))
gs = fig.add_gridspec(2, 3, hspace=0.5, wspace=0.35, left=0.07, right=0.98, bottom=0.09, top=0.93)
ax = fig.add_subplot(gs[0, :])
sel = slice(int(1.0 * fs), int(1.3 * fs))
tt = np.arange(n)[sel] / fs * 1000 - 1000
ax.plot(tt, x[0, sel], color=charts.line("neutral"), lw=0.6)
ax.axhline(thr, color=charts.line("highlight"), lw=1, ls="--")
ax.text(300, thr - 8, "threshold", fontsize=FT["tiny"], color=charts.line("highlight"), ha="right", va="top")
charts.style_axes(ax, "t / ms", "channel 1 / µV")
charts.title(ax, "A  Band-passed extracellular signal")

ax = fig.add_subplot(gs[1, 0])
for j, k in enumerate(order):
    m = lab == k
    ax.plot(F[m, 0], F[m, 1], ".", ms=2, color=charts.line(toks[j]), alpha=0.6)
charts.style_axes(ax, "PC 1", "PC 2")
ax.set_xticks([]); ax.set_yticks([])
charts.title(ax, "B  PCA features, 3 clusters")

ax = fig.add_subplot(gs[1, 1])
for j, k in enumerate(order):
    mw = W[lab == k].mean(0).reshape(4, -1)
    for ch in range(4):
        ax.plot(tw + ch * 3.3, mw[ch] - 0 * j, color=charts.line(toks[j]), lw=1.3)
ax.set_xticks([0, 3.3, 6.6, 9.9]); ax.set_xticklabels(["ch 1", "ch 2", "ch 3", "ch 4"])
charts.style_axes(ax, None, "mean waveform / µV")
charts.title(ax, "C  Cluster templates")

ax = fig.add_subplot(gs[1, 2])
st = peaks[lab == order[0]] / fs
d = (st[None, :] - st[:, None]).ravel() * 1000
d = d[(np.abs(d) < 25) & (d != 0)]
ax.hist(d, bins=np.arange(-25, 25.5, 1), color=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.5)
charts.style_axes(ax, "lag / ms", "count")
charts.title(ax, "D  Autocorrelogram, cluster 1")
