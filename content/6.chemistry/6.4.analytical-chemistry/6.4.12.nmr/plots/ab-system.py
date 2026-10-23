"""Spectrum of two coupled spin-1/2 nuclei (AB system, J = 8 Hz) as the chemical shift
difference dnu shrinks from 10 J (first order, AX) to 0 (A2: a single line).
Exact line positions: center +- (D +- J)/2 with D = sqrt(dnu^2 + J^2); inner lines have
relative intensity 1 + J/D, outer lines 1 - J/D (the roof effect)."""

import numpy as np
import matplotlib.pyplot as plt

J = 8.0
ratios = [10, 4, 2, 1, 0.5, 0]
x = np.linspace(-60, 60, 6001)
w = 0.9

fig, ax = plt.subplots(figsize=(7.5, 6.4))
for k, r in enumerate(ratios):
    dnu = r * J
    D = np.hypot(dnu, J)
    lines = [(-(D + J) / 2, 1 - J / D), (-(D - J) / 2, 1 + J / D),
             ((D - J) / 2, 1 + J / D), ((D + J) / 2, 1 - J / D)]
    y = np.zeros_like(x)
    for p, a in lines:
        y += a * (w / 2)**2 / ((x - p)**2 + (w / 2)**2)
    off = 2.4 * (len(ratios) - 1 - k)
    ax.plot(x, off + y / 2, color="k", lw=1.0)
    label = "A$_2$ (dnu = 0)" if r == 0 else f"dnu/J = {r:g}"
    ax.text(58, off + 0.25, label, ha="right", fontsize=9)
    if r > 0:
        for s in (-1, 1):
            ax.plot([s * dnu / 2] * 2, [off - 0.2, off - 0.05], color="C3", lw=1.2)
ax.set_xlim(60, -60)
ax.set_yticks([])
ax.set_xlabel("frequency offset / Hz")
ax.text(-58, 2.4 * (len(ratios) - 1) + 1.4, "red ticks: chemical shifts of A and B",
        fontsize=8, color="C3", ha="right")
fig.tight_layout()
