"""Working memory capacity in the synaptic theory (Mi, Katkov and Tsodyks, 2017).

The mean-field network of stp-memory.py with P = 10 clusters and a high background input
I_b = 8, at which loaded clusters reactivate in periodic population spikes that take turns
(only one cluster can fire at a time because of the shared inhibition). Ten items are loaded one
after another (30 ms inputs I = 40, every 250 ms); an item counts as maintained if its cluster
still emits population spikes in the last 2 s of a 5 s simulation. All parameter sets are
simulated in parallel (vectorized), seed-free and deterministic.
A: number of maintained items against the depression time constant tau_d for two values of the
   synaptic time constant tau (8 ms and 4 ms): capacity grows with tau_d / tau.
B: rates of the ten clusters in the last second for tau = 8 ms, tau_d = 0.3 s: five items take
   turns in each cycle; the others have been lost.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
U, JEE, JEI, JIE, alpha, tauf, Ib = 0.3, 8.0, 1.1, 1.75, 1.5, 1.5, 8.0
Pn, T, dt = 10, 5.0, 0.0002
taud_vals = np.array([0.15, 0.2, 0.3, 0.45, 0.6])
taus = np.array([0.008, 0.004])
TD, TA = np.meshgrid(taud_vals, taus)
taud = TD.ravel()[:, None]
tau = TA.ravel()[:, None]
B = taud.shape[0]
h = np.zeros((B, Pn))
hI = np.zeros((B, 1))
u = np.full((B, Pn), U)
x = np.ones((B, Pn))
n = int(T / dt)
keep = int(2.0 / dt)
hist = np.zeros((keep // 5, B, Pn))
for s in range(n):
    t = s * dt
    I = np.zeros(Pn)
    k = int((t - 0.1) // 0.25)
    if 0 <= k < Pn and (t - 0.1 - 0.25 * k) < 0.03:
        I[k] = 40.0
    R = alpha * np.logaddexp(0.0, h / alpha)
    RI = np.maximum(hI, 0)
    dh = (-h + JEE * u * x * R - JEI * RI + Ib + I) / tau
    dhI = (-hI + JIE * R.sum(axis=1, keepdims=True)) / tau
    du = (U - u) / tauf + U * (1 - u) * R
    dx = (1 - x) / taud - u * x * R
    h += dt * dh
    hI += dt * dhI
    u += dt * du
    x += dt * dx
    j = s - (n - keep)
    if j >= 0 and j % 5 == 0:
        hist[j // 5] = R
spikes = np.diff((hist > 20).astype(int), axis=0) == 1
cap = (spikes.sum(axis=0) > 0).sum(axis=1).reshape(TA.shape)

fig, axs = plt.subplots(1, 2, figsize=(11, 3.9), gridspec_kw=dict(width_ratios=[1, 1.4]))
for i, (tv, c) in enumerate(zip(taus, (P.edge("dna"), P.edge("negative")))):
    axs[0].plot(taud_vals, cap[i], "o-", ms=5, lw=1.8, color=c, label=f"$\\tau$ = {tv * 1000:.0f} ms")
axs[0].set_xlabel("Depression time constant $\\tau_d$ / s")
axs[0].set_ylabel("Items maintained (of 10)")
axs[0].set_ylim(0, 10.5)
axs[0].set_title("A  Capacity grows with $\\tau_d/\\tau$", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="upper left")
idx = list(TD.ravel()).index(0.3)
tt = 3.0 + np.arange(hist.shape[0]) * dt * 5
sel = tt >= 4.0

for p in range(Pn):
    if hist[sel, idx, p].max() > 20:
        axs[1].plot(tt[sel], hist[sel, idx, p], lw=1.2, color=P.edge(P.protein(p % 8)), label=f"item {p + 1}")
axs[1].legend(frameon=False, fontsize=7, ncol=5, loc="upper center", bbox_to_anchor=(0.5, 1.0))
axs[1].set_xlabel("Time / s")
axs[1].set_ylabel("Rate / Hz")
axs[1].set_title("B  Items take turns ($\\tau$ = 8 ms, $\\tau_d$ = 0.3 s)", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
