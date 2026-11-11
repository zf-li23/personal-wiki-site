"""Synchronization of two leaky integrate-and-fire neurons by an electrical synapse.

tau_m dV_i/dt = -(V_i - E_L) + R I_i + R g_c (V_j - V_i) (units: mV, ms; tau_m = 20 ms,
E_L = -65 mV, threshold -50 mV, reset -65 mV, R = 100 MOhm). The two neurons receive slightly
different constant currents (0.20 and 0.205 nA). A spike is modeled as a brief suprathreshold
excursion: the spiking cell's voltage is treated as +20 mV for 1 ms before reset, so that the
junction transmits a depolarizing spikelet and the after-reset hyperpolarization.
A: without coupling (g_c = 0) the neurons drift in phase.
B: with g_c = 2 nS (coupling coefficient about 0.17) they lock in phase.
C: phase of neuron 2 relative to neuron 1 (fraction of the cycle, wrapped to -0.5..0.5; positive
means neuron 2 lags) at each spike of neuron 1.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt, T = 0.02, 800.0
tau, EL, Vth, Vr, R = 20.0, -65.0, -50.0, -65.0, 0.1  # R in GOhm (nA * GOhm = V -> use mV: *1000)
I = np.array([0.20, 0.205])


def run(gc):
    n = int(T / dt)
    V = np.array([-60.0, -55.0])
    hold = np.zeros(2)
    trace = np.zeros((n, 2))
    spikes = [[], []]
    for k in range(n):
        Veff = np.where(hold > 0, 20.0, V)
        dV = (-(V - EL) + R * 1000 * I + R * gc * (Veff[::-1] - V)) / tau
        V = np.where(hold > 0, V, V + dt * dV)
        hold = np.maximum(hold - dt, 0)
        for i in range(2):
            if hold[i] == 0 and V[i] >= Vth:
                hold[i] = 1.0
                V[i] = Vr
                spikes[i].append(k * dt)
        trace[k] = np.where(hold > 0, 20.0, V)
    return trace, spikes


fig = plt.figure(figsize=(12, 5.2))
gs = fig.add_gridspec(2, 2, width_ratios=[2.2, 1])
tt = np.arange(int(T / dt)) * dt
res = {}
for row, gc in enumerate((0.0, 2.0)):
    tr, sp = run(gc)
    res[gc] = sp
    ax = fig.add_subplot(gs[row, 0])
    ax.plot(tt, tr[:, 0], color=P.edge("dna"), lw=1.0, label="neuron 1")
    ax.plot(tt, tr[:, 1], color=P.edge("negative"), lw=1.0, label="neuron 2")
    ax.set_xlim(0, 400)
    ax.set_ylabel("V / mV")
    ax.set_title(("A  Uncoupled" if gc == 0 else "B  Coupled, $g_{\\mathrm{c}}$ = 2 nS"), loc="left", fontsize=10)
    ax.grid(True, alpha=0.3)
    if row == 0:
        ax.legend(frameon=False, fontsize=8, loc="lower right", ncol=2, bbox_to_anchor=(1.0, 1.0))
    else:
        ax.set_xlabel("Time / ms")
ax = fig.add_subplot(gs[:, 1])
for gc, c in ((0.0, P.muted()), (2.0, P.edge("positive"))):
    s1, s2 = np.array(res[gc][0]), np.array(res[gc][1])
    ph = []
    for a, b in zip(s1[:-1], s1[1:]):
        nxt = s2[(s2 >= a) & (s2 < b)]
        if len(nxt):
            d = (nxt[0] - a) / (b - a)
            ph.append(d - 1.0 if d > 0.5 else d)
    ax.plot(np.arange(len(ph)), ph, "o-", ms=3, color=c, lw=1.2, label=f"$g_{{\\mathrm{{c}}}}$ = {gc:.0f} nS")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-0.55, 0.55)
ax.set_xlabel("Cycle of neuron 1")
ax.set_ylabel("Phase lag of neuron 2 / cycle")
ax.set_title("C  Phase locking", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
ax.grid(True, alpha=0.3)
fig.tight_layout()
