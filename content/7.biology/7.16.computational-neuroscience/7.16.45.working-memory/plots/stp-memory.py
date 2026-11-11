"""Synaptic working memory based on short-term facilitation (Mongillo, Barak and Tsodyks, 2008).

Mean-field network of P excitatory clusters (one per memory item) and one inhibitory pool
(Mi, Katkov and Tsodyks, 2017; Formula 45.4.1):
  tau dh_a/dt = -h_a + J_EE u_a x_a R_a - J_EI R_I + I_b + I_a(t),   R_a = alpha ln(1 + exp(h_a / alpha)),
  tau dh_I/dt = -h_I + J_IE sum_a R_a,   R_I = [h_I]_+,
  du_a/dt = (U - u_a) / tau_f + U (1 - u_a) R_a,     dx_a/dt = (1 - x_a) / tau_d - u_a x_a R_a,
tau = 8 ms, tau_f = 1.5 s, tau_d = 0.3 s, U = 0.3, J_EE = 8, J_EI = 1.1, J_IE = 1.75,
alpha = 1.5 (rates in Hz). Two clusters; item 1 is loaded by a 30 ms input (I = 40) at t = 0.1 s.
A: background I_b = -3: after the cue the network returns to a silent state; the facilitation
   u of the loaded cluster stays elevated for about tau_f. Nonspecific readout pulses to both
   clusters (I = 6 for 30 ms at t = 1.0 and 2.2 s) reactivate only the loaded cluster, in a brief
   population spike, which also refreshes u.
B: synaptic efficacy u x of the two clusters in A.
C: background I_b = -1: the loaded cluster reactivates spontaneously in periodic population
   spikes, maintaining the memory without readout signals.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
tau, tauf, taud, U, JEE, JEI, JIE, alpha = 0.008, 1.5, 0.3, 0.3, 8.0, 1.1, 1.75, 1.5
dt = 0.0002


def simulate(Ib, T, inputs, nc=2):
    h = np.zeros(nc)
    hI = 0.0
    u = np.full(nc, U)
    x = np.ones(nc)
    n = int(T / dt)
    out = np.zeros((n // 10, 3, nc))
    for s in range(n):
        t = s * dt
        I = np.zeros(nc)
        for t0, d, amp, who in inputs:
            if t0 <= t < t0 + d:
                I[who] += amp
        R = alpha * np.logaddexp(0.0, h / alpha)
        RI = max(hI, 0.0)
        dh = (-h + JEE * u * x * R - JEI * RI + Ib + I) / tau
        dhI = (-hI + JIE * R.sum()) / tau
        du = (U - u) / tauf + U * (1 - u) * R
        dxx = (1 - x) / taud - u * x * R
        h += dt * dh
        hI += dt * dhI
        u += dt * du
        x += dt * dxx
        if s % 10 == 0:
            out[s // 10] = (R, u, u * x)
    return np.arange(n // 10) * dt * 10, out


load = [(0.1, 0.03, 40.0, [0])]
readout = [(1.0, 0.03, 6.0, [0, 1]), (2.2, 0.03, 6.0, [0, 1])]
tA, A = simulate(-3.0, 3.0, load + readout)
tC, C = simulate(-1.0, 3.0, load)

fig, axs = plt.subplots(3, 1, figsize=(10, 7.2), sharex=True)
cols = [P.edge("dna"), P.edge("neutral")]
ax = axs[0]
for c in range(2):
    ax.plot(tA, A[:, 0, c], color=cols[c], lw=1.4, label=f"Cluster {c + 1}" + (" (loaded)" if c == 0 else ""))
ax2 = ax.twinx()
ax2.plot(tA, A[:, 1, 0], color=P.edge("negative"), lw=1.6, ls="--", label="$u$, cluster 1")
ax2.set_ylabel("Facilitation $u$", color=P.edge("negative"))
ax2.set_ylim(0, 1)
for t0, *_ in load + readout:
    ax.axvline(t0, color=P.muted(), lw=0.8, ls=":")
ax.text(0.12, 60, "cue", fontsize=8)
ax.text(1.02, 60, "readout", fontsize=8)
ax.text(2.22, 60, "readout", fontsize=8)
ax.set_ylabel("Rate / Hz")
ax.set_title("A  Activity-silent memory, $I_b = -3$", loc="left", fontsize=10)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, loc="upper right")
ax = axs[1]
for c in range(2):
    ax.plot(tA, A[:, 2, c], color=cols[c], lw=1.8, label=f"Cluster {c + 1}")
ax.set_ylabel("Efficacy $ux$")
ax.set_title("B  Synaptic efficacy holds the memory", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax = axs[2]
for c in range(2):
    ax.plot(tC, C[:, 0, c], color=cols[c], lw=1.4)
ax.set_ylabel("Rate / Hz")
ax.set_xlabel("Time / s")
ax.set_title("C  Periodic reactivation, $I_b = -1$", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
