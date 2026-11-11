"""Behavioral time scale synaptic plasticity (BTSP): one plateau potential creates a place field.

A CA1 neuron receives 200 inputs on a track; each input i is active at a preferred time t_i of a
8 s lap (Gaussian, sigma = 0.25 s, running at constant speed), so time and position are
interchangeable. Each synapse keeps a slow eligibility trace of its own presynaptic activity
(decay tau_ET = 1.5 s) and the cell has an instructive signal, a trace of the dendritic plateau
potential (plateau of 0.4 s at t_0 = 5 s, trace decay tau_IS = 0.8 s). The weight change in one
lap is proportional to the overlap of the two traces,
  Delta w_i = eta (w_max - w_i) * integral ET_i(t) IS(t) dt,
with w_max = 1 and the initial weight 0.1. Synapses active up to about 3 s before the plateau
and 1 s after it are potentiated: the kernel is asymmetric and wider on the "before" side.
A: the eligibility trace of one input (preferred time 3.5 s), the instructive signal and their
   product.
B: the learned kernel, the weight against preferred time after the single plateau.
C: the membrane-potential-like output (sum of weighted inputs) in the lap before and after the
   plateau: a field appears whose peak precedes the plateau time (dashed line).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.01
t = np.arange(0, 8.0, dt)
ti = np.linspace(0, 8, 200)
sig, tauET, tauIS, t0, dur = 0.25, 1.5, 0.8, 5.0, 0.4
a = np.exp(-(t[None, :] - ti[:, None]) ** 2 / (2 * sig**2))  # inputs x time


def trace(sig_t, tau):
    out = np.zeros_like(sig_t)
    d = np.exp(-dt / tau)
    for k in range(1, len(sig_t)):
        out[k] = out[k - 1] * d + sig_t[k] * dt / tau
    return out


plateau = ((t >= t0) & (t < t0 + dur)).astype(float)
IS = trace(plateau, tauIS)
IS /= IS.max()
ET = np.array([trace(row, tauET) for row in a])
ET /= ET.max()
overlap = (ET * IS[None, :]).sum(axis=1) * dt
eta = 1.0 / overlap.max() * 0.95
w0 = 0.1
w1 = w0 + eta * (1 - w0) * overlap

fig, axs = plt.subplots(1, 3, figsize=(13, 3.8))
ax = axs[0]
k = np.argmin(abs(ti - 3.5))
ax.plot(t, a[k], color=P.muted(), lw=1.0, ls=":", label="input activity")
ax.plot(t, ET[k], color=P.edge("dna"), lw=2.0, label="eligibility trace")
ax.plot(t, IS, color=P.edge("negative"), lw=2.0, label="instructive signal")
ax.fill_between(t, 0, ET[k] * IS, color=P.fill("highlight"), alpha=0.8, label="overlap")
ax.axvspan(t0, t0 + dur, color=P.edge("negative"), alpha=0.12, lw=0)
ax.set_xlabel("Time in lap / s")
ax.set_ylabel("Trace (normalized)")
ax.set_title("A  Two slow traces", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7.5, loc="upper left")

ax = axs[1]
ax.plot(ti, w1, color=P.edge("positive"), lw=2.2)
ax.axhline(w0, color=P.muted(), lw=0.8, ls=":")
ax.axvline(t0 + dur / 2, color=P.edge("negative"), lw=1.0, ls="--")
ax.text(t0 + dur / 2 + 0.1, 0.9 * w1.max(), "plateau", fontsize=8, color=P.edge("negative"))
ax.set_xlabel("Preferred time of the input / s")
ax.set_ylabel("Weight after one lap")
ax.set_title("B  Learned kernel", loc="left", fontsize=10)

ax = axs[2]
before = (w0 * a).sum(axis=0)
after = (w1[:, None] * a).sum(axis=0)
ax.plot(t, before, color=P.muted(), lw=1.8, label="before")
ax.plot(t, after, color=P.edge("protein"), lw=2.2, label="after")
ax.axvline(t0 + dur / 2, color=P.edge("negative"), lw=1.0, ls="--")
ax.axvline(t[after.argmax()], color=P.edge("protein"), lw=0.9, ls=":")
ax.set_xlabel("Time in lap / s")
ax.set_ylabel("Summed input (arb.)")
ax.set_title("C  Place field", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")
for x in axs:
    x.grid(True, alpha=0.3)
fig.tight_layout()
