"""What an extracellular electrode sees. A: amplitude of the spike of a single neuron as a function of
distance d from a point current source, V(d) = V_1 * (d_1/d) with a soma-level amplitude of 300 uV at
d_1 = 20 um (a conductor of conductivity 0.3 S/m: V = I/(4 pi sigma d)), against the detection
threshold 4.5 sigma for noise sigma = 15 uV. B: number of neurons within distance d for the cell
density of mouse cortex (9 x 10^4 per mm^3), compared with the number of neurons whose spikes exceed
the threshold (d < d_max) and the number that can be sorted (a larger amplitude, 8 sigma)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
d = np.logspace(np.log10(10), np.log10(300), 200)
V = 300 * 20 / d
sigma = 15.0
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.6))
fig.subplots_adjust(wspace=0.32, left=0.08, right=0.98, bottom=0.17, top=0.9)
ax = axs[0]
ax.loglog(d, V, color=charts.line("neuron"), lw=1.8)
for k, lab, tok in [(4.5, "detection 4.5 σ", "highlight"), (8, "sorting 8 σ", "negative")]:
    ax.axhline(k * sigma, color=charts.line(tok), lw=1, ls="--")
    dm = 6000 / (k * sigma)
    ax.plot([dm], [k * sigma], "o", ms=4, color=charts.line(tok))
    ax.text(300, k * sigma * 1.08, f"{lab}: d < {dm:.0f} µm", ha="right", va="bottom", fontsize=FT["tiny"], color=charts.line(tok))
charts.style_axes(ax, "distance d / µm", "spike amplitude / µV")
charts.title(ax, "A  Amplitude falls as 1/d")
ax = axs[1]
rho = 9e4 / 1e9  # per um^3
N = 4 / 3 * np.pi * d**3 * rho
ax.loglog(d, N, color=charts.line("neutral"), lw=1.8, label="neurons within d")
for k, tok in [(4.5, "highlight"), (8, "negative")]:
    dm = 6000 / (k * sigma)
    n = 4 / 3 * np.pi * dm**3 * rho
    ax.plot([dm], [n], "o", ms=5, color=charts.line(tok))
    ax.text(dm * 1.1, n * 0.55, f"{n:.0f}", fontsize=FT["tiny"], color=charts.line(tok), va="top")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "distance d / µm", "number of neurons")
charts.title(ax, "B  Cells in range grow as d³")
