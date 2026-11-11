"""Opponent-process model of tolerance and withdrawal (after Solomon and Corbit 1974).

A drug exposure (1 h) evokes a primary a-process a(t) (fast, tau_a = 0.1 h, amplitude 1 while present)
and a sluggish opposing b-process: tau_b db/dt = -b + k a, tau_b = 1.5 h.
The gain k grows with repeated exposure, k_n = 2.7 (1 - 0.8^n), modeling neuroadaptation.
Net effect = a - b. Panels show exposure 1 and exposure 10.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.01
t = np.arange(-1, 8, dt)


def episode(k):
    a = np.zeros_like(t)
    b = np.zeros_like(t)
    for i in range(1, len(t)):
        drive = 1.0 if 0 <= t[i] < 1 else 0.0
        a[i] = a[i - 1] + dt / 0.1 * (drive - a[i - 1])
        b[i] = b[i - 1] + dt / 1.5 * (-b[i - 1] + k * a[i - 1])
    return a, b


fig, axs = plt.subplots(1, 2, figsize=(10, 3.6), sharey=True)
for ax, n, letter in zip(axs, [1, 10], "AB"):
    k = 2.7 * (1 - 0.8 ** n)
    a, b = episode(k)
    ax.axvspan(0, 1, color=P.light("highlight"), zorder=0)
    ax.plot(t, a, color=P.edge("dna"), lw=1.4, ls="--", label="a-process")
    ax.plot(t, -b, color=P.edge("negative"), lw=1.4, ls="--", label="b-process (opposing)")
    ax.plot(t, a - b, color=P.ink(), lw=2.2, label="net effect")
    ax.axhline(0, color=P.muted(), lw=0.8)
    ax.set_title(f"{letter}  Exposure {n} (gain $k = {k:.2f}$)", loc="left", fontsize=10)
    ax.set_xlabel("Time from exposure onset / h")
    ax.grid(True, alpha=0.3)
axs[0].set_ylabel("Effect (arbitrary units)")
axs[1].legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
