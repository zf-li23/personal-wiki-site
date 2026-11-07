"""Rapid and slow adaptation to a ramp-and-hold indentation (schematic models).

Stimulus: indentation ramps up in 10 ms, is held for 400 ms and released in 10 ms.
Generator potential (normalised):
  intact Pacinian corpuscle: the capsule is an effective high pass (tau = 3 ms);
    the ending responds to the magnitude of core displacement, so it fires at onset and offset;
  capsule removed: the bare ending follows the indentation, with slow viscous creep
    (40 % decline, tau = 150 ms), and has no off response;
  slowly adapting ending (Merkel / Ruffini type): low pass (tau = 15 ms) plus a small dynamic term.
Spike encoder: leaky integrate-and-fire with a spike-triggered adaptation current
  (tau_m = 5 ms, threshold 1, reset 0, refractory 1.5 ms); the adaptation is strong at the
  Pacinian first node (increment 4, tau_a = 200 ms) and weak in the slowly adapting ending
  (increment 0.1, tau_a = 300 ms). Drive = 3.5 x generator potential.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 5e-5
t = np.arange(0, 0.55, dt)
on, hold, rise = 0.05, 0.40, 0.01
x = np.clip((t - on) / rise, 0, 1) - np.clip((t - on - rise - hold) / rise, 0, 1)


def lowpass(u, tau):
    y = np.zeros_like(u)
    for i in range(1, len(u)):
        y[i] = y[i - 1] + dt * (u[i] - y[i - 1]) / tau
    return y


def highpass(u, tau):
    return u - lowpass(u, tau)


core = highpass(x, 3e-3)
g_intact = np.abs(core) / np.abs(core).max()
g_bare = x * (0.6 + 0.4 * (1 - lowpass(x, 0.15))) / 1.0
g_sa = lowpass(x, 0.015) + 0.4 * np.clip(highpass(lowpass(x, 0.003), 0.03), 0, None)
g_sa /= g_sa.max()


def lif(g, inc, tau_a, gain=3.5, tau_m=5e-3, ref=1.5e-3):
    v = a = 0.0
    last = -1.0
    spikes = []
    for i, ti in enumerate(t):
        a -= dt * a / tau_a
        if ti - last < ref:
            continue
        v += dt * (-v + gain * g[i] - a) / tau_m
        if v >= 1.0:
            spikes.append(ti)
            v = 0.0
            a += inc
            last = ti
    return np.array(spikes)


cases = [
    ("Pacinian, intact", g_intact, (4.0, 0.2), P.edge("rna")),
    ("Pacinian, capsule removed", g_bare, (4.0, 0.2), P.edge("dna")),
    ("Slowly adapting ending", g_sa, (0.1, 0.3), P.edge("enzyme")),
]

fig, axs = plt.subplots(3, 1, figsize=(10, 6.4), sharex=True,
                        gridspec_kw={"height_ratios": [0.7, 2, 1.3]})
axs[0].plot(t * 1e3, x, color=P.ink(), lw=1.8)
axs[0].set_ylabel("Indentation")
axs[0].set_yticks([])
axs[0].set_title("A  Ramp-and-hold stimulus", loc="left", fontsize=10)
for k, (name, g, (inc, ta), c) in enumerate(cases):
    axs[1].plot(t * 1e3, g + 1.3 * (2 - k), color=c, lw=1.8)
    axs[1].text(120, 1.3 * (2 - k) + 0.12, name, fontsize=8, color=c, ha="left", va="bottom")
    sp = lif(g, inc, ta)
    axs[2].vlines(sp * 1e3, 2 - k + 0.1, 2 - k + 0.9, color=c, lw=1.2)
axs[1].set_ylabel("Generator potential")
axs[1].set_yticks([])
axs[1].set_title("B  Receptor (generator) potential", loc="left", fontsize=10)
axs[2].set_yticks([2.5, 1.5, 0.5])
axs[2].set_yticklabels(["intact", "decapsulated", "slowly adapting"], fontsize=8)
axs[2].set_ylim(0, 3)
axs[2].set_xlabel("Time / ms")
axs[2].set_title("C  Action potentials", loc="left", fontsize=10)
axs[2].set_xlim(0, 560)
for a in axs:
    a.grid(True, axis="x", alpha=0.3)
fig.tight_layout()
