"""Phasor diagrams for a single slit: N equal phasors whose total phase spread is 2 alpha."""

import numpy as np
import matplotlib.pyplot as plt

N = 60
cases = [(0.0, "α = 0"), (0.5 * np.pi, "α = π/2"), (np.pi, "α = π  (dark)"),
         (1.430 * np.pi, "α = 1.43π  (1st secondary max)")]

fig, axes = plt.subplots(1, 4, figsize=(10.0, 3.0))
for ax, (alpha, title) in zip(axes, cases):
    dphi = 2 * alpha / N
    steps = np.exp(1j * dphi * np.arange(N)) / N      # total length 1 (= E0)
    pts = np.concatenate([[0], np.cumsum(steps)])
    ax.plot(pts.real, pts.imag, color="C0", lw=1.6)
    ax.annotate("", xy=(pts[-1].real, pts[-1].imag), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color="C3", lw=1.4))
    ax.plot(0, 0, "o", color="0.4", ms=3)
    amp = abs(pts[-1])
    ax.set_title(f"{title}\nE_P / E0 = {amp:.3f}", fontsize=8.5)
    ax.set_aspect("equal")
    ax.set_xlim(-0.22, 1.05)
    ax.set_ylim(-0.08, 0.70)
    ax.axis("off")
fig.tight_layout()
