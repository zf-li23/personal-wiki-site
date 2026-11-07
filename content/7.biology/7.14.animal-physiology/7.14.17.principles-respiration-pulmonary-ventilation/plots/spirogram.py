"""Lung volumes and capacities on a schematic spirogram (healthy young man, values in mL).

Tidal volume 500, inspiratory reserve 3000, expiratory reserve 1100, residual 1200; inspiratory capacity 3500,
functional residual capacity 2300, vital capacity 4600, total lung capacity 5800. Quiet breathing at 12 /min,
one maximal inspiration followed by a maximal expiration, then quiet breathing again. The spirometer
cannot measure the residual volume (it never leaves the lung).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
RV, ERV, TV, IRV = 1200, 1100, 500, 3000
FRC = RV + ERV
TLC = RV + ERV + TV + IRV

t = np.linspace(0, 40, 4000)
v = FRC + TV / 2 * (1 - np.cos(2 * np.pi * t / 5))
m1 = (t > 15) & (t < 25)
# maximal inspiration (15-19 s), maximal expiration (19-25 s)
s = t[m1]
up = s < 19
v[m1] = np.where(up, FRC + (TLC - FRC) * np.sin(np.pi / 2 * (s - 15) / 4),
                 RV + (TLC - RV) * (1 + np.cos(np.pi * (s - 19) / 6)) / 2)
m2 = t >= 25
v[m2] = RV + (FRC - RV) * (1 - np.exp(-(t[m2] - 25) / 0.8)) + TV / 2 * (1 - np.cos(2 * np.pi * (t[m2] - 25) / 5)) * (1 - np.exp(-(t[m2] - 25) / 0.8))

fig, ax = plt.subplots(figsize=(11, 4.8))
ax.plot(t, v, color=P.edge("dna"), lw=2)
for y in (RV, FRC, FRC + TV, TLC):
    ax.axhline(y, color=P.muted(), lw=0.7, ls=":", xmax=40 / 57 if y == FRC + TV else 1)


def bracket(x, y0, y1, text, side="right"):
    ax.annotate("", xy=(x, y0), xytext=(x, y1), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=1))
    ax.text(x + (0.4 if side == "right" else -0.4), (y0 + y1) / 2, text, fontsize=8.5,
            ha="left" if side == "right" else "right", va="center", color=P.ink())


bracket(3.2, FRC, FRC + TV, "TV 500")
bracket(9.5, FRC + TV, TLC, "IRV 3000")
bracket(9.5, RV, FRC, "ERV 1100")
bracket(9.5, 0, RV, "RV 1200")
bracket(41, FRC, TLC, "IC 3500")
bracket(44.5, 0, FRC, "FRC 2300")
bracket(48.5, RV, TLC, "VC 4600")
bracket(52.5, 0, TLC, "TLC 5800")
ax.text(25, 600, "residual volume: not measurable by spirometry", ha="center", fontsize=8, color=P.muted())
ax.set_xlim(0, 57)
ax.set_xticks(range(0, 41, 5))
ax.set_ylim(0, 6300)
ax.set_xlabel("Time / s")
ax.set_ylabel("Lung volume / mL")
ax.grid(True, axis="x", alpha=0.3)
fig.tight_layout()
