"""Reconstructing a stimulus from spike trains with an optimal linear filter.

Stimulus: Gaussian noise low-pass filtered with an exponential kernel (time constant 30 ms),
5 ms bins, 80 s for fitting and 40 s for testing. Neurons: half ON, half OFF, rate
r_i(t) = [10 + g_i s(t - 20 ms)]_+ Hz with random gains |g_i| in 15..30 Hz per unit s.d., independent
Poisson spikes. Reconstruction s_est(t) = sum_i sum_tau K_i(tau) n_i(t - tau), spikes from 50 ms before to 100 ms after t, K fitted by ridge regression on the fitting data.
A: stimulus and its reconstruction from 1 and 20 neurons (test data). B: filters of the 20-neuron
decoder for one ON and one OFF neuron. C: test correlation coefficient against the number of neurons.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
dt = 0.005
lags = np.arange(-20, 11)   # bins: -100 ms .. +50 ms


def make(T, g):
    n = int(T / dt)
    x = rng.normal(size=n + 200)
    k = np.exp(-np.arange(200) * dt / 0.03)
    s = np.convolve(x, k)[200:200 + n]
    s = (s - s.mean()) / s.std()
    delay = 4
    drive = np.roll(s, delay)
    rate = np.maximum(10 + g[:, None] * drive[None, :], 0)
    spk = rng.poisson(rate * dt)
    return s, spk


def design(spk, N):
    cols = [np.roll(spk[i], l) for i in range(N) for l in lags]
    return np.array(cols).T.astype(float)


Nmax = 20
g = rng.uniform(15, 30, Nmax) * np.where(np.arange(Nmax) % 2 == 0, 1, -1)
s_tr, spk_tr = make(80, g)
s_te, spk_te = make(40, g)


def fit(N):
    idx = list(range(N))
    X = design(spk_tr[idx], N)
    m = X.mean(0)
    w = np.linalg.solve((X - m).T @ (X - m) + 50 * np.eye(X.shape[1]), (X - m).T @ (s_tr - s_tr.mean()))
    return w, m


def predict(N, w, m):
    return (design(spk_te[:N], N) - m) @ w


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1), gridspec_kw={"width_ratios": [1.5, 1, 1]})
ax = axs[0]
t = np.arange(len(s_te)) * dt
sel = (t > 10) & (t < 11.5)
ax.plot(t[sel], s_te[sel], color=P.ink(), lw=2, label="stimulus")
for N, c in ((1, P.edge("rna")), (20, P.edge("dna"))):
    w, m = fit(N)
    ax.plot(t[sel], predict(N, w, m)[sel], color=c, lw=1.4, label=f"{N} neuron" + ("s" if N > 1 else ""))
ax.set_xlabel("Time / s")
ax.set_ylabel("Stimulus (s.d. units)")
ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper center")
ax.set_ylim(-3.2, 3.8)
ax.set_title("A  Reconstruction", loc="left", fontsize=10)

ax = axs[1]
w, m = fit(20)
W = w.reshape(20, len(lags))
ax.plot(-lags * dt * 1e3, W[0], color=P.edge("rna"), lw=2, label="ON neuron")
ax.plot(-lags * dt * 1e3, W[1], color=P.edge("dna"), lw=2, label="OFF neuron")
ax.axvline(0, color=P.muted(), lw=0.6)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlabel("Spike time minus t / ms")
ax.set_ylabel("Filter weight")
ax.legend(frameon=False, fontsize=8)
ax.set_title("B  Decoding filters", loc="left", fontsize=10)

ax = axs[2]
Ns = [1, 2, 4, 8, 12, 16, 20]
cc = []
for N in Ns:
    w, m = fit(N)
    cc.append(np.corrcoef(predict(N, w, m), s_te)[0, 1])
ax.plot(Ns, cc, "o-", color=P.edge("dna"), lw=1.8, ms=4)
ax.set_xlabel("Number of neurons")
ax.set_ylabel("Correlation (test data)")
ax.set_ylim(0, 1)
ax.set_title("C  Quality against population size", loc="left", fontsize=10)
fig.tight_layout()
