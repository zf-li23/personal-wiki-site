"""A firing-rate model of the dorsal horn gate (after Melzack and Wall 1965, with later revisions).

Projection neuron T and inhibitory interneuron I (rates, tau = 10 ms, rectified-linear):
  tau dI/dt = -I + [w_AI A + D - w_CI C]_+,   tau dT/dt = -T + [w_AT A + w_CT C - g w_IT I]_+
A = Abeta (touch) input, C = C/Adelta (nociceptive) input, D = descending drive to the interneuron.
w_AI = 1.0, w_CI = 0.1, w_AT = 0.8, w_CT = 1.0, w_IT = 2.0; g scales inhibition (1 = normal).
A: steady output of T against C input with no touch, with touch (rubbing, A = 20 Hz) and with
descending drive (D = 15 Hz). B: response of T to touch alone (A from 0 to 40 Hz): normally the gate
stays closed; with inhibition reduced to g = 0.2 (disinhibition after nerve injury) touch alone
drives the pain-projection neuron (allodynia). C: wind-up: a train of C-fibre volleys at 1 Hz;
each volley adds a slow NMDA-like depolarization (decay 3 s) that raises the efficacy of the next.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
wAI, wCI, wAT, wCT, wIT = 1.0, 0.1, 0.8, 1.0, 2.0


def steady(A, C, D=0.0, g=1.0):
    I = np.clip(wAI * A + D - wCI * C, 0, None)
    return np.clip(wAT * A + wCT * C - g * wIT * I, 0, None)


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
ax = axs[0]
C = np.linspace(0, 60, 300)
for A, D, c, lab in ((0, 0, P.edge("negative"), "noxious input only"), (20, 0, P.edge("dna"), "plus touch (rubbing)"),
                     (0, 15, P.edge("positive"), "plus descending drive")):
    ax.plot(C, steady(A, C, D), color=c, lw=2, label=lab)
ax.set_xlabel("Nociceptive input C / Hz")
ax.set_ylabel("Projection neuron T / Hz")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Closing the gate", loc="left", fontsize=10)

ax = axs[1]
A = np.linspace(0, 40, 300)
for g, c, lab in ((1.0, P.edge("dna"), "normal inhibition"), (0.2, P.edge("negative"), "disinhibited (g = 0.2)")):
    ax.plot(A, steady(A, 0.0, g=g), color=c, lw=2, label=lab)
ax.set_xlabel("Touch input A / Hz")
ax.set_ylabel("Projection neuron T / Hz")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("B  Disinhibition and allodynia", loc="left", fontsize=10)

ax = axs[2]
dt = 0.001
t = np.arange(0, 16, dt)
n_stim = 16
times = np.arange(n_stim) * 1.0 + 0.5
u = np.zeros_like(t)  # slow depolarization (NMDA-like)
out = []
uu = 0.0
for k, tk in enumerate(t):
    uu -= dt * uu / 3.0
    if np.any(np.abs(tk - times) < dt / 2):
        resp = 5.0 * (1 + 1.5 * uu)  # spikes per volley grow with the slow depolarization
        out.append(resp)
        uu += 0.25
    u[k] = uu
ax.bar(times, out, width=0.5, color=P.fill("negative"), edgecolor=P.edge("negative"))
ax2 = ax.twinx()
ax2.plot(t, u, color=P.edge("protein"), lw=1.4)
ax2.set_ylabel("Slow depolarization (a.u.)", color=P.edge("protein"))
ax2.tick_params(axis="y", colors=P.edge("protein"))
ax.set_xlabel("Time / s (C-fibre volleys at 1 Hz)")
ax.set_ylabel("Spikes per volley")
ax.set_title("C  Wind-up", loc="left", fontsize=10)
fig.tight_layout()
