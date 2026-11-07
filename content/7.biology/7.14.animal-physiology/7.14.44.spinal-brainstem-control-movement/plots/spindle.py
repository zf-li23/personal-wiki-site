"""Muscle spindle afferents during a ramp-and-hold stretch (phenomenological model).

Stretch: 6 mm in 0.25 s, held for 1 s, released in 0.25 s.
Firing rate r = max(0, r0 + k_s * L + k_d * sign(v) |v|^0.5) (impulses/s; L in mm, v in mm/s),
low-pass filtered with tau = 20 ms. The square-root velocity term follows the power-law
velocity sensitivity of primary endings.
Primary (Ia): r0 = 20, k_s = 4, k_d = 9; with dynamic gamma drive k_d is doubled (and r0 = 30);
with static gamma drive k_s = 8, k_d = 5, r0 = 40.
Secondary (II): r0 = 15, k_s = 5, k_d = 1 (gamma effects not shown).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 1e-3
t = np.arange(0, 2.2, dt)
t0, tr, th = 0.3, 0.25, 1.0
L = 6 * (np.clip((t - t0) / tr, 0, 1) - np.clip((t - t0 - tr - th) / tr, 0, 1))
v = np.gradient(L, dt)


def rate(r0, ks, kd):
    r = np.clip(r0 + ks * L + kd * np.sign(v) * np.sqrt(np.abs(v)), 0, None)
    y = np.zeros_like(r)
    y[0] = r[0]
    for i in range(1, len(r)):
        y[i] = y[i - 1] + dt * (r[i] - y[i - 1]) / 0.02
    return y


fig, axs = plt.subplots(3, 1, figsize=(9, 6.6), sharex=True,
                        gridspec_kw={"height_ratios": [0.8, 2, 1.4]})
axs[0].plot(t, L, color=P.ink(), lw=1.8)
axs[0].set_ylabel("Stretch / mm")
axs[0].set_title("A  Ramp-and-hold stretch", loc="left", fontsize=10)
for (r0, ks, kd), c, lab in (((20, 4, 9), P.edge("rna"), "Ia, no gamma drive"),
                             ((30, 4, 18), P.edge("protein"), r"Ia, dynamic $\gamma$"),
                             ((40, 8, 5), P.edge("enzyme"), r"Ia, static $\gamma$")):
    axs[1].plot(t, rate(r0, ks, kd), color=c, lw=1.8, label=lab)
axs[1].set_ylabel("Rate / (impulses/s)")
axs[1].legend(frameon=False, fontsize=8, loc="upper right")
axs[1].set_title("B  Primary ending: length + velocity", loc="left", fontsize=10)
axs[2].plot(t, rate(15, 5, 1), color=P.edge("dna"), lw=1.8, label="II (secondary)")
axs[2].set_ylabel("Rate / (impulses/s)")
axs[2].legend(frameon=False, fontsize=8, loc="upper right")
axs[2].set_title("C  Secondary ending: mostly length", loc="left", fontsize=10)
axs[2].set_xlabel("Time / s")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
