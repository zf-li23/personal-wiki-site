"""Training a spiking neuron with a surrogate gradient.

A discrete-time LIF neuron (dt = 1 ms, tau_m = 20 ms, beta = exp(-dt / tau_m)) receives 100 frozen
Poisson inputs (10 Hz, 500 ms), filtered by synaptic currents (tau_s = 5 ms):
  v[t+1] = beta v[t] + (1 - beta) W i[t] - theta s[t],  s[t] = H(v[t] - theta), theta = 1.
Target: 8 spikes at fixed times. Loss: van Rossum distance, L = 1/2 sum_t (f_out - f_target)^2, where f
is the spike train filtered with a 10 ms exponential kernel. The Heaviside step has zero derivative almost
everywhere; backpropagation through time replaces dH/dv by the fast-sigmoid surrogate
  sigma'(v) = 1 / (1 + 10 |v - theta|)^2   (Zenke and Ganguli 2018),
with the reset treated as a constant. Plain gradient descent on W, 400 iterations, step 0.002; initial weights N(0.3, 0.3^2).
A: the step function and the surrogate derivative. B: output spike raster every 25 iterations (red ticks:
target). C: the loss.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(2)
nin, T = 100, 500
beta = np.exp(-1 / 20.0)
syn = np.exp(-1 / 5.0)
kern = np.exp(-1 / 10.0)
spk_in = (rng.random((T, nin)) < 0.01).astype(float)
I = np.zeros((T, nin))
acc = np.zeros(nin)
for t in range(T):
    acc = syn * acc + spk_in[t]
    I[t] = acc
target_times = np.array([40, 95, 150, 210, 270, 330, 400, 460])
s_tgt = np.zeros(T)
s_tgt[target_times] = 1


def filt(s):
    f = np.zeros(T)
    a = 0.0
    for t in range(T):
        a = kern * a + s[t]
        f[t] = a
    return f


f_tgt = filt(s_tgt)


def surrogate(v):
    return 1.0 / (1.0 + 10.0 * np.abs(v - 1.0)) ** 2


def forward(W):
    v = np.zeros(T)
    s = np.zeros(T)
    x = 0.0
    drive = (1 - beta) * I @ W
    for t in range(T):
        v[t] = x
        s[t] = float(x >= 1.0)
        x = beta * x + drive[t] - s[t]
    return v, s


W = rng.normal(0.3, 0.3, nin)
losses, rasters = [], []
for it in range(401):
    v, s = forward(W)
    err = filt(s) - f_tgt
    losses.append(0.5 * np.sum(err ** 2))
    if it % 25 == 0:
        rasters.append(np.nonzero(s)[0])
    # dL/ds[t] = sum_{t' >= t} err[t'] kern^(t' - t)
    gs = np.zeros(T)
    a = 0.0
    for t in range(T - 1, -1, -1):
        a = kern * a + err[t]
        gs[t] = a
    # backward through v[t+1] = beta v[t] + drive[t] - s[t] (reset detached)
    gv = np.zeros(T)
    nxt = 0.0
    for t in range(T - 1, -1, -1):
        gv[t] = gs[t] * surrogate(v[t]) + beta * nxt
        nxt = gv[t]
    # drive[t] enters v[t+1]
    gW = (1 - beta) * (I[:-1].T @ gv[1:])
    W -= 0.002 * gW

fig, axs = plt.subplots(1, 3, figsize=(13.5, 3.9), gridspec_kw={"width_ratios": [1, 1.6, 1]})
ax = axs[0]
vv = np.linspace(-0.5, 2.5, 400)
ax.plot(vv, (vv >= 1).astype(float), color=P.edge("dna"), lw=1.8, label="spike $H(V - \\theta)$")
ax.plot(vv, surrogate(vv), color=P.edge("negative"), lw=1.8, label="surrogate derivative")
ax.set_xlabel("Membrane potential $V$ (units of $\\theta$)")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("A  Step and surrogate", loc="left", fontsize=10)
ax.grid(True, alpha=0.3)
ax = axs[1]
for k, sp in enumerate(rasters):
    ax.vlines(sp, k + 0.6, k + 1.4, color=P.ink(), lw=1.0)
for tt in target_times:
    ax.axvline(tt, color=P.edge("negative"), lw=0.8, alpha=0.6)
ax.set_xlim(0, T)
ax.set_ylim(0.3, len(rasters) + 0.7)
ax.set_yticks([1, 5, 9, 13, 17])
ax.set_yticklabels(["0", "100", "200", "300", "400"])
ax.set_xlabel("Time / ms")
ax.set_ylabel("Iteration")
ax.set_title("B  Output spikes during training (red: target)", loc="left", fontsize=10)
ax = axs[2]
ax.semilogy(losses, color=P.edge("protein"), lw=1.6)
ax.set_xlabel("Iteration")
ax.set_ylabel("van Rossum loss")
ax.set_title("C  Loss", loc="left", fontsize=10)
ax.grid(True, alpha=0.3)
fig.tight_layout()
