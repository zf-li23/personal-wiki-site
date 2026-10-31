"""Poiseuille flow in a pipe. A: parabolic velocity profile v(r) = (dp/4 eta l)(d^2/4 - r^2),
normalized by the mean velocity (maximum 2). B: volumetric flow rate Q = pi dp d^4/(128 eta l)
at fixed pressure drop, relative to a vessel of diameter d0: a 20 % narrowing (atherosclerotic
plaque) cuts the flow by 59 %. The resistance of a vessel bed is dominated by its narrowest
segments, the arterioles and capillaries."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(8.0, 3.1))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.97, bottom=0.18, top=0.87)

ax = axs[0]
r = np.linspace(-1, 1, 200)
v = 2 * (1 - r**2)
ax.fill_betweenx(r, 0, v, color=P.fill("blood"), alpha=0.3, lw=0)
ax.plot(v, r, color=charts.line("blood"), lw=1.7)
for rr in np.linspace(-0.85, 0.85, 7):
    vv = 2 * (1 - rr**2)
    ax.annotate("", (vv, rr), (0, rr), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=0.7))
ax.axhline(1, color=P.ink(), lw=2); ax.axhline(-1, color=P.ink(), lw=2)
ax.axvline(1, color=P.muted(), lw=0.7, ls="--"); ax.text(1.03, -0.15, "mean", color=P.muted(), fontsize=bio.core.FONT["tiny"])
ax.set_xlim(0, 2.3)
charts.style_axes(ax, r"$v / \bar v$", "r / (d/2)")
charts.title(ax, "A  No slip at the wall")

ax = axs[1]
s = np.linspace(0.5, 1.0, 200)
ax.plot(s, s**4, color=charts.line("blood"), lw=1.7, label=r"$Q \propto d^4$ (Poiseuille)")
ax.plot(s, s**2, color=P.muted(), lw=1.0, ls="--", label=r"$\propto d^2$ (plug flow at fixed speed)")
ax.plot(0.8, 0.8**4, "o", color=charts.line("negative"), ms=5)
ax.annotate("20 % narrower:\n41 % of the flow", (0.8, 0.41), (0.55, 0.62), fontsize=bio.core.FONT["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"diameter $d/d_0$", r"flow rate $Q/Q_0$")
charts.title(ax, "B  The fourth power")
