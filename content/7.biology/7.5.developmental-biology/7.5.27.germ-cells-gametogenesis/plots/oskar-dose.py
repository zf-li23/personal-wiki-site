"""Pole-cell number against the number of copies of oskar in the mother (about 12.5, 35 and 50 pole cells for
1, 2 and 4 copies; 0 without functional oskar). A Hill curve through the three points (N_max = 55, K = 1.6
copies, n = 2.6) is sigmoidal: a threshold for assembling functional pole plasm at low dose and saturation at
high dose. The dashed curve is the logarithmic law of a threshold read on an exponential profile (Example 27.2.1)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
c = np.array([0, 1, 2, 4.0])
N = np.array([0, 12.5, 35, 50])
Nmax, K, n = 54.69, 1.601, 2.585
x = np.linspace(0, 6, 300)
fig, ax = plt.subplots(figsize=(5.6, 3.6))
fig.subplots_adjust(left=0.13, right=0.97, bottom=0.16, top=0.9)
ax.plot(x, Nmax * x**n / (K**n + x**n), color=charts.line("protein"), lw=1.8, label="Hill fit, n = 2.6")
a, c0 = 22.5 / np.log(2), np.exp(-12.5 / (22.5 / np.log(2)))
xl = np.linspace(c0, 6, 200)
ax.plot(xl, a * np.log(xl / c0), color=P_.muted(), lw=1.3, ls="--", label="threshold on exponential profile")
ax.plot(c, N, "o", color=charts.line("negative"), ms=6, zorder=5, label="observed")
ax.axhline(Nmax, color=P_.muted(), lw=0.7, ls=":")
ax.set_xlim(0, 6)
ax.set_ylim(0, 75)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(ax, r"copies of $\it{oskar}$ in the mother", "pole cells per embryo")
charts.title(ax, "Pole plasm dose and germ-cell number")
