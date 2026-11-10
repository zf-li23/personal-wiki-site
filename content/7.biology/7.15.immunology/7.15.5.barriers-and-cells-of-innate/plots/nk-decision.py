# Threshold model of the NK-cell killing decision: p_kill = 1 / (1 + exp(-beta (S_a - S_i - theta))),
# with S_a the activating signal (stress ligands) and S_i the inhibitory signal (MHC class I). Schematic.
import matplotlib.patheffects as pe
import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
fig, ax = bio.canvas(20.0, 8.4)
BETA, THETA = 4.0, 0.5


def pkill(sa, si, theta=THETA):
    return 1 / (1 + np.exp(-BETA * (sa - si - theta)))


bio.panel(ax, "A", (0.1, 8.3))
pax = charts.axes_at(ax, (1.8, 1.4, 6.6, 6.2))
sa = np.linspace(0, 3, 300)
si = np.linspace(0, 3, 300)
SA, SI = np.meshgrid(sa, si)
im = pax.imshow(pkill(SA, SI), origin="lower", extent=(0, 3, 0, 3), cmap="magma", vmin=0, vmax=1, aspect="auto")
pax.plot(sa, sa - THETA, color="white", lw=1.4, ls="--")
pax.set_xlim(0, 3)
pax.set_ylim(0, 3)
charts.style_axes(pax, "activating signal $S_a$ (stress ligands)", "inhibitory signal $S_i$ (MHC class I)")
pts = {"healthy cell": (0.5, 2.4), "MHC I lost\n(missing self)": (0.6, 0.25), "stress ligands up\n(induced self)": (2.55, 1.2)}
for name, (x, y) in pts.items():
    pax.plot([x], [y], "o", color="white", ms=7, mec="#3b2747", mew=0.8)
    off = (-40, -34) if x > 2 else (6, 6)
    pax.annotate(name, (x, y), xytext=off, textcoords="offset points", color="white", fontsize=7.5,
                 path_effects=[pe.withStroke(linewidth=2.2, foreground="#3b2747")])
pax.annotate("", xy=(0.6, 0.45), xytext=(0.5, 2.25), arrowprops=dict(arrowstyle="->", color="white", lw=1.2))
pax.annotate("", xy=(2.45, 1.4), xytext=(0.7, 2.35), arrowprops=dict(arrowstyle="->", color="white", lw=1.2))
cb = fig.colorbar(im, ax=pax, fraction=0.05, pad=0.03)
cb.set_label("$p_{kill}$", fontsize=8)
cb.ax.tick_params(labelsize=7)

bio.panel(ax, "B", (11.0, 8.3))
pl = quant.Plot(ax, (12.6, 1.4, 6.8, 6.2), xlim=(0, 1), ylim=(0, 1.02), xlabel="MHC class I on target (fraction of normal)",
                ylabel="$p_{kill}$", xticks=[0, 0.25, 0.5, 0.75, 1], yticks=[0, 0.5, 1])
m = np.linspace(0, 1, 300)
for theta, tok, name in ((0.5, "dna", "licensed NK cell, θ = 0.5"), (1.2, "drug", "unlicensed, θ = 1.2")):
    pl.line(m, pkill(1.0, 2.0 * m, theta), tok, lw=2.0)
pl.legend([("licensed NK cell (θ = 0.5)", "dna", "-"), ("unlicensed (θ = 1.2)", "drug", "-")], at=(15.4, 7.3))
pl.text(0.33, 0.7, "fixed $S_a$ = 1;  $S_i$ = 2 × MHC level", size="tiny", ha="left")
