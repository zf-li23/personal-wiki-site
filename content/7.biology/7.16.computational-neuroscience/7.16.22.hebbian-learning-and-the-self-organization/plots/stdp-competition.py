"""Competition under spike-timing-dependent plasticity (after Song, Miller and Abbott 2000).

One integrate-and-fire neuron (tau_m = 20 ms, rest -70 mV, threshold -54 mV, reset -60 mV, excitatory reversal 0 mV)
receives 200 excitatory inputs with exponential conductances (tau_s = 5 ms), each a Poisson train at 15 Hz. Inputs
1-100 form a correlated group: they copy spikes of a common Poisson train (15 Hz) with probability c = 0.2 and fire
independently at 12 Hz otherwise (rate 15 Hz in total); inputs 101-200 are independent. Weights lie in [0, g_max] with
g_max = 0.05 (in units of the leak conductance). Pair-based STDP with all-to-all interactions:
  w += A_plus g_max exp(-dt/tau) for a pre spike before a post spike, w -= A_minus g_max exp(-dt/tau) for post before pre,
tau = 20 ms, A_plus = 0.005, A_minus = 1.2 A_plus (Song et al. used 1.05 with 1000 inputs; fewer, stronger inputs need stronger depression) (net depression: A_minus > A_plus). Initial weights 0.5 g_max with 5 % noise.
Time step 1 ms, 600 s (one point of the traces every 5 s).
A: weights at the end, by input number. B: mean weight of the correlated and uncorrelated groups against time.
C: STDP window.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(2)
N, Nc = 200, 100
dt, T = 1.0, 600_000  # ms
tau_m, tau_s, tau = 20.0, 5.0, 20.0
Vr, Vth, Vre, Ee = -70.0, -54.0, -60.0, 0.0
gmax, Ap = 0.05, 0.005
Am = 1.2 * Ap
rate, c = 15e-3, 0.2  # per ms

w = gmax * 0.5 * (1 + 0.05 * rng.normal(size=N))
V, ge = Vr, 0.0
xpre = np.zeros(N)  # pre-synaptic trace
ypost = 0.0
trace_c, trace_u, ts = [], [], []
for t in range(T):
    common = rng.random() < rate
    spk = rng.random(N) < rate * (1 - c)
    if common:
        spk[:Nc] |= rng.random(Nc) < c
    xpre *= np.exp(-dt / tau)
    ypost *= np.exp(-dt / tau)
    if spk.any():
        ge += w[spk].sum()
        # pre after post: depression
        w[spk] = np.clip(w[spk] - Am * gmax * ypost, 0, gmax)
        xpre[spk] += 1.0
    ge -= ge * dt / tau_s
    V += dt * (-(V - Vr) - ge * (V - Ee)) / tau_m
    if V >= Vth:
        V = Vre
        w = np.clip(w + Ap * gmax * xpre, 0, gmax)
        ypost += 1.0
    if t % 5000 == 0:
        trace_c.append(w[:Nc].mean() / gmax)
        trace_u.append(w[Nc:].mean() / gmax)
        ts.append(t / 1000)

fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axs[0]
ax.bar(np.arange(N), w / gmax, width=1.0, color=[P.fill("dna")] * Nc + [P.fill("rna")] * (N - Nc))
ax.set_xlabel("Input number (1-100 correlated, 101-200 independent)")
ax.set_ylabel("Weight / $g_{\\max}$")
ax.set_title("A  Final weights", loc="left", fontsize=10)
bx = axs[1]
bx.plot(ts, trace_c, color=P.edge("dna"), lw=1.8, label="correlated group")
bx.plot(ts, trace_u, color=P.edge("rna"), lw=1.8, label="independent group")
bx.set_xlabel("Time (s)")
bx.set_ylabel("Mean weight / $g_{\\max}$")
bx.set_ylim(0, 1)
bx.legend(frameon=False, fontsize=8)
bx.set_title("B  The correlated group wins", loc="left", fontsize=10)
cx = axs[2]
s = np.linspace(-80, 80, 400)
Wd = np.where(s > 0, Ap * np.exp(-s / tau), -Am * np.exp(s / tau))
cx.plot(s[s > 0], Wd[s > 0], color=P.edge("positive"), lw=2)
cx.plot(s[s < 0], Wd[s < 0], color=P.edge("negative"), lw=2)
cx.axhline(0, color=P.muted(), lw=0.8)
cx.axvline(0, color=P.muted(), lw=0.8)
cx.set_xlabel(r"$t_{\mathrm{post}} - t_{\mathrm{pre}}$ (ms)")
cx.set_ylabel("Weight change / $g_{\\max}$")
cx.set_title("C  STDP window", loc="left", fontsize=10)
fig.tight_layout()
