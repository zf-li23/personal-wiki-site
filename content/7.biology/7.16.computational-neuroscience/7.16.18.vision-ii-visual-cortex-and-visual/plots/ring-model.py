"""The ring model of orientation selectivity (recurrent amplification, Dayan and Abbott 7.4).

tau_r dr(theta)/dt = -r + [h(theta) + int_{-pi/2}^{pi/2} (dtheta'/pi) (-lam0 + lam1 cos 2(theta - theta')) r(theta')]_+
Input: h(theta) = A c (1 - eps + eps cos 2 theta), A = 40 Hz, eps = 0.1 (weakly tuned feedforward input).
Recurrent weights: lam0 = 7.3 (uniform inhibition), lam1 = 11 (tuned excitation).
Integrated to steady state with Euler steps (tau_r = 10 ms); N = 120 neurons.
A: input h(theta) at four contrasts. B: steady-state network responses (sharp, contrast-invariant width).
C: the same curves normalized to their maxima, with the normalized input for comparison.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
N = 120
th = np.linspace(-np.pi / 2, np.pi / 2, N, endpoint=False)
dth = np.pi / N
A, eps, lam0, lam1 = 40.0, 0.1, 7.3, 11.0
Wm = (-lam0 + lam1 * np.cos(2 * (th[:, None] - th[None, :]))) * dth / np.pi


def steady(c):
    h = A * c * (1 - eps + eps * np.cos(2 * th))
    r = np.zeros(N)
    dt, tau = 0.0005, 0.01
    for _ in range(6000):
        r += dt / tau * (-r + np.maximum(h + Wm @ r, 0))
    return h, r


cs = (0.1, 0.2, 0.4, 0.8)
cols = [P.mix(P.edge("dna"), P.edge("rna"), j / 3) for j in range(4)]
res = [steady(c) for c in cs]
deg = np.degrees(th)
fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
for (h, r), c, col in zip(res, cs, cols):
    axs[0].plot(deg, h, color=col, lw=1.6, label=f"contrast {c}")
    axs[1].plot(deg, r, color=col, lw=1.8, label=f"contrast {c}")
    axs[2].plot(deg, r / r.max(), color=col, lw=1.8)
h, _ = res[-1]
axs[2].plot(deg, (h - h.min()) / (h.max() - h.min()), color=P.muted(), lw=1.2, ls="--",
            label="input (rescaled to 0-1)")
axs[0].set_ylabel("Input h / Hz")
axs[0].set_ylim(0, 45)
axs[0].legend(frameon=False, fontsize=8, loc="upper center", ncol=2)
axs[0].set_title("A  Weakly tuned input", loc="left", fontsize=10)
axs[1].set_ylabel("Steady rate r / Hz")
axs[1].legend(frameon=False, fontsize=8)
axs[1].set_title("B  Network output", loc="left", fontsize=10)
axs[2].set_ylabel("Normalized rate")
axs[2].legend(frameon=False, fontsize=8, loc="upper right")
axs[2].set_title("C  Contrast-invariant tuning width", loc="left", fontsize=10)
for ax in axs:
    ax.set_xlabel("Orientation relative to preferred / deg")
    ax.set_xticks([-90, -45, 0, 45, 90])
fig.tight_layout()
