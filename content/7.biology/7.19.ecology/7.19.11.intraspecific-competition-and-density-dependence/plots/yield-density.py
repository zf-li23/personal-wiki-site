"""Constant final yield from the Shinozaki-Kira logistic theory (Section 11.4.1).

Biomass per unit area Y = d w grows logistically, dY/dt = lam Y (1 - Y/Ymax), with the same lam = 0.12 per
day and ceiling Ymax = 1000 g m^-2 at every sowing density d, from Y0 = d w0 (w0 = 1 g per seedling).
Then 1/w = A(t) + B(t) d with A = exp(-lam t)/w0 and B = (1 - exp(-lam t))/Ymax (Proposition 11.4.1).
A: log mean plant mass against log density at t = 20, 40, 60, 90 days (slope tends to -1).
B: yield per unit area against density. C: the reciprocal yield-density lines 1/w against d.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
lam, Ymax, w0 = 0.12, 1000.0, 1.0
d = np.geomspace(1, 1e4, 200)
times = [(20, C.line("neutral")), (40, C.line("rna")), (60, C.line("positive")), (90, C.line("dna"))]


def mean_mass(t, d):
    return 1 / (np.exp(-lam * t) / w0 + d * (1 - np.exp(-lam * t)) / Ymax)


fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.9))
for t, col in times:
    w = mean_mass(t, d)
    axes[0].plot(np.log10(d), np.log10(w), color=col, lw=2, label=f"day {t}")
    axes[1].plot(d, d * w, color=col, lw=2)
    dd = np.linspace(0, 400, 50)
    axes[2].plot(dd, 1 / mean_mass(t, dd), color=col, lw=2)
axes[0].plot([2.5, 4], [1.6, 0.1], color=P.muted(), lw=1, ls=(0, (4, 2)))
axes[0].text(3.3, 1.05, "slope −1", fontsize=FS["tiny"], color=P.muted())
C.style_axes(axes[0], "log₁₀ density (plants m⁻²)", "log₁₀ mean plant mass (g)")
axes[0].legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
C.title(axes[0], "A  Mass–density")
axes[1].set_xscale("log")
axes[1].axhline(Ymax, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
axes[1].text(1.5, Ymax * 1.03, "Y_max", fontsize=FS["tiny"], color=P.muted())
axes[1].set_ylim(0, 1100)
C.style_axes(axes[1], "density (plants m⁻², log scale)", "yield (g m⁻²)")
C.title(axes[1], "B  Constant final yield")
axes[2].set_ylim(0, 0.6)
C.style_axes(axes[2], "density d (plants m⁻²)", "1 / mean plant mass (g⁻¹)")
C.title(axes[2], "C  Reciprocal equation 1/w = A + Bd")
fig.tight_layout()
