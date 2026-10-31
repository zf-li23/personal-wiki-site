# Kinetics from a single-molecule FRET trajectory with a hidden Markov model (simulation).
# A molecule switches between E = 0.30 (state 1) and E = 0.75 (state 2) with k12 = 2 /s and k21 = 1 /s,
# recorded with 20 ms frames, 150 photons per frame, until the acceptor bleaches at 200 s.
# A: donor and acceptor intensities. B: apparent efficiency per frame with the Viterbi path of a two-state
# Gaussian HMM fitted by the Baum-Welch algorithm. C: dwell-time histograms from the Viterbi path with
# exponential fits; rates recovered from the mean dwell times (true values in parentheses).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
dt, T, Tb = 0.02, 220.0, 200.0
k12, k21 = 2.0, 1.0
nf = int(T / dt)
# exact continuous-time switching, then frame averages of E
t, s, sw, st = 0.0, 0, [0.0], [0]
while t < T:
    t += rng.exponential(1 / (k12 if s == 0 else k21))
    s = 1 - s
    sw.append(t)
    st.append(s)
sw, st = np.array(sw), np.array(st)
edges = np.arange(nf + 1) * dt
fine = np.linspace(0, T, nf * 20, endpoint=False) + dt / 40
state_f = st[np.searchsorted(sw, fine, side="right") - 1]
Etrue = np.where(state_f == 0, 0.30, 0.75).reshape(nf, 20).mean(1)
tt = edges[:-1]
alive = tt < Tb
n = rng.poisson(150, nf)
nA = rng.binomial(n, Etrue)
nD = n - nA
nA = np.where(alive, nA, 0) + rng.poisson(4, nf)
nD = np.where(alive, nD, n) + rng.poisson(4, nf)
E = nA / (nA + nD)
obs = E[alive]

# Baum-Welch for a two-state Gaussian HMM (scaled forward-backward)
mu = np.array([0.2, 0.8])
sd = np.array([0.1, 0.1])
A = np.array([[0.95, 0.05], [0.05, 0.95]])
pi = np.array([0.5, 0.5])
for _ in range(40):
    B = np.exp(-(obs[:, None] - mu) ** 2 / (2 * sd**2)) / sd
    al = np.zeros((obs.size, 2))
    c = np.zeros(obs.size)
    al[0] = pi * B[0]
    c[0] = al[0].sum()
    al[0] /= c[0]
    for i in range(1, obs.size):
        al[i] = (al[i - 1] @ A) * B[i]
        c[i] = al[i].sum()
        al[i] /= c[i]
    be = np.ones((obs.size, 2))
    for i in range(obs.size - 2, -1, -1):
        be[i] = (A @ (B[i + 1] * be[i + 1])) / c[i + 1]
    g = al * be
    g /= g.sum(1, keepdims=True)
    xi = al[:-1, :, None] * A[None] * (B[1:] * be[1:])[:, None, :] / c[1:, None, None]
    A = xi.sum(0) / g[:-1].sum(0)[:, None]
    mu = (g * obs[:, None]).sum(0) / g.sum(0)
    sd = np.sqrt((g * (obs[:, None] - mu) ** 2).sum(0) / g.sum(0))
    pi = g[0]
# Viterbi
B = np.exp(-(obs[:, None] - mu) ** 2 / (2 * sd**2)) / sd
lA = np.log(A)
V = np.log(pi + 1e-300) + np.log(B[0])
back = np.zeros((obs.size, 2), int)
for i in range(1, obs.size):
    m = V[:, None] + lA
    back[i] = m.argmax(0)
    V = m.max(0) + np.log(B[i])
path = np.zeros(obs.size, int)
path[-1] = V.argmax()
for i in range(obs.size - 1, 0, -1):
    path[i - 1] = back[i, path[i]]

fig = plt.figure(figsize=(13.5, 6.2))
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.1])
ax = fig.add_subplot(gs[0, :])
ax.plot(tt, nD, color=charts.line("positive"), lw=0.6, label="donor")
ax.plot(tt, nA, color=charts.line("negative"), lw=0.6, label="acceptor")
ax.axvline(Tb, color=P.muted(), lw=0.8, ls=":")
ax.text(Tb + 0.3, 140, "acceptor\nbleaches", fontsize=8, color=P.muted())
ax.legend(fontsize=8, frameon=False, loc="upper left", ncol=2)
charts.style_axes(ax, "time / s", "photons per frame")
charts.title(ax, "A   Donor and acceptor intensities (20 ms frames)")
ax = fig.add_subplot(gs[1, :2])
ax.plot(tt[alive], obs, color=P.muted(), lw=0.6)
ax.plot(tt[alive], mu[path], color=charts.line("dna"), lw=1.4, label="Viterbi path")
ax.set_xlim(0, 25)
ax.set_ylim(0, 1)
ax.legend(fontsize=8, frameon=False, loc="upper right")
charts.style_axes(ax, "time / s", "apparent E")
charts.title(ax, f"B   HMM: E = {mu.min():.2f}, {mu.max():.2f}")
ax = fig.add_subplot(gs[1, 2])
lo = int(np.argmin(mu))
chg = np.flatnonzero(np.diff(path)) + 1
segs = np.split(path, chg)
lengths = {0: [], 1: []}
for sgm in segs[1:-1]:
    lengths[int(sgm[0] == lo)].append(sgm.size * dt)
for key, tok, lab, ktrue in ((1, "dna", "low-E state", k12), (0, "rna", "high-E state", k21)):
    d = np.array(lengths[key])
    kfit = 1 / d.mean()
    ax.hist(d, bins=np.arange(0, 4.0, 0.25), density=True, histtype="step", color=charts.line(tok), lw=1.4)
    x = np.linspace(0, 4, 100)
    ax.plot(x, kfit * np.exp(-kfit * x), color=charts.line(tok), lw=1.0, ls="--",
            label=f"{lab}: k = {kfit:.2f} s⁻¹ ({ktrue:g})")
ax.set_yscale("log")
ax.legend(fontsize=7, frameon=False)
charts.style_axes(ax, "dwell time / s", "density / s⁻¹")
charts.title(ax, "C   Dwell times give the rates")
fig.tight_layout()
