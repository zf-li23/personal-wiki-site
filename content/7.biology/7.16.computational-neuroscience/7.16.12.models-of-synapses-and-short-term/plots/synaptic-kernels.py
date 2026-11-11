"""Phenomenological synaptic conductance kernels and the PSPs they produce.

A: normalized conductance waveforms s(t) after a presynaptic spike at t = 0: exponential
(tau = 5 ms), alpha function (tau = 2 ms) and difference of exponentials (tau_r = 1 ms,
tau_d = 5 ms), each scaled to a peak of 1; the delta synapse is drawn as an arrow.
B: PSPs of a passive membrane (tau_m = 20 ms, C dV/dt = -g_L (V - E_L) - g_syn(t)(V - E_syn),
E_L = -65 mV, E_syn = 0 mV, g_L = 10 nS) for the same total charge-equivalent conductance
(integral of g_syn = 10 nS ms); the delta synapse gives an instantaneous jump followed by decay.
C: the same alpha-synapse input in a low-conductance state (g_L = 10 nS, tau_eff = 20 ms) and
in a high-conductance state with a tonic background conductance of 40 nS (tau_eff = 4 ms):
the PSP becomes smaller and briefer, which narrows the window of temporal summation.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.01
t = np.arange(-5, 80, dt)
s0 = np.clip(t, 0, None)
on = t >= 0
expk = np.exp(-s0 / 5.0) * on
alph = (s0 / 2.0) * np.exp(1 - s0 / 2.0) * on
dexp = (np.exp(-s0 / 5.0) - np.exp(-s0 / 1.0)) * on
dexp /= dexp.max()
kernels = [("exponential", expk, P.edge("dna")), ("alpha", alph, P.edge("protein")),
           ("difference of exponentials", dexp, P.edge("negative"))]

fig, axs = plt.subplots(1, 3, figsize=(13, 3.8))
ax = axs[0]
for nm, k, c in kernels:
    ax.plot(t, k, color=c, lw=2.0, label=nm)
ax.annotate("", xy=(0, 1.05), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.6))
ax.text(0.8, 1.0, "delta", fontsize=8, color=P.ink())
ax.set_xlim(-3, 30)
ax.set_xlabel("Time after presynaptic spike / ms")
ax.set_ylabel("s(t)")
ax.set_title("A  Conductance kernels", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

C, gL, EL, Es = 200.0, 10.0, -65.0, 0.0  # pF, nS, mV -> tau = 20 ms


def psp(g, gl=gL, extra=0.0):
    V = np.empty_like(t)
    v = EL
    for k in range(len(t)):
        v += dt / C * (-(gl) * (v - EL) - extra * (v - EL) - g[k] * (v - Es))
        V[k] = v
    return V


ax = axs[1]
Q = 10.0
for nm, k, c in kernels:
    g = Q * k / (k.sum() * dt)
    ax.plot(t, psp(g) - EL, color=c, lw=2.0, label=nm)
jump = Q * (Es - EL) / C
ax.plot(t, jump * np.exp(-s0 / 20.0) * on, color=P.ink(), lw=1.4, ls="--", label="delta")
ax.set_xlabel("Time / ms")
ax.set_ylabel("PSP / mV")
ax.set_title("B  PSPs, $\\tau_{\\mathrm{m}}$ = 20 ms", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

ax = axs[2]
g = 20.0 * alph
lo = psp(g) - EL
hi = psp(g, extra=40.0) - EL
ax.plot(t, lo, color=P.edge("dna"), lw=2.0, label="low conductance ($\\tau_{\\mathrm{eff}}$ = 20 ms)")
ax.plot(t, hi, color=P.edge("negative"), lw=2.0, label="high conductance ($\\tau_{\\mathrm{eff}}$ = 4 ms)")
ax.plot(t, hi * lo.max() / hi.max(), color=P.edge("negative"), lw=1.0, ls=":", label="high, rescaled")
ax.set_xlabel("Time / ms")
ax.set_ylabel("PSP / mV")
ax.set_title("C  Background conductance", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
